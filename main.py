from persona import Persona
from producto import Producto
from factura import Factura
from factura_detalle import FacturaDetalle
personas: Persona = []
productos: Producto = []
factutas: Factura = []


def persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)


def listar_personas():
    for persona in personas:
        Persona.convertir_a_string(persona)


def buscar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            return persona


def editar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            persona.nombres = str(input("Ingrese nuevo nombre: "))
            Persona.convertir_a_string(persona)


def eliminar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for indice, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(indice)


def producto():
    codigo: str = str(input("Ingrese código del producto: "))
    nombre: str = str(input("Ingrese nombre del producto: "))
    precio: float = float(input("Ingrese precio del producto: "))
    marca: str = str(input("Ingrese marca del producto: "))
    producto: Producto = Producto(codigo, nombre, precio, marca)
    productos.append(producto)


def listar_producto():
    for producto in productos:
        Producto.convertir_a_string(producto)


def buscar_producto():
    codigo: str = str(input("Ingrese Código para buscar el producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            return producto


def nueva_factura():
    print("para generar una factura busca un cliente")
    cliente: Persona = buscar_persona()
    factura: Factura = Factura(len(factutas)+1, cliente)
    continuar: bool = True

    while continuar:

        producto: Producto = buscar_producto()
        cantidad: int = int(input("Ingrese la cantidad: "))
        factura.detalle.append(FacturaDetalle(
            producto.codigo, producto.nombre, cantidad, producto.precio))
        
        condicion: str = str(input("SI para agregar productos: "))

        if condicion == "SI":
            continuar = True
        else:
            continuar = False
            factura.calcular_igv()
            factutas.append(factura)


def listar_factura():
    for factura in factutas:
        Factura.convertir_a_string(factura)

def buscar_factura():
    numero:int=int(input("Ingrese el numero de la factura: "))
    for factura in factutas:
        if factura.numero==numero:
            Factura.convertir_a_string(factura)
            print("===========================")
            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)
def main():
    continuar: bool = True

    while continuar:
        print("*****************************************")
        print("***********SISTEMA DE VENTAS*************")
        print("                                         ")
        print("===================MENÚ==================")
        print("**************INGRESE OPCIONES***********")
        print("       1: PARA AGREGAR PERSONA")
        print("       2: PARA LISTAR PERSONAS")
        print("       3: PARA BUSCAR PERSONA")
        print("       4: PARA EDITAR PERSONA")
        print("       5: PARA ELIMINAR PERSONA")
        print("       6: PARA AGREGAR PRODUCTO")
        print("       7: PARA LISTAR PRODUCTO")
        print("       15: PARA CREAR FACTURA")
        print("       16: PARA LISTAR  FACTURA")
        print("       17: PARA BUSCAR FACTURA")
        print("       20: PARA SALIR")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "6":
                producto()
            case "7":
                listar_producto()
            case "15":
                nueva_factura()
            case "16":
                listar_factura()
            case "17":
                buscar_factura()

            case "20":
                continuar = False


if __name__ == '__main__':
    main()
