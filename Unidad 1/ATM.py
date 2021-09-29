##atm ciisa

class ATM():

    nombrePersona = "jose"
    nCuenta = "12345"

    def mostrarOpciones(self):
        ADORNO = "=" * 20

        print(ADORNO)
        print("Por favor selecciona una de las opciones a realizar en tu ATM")
        print(ADORNO)
        print("1.-Ver estado cuenta")
        opcion = int(input("Opcion : "))

        if(opcion == 1):
            print("Tu saldo es de 200000")
        

    def verificacion(self, nombrePersona, nCuenta ):
        if(self.nombrePersona == nombrePersona and self.nCuenta == nCuenta):
            self.mostrarOpciones()
        else:
            print(f'{nombrePersona} no tiene cuenta en este banco')



if __name__ == '__main__':
    ADORNO = "=" * 20
    print(ADORNO)
    print("Bienvenido a tu ATM")

    nombrePersona = input("Por favor ingresa tu nombre: ")
    numeroCuenta = input("Por fa ingresa tu numero de cuenta")

    atm = ATM()

    atm.verificacion(nombrePersona, numeroCuenta)
