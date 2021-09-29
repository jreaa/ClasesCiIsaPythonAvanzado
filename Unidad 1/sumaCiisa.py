##objeto - caracteriticas, funciones
"""
    n1 = int(input("Escribe un valor 1"))
    
    n2 = int(input("Escribe un valor 2"))

    
    operacion = Operacion(n1,n2)
    operacion.sumar()"""

"""
    doctor = Doctor("jose")
    doctor2 = Doctor("Alejandro")
    
    print(f'El id del doctor {doctor.mostrarNombre()} es {doctor.mostrarId()}')

    ############doctor2############
    print(f'El id del doctor {doctor2.mostrarNombre()} es {doctor2.mostrarId()}')


    #################llamado metodo static##################333
    Doctor.mostrarId()"""

class Operacion: #objeto

    #variables estaticas
    n1 = 0 #caracteristicas - atributos
    n2 = 0 #caracteristicas - atributos

    #plantilla incial con la que definimos nuestro objeto
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    #funcion de nuestro objeto - metodo
    def sumar(self):
        resultado = self.n1 + self.n2
        print(f'El resultado es {resultado}')

    def restar(self):
        resultado = self.n1 - self.n2
        print(f'El resultado es {resultado}')


class Alumno: #punto a

    #punto b
    asignaturas = 0
    titulacion = 0
    creditosSuperados = 0
    dni = 0
    nombre = ""

    #punto3
    def rendirExamen(self):
        print("Esta rindiendo la clase!!")

    def verClases(self):
        print("Estamos viendo clases")
            


class Doctor:
    identificador = 0

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrarNombre(self):
        return self.nombre
    
    def mostrarId(self):
        Doctor.identificador = Doctor.identificador + 1
        return Doctor.identificador

    @staticmethod
    def asignarPacientes():
        print("::Asignando paciente...")


class Menu:

    @staticmethod
    def menuPrincipal():
        opcion = 0

        while(opcion == 0):
            print("1.-Paciente")
            print("2.-Doctor")
            print("3.-Salir")

            seleccion = int(input("Por favor selecciona uno : "))

            if(seleccion == 1):
                print("Hola paciente...")
                opcion = 1
                break
            
        
        

############################logica a utilizar #######################################

if __name__ == "__main__":
    Menu.menuPrincipal()
    
    

    

    
