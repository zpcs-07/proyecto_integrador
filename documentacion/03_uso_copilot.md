# Etapa 5 — Cómo usé GitHub Copilot

## 1. ¿Cómo utilizaste las especificaciones para solicitar código a Copilot?

Antes de escribir una sola línea de Python hice los archivos de la carpeta especificaciones/
Ahí quedó escrito el nombre de cada clase, sus atributos con su tipo, qué recibe el
constructor, el algoritmo de cada método en pseudocódigo, y una lista de reglas numeradas
que no se podían cambiar

Cuando ya estaba eso, abría el archivo .py vacío en VS Code y en el chat de Copilot ponía
algo así:

```
Lee #file:especificacion_funcion_polinomial.md e implementa la clase FuncionPolinomial

Respeta los nombres tal cual vienen ahi
Los coeficientes van de mayor a menor potencia
Respeta las reglas RF1 a RF5

No agregues metodos que no esten en la especificacion
No uses input ni print dentro de la clase
No importes ninguna libreria
```

Lo del #file: es lo que hace la diferencia Sin eso, Copilot se inventa una clase genérica
de polinomios con los métodos que a él se le ocurren Con eso, lee mi documento y hace lo que
yo escribí

Fui una clase a la vez, como lo pide el proyecto Primero FuncionPolinomial, la revisé y la
probé, y hasta entonces seguí con IntegralDefinida Esa la pedí en dos tandas: primero el
constructor y los cuatro métodos de los pasos, y cuando ya estaban bien le pedí suma_riemann
y detalle_rectangulos Lo hice así porque es la clase más grande y si se la pido completa es
más fácil que invente atajos

## 2. ¿Qué revisaste o modificaste del código generado?

Lo primero que revisaba siempre era si había respetado las reglas numeradas de la
especificación Las tres que más vigilé:

- **RF1**, que los coeficientes quedaran de mayor a menor potencia Esta se puede romper sin
  que se note y el polinomio ya no es el mismo
- **RI1**, que la i del ciclo fuera de 1 hasta n y no de 0 hasta n-1 En Python lo normal es
  empezar en 0, pero mi fórmula de la libreta es x_i = x_0 + i·Δx con i de 1 a n
- **RI4**, que suma_riemann le pidiera la altura a self.funcion.evaluar(x) en vez de copiar
  la fórmula del polinomio adentro Si hace eso, las dos clases dejan de colaborar y una sola
  hace todo

Las tres las respetó Para comprobar la RI1 corrí calcular_coordenada con i = 5 y n = 5: si
hubiera arrancado en 0 me daría 2.0, y me dio 3.0, que es justo el límite superior del
intervalo

Lo que sí le encontré fue algo que yo **no** le pedí Copilot agregó esto en el constructor:

```python
if isinstance(coeficiente, bool) or not isinstance(coeficiente, (int, float)):
    raise ValueError("todos los coeficientes deben ser int o float")
```

El isinstance de bool no estaba en mi especificación Lo revisé y resulta que tiene razón: en
Python True es un int por dentro, entonces sin esa línea FuncionPolinomial([True, 3]) pasaría
la validación y el polinomio se evaluaría como si fuera [1, 3], sin que nadie se entere Lo
dejé porque lo entendí, no porque se vea bien, y después lo agregué a la especificación para
que el documento y el código digan lo mismo

## 3. ¿Copilot generó una respuesta incorrecta o distinta de lo solicitado?

Sí, una vez, y en un lugar donde no se veía a simple vista

El método a_texto escribía bien la función cuando los coeficientes eran enteros:

```
FuncionPolinomial([1, 3]).a_texto()  ->  f(x) = x + 3
```

Pero con decimales escribía el .0:

```
FuncionPolinomial([1.0, 3.0]).a_texto()  ->  f(x) = x + 3.0
```

Y eso no era un caso raro: era **exactamente** como el programa la iba a usar, porque main.py
pide los coeficientes con pedir_decimal, que siempre devuelve float Si no lo detecto, mi
función se habría visto como f(x) = x + 3.0 en todas las capturas de pantalla, cuando en mi
libreta dice f(x) = x + 3

Lo que más me sirvió de esto fue entender de quién era la culpa Copilot no se equivocó en la
lógica, hizo lo que decía mi especificación El hueco estaba en mi documento, que nunca dijo
qué hacer con un float que vale un entero Le pedí la corrección siendo específico:

```
a_texto escribe "f(x) = x + 3.0" cuando los coeficientes son floats, pero deberia escribir
"f(x) = x + 3"

Corrige solamente a_texto para que un coeficiente entero aunque venga como float se escriba
sin el .0 Los que si tienen decimales, como 2.5, se siguen escribiendo igual

No toques evaluar ni el constructor
```

