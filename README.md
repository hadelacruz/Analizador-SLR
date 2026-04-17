# Proyecto SLR - Cerradura LR(0)

## Descripción
Este proyecto implementa la función CERRADURA (closure) para ítems LR(0), como parte del análisis sintáctico SLR. Permite ingresar conjuntos de ítems y determinar todas las demás producciones que pertenecen a la misma cerradura, según el cálculo iterativo requerido.

## Video Demostrativo
🔗 [Ver Video en YouTube](https://youtu.be/ehOEoI3ApWs)

Se soportan las siguientes gramáticas precargadas:
1. **Gramática de Clase**:
   ```
   E -> E + T | T
   T -> T * F | F
   F -> ( E ) | id
   ```
2. **Problema 1**:
   ```
   S -> S S + | S S * | a
   ```

## Estructura
- `grammar/`: Manejo interno y registro de las producciones de las gramáticas (símbolos terminales y no terminales).
- `lr0/`: Implementación fundamental (`Item` y función `closure()`).
- `utils/`: Funciones para imprimir la información en formato leíble.
- `main.py`: Menú interactivo y ejecución principal de todas las pruebas.

## Ejecución y Uso

Para ejecutar el programa, abre la terminal y usa:

```bash
python main.py
```

Al abrirlo te encontrarás con un menú interactivo con dos opciones principales:
1. **Ejecutar pruebas predefinidas**: Evaluará automáticamente el estado inicial (`I0`) con el punto al inicio, mostrando el desglose paso a paso de la cerradura tanto para la gramática de la clase como para la gramática del Problema 1.
2. **Entrada manual (Gramática e Ítems)**: Te permite probar el algoritmo LR(0) con cualquier gramática que desees crear desde cero.
   - **Paso 1 (Tu Gramática):** El programa te pedirá ingresar el lado izquierdo (ej: `A`) y el lado derecho separado por espacios (ej: `A + T`). Te irá preguntando `(s/n)` si deseas seguir agregando reglas. *Recuerda*: para calcular un Estado $I_0$ real, es buena práctica agregar primero tu producción extendida (Ej: `A' -> A`).
   - **Paso 2 (Tu Ítem Inicial):** Una vez construida la gramática, ingresarás tu ítem "semilla" para iniciar la cerradura LR(0). Indicarás lado izquierdo, lado derecho, y la posición del punto (ej: `0` para que esté al inicio). El calculador hará el resto de forma iterativa y en cascada.

