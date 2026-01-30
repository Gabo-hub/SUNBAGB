import os
import shutil
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, QImage, QPainter, QFont, QColor, QPageSize, QPageLayout
from PySide6.QtCore import Qt, QSize, QMarginsF, QSizeF
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from views.modal_carnet import Ui_ModalCarnet
from PIL import Image, ImageDraw, ImageFont

class ModalCarnet(QDialog, Ui_ModalCarnet):
    def __init__(self, parent=None, student_data=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setModal(True)
        self.student_data = student_data  # Expecting dict: {'cedula', 'nombres', 'apellidos', 'grado', ...}
        
        # Paths
        self.base_dir = os.getcwd()
        self.photos_dir = os.path.join(self.base_dir, "static", "fotos_estudiantes")
        self.template_front = os.path.join(self.base_dir, "carnet_template", "4.png")
        self.template_back = os.path.join(self.base_dir, "carnet_template", "5.png")
        
        # Connections
        self.bttn_cargar_foto.clicked.connect(self.cargar_foto)
        self.bttn_imprimir.clicked.connect(self.imprimir_carnet)
        self.bttn_pdf.clicked.connect(self.guardar_pdf)
        self.bttn_cerrar.clicked.connect(self.close)
        
        # Calibration Connections
        self.sb_foto_x.valueChanged.connect(self.generar_vista_previa_carnet)
        self.sb_foto_y.valueChanged.connect(self.generar_vista_previa_carnet)
        self.sb_nombre_x.valueChanged.connect(self.generar_vista_previa_carnet)
        self.sb_nombre_y.valueChanged.connect(self.generar_vista_previa_carnet)
        self.sb_cedula_x.valueChanged.connect(self.generar_vista_previa_carnet)
        self.sb_cedula_y.valueChanged.connect(self.generar_vista_previa_carnet)
        self.sb_grado_x.valueChanged.connect(self.generar_vista_previa_carnet)
        self.sb_grado_y.valueChanged.connect(self.generar_vista_previa_carnet)
        self.sb_foto_w.valueChanged.connect(self.generar_vista_previa_carnet)
        self.sb_foto_h.valueChanged.connect(self.generar_vista_previa_carnet)
        
        # Initial Load
        self.group_calibration.hide() # Hide for now as requested
        self.cargar_preview_foto()
        self.generar_vista_previa_carnet()
        
    def cargar_preview_foto(self):
        cedula = self.student_data.get('cedula', '')
        photo_path = os.path.join(self.photos_dir, f"{cedula}.jpg")
        
        if os.path.exists(photo_path):
            pixmap = QPixmap(photo_path)
        else:
            # Placeholder or empty
            pixmap = QPixmap(150, 150)
            pixmap.fill(QColor("gray"))
            
        self.lbl_foto_preview.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def cargar_foto(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar Foto", "", "Imagenes (*.png *.jpg *.jpeg)")
        if file_name:
            try:
                # Save to static dir
                cedula = self.student_data.get('cedula', '')
                dest_path = os.path.join(self.photos_dir, f"{cedula}.jpg")
                
                # Use PIL to resize and save as JPG
                img = Image.open(file_name)
                img = img.convert('RGB')
                img = img.resize((300, 300)) # Standardize size
                img.save(dest_path, "JPEG")
                
                self.cargar_preview_foto()
                self.generar_vista_previa_carnet() # Regenerate carnet with new photo
                
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo guardar la imagen: {e}")

    def generar_vista_previa_carnet(self):
        try:
            # Font setup
            try:
                font = ImageFont.truetype("arial.ttf", 24)
                font_bold = ImageFont.truetype("arialbd.ttf", 24)
            except:
                font = ImageFont.load_default()
                font_bold = font

            # Load Template
            if not os.path.exists(self.template_front):
                self.lbl_carnet_preview.setText("Plantilla no encontrada")
                return

            front = Image.open(self.template_front).convert("RGBA")
            draw = ImageDraw.Draw(front)
            
            # Load Photo
            cedula = self.student_data.get('cedula', '')
            photo_path = os.path.join(self.photos_dir, f"{cedula}.jpg")
            
            if os.path.exists(photo_path):
                photo = Image.open(photo_path).convert("RGBA")
                # Resize Photo from SpinBoxes
                photo_w = self.sb_foto_w.value()
                photo_h = self.sb_foto_h.value()
                photo = photo.resize((photo_w, photo_h)) 
                
                # Overlay Position (From SpinBoxes)
                foto_x = self.sb_foto_x.value()
                foto_y = self.sb_foto_y.value()
                front.paste(photo, (foto_x, foto_y)) 
            
            # Draw Data
                
            nombres = f"{self.student_data.get('nombres', '')} {self.student_data.get('apellidos', '')}"
            grado = self.student_data.get('grado', 'N/A')
            
            # Auto-Center Text Logic
            # The user wants "Name", "Cedula", "Grade" to be centered relative to the Photo width
            # Photo Center X
            foto_center_x = self.sb_foto_x.value() + (self.sb_foto_w.value() / 2)

            def draw_centered_text(draw_obj, text, font_obj, center_x, y_pos, color="black"):
                # Calculate text width
                bbox = draw_obj.textbbox((0, 0), text, font=font_obj)
                text_width = bbox[2] - bbox[0]
                # Calculate starting X
                start_x = center_x - (text_width / 2)
                draw_obj.text((start_x, y_pos), text, font=font_obj, fill=color)

            # Name logic: Attempt to get First Name [0] and First Surname [2]
            parts = nombres.split(' ')
            first_name = parts[0] if len(parts) > 0 else ""
            first_surname = parts[2] if len(parts) > 2 else (parts[1] if len(parts) > 1 else "")
            name_text = f"{first_name} {first_surname}".strip().upper()
            
            draw_centered_text(draw, name_text, font_bold, foto_center_x, self.sb_nombre_y.value())

            # Cedula
            cedula_text = f"C.E: {cedula}".upper()
            draw_centered_text(draw, cedula_text, font, foto_center_x, self.sb_cedula_y.value())

            # Grade
            grade_text = f"{grado}".upper()
            draw_centered_text(draw, grade_text, font, foto_center_x, self.sb_grado_y.value())
            
            # Save temporary for preview conversion
            temp_path = os.path.join(self.base_dir, "temp_preview_carnet.png")
            front.save(temp_path)
            
            # Display
            pixmap = QPixmap(temp_path)
            self.lbl_carnet_preview.setPixmap(pixmap.scaled(self.lbl_carnet_preview.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            
        except Exception as e:
            print(f"Error generando carnet: {e}")
            self.lbl_carnet_preview.setText("Error generando vista previa")

    def imprimir_carnet(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        
        if dialog.exec() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            
            # Draw Front
            temp_path = os.path.join(self.base_dir, "temp_preview_carnet.png")
            if os.path.exists(temp_path):
                img = QImage(temp_path)
                # Scale logic for printer PPI?
                rect = painter.viewport()
                size = img.size()
                size.scale(rect.size(), Qt.KeepAspectRatio)
                painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
                painter.setWindow(img.rect())
                painter.drawImage(0, 0, img)
                
            painter.end()

    def guardar_pdf(self):
        try:
            # First ensure Vista Previa (Front) is updated
            self.generar_vista_previa_carnet()
            
            # Prepare paths
            cedula = self.student_data.get('cedula', 'estudiante')
            nombre = self.student_data.get('nombres', 'estudiante').replace(" ", "_")
            apellido = self.student_data.get('apellidos', 'estudiante').replace(" ", "_")
            default_name = f"CARNET_{nombre}_{apellido}_{cedula}.pdf"
            
            file_path, _ = QFileDialog.getSaveFileName(self, "Guardar Carnet como PDF", default_name, "PDF Files (*.pdf)")
            
            if not file_path:
                return

            # Setup Printer for PDF
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(file_path)
            
            # Standard ID Size (roughly CR80)
            # 85.6mm x 54mm. Portrait is 54 x 85.6.
            page_size = QPageSize(QSizeF(54, 86), QPageSize.Unit.Millimeter)
            printer.setPageLayout(QPageLayout(page_size, QPageLayout.Orientation.Portrait, QMarginsF(0, 0, 0, 0)))

            painter = QPainter(printer)
            
            # 1. Front (already generated in temp_preview_carnet.png)
            temp_front = os.path.join(self.base_dir, "temp_preview_carnet.png")
            if os.path.exists(temp_front):
                img_front = QImage(temp_front)
                # Draw front on first page
                painter.drawImage(printer.pageRect(QPrinter.DevicePixel).toRect(), img_front)
            
            # 2. Back
            if os.path.exists(self.template_back):
                printer.newPage()
                img_back = QImage(self.template_back)
                # Draw back on second page
                painter.drawImage(printer.pageRect(QPrinter.DevicePixel).toRect(), img_back)
                
            painter.end()
            QMessageBox.information(self, "Éxito", f"PDF guardado exitosamente en:\n{file_path}")
            
        except Exception as e:
            print(f"Error guardando PDF: {e}")
            QMessageBox.warning(self, "Error", f"No se pudo generar el PDF: {e}")
