from clases.funcion_polinomial import FuncionPolinomial


class IntegralDefinida:
    """Representa una integral definida sobre un intervalo y sus rectangulos."""

    def __init__(self, funcion, limite_inferior, limite_superior):
        """Inicializa la integral con una funcion y sus limites."""
        if not isinstance(funcion, FuncionPolinomial):
            raise TypeError("funcion debe ser un objeto FuncionPolinomial")
        if isinstance(limite_inferior, bool) or not isinstance(limite_inferior, (int, float)):
            raise TypeError("limite_inferior debe ser int o float")
        if isinstance(limite_superior, bool) or not isinstance(limite_superior, (int, float)):
            raise TypeError("limite_superior debe ser int o float")

        self.funcion = funcion
        self.limite_inferior = limite_inferior
        self.limite_superior = limite_superior

    def calcular_amplitud(self):
        """Calcula la amplitud del intervalo."""
        return float(self.limite_superior - self.limite_inferior)

    def calcular_delta_x(self, n):
        """Calcula el ancho de cada subintervalo."""
        if isinstance(n, bool) or not isinstance(n, int) or n < 1:
            raise ValueError("n debe ser un entero mayor o igual a 1")
        return self.calcular_amplitud() / n

    def calcular_coordenada(self, i, n, tipo):
        """Calcula la coordenada del rectangulo segun el tipo indicado."""
        if tipo not in ("derecho", "izquierdo", "medio"):
            raise ValueError("tipo debe ser derecho, izquierdo o medio")
        if isinstance(n, bool) or not isinstance(n, int) or n < 1:
            raise ValueError("n debe ser un entero mayor o igual a 1")
        if isinstance(i, bool) or not isinstance(i, int) or i < 1 or i > n:
            raise ValueError("i debe estar entre 1 y n")

        delta = self.calcular_delta_x(n)
        if tipo == "derecho":
            return self.limite_inferior + i * delta
        if tipo == "izquierdo":
            return self.limite_inferior + (i - 1) * delta
        return self.limite_inferior + (i - 0.5) * delta

    def es_intervalo_valido(self):
        """Indica si el limite inferior no supera al limite superior."""
        return self.limite_inferior <= self.limite_superior

    def suma_riemann(self, n, tipo="derecho"):
        """Calcula la aproximacion del area mediante una suma de Riemann."""
        if self.limite_inferior == self.limite_superior:
            return 0

        delta = self.calcular_delta_x(n)
        suma = 0
        for i in range(1, n + 1):
            x = self.calcular_coordenada(i, n, tipo)
            suma = suma + self.funcion.evaluar(x)
        return suma * delta

    def detalle_rectangulos(self, n, tipo, cuantos=5):
        """Devuelve el detalle de los primeros rectangulos solicitados."""
        if isinstance(cuantos, bool) or not isinstance(cuantos, int) or cuantos <= 0:
            raise ValueError("cuantos debe ser un entero mayor que 0")

        detalle = []
        limite = min(cuantos, n)
        delta = self.calcular_delta_x(n)
        for i in range(1, limite + 1):
            x = self.calcular_coordenada(i, n, tipo)
            altura = self.funcion.evaluar(x)
            area = altura * delta
            detalle.append([i, x, altura, area])
        return detalle