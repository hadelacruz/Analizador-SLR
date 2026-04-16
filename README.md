# Proyecto SLR - Cerradura LR(0)

## Descripción
Este proyecto implementa la función CERRADURA (closure) para ítems LR(0), como parte del análisis sintáctico SLR. Permite ingresar conjuntos de ítems y determinar todas las demás producciones que pertenecen a la misma cerradura, según el cálculo iterativo requerido.

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

Al abrirlo te encontrarás con un menú amigable con dos opciones principales:
1. **Ejecutar pruebas predefinidas**: Evaluará automáticamente el estado `I0` con punto al inicio tanto para la gramática de la clase como para la gramática del Problema 1.
2. **Entrada manual de ítems**: Entrarás en un modo para probar el comportamiento de la función iterativa. 
   - Se te pedirá elegir la gramática (Clase o Problema 1).
   - Puedes colocar cualquier lado izquierdo (ej: `E`), el derecho separado por espacios (ej: `E + T`), y la posición que quieras para el "Punto" de análisis (dot).
   - Termina presionando `Enter` sin escribir lado izquierdo para iniciar el cálculo.