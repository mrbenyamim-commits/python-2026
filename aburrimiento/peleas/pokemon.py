import random
import math

class pokemon:
    def __init__(self,nivel, nombre, vida, ataque_F, defensa_F, ataque_P, defensa_P, velocidad):
        self.nivel = nivel
        self.nombre = nombre
        self.vida = vida
        self.ataque_F = ataque_F
        self.defensa_F = defensa_F
        self.ataque_P = ataque_P
        self.defensa_P = defensa_P
        self.velocidad = velocidad
        
class movimient_fisico:
    def __init__(self, nombre,poder,tipo,precision,pp):
        self.nombre = nombre
        self.poder = poder
        self.tipo = tipo
        self.precision = precision
        self.pp = pp
        

smash = movimient_fisico("smash", 15, "lucha", 100, 20)

pikachu = pokemon(5, "pikachu", 53, 18, 10, 23, 8, 31)
ratata = pokemon(5, "ratata", 42, 15, 14, 12, 16, 11)
    
def fisico(vida_poke, poke_1, poke_2, movimiento):
    dano = float(((2*poke_1.nivel/5)+2)*movimiento.poder*(poke_1.ataque_F/poke_2.defensa_F)+100)/50
    critico = random.randint(1,100)
    
    if critico <= 50:
        golpe = math.ceil(dano * 1.5)    
        print("\n", "impacto critico")  
    else:
        golpe = math.ceil(dano)
    vida_poke = vida_poke - golpe
    print("\n", poke_1.nombre,"le hiso", golpe, "de daño a", poke_2.nombre, "dejandolo con", vida_poke, "de", poke_2.vida , "\n")

vida_ratata = float(ratata.vida)
vida_pikachu = float(pikachu.vida)

fisico(vida_ratata, pikachu, ratata, smash)

