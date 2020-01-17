
class Persona():

    def __init__(self, sexo , nombre , estatura , edad , peso , color_de_piel , color_de_pelo , pelo , color_de_ojos , gafas):
        self.sexo = sexo
        self.nombre = nombre
        self.estatura = estatura
        self.edad = edad
        self.peso = peso 
        self.color_de_piel = color_de_piel
        self.color_de_pelo = color_de_pelo
        self.pelo = pelo
        self.color_de_ojos = color_de_ojos
        self.gafas = gafas

'''METODOS'''

    #   Cumple años 
    def cumple_anos(self):
        '''
        La persona cumple 1 año
        :return self.edad
        '''
        self.edad += 1
        return self.edad
    
    #   Comer
    def comer(self,comida):
        '''
        La persona come la comida
        - param comida: de lo que se alimenta
        '''
        print(f"La persona esta comiendo {comida}")

    def dormir(self):
        """
        La persona se duerme
        """
        print(f"La persona esta dormida")

    #   Despertar
    def despertar(self):
        print(f"La persona se ha despertado")

    #   Andar
    def andar(self, direccion, tiempo = 0 , distancia = 0):
        if (tiempo != 0):
            print(f"La persona va hacia {direccion} a andar {tiempo} minutos")
        
        elif (distancia != 0):
            print(f"La persona va hacia {direccion} a andar {distancia} Km")
        
        else: 
            print("La persona esta parada")

    
