class Persona:

    citas = []
    
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def mostrarNombreCompleto(self):
        nombreCompleto = self.getNombre()
        return nombreCompleto

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre

    class agendarCitas:
        def __init__(self, fecha, hora):
            self.fecha = fecha
            self.hora = hora


    def addAgendamiento(self, fecha, hora):
        agendar = self.agendarCitas(fecha, hora)
        self.citas.append( agendar )

    def getAgendamiento(self):
        return self.citas
    


class Estudiante(Persona):
    def __init__(self, nombre, apellido, rut):
        super().__init__(self,nombre)
        self.rut = rut





if __name__ == '__main__':

    persona = Persona("Jose", "Era")
    persona.setNombre("Alejandro")

    print(persona.getNombre())

    persona.addAgendamiento("02-06-2021", "14:20")

    for item in persona.getAgendamiento():
        print(item.fecha)

    #print(persona.mostrarNombreCompleto())

    estudiante = Estudiante("Jose", "Era", "12345678-9")
    estudiante.setNombre("pedro")
    print(estudiante.getNombre())
