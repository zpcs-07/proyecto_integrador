from clases.funcion_polinomial import FuncionPolinomial
from clases.integral_definida import IntegralDefinida
from clases.historial_calculos import HistorialCalculos


def mostrar_menu():
    print("==========================================")
    print("  AREA BAJO LA CURVA - SUMAS DE RIEMANN")
    print("==========================================")
    print("1. Definir la funcion")
    print("2. Ver la funcion")
    print("3. Definir el intervalo")
    print("4. Ver la amplitud y el delta x")
    print("5. Calcular el area con suma de Riemann")
    print("6. Ver el detalle de los rectangulos")
    print("7. Ver el historial")
    print("8. Salir")
    print("==========================================")


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
    historial = HistorialCalculos()
    funcion = None
    integral = None
    a = None
    b = None

    while True:
        mostrar_menu()
        opcion = pedir_entero("Elige una opcion: ", 1, 8)

        if opcion == 1:
            grado = pedir_entero("Grado del polinomio: ", 0, 10)
            coeficientes = []
            for potencia in range(grado, -1, -1):
                coeficiente = pedir_decimal("Coeficiente de x^" + str(potencia) + ": ")
                coeficientes.append(coeficiente)
            funcion = FuncionPolinomial(coeficientes)
            integral = None
            print(funcion.a_texto())

        elif opcion == 2:
            if funcion is None:
                print("Primero define una funcion con la opcion 1")
            else:
                print(funcion.a_texto())
                print("Grado:", funcion.grado)

        elif opcion == 3:
            if funcion is None:
                print("Primero define una funcion con la opcion 1")
            else:
                a = pedir_decimal("Limite inferior (a): ")
                b = pedir_decimal("Limite superior (b): ")
                integral = IntegralDefinida(funcion, a, b)
                if not integral.es_intervalo_valido():
                    print("a no puede ser mayor que b")
                    integral = None
                else:
                    print("Intervalo definido:", a, "a", b)

        elif opcion == 4:
            if integral is None:
                print("Primero define un intervalo valido con la opcion 3")
            else:
                n = pedir_entero("Numero de rectangulos (n): ", 1, 1000000)
                amplitud = integral.calcular_amplitud()
                delta_x = integral.calcular_delta_x(n)
                print("Paso 1 - Amplitud:", round(amplitud, 6))
                print("Paso 2 - Delta x:", round(delta_x, 6))

        elif opcion == 5:
            if integral is None:
                print("Primero define un intervalo valido con la opcion 3")
            else:
                n = pedir_entero("Numero de rectangulos (n): ", 1, 1000000)
                tipo = pedir_tipo()
                resultado = integral.suma_riemann(n, tipo)
                print("Resultado:", round(resultado, 6))
                historial.agregar(funcion.a_texto(), a, b, n, tipo, resultado)

        elif opcion == 6:
            if integral is None:
                print("Primero define un intervalo valido con la opcion 3")
            else:
                n = pedir_entero("Numero de rectangulos (n): ", 1, 1000000)
                tipo = pedir_tipo()
                cuantos = pedir_entero("Cuantos quieres ver: ", 1, 20)
                detalle = integral.detalle_rectangulos(n, tipo, cuantos)
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

        elif opcion == 7:
            if historial.esta_vacio():
                print("Todavia no has calculado nada")
            else:
                for calculo in historial.listar():
                    print(
                        "Funcion:", calculo["funcion"],
                        "- intervalo: [", calculo["a"], ",", calculo["b"], "]",
                        "- n:", calculo["n"],
                        "- tipo:", calculo["tipo"],
                        "- resultado:", round(calculo["resultado"], 6),
                    )
                print("Calculos guardados:", historial.contar())

        elif opcion == 8:
            print("Hasta luego")
            break


if __name__ == "__main__":
    main()