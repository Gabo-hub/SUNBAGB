class Cuerpo:
    """ Permite Calcular el Área de un cuerpo Rectángulo o Triángulo 
        colocando en la variable tipo (1 para Rectángulo, 2 para Triángulo"""
    def __init__(self,base,altura,figura,tipo) -> None:
        self.altura=altura
        self.base=base
        self.tipo=tipo
        self.figura=figura
    def calculo(self) -> None:
        print("El Área del "+self.figura,self.altura*self.base/self.tipo)

paraCalcular=Cuerpo(20,10,"Rectángulo",1)
paraCalcular.calculo()
paraCalcular=Cuerpo(20,12,"Triángulo",2)
paraCalcular.calculo()

# *************************************************************************************************
class Poligono:
    """
    Define un polígono según su base y su altura.
    """
    
    def __init__(self, b, h):
        self.b = b
        self.h = h
 
class Rectangulo(Poligono):

    def area(self):
        return self.b * self.h

class Triangulo(Poligono):

    def area(self):
        return (self.b * self.h) / 2

rectangulo = Rectangulo(20, 10)
triangulo = Triangulo(20, 12)

print("Área del rectángulo: ", rectangulo.area())
print("Área del triángulo:", triangulo.area())

