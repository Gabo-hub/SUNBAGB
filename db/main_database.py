import psycopg2
from psycopg2 import sql


import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)    

class DatabaseManager:
    def __init__(self):
        self.config = {
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT"),
            "database": os.getenv("DB_NAME")
        }

    def _get_connection(self):
        return psycopg2.connect(**self.config)

    def consultar(self, query, params=None, fetch_all=False):
        conn = None
        try:
            conn = self._get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                if fetch_all:
                    return cursor.fetchall()
                return cursor.fetchone()
        except Exception as e:
            print(f"Error en consulta: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def ejecutar(self, query, params=None):
        conn = None
        try:
            conn = self._get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()
                try:
                    return cursor.fetchall()
                except psycopg2.ProgrammingError:
                    return True
        except Exception as e:
            print(f"Error en ejecución: {e}")
            if conn:
                conn.rollback()
            return False
        finally:
            if conn:
                conn.close()

# Mantener compatibilidad temporal con funciones antiguas mientras se refactorizan los controladores
def conectarse():
    # Retorna un objeto simulado que maneja las consultas para no romper todo de una vez
    return DatabaseManager()

def consultardb(manager, query, params=None):
    if hasattr(manager, 'consultar'):
        return manager.consultar(query, params)
    # Fallback si todavía se pasa un cursor real (para migración gradual)
    manager.execute(query, params)
    return manager.fetchone()

def guardardb(manager, query, params=None):
    if hasattr(manager, 'ejecutar'):
        return manager.ejecutar(query, params)
    manager.execute(query, params)
    return True

def consultarvista(manager, query, params=None):
    if hasattr(manager, 'consultar'):
        return manager.consultar(query, params, fetch_all=True)
    manager.execute(query, params)
    return manager.fetchall()

# --- Funciones de Compatibilidad (Para migración gradual) ---

def consultaestados(manager, query, params=None):
    return consultarvista(manager, query, params)

def consultaparentesco(manager, query, params=None):
    return consultarvista(manager, query, params)

def consultaidstud(manager, query, params=None):
    return consultarvista(manager, query, params)

def actualizarinfo(manager, query, params=None):
    return consultarvista(manager, query, params)

def cargarestudiantes(manager, query, params=None):
    return consultarvista(manager, query, params)

