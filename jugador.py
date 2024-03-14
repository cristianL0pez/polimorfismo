import random 
from personaje import Personaje


class Jugador(Personaje):
    
    def __init__(self, hp: int, atk: int, df: int, arma) -> None:
        super().__init__(hp, atk, df)
        self.__arma = arma
        
        
        
        
    def ataque(self) -> int:
        return (self.atk + random.randint(1, 5)
        if self.__arma else self.atk) 
        
    def defensa(self, ataque: int) -> None:
        self.hp -= max(ataque - random.randint(1, self.df), 0)
    