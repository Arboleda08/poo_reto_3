import math
import numpy as np
   
# Clase que representa un punto en el plano cartesiano
class Punto:
    def __init__(self, x, y):
      # Coordenada en el eje x
      self.x = x
      # Coordenada en el eje y
      self.y = y


# Clase que representa una línea definida por dos puntos
class Linea:

    def __init__(self, **kwargs):
      # Punto inicial de la línea
      self.inicio = kwargs.get("inicio")
      # Punto final de la línea
      self.final = kwargs.get("final")
    
      # Longitud opcional (si se proporciona)
      if "largo" in kwargs:
        self.largo = kwargs.get("largo")
    
      # Pendiente opcional (si se proporciona)
      if "pendiente" in kwargs:
        self.pendiente = kwargs.get("pendiente")

    # Calcula la longitud de la línea usando la fórmula de distancia
    def calcular_longitud(self):
      dx = self.final.x - self.inicio.x
      dy = self.final.y - self.inicio.y
      self.largo = math.sqrt(dx ** 2 + dy ** 2)
      return self.largo

    # Calcula la pendiente y retorna el ángulo en radianes
    def calcular_pendiente(self):
      self.pendiente = (self.final.y - self.inicio.y)/(self.final.x - self.inicio.x)
      grados = math.atan(self.pendiente)
      return grados

    # Verifica si la línea cruza el eje horizontal (y = 0)
    def calcular_cruce_horizontal(self):
      y1 = self.inicio.y
      y2 = self.final.y
      if y1 * y2 <= 0:
        return True
      else:
        return False

    # Verifica si la línea cruza el eje vertical (x = 0)
    def calcular_cruce_vertical(self):
      x1 = self.inicio.x
      x2 = self.final.x
      if x1 * x2 <= 0:
        return True
      else:
        return False

    # Divide la línea en n puntos equidistantes
    def linea_discreta(self, n: int):
      if n < 2:
        return False
    
      # Diferencias absolutas en cada eje
      a = abs(self.inicio.x - self.final.x)  # eje x
      b = abs(self.inicio.y - self.final.y)  # eje y
    
      # Incrementos por paso
      c = a / (n - 1)
      d = b / (n - 1)
    
      i = 0
      listax = [self.inicio.x]
      listay = [self.inicio.y]
    
      # Genera los puntos intermedios
      while i < (n - 1):
        i += 1
        listax.append(self.inicio.x + i * c)
        listay.append(self.inicio.y + i * d)
    
      # Convierte las listas en un arreglo de numpy
      self.array_punto = np.array([listax, listay])
      self.array_punto = self.array_punto.T

      return self.array_punto


# Clase que representa un rectángulo
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
    def punto_interferencia_cálculo(self, Punto: Punto):
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



# Prueba:

if __name__ == "__main__":
  p1 = Punto(0, 0)
  p2 = Punto(4, 3)

  linea1 = Linea(inicio=p1, final=p2)

  print("Longitud de la línea:", linea1.calcular_longitud())
  print("Ángulo (rad):", linea1.calcular_pendiente())
  print("Cruza eje X:", linea1.calcular_cruce_horizontal())
  print("Cruza eje Y:", linea1.calcular_cruce_vertical())
  print("Discretización:", linea1.linea_discreta(5))

 
  rect = Rectangulo(boton_izquierdo=Punto(0, 0), ancho=10, altura=5)

  print("Área del rectángulo:", rect.área_de_cálculo())
  print("Perímetro del rectángulo:", rect.perímetro_de_cálculo())

  
  print(rect.punto_interferencia_cálculo(p2))




