# ADALBERTO EMMANUEL ROJAS
# MAESTRIA EN INGENIERIA EN CIENCIAS COMPUTACIONALES
# CODIGO PARA PROBLEMA DE MONTY HALL
import random

# CREO ARREGLO CON EL CARRO DENTRO DE LAS PUERTAS ALEATORIAMENTE


def puerta_aleatoria():
    puertas = ["burro", "burro", "burro"]
    puertas[random.randint(0, 2)] = "carro"
    return puertas

# FUNCION PARA ABRIR PUERTA ALEATORIAMENTE


def abrirpuerta(puerta_elegida, puertas):
    abrir_p = puerta_elegida
    if (puertas[puerta_elegida] == "carro"):
        abrir_p = random.randint(0, 2)
        while (abrir_p == puerta_elegida):
            abrir_p = random.randint(0, 2)
        puertas[abrir_p] = "abrir_p"
    else:
        index = puertas.index("carro")
        while ((abrir_p == puerta_elegida) or (abrir_p == index)):
            abrir_p = random.randint(0, 2)
        puertas[abrir_p] = "abrir_p"

    return puertas


def main():

    num_intentos = 100000
    aciertos = 0
    sin_carro = 0

    for i in range(num_intentos):
        # Generar puertas
        puertas = puerta_aleatoria()

        # Seleccion de puerta
        puerta_elegidaection = random.randint(0, 2)

        # Puerta con burro
        puertas = abrirpuerta(puerta_elegidaection, puertas)

        # Si el jugador cambia la puerta
        if (puerta_elegidaection == puertas.index("carro")):
            puerta_elegidaection = puertas.index("burro")

        elif (puerta_elegidaection == puertas.index("burro")):
            puerta_elegidaection = puertas.index("carro")

        # Cuenta final con carro y burro
        if puertas[puerta_elegidaection] == "carro":
            aciertos = aciertos + 1
        else:
            sin_carro = sin_carro + 1

    print(f"{num_intentos} num_intentos")
    print(f"Ganaste el carro: {aciertos} veces.")
    print(f"Tienes un burro: {sin_carro} veces.")

    print("Porcentaje de carro: {:.2f}%".format(((aciertos/num_intentos)*100)))


if __name__ == "__main__":
    main()
