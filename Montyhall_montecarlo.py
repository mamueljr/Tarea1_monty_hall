# ADALBERTO EMMANUEL ROJAS
# MAESTRIA EN INGENIERIA EN CIENCIAS COMPUTACIONALES
# CODIGO PARA PROBLEMA DE MONTY HALL
import random

# CREO ARREGLO CON EL CARRO DENTRO DE LAS PUERTAS ALEATORIAMENTE


def puerta_aleatoria():
    puertas = ["burro", "burro", "burro"]
    puertas[random.randint(0, 2)] = "carro"
    return puertas

# Monty Hall abrir_p a door


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

    num_intentos = 1000000
    aciertos = 0
    sin_carro = 0

    for i in range(num_intentos):
        # Generate the puertas
        puertas = puerta_aleatoria()

        # Player selects the door
        puerta_elegidaection = random.randint(0, 2)

        # Monty Hall abrir_ps a door with a burro
        puertas = abrirpuerta(puerta_elegidaection, puertas)

        # Player changes of door
        if (puerta_elegidaection == puertas.index("carro")):
            puerta_elegidaection = puertas.index("burro")

        elif (puerta_elegidaection == puertas.index("burro")):
            puerta_elegidaection = puertas.index("carro")

        # Count of aciertos and sin_carro
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
