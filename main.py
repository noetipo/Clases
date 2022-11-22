from persona import Persona

personas: Persona = []


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


def main():
    continuar: bool = True

    while continuar:
        valor: str = str(
            input("ingrese caso 1 para agregar persona,2 para listar personas, 10 para terminar: "))
        match valor:
            case "1":
                persona()
            case "2":
                listar_personas()

            case "10":
                continuar = False


if __name__ == '__main__':
    main()
