from clases.funcion_polinomial import FuncionPolinomial
from clases.integral_definida import IntegralDefinida


def mostrar_menu():
    print("  AREA BAJO LA CURVA - SUMAS DE RIEMANN")
    print("1. Definir la funcion y el intervalo")
    print("2. Calcular el area")
    print("3. Salir")



def pedir_entero(mensaje, minimo, maximo):
    while True:
        texto = input(mensaje)
        try:
            numero = int(texto)
        except (TypeError, ValueError):
            print("Eso no es un numero entero, intenta otra vez")
            continue
        if numero < minimo or numero > maximo:
            print("El numero debe estar entre", minimo, "y", maximo)
            continue
        return numero


def pedir_decimal(mensaje):
    while True:
        texto = input(mensaje)
        try:
            numero = float(texto)
        except (TypeError, ValueError):
            print("Eso no es un numero, intenta otra vez")
            continue
        return numero


def pedir_tipo():
    print("1. Derecho")
    print("2. Izquierdo")
    print("3. Medio")
    opcion = pedir_entero("Elige: ", 1, 3)
    if opcion == 1:
        return "derecho"
    if opcion == 2:
        return "izquierdo"
    return "medio"


def main():
    funcion = None
    integral = None

    while True:
        mostrar_menu()
        opcion = pedir_entero("Elige una opcion: ", 1, 3)

        if opcion == 1:
            grado = pedir_entero("Grado del polinomio: ", 0, 10)
            coeficientes = []
            for potencia in range(grado, -1, -1):
                coeficiente = pedir_decimal(
                    "Coeficiente de x^" + str(potencia) + ": "
                )
                coeficientes.append(coeficiente)
            funcion = FuncionPolinomial(coeficientes)
            print(funcion.a_texto())

            a = pedir_decimal("Limite inferior (a): ")
            b = pedir_decimal("Limite superior (b): ")
            integral = IntegralDefinida(funcion, a, b)
            if not integral.es_intervalo_valido():
                print("a no puede ser mayor que b")
                integral = None
            else:
                print("Intervalo definido:", a, "a", b)

        elif opcion == 2:
            if integral is None:
                print("Primero define la funcion y el intervalo con la opcion 1")
            else:
                n = pedir_entero("Numero de rectangulos (n): ", 1, 1000000)
                tipo = pedir_tipo()

                amplitud = integral.calcular_amplitud()
                print("Paso 1 - Amplitud:", round(amplitud, 6))

                delta_x = integral.calcular_delta_x(n)
                print("Paso 2 - Delta x:", round(delta_x, 6))

                detalle = integral.detalle_rectangulos(n, tipo, 5)
                for renglon in detalle:
                    i = renglon[0]
                    x = renglon[1]
                    altura = renglon[2]
                    area = renglon[3]
                    print(
                        "Rectangulo", i,
                        "- x:", round(x, 6),
                        "- altura:", round(altura, 6),
                        "- area:", round(area, 6),
                    )

                resultado = integral.suma_riemann(n, tipo)
                print("Resultado:", round(resultado, 6))

        elif opcion == 3:
            print("Hasta luego")
            break


if __name__ == "__main__":
    main()
