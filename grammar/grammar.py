class Grammar:
    def __init__(self):
        self.productions = {}  # {A: [[symbols], [symbols]]}

    def add_production(self, non_terminal, production):
        if non_terminal not in self.productions:
            self.productions[non_terminal] = []
        self.productions[non_terminal].append(production)

    def get_productions(self, non_terminal):
        return self.productions.get(non_terminal, [])

    def is_non_terminal(self, symbol):
        return symbol in self.productions