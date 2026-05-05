    "# programacion-tarea-4"

from abc import ABC, abstractmethod
import logging

logging.basicConfig(filename='registro.log', level=logging.ERROR)

    class BaseModel(ABC):
    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    @abstractmethod
    def score(self, X, y):
        pass

    class cliente:
    
    def __init__(self, nome, idade):
        if not nome.strip():
            raise ValueError("Nombre inválido")
        if idade <= 0:
            raise ValueError("Edad inválida")

        self._nome = nome
        self._idade = idade      

    def mostrar_informaciones(self):
        print(f"Nombre: {self._nome}, Edad: {self._idade}")

    def get_nombre(self):
        return self._nome

    class servicio(ABC):

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir(self):
        pass

    class sala(servicio):
    def __init__(self, horas):
        if horas <= 0:
            raise ValueError("Horas inválidas")
        self.horas = horas    

    def calcular_costo(self):
        return self.horas * 50

    def describir(self):
        return f"Sala por {self.horas} horas"
            
    class equipo(servicio):
    def __init__(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad inválida")
        self.cantidad = cantidad    

    def calcular_costo(self):
        return self.cantidad * 30

    def describir(self):
        return f"{self.cantidad} equipos"

    class asesoria(servicio):
    def __init__(self, horas):
        if horas <= 0:
            raise ValueError("Horas inválidas")
        self.horas = horas    

    def calcular_costo(self):
        return self.horas * 100

    def describir(self):
        return f"Asesoría por {self.horas} horas"
            
    class reserva:
    def __init__(self, cliente_obj, servicios):
        if not isinstance(cliente_obj, cliente):
            raise ValueError("Cliente inválido")
        if not all(isinstance(s, servicio) for s in servicios):
            raise ValueError("Servicios inválidos")

        self.cliente = cliente_obj
        self.servicios = servicios
        self.estado = "pendiente"

    def confirmar(self):
        self.estado = "confirmada"

    def cancelar(self):
        self.estado = "cancelada"

    def calcular_costo_total(self):
        return sum(s.calcular_costo() for s in self.servicios)

    def calcular_total(self, impuesto=0, descuento=0):
        base = self.calcular_costo_total()
        return base + (base * impuesto) - descuento

    def procesar(self):
        try:
            total = self.calcular_costo_total()
            self.confirmar()
            return total
        except Exception as e:
            self.cancelar()
            logging.error(f"Error al procesar reserva: {e}")
            raise e

    def mostrar_resumen(self):
        print(f"\nReserva para {self.cliente.get_nombre()} (Estado: {self.estado}):")
        for s in self.servicios:
            print(f"- {s.describir()}: ${s.calcular_costo()}")
        print(f"Costo total: ${self.calcular_costo_total()}")