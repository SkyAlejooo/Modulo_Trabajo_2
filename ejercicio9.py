def main():

    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
        {"nombre": "Gorra", "precio": 25000}
    ]


    productos_con_iva = {
        producto['nombre']: round(producto['precio'] * 1.19, 2)
        for producto in productos
    }

    print("Productos con IVA incluido:")
    for producto, precio in productos_con_iva.items():
        print(f"{producto}: ${precio:,.2f}")


if __name__ == "__main__":
    main()