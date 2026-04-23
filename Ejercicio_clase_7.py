import math
import numpy as np
   
# Clase que representa un punto en el plano cartesiano
class Punto:
    def __init__(self, x, y):
      # Coordenada en el eje x
      self.x = x
      # Coordenada en el eje y
      self.y = y

class Rectangulo:

    def __init__(self, **kwargs):

      # Inicialización con esquina inferior izquierda, ancho y alto
      if "boton_izquierdo" in kwargs and "ancho" in kwargs and "altura" in kwargs:
        self.ancho = kwargs.get("ancho")
        self.altura = kwargs.get("altura")
        self.boton_izquierdo = kwargs.get("boton_izquierdo")
        self.centro = Punto(self.boton_izquierdo.x + self.ancho / 2, self.boton_izquierdo.y + self.altura / 2)

      # Inicialización con centro, ancho y alto
      elif "centro" in kwargs and "ancho" in kwargs and "altura" in kwargs:
        self.centro = kwargs.get("centro")
        self.ancho = kwargs.get("ancho")
        self.altura = kwargs.get("altura")

      # Inicialización con dos esquinas opuestas
      elif "boton_izquierdo" in kwargs and "top_derecho" in kwargs:
        self.ancho = kwargs.get("top_derecho").x - kwargs.get("boton_izquierdo").x
        self.altura = kwargs.get("top_derecho").y - kwargs.get("boton_izquierdo").y
        self.centro = Punto( (kwargs.get("boton_izquierdo").x + kwargs.get("top_derecho").x) / 2, (kwargs.get("boton_izquierdo").y + kwargs.get("top_derecho").y) / 2)

      # Inicialización con líneas que forman el rectángulo
      elif "linea_derecha" in kwargs and "linea_izquierda" in kwargs and "linea_superior" in kwargs and "linea_inferior" in kwargs:
        self.ancho = kwargs.get("linea_superior").compute_length()
        self.altura = kwargs.get("linea_derecha").compute_length()
        self.centro = Punto( (kwargs.get("linea_inferior").start.x + kwargs.get("linea_superior").end.x) / 2, (kwargs.get("boton_izquierdo").y + kwargs.get("top_derecho").y) / 2)

      else:
        print("Valores inválidos para Rectangle")

    # Calcula el área del rectángulo
    def área_de_cálculo(self):
      return self.ancho * self.altura

    # Calcula el perímetro del rectángulo
    def perímetro_de_cálculo(self):
      return 2 * (self.ancho + self.altura)

    # Verifica si un punto está dentro del rectángulo
    def punto_interferencia_cálculo(self, Point: Punto):
      izquierda = self.centro.x - self.ancho / 2
      derecha = self.centro.x + self.ancho / 2
      abajo = self.centro.y - self.altura / 2
      alto = self.centro.y + self.altura / 2

      return izquierda <= Punto.x <= derecha and abajo <= Punto.y <= alto

    # Verifica la relación de una línea con el rectángulo
    def linea_interferencia_cálculo(self, Punto_inicio: Punto, Punto_fin: Punto):
      A = self.linea_interferencia_cálculo(Punto_inicio)
      B = self.linea_interferencia_cálculo(Punto_fin)

      if A and B:
        print("Esta dentro del triangulo")

      elif A and not B or B and not A:
        print("Esta parcialmente adentro")

      elif not A and not B:
        print("Esta afuera")

      else:
        print("Valores inválidos para Rectangle")
