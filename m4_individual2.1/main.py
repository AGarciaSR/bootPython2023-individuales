import time
class Piloto:
    def __init__(self, nombre, edad, agresividad):
        self.nombre = nombre
        self.edad = edad
        self.agresividad = agresividad
        self.__estres = 0
        self.__ahorro = 0
        self.en_coche = False
        
    def subir_al_coche(self):
        self.en_coche = True
    
    def bajar_del_coche(self):
        self.en_coche = False
    
    def atacar(self):
        pass
    
    def defender(self):
        pass
    
    def modo_ahorro(self, ahorro):
        self.ahorro = ahorro
    
    def modifica_estres(self, estres):
        self.ahorro = estres
    
    def entra_boxes(self):
        pass

class Equipo:
    def __init__(self, nombre, pilotos, coche):
        self.nombre = nombre
        self.pilotos = pilotos
        self.coche = coche
    
    def llama_box(self):
        coche.en_box = True
    
    # Método "sobrecargado"
    def cambia_piloto(self, piloto):
        if coche.piloto is None:
            piloto.subir_al_coche()
            coche.piloto = piloto
            time.sleep(2)
        else:
            pilotoAct = coche.piloto
            pilotoAct.bajar_del_coche()
            piloto.subir_al_coche()
            coche.piloto = piloto
            time.sleep(4)
    
    # Método "sobrecargado"
    def cambiar_ruedas(self, coche, ruedas=None):
        if ruedas is None:
            coche.ruedas = [100, 100, 100, 100]
            time.sleep(4)
        else:
            for rueda in ruedas:
                coche.ruedas[rueda] = 100
            time.sleep(len(ruedas))
    
    # Método "sobrecargado"
    def llena_combustible(self, porcentaje=None):
        if porcentaje is None:
            time.sleep((100 - coche.combustible) * 0.1)
            coche.combustible = 100
        else:
            time.sleep((porcentaje) * 0.1)
            coche.combustible += porcentaje
    
class Circuito:
    def __init__(self, nombre, longitud, curvas):
        self.nombre = nombre
        self.longitud = longitud
        self.curvas = curvas
        self.limpieza = 0
        self.lluvia = 0
    
    def modifica_limpieza(self, limpieza):
        self.limpieza += limpieza
    
    def aplica_lluvia(self, lluvia):
        self.lluvia = lluvia
    
class Coche:
    def __init__(self, modelo, potencia, peso, piloto=None):
        self.modelo = modelo
        self.potencia = potencia
        self.peso = peso
        self.ruedas = [100, 100, 100, 100]
        self.en_box = True
        self.combustible = 100
        self.velocidad = 0
        self.flashing_lights = False
        self.piloto = None
    
    def acelerar(self):
        pass
    
    def frenar(self):
        pass
    
    def flash_luces(self):
        self.flashing_lights = True
        time.sleep(2)
        self.flashing_lights = False
    
    def gasta_combustible(self):
        pass
    
    def modifica_ruedas(self):
        pass
    
    def rotura_aleatoria(self):
        pass
    
coche = Coche('Peugeot 905', 670, 750)
piloto1 = Piloto('Thierry Boutsen', 45, 85)
piloto2 = Piloto('Mark Blundell', 51, 76)
equipo = Equipo('Peugeot Talbot Sport', [piloto1, piloto2], coche)
equipo.cambia_piloto(equipo.pilotos[0])
print(equipo.coche.piloto.nombre)
equipo.cambia_piloto(equipo.pilotos[1])
print(equipo.coche.piloto.nombre)