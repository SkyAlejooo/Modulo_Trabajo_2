import pytest
from ejercicio9 import main


def test_main_muestra_reporte_correcto(capsys):
    main()


    captured = capsys.readouterr()
    output = captured.out


    assert "Productos con IVA incluido:" in output
    assert "Camisa: $59,500.00" in output
    assert "Pantalón: $95,200.00" in output
    assert "Zapatos: $142,800.00" in output
    assert "Gorra: $29,750.00" in output


def test_main_formato_moneda_correcto(capsys):
    main()


    captured = capsys.readouterr()
    output = captured.out

    assert "$59,500.00" in output
    assert "$95,200.00" in output
    assert "$142,800.00" in output
    assert "$29,750.00" in output


def test_calculo_iva_correcto():

    lista_productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
        {"nombre": "Gorra", "precio": 25000}
    ]


    productos_con_iva = {
        producto['nombre']: round(producto['precio'] * 1.19, 2)
        for producto in lista_productos
    }


    assert productos_con_iva["Camisa"] == 59500.00
    assert productos_con_iva["Pantalón"] == 95200.00
    assert productos_con_iva["Zapatos"] == 142800.00
    assert productos_con_iva["Gorra"] == 29750.00


def test_estructura_datos_correcta():

    lista_productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    productos_con_iva = {
        producto['nombre']: round(producto['precio'] * 1.19, 2)
        for producto in lista_productos
    }


    assert isinstance(productos_con_iva, dict)


    assert "Camisa" in productos_con_iva
    assert "Pantalón" in productos_con_iva


    assert isinstance(productos_con_iva["Camisa"], float)
    assert isinstance(productos_con_iva["Pantalón"], float)


def test_redondeo_correcto():

    producto_prueba = [{"nombre": "Test", "precio": 10000}]

    precio_con_iva = {
        producto['nombre']: round(producto['precio'] * 1.19, 2)
        for producto in producto_prueba
    }


    assert precio_con_iva["Test"] == 11900.00
    assert precio_con_iva["Test"] == 11900.0


def test_lista_vacia():
    lista_vacia = []
    productos_con_iva = {
        producto['nombre']: round(producto['precio'] * 1.19, 2)
        for producto in lista_vacia
    }


    assert productos_con_iva == {}
    assert len(productos_con_iva) == 0


def test_precio_cero():

    producto_cero = [{"nombre": "Producto Gratis", "precio": 0}]

    productos_con_iva = {
        producto['nombre']: round(producto['precio'] * 1.19, 2)
        for producto in producto_cero
    }

    assert productos_con_iva["Producto Gratis"] == 0.00


def test_precio_decimal():

    producto_decimal = [{"nombre": "Producto Decimal", "precio": 1234.56}]

    productos_con_iva = {
        producto['nombre']: round(producto['precio'] * 1.19, 2)
        for producto in producto_decimal
    }


    precio_esperado = round(1234.56 * 1.19, 2)
    assert productos_con_iva["Producto Decimal"] == precio_esperado



def crear_datos_prueba():
    return {
        'productos': [
            {"nombre": "Camiseta", "precio": 30000},
            {"nombre": "Short", "precio": 40000}
        ],
        'esperado': {
            "Camiseta": 35700.00,
            "Short": 47600.00
        }
    }


def test_con_funcion_helper():
    datos = crear_datos_prueba()

    productos_con_iva = {
        producto['nombre']: round(producto['precio'] * 1.19, 2)
        for producto in datos['productos']
    }

    assert productos_con_iva == datos['esperado']
    assert productos_con_iva["Camiseta"] == 35700.00
    assert productos_con_iva["Short"] == 47600.00


def test_orden_productos():
    lista_productos = [
        {"nombre": "A", "precio": 100},
        {"nombre": "B", "precio": 200}
    ]

    productos_con_iva = {
        producto['nombre']: round(producto['precio'] * 1.19, 2)
        for producto in lista_productos
    }

    assert set(productos_con_iva.keys()) == {"A", "B"}
    assert set(productos_con_iva.values()) == {119.00, 238.00}