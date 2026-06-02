import random, time, math

class pj():
    def __init__(self, nombre, hp, ATQ_F, DEF_F, ATQ_S, DEF_S, velocidad):
        self.nombre = nombre
        self.hp = hp
        self.ATQ_F = ATQ_F
        self.DEF_F = DEF_F
        self.ATQ_S = ATQ_S
        self.DEF_S = DEF_S
        self.velocidad = velocidad
        
class tecnica():
    def __init__(self, nombre, potencia, tipo):
        self.nombre = nombre
        self.potencia = potencia
        self.tipo = tipo
        
