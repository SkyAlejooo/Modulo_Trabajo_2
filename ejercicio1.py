def calcular_precio_entrada(edad: int, es_estudiante: str) -> float:

    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    # Podrías hacer los mensajes más específicos
    if es_estudiante not in ['si', 'no']:
        raise ValueError("Debe responder 'si' o 'no' para la pregunta de estudiante")

    if edad < 12:
        precio = 10000
    elif 12 <= edad <= 17:
        precio = 15000
    else:
        precio = 20000

    if es_estudiante == 'si':
        precio *= 0.9

    return precio


def main():

    try:
        edad = int(input("Ingrese su edad: "))
        estudiante = input("¿Es estudiante? (si/no): ")

        precio = calcular_precio_entrada(edad, estudiante)
        print(f"El precio de su entrada es: ${precio:,.0f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
