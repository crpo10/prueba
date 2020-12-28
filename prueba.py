class auto:
  def __init__(self, modelo, ruedas, sonido):
    self.modelo = modelo 
    self.ruedas = ruedas
    self.sonido = sonido

  def mostraAuto(self):
    print("El auto es un " + self.modelo + ".")
    print("El auto tiene " + str(self.ruedas) + " ruedas.")
    print("El auto tiene un equipo " + self.sonido + ".")

#Aveo = auto("Chevrolet", 4, "Century")
#Aveo.mostraAuto()

class autoDeluxe(auto):
  def __init__(self, modelo, ruedas, sonido, precio, pais):
    self.precio = precio
    self.pais = pais
    super().__init__(modelo, ruedas, sonido)

  def mostraAuto(self):
    super().mostraAuto()
    print("El precio del vehiculo es de: " + str(self.precio) + " dolares.")
    print("Su fabricacion fue en " + self.pais + ".")

Murcielago = autoDeluxe("Lamborginhi", 4, "Century 2.0", 100000, "Italia")
Murcielago.mostraAuto()
  


