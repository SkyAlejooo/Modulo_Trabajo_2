def main():

    lista_numeros = [-5, 10, -15, 20, -25, 30]

    numeros_positivos = [numero for numero in lista_numeros if numero > 0]

    cuadrados_numeros = [numero ** 2 for numero in lista_numeros]

    clasificacion_numeros = ["positivo" if numero >= 0 else "negativo" for numero in lista_numeros]

    print("Lista original de números:", lista_numeros)
    print("Números positivos filtrados:", numeros_positivos)
    print("Cuadrados de cada número:", cuadrados_numeros)
    print("Clasificación de números:", clasificacion_numeros)


if __name__ == "__main__":
    main()