Esa última línea la puse porque tenía miedo de que lo resolviera metiendo un int() a lo
bruto, y eso me habría roto las funciones con decimales de verdad No lo hizo, usó
is_integer() y quedó bien Lo comprobé: f(x) = 2.5x + 1 sigue escribiéndose con su 2.5

Después de eso actualicé la especificación para que incluyera la regla del .0, porque si no
el documento se queda diciendo una cosa y el código haciendo otra

## 4. ¿Cómo comprobaste el funcionamiento de clases y métodos?

Con los números de mi propia libreta, que es la ventaja de haber escogido un problema que ya
había resuelto a mano

Método por método:

- calcular_amplitud() con a = -2 y b = 3 tiene que dar 5, que es mi paso 1
- calcular_delta_x(5) tiene que dar 1.0, que es mi paso 2 con n = 5
- calcular_coordenada(1, 5, derecho) tiene que dar -1.0, que es mi x_1
- evaluar(-1) tiene que dar 2.0, que es f(x_1) = 1 + 5/5

Y la clase completa:

- suma_riemann(5) tiene que dar 20.0
- suma_riemann(100) tiene que dar 17.625
- suma_riemann(10000) tiene que dar 17.50125, ya bien cerca del 17.5

Esos números no los saqué del programa, los saqué de la fórmula Como mi suma usa el extremo
derecho, se puede cerrar en S(n) = 17.5 + 12.5/n, y de ahí sale cada uno Entonces no estaba
comprobando que el programa fuera consistente consigo mismo, estaba comprobando que diera lo
mismo que las matemáticas

También lo probé con cosas que no tienen nada que ver con mi ejercicio, para ver que no
estuviera amarrado a mi caso: la integral de x^2 de 0 a 1 da 0.333333, que es 1/3, y la de
x^2 - 4 de -2 a 2 da negativo, porque esa parábola va toda por debajo del eje

Todo eso quedó documentado en documentacion/02_pruebas.md

## 5. ¿Qué ventajas y limitaciones observaste?

**Lo bueno:**

- Escribe rápido lo aburrido El ciclo de a_texto con todos sus casos (el coeficiente 1 que
  no se escribe, el signo, la potencia 1 que va sin exponente) me habría llevado un buen rato
  y él lo sacó de una
- Cuando las reglas están numeradas y escritas, las respeta La RF1, la RI1 y la RI4 las
  cumplió sin que se lo tuviera que repetir
- Si le dices qué no hacer, no lo hace Le puse que no usara print dentro de las clases y no
  lo usó ni una vez

**Lo malo:**

- No puede adivinar lo que no está escrito El error del .0 pasó porque mi especificación no
  lo cubría Copilot no sabe cómo se va a ver mi función en pantalla, ni le importa
- Le gusta agregar de más Lo de los booleanos estuvo bien, pero fue suerte Si yo no lo
  reviso, no sé si lo que agregó ayuda o estorba
- Si le pides mucho de un jalón, sale peor Por eso pedí IntegralDefinida en dos tandas

La conclusión que me queda es que Copilot es tan bueno como el documento que le das Lo que
estuvo bien pensado en la especificación, salió bien a la primera Donde mi especificación
tenía un hueco, el código salió con el hueco

## 6. ¿Por qué es necesario comprender código producido con ayuda de IA?

Por tres razones que me pasaron a mí en este proyecto

**La primera**, porque si no lo entiendes no puedes encontrarle los errores El bug del .0 no
lo encontró ninguna prueba automática ni me lo avisó nadie Lo encontré porque me senté a leer
el método línea por línea y me pregunté qué pasaba cuando el coeficiente fuera un float Un
programa que corre sin tronar no es un programa correcto

**La segunda**, porque el código no sirve de nada si no sabes defenderlo Si el profesor me
pregunta por qué calcular_coordenada tiene tres casos, o por qué la i empieza en 1 y no en 0,
o por qué IntegralDefinida guarda adentro un objeto FuncionPolinomial en lugar de los
coeficientes, tengo que poder contestar Y la única forma de contestar es haber entendido qué
hace cada parte y por qué está ahí

**La tercera**, y es la que más me sorprendió, porque no se puede revisar lo que no se
entiende Cuando Copilot metió el isinstance de bool, yo tenía dos opciones: aceptarlo porque
se veía bien, o entender qué hacía Si lo acepto sin más, hoy tendría en mi proyecto una línea
que no sé explicar Y si resultara que está mal, tampoco me habría dado cuenta

Al final la responsabilidad del código es mía, no de Copilot Él propone, pero el que entrega
el proyecto y el que lo tiene que explicar soy yo
