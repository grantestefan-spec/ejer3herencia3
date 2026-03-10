from clases.herencia1.taxi import Taxi
from clases.herencia1.auto_particular import AutoParticular

def main():
    coche = Taxi("448-GTO","TurboS",3500,"484-a")
    print("************")
    print(coche)
    coche.encender()
    coche.subirPasajeros()
    coche.acelerar()
    coche.frenar()
    coche.cobrarCuota()

    ap= AutoParticular("123","Estefan",18,"Audi","Gris","564-G")
    print(ap)
    
    ap.subirseAuto()
    ap.arrancarAuto()
    ap.llegarDestino()
    ap.bajandoAuto()

if __name__=='__main__':
    main()