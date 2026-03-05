from clases.herencia1.taxi import Taxi

def main():
    coche = Taxi("448-GTO","TurboS",1000,"484-a")
    print("************")
    print(coche)
    coche.encender()
    coche.subirPasajeros()
    coche.acelerar()
    coche.frenar()
    coche.cobrarCuota()

if __name__=='__main__':
    main()