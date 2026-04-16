from lr0.item import Item

def closure(grammar, items):
    closure_set = set(items)
    added = True

    print("\nCálculo de CERRADURA:\n")

    while added:
        added = False
        new_items = set()

        for item in closure_set:
            symbol = item.next_symbol()

            if symbol and grammar.is_non_terminal(symbol):
                for prod in grammar.get_productions(symbol):
                    new_item = Item(symbol, prod, 0)

                    if new_item not in closure_set:
                        print(f"Agregado: {new_item}")
                        new_items.add(new_item)

        if new_items:
            closure_set.update(new_items)
            added = True

    return closure_set