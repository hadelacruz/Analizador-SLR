from grammar.grammar import Grammar
from lr0.item import Item
from lr0.closure import closure
from utils.printer import print_items


def build_grammar_class():
    grammar = Grammar()
    grammar.add_production("E'", ["E"])
    grammar.add_production("E", ["E", "+", "T"])
    grammar.add_production("E", ["T"])
    grammar.add_production("T", ["T", "*", "F"])
    grammar.add_production("T", ["F"])
    grammar.add_production("F", ["(", "E", ")"])
    grammar.add_production("F", ["id"])
    return grammar


def build_grammar_prob1():
    grammar = Grammar()
    grammar.add_production("S'", ["S"])
    grammar.add_production("S", ["S", "S", "+"])
    grammar.add_production("S", ["S", "S", "*"])
    grammar.add_production("S", ["a"])
    return grammar


def manual_grammar_input():
    grammar = Grammar()
    print("\n--- 1. Ingresar Gramática ---")
    while True:
        left = input("Lado izquierdo (No-Terminal): ").strip()
        if not left:
            print("El lado izquierdo no puede estar vacío. Intente de nuevo.")
            continue
        right_str = input("Lado derecho (símbolos separados por un espacio, ej: E + T): ").strip()
        right = right_str.split() if right_str else []
        grammar.add_production(left, right)
        print(f"=> Producción agregada: {left} -> {' '.join(right)}\n")
        
        continuar = input("¿Desea agregar otra producción? (s/n): ").strip().lower()
        if continuar != 's':
            break
            
    return grammar


def manual_input(grammar):
    items = set()
    print("\n--- 2. Ingresar Conjunto de Ítems Iniciales ---")
    while True:
        left = input("Lado izquierdo: ").strip()
        if not left:
            print("El lado izquierdo no puede estar vacío. Intente de nuevo.")
            continue
        right_str = input("Lado derecho (símbolos separados por un espacio, ej: E + T): ").strip()
        right = right_str.split() if right_str else []
        try:
            dot = int(input(f"Posición del punto (0 a {len(right)}): ").strip())
            items.add(Item(left, right, dot))
            print("=> Ítem agregado.\n")
        except ValueError:
            print("=> Posición inválida. Intente de nuevo.\n")
            continue

        continuar = input("¿Desea agregar otro ítem al conjunto inicial? (s/n): ").strip().lower()
        if continuar != 's':
            break

    if not items:
        print("No ingresó ningún ítem. Cancelando y volviendo al menú principal...\n")
        return

    print_items("Ítem(s) inicial(es)", items)
    result = closure(grammar, items)
    print_items("Cerradura final", result)


def run_tests():
    print("\n" + "="*40)
    print("PRUEBA 1: Gramática de Clase (Estado I0)")
    print("="*40)
    grammar_class = build_grammar_class()
    items_class = {Item("E'", ["E"], 0)}
    print_items("Ítem(s) inicial(es)", items_class)
    print_items("Cerradura final", closure(grammar_class, items_class))

    print("\n" + "="*40)
    print("PRUEBA 2: Problema 1 (S -> SS+ | SS* | a) (Estado I0)")
    print("="*40)
    grammar_prob1 = build_grammar_prob1()
    items_prob1 = {Item("S'", ["S"], 0)}
    print_items("Ítem(s) inicial(es)", items_prob1)
    print_items("Cerradura final", closure(grammar_prob1, items_prob1))


def main():
    while True:
        print("\n" + "-"*35)
        print("    MENÚ DE CERRADURA LR(0)    ")
        print("-"*35)
        print("1. Ejecutar pruebas predefinidas (Clase y Problema 1)")
        print("2. Entrada manual (Gramática e Ítems)")
        print("3. Salir")
        opc = input("Opción: ").strip()

        if opc == '1':
            run_tests()
        elif opc == '2':
            custom_grammar = manual_grammar_input()
            manual_input(custom_grammar)
        elif opc == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()