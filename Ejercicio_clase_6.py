# Definición de la clase Person
class Persona:
  # Atributo de clase que indica la especie (compartido por todas las instancias)
  Especie: str = "homosapiens"

  def __init__(self, edad: int, nombre: str):
    # Constructor de la clase
    # Inicializa la edad de la persona
    self.edad = edad
    # Inicializa el nombre de la persona
    self.nombre = nombre

  def saludar(self, nombre: str):
    # Método que imprime un saludo hacia otra persona
    print(f"{nombre} es bueno verte!")

  def es_mayor_que(self, persona: "Persona") -> bool:
    # Método que compara la edad de esta persona con otra
    # Retorna True si la persona actual es mayor que la otra
    return self.edad > persona.edad


# Prueba:
first_peron = Persona(20, "Bob")
second_person = Persona(15, "Alice")
print(first_peron.es_mayor_que(second_person))
