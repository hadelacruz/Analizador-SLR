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


def manual_input(grammar):
    items = set()
    print("\n--- Ingresar Conjunto de Ítems Iniciales ---")
    while True:
        left = input("Lado izquierdo (Deje en blanco para terminar): ").strip()
        if not left:
            if not items:
                print("Debe ingresar al menos un ítem.\n")
                continue
            break
        right_str = input("Lado derecho (símbolos separados por un espacio, ej: E + T): ").strip()
        right = right_str.split() if right_str else []
        try:
            dot = int(input(f"Posición del punto (0 a {len(right)}): ").strip())
            items.add(Item(left, right, dot))
            print("=> Ítem agregado. Ingrese otro o deje el lado izquierdo en blanco para finalizar.\n")
        except ValueError:
            print("=> Posición inválida. Intente de nuevo.\n")

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
        print("2. Entrada manual de ítems")
        print("3. Salir")
        opc = input("Opción: ").strip()

        if opc == '1':
            run_tests()
        elif opc == '2':
            print("\nSeleccione la gramática a utilizar para sus ítems:")
            print("1. Gramática de Clase (E -> E + T | T ...)")
            print("2. Gramática Problema 1 (S -> SS+ | SS* | a)")
            g_opc = input("Opción de gramática: ").strip()
            
            if g_opc == '1':
                manual_input(build_grammar_class())
            elif g_opc == '2':
                manual_input(build_grammar_prob1())
            else:
                print("Opción no válida. Volviendo al menú principal.")
        elif opc == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()