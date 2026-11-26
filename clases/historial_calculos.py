class HistorialCalculos:
    """Guarda y entrega los calculos realizados durante la sesion."""

    def __init__(self):
        """Inicializa el historial con una lista vacia."""
        self.calculos = []

    def agregar(self, texto_funcion, a, b, n, tipo, resultado):
        """Agrega un diccionario con los datos de un calculo al historial."""
        calculo = {
            "funcion": texto_funcion,
            "a": a,
            "b": b,
            "n": n,
            "tipo": tipo,
            "resultado": resultado,
        }
        self.calculos.append(calculo)

    def listar(self):
        """Devuelve la lista completa de calculos."""
        return self.calculos

    def contar(self):
        """Devuelve la cantidad de calculos almacenados."""
        return len(self.calculos)

    def esta_vacio(self):
        """Indica si el historial no contiene calculos."""
        return len(self.calculos) == 0

    def obtener_ultimo(self):
        """Devuelve el ultimo calculo o None si el historial esta vacio."""
        if len(self.calculos) == 0:
            return None
        return self.calculos[-1]