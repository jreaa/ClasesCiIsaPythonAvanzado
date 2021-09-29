#accesos
#interfaces
#polimorfismo 

class Regla:
    def holamundo(self):
        pass

class Persona(Regla):

    disponible = []

    def __init__(self,nombre, apellido, rut):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__rut = rut

    #polimorfismo
    def holamundo(self):
        return "Hola mundo persona!!"

    #getters and setters

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido
    def setApellido(self,apellido):
        self.__apellido = apellido

    def getRut(self):
        return self.rut

    class agendar:

        def __init__(self,date,time):
            self.date = date
            self.time = time

    def addDisponible(self,date,time):
        agendamiento = self.agendar(date, time)
        self.disponible.append(agendamiento)

    def getDisponible(self):
        return self.disponible


class Estudiante(Persona):

    def __init__(self,nombre,apellido,rut, asignatura):
        super().__init__(nombre,apellido, rut)
        self.asignatura = asignatura
    def estudiando(self):
        return "Estoy estudiando"

    def holamundo(self):
        return "Hola mundo estudiante!!"


  

if __name__ == '__main__':

    ejemplo = "ejemplo x"
    persona = Persona("Jose", "Era", "12345678-9")
    estudiante = Estudiante("Alejandro", "Era", "12345678-9", "programacion")
    print(persona.holamundo())
    print(estudiante.holamundo())

    pasajeros = ["jose", "pablo", "fernando", "maria", "juan"]
    print(len(pasajeros))

    #persona.addDisponible("Miercoles", "4pm")
    #persona.addDisponible("Jueves", "4pm")
    #persona.addDisponible("Viernes", "8pm")
    #persona.addDisponible("Lunes", "6pm")


    #for item in persona.getDisponible():
        #print(item.date, item.time)

    
    #persona.__nombre = "Alejandro"
    #print(persona.getNombre())

    #estudiante = Estudiante("Pedro", "Lopez", "12345678-9", "matematicas")
    #print(estudiante.estudiando())
    
    
    
