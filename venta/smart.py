class SIM:
    def __init__(self, numero):
        self.numero = numero

    def activar(self):
        return f"Activando la SIM con número {self.numero}"

class Bateria:
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def cargar(self):
        return "Cargando la batería"

class Celular:
    def __init__(self, modelo, numero_sim, capacidad_bateria):
        self.modelo = modelo
        self.sim = SIM(numero_sim)
        self.bateria = Bateria(capacidad_bateria)

    def encender(self):
        return f"Encendiendo el celular {self.modelo}"

    def realizar_llamada(self, numero):
        return f"Llamando al número {numero}"

# Uso de la composición
mi_celular = Celular("iPhone", "123456789", "3000mAh")

print(mi_celular.encender())
print(mi_celular.sim.activar())
print(mi_celular.bateria.cargar())

print(mi_celular.realizar_llamada("987654321"))