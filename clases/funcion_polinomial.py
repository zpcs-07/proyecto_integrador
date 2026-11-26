class FuncionPolinomial:
    """Representa una funcion polinomial y permite evaluarla y mostrarla."""

    def __init__(self, coeficientes):
        """Inicializa el polinomio validando y guardando sus coeficientes."""
        if not isinstance(coeficientes, list) or len(coeficientes) == 0:
            raise ValueError("coeficientes debe ser una lista no vacia")

        for coeficiente in coeficientes:
            if isinstance(coeficiente, bool) or not isinstance(coeficiente, (int, float)):
                raise ValueError("todos los coeficientes deben ser int o float")

        self.coeficientes = coeficientes
        self.grado = len(self.coeficientes) - 1

    def evaluar(self, x):
        """Devuelve el valor del polinomio evaluado en x."""
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError("x debe ser int o float")

        resultado = 0.0
        potencia = self.grado
        for coeficiente in self.coeficientes:
            resultado = resultado + coeficiente * (x ** potencia)
            potencia = potencia - 1
        return resultado

    def a_texto(self):
        """Construye la representacion textual del polinomio."""
        if all(coeficiente == 0 for coeficiente in self.coeficientes):
            return "f(x) = 0"

        partes = []
        potencia = self.grado

        for coeficiente in self.coeficientes:
            if coeficiente == 0:
                potencia = potencia - 1
                continue

            coeficiente_absoluto = abs(coeficiente)
            if isinstance(coeficiente_absoluto, float) and coeficiente_absoluto.is_integer():
                coeficiente_texto = str(int(coeficiente_absoluto))
            else:
                coeficiente_texto = str(coeficiente_absoluto)

            if potencia == 0:
                termino = coeficiente_texto
            elif coeficiente_absoluto == 1:
                if potencia == 1:
                    termino = "x"
                else:
                    termino = "x^" + str(potencia)
            else:
                if potencia == 1:
                    termino = coeficiente_texto + "x"
                else:
                    termino = coeficiente_texto + "x^" + str(potencia)

            if coeficiente < 0:
                if not partes:
                    partes.append("-" + termino)
                else:
                    partes.append("- " + termino)
            else:
                if not partes:
                    partes.append(termino)
                else:
                    partes.append("+ " + termino)

            potencia = potencia - 1

        texto = ""
        for indice, parte in enumerate(partes):
            if indice == 0:
                texto = parte
            else:
                texto = texto + " " + parte

        return "f(x) = " + texto