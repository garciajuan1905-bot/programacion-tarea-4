"# programacion-tarea-4"

from abc  import ABC, abstractmethod
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
        if not nome or not idade:
            raise ValueError("O nome e a idade são obrigatórios.")
        self.nome = nome
        self.idade = idade      
    
