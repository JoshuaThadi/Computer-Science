'''
Program for generating derivation sequence/ language for the given sequence of productions.
'''

def cyk_parse(cfg, input_string):
    """Parse the input string using the CYK algorithm.
    Returns a tuple (is_in_language, parse_table)."""

    n = len(input_string)

    # Initialize the parse table with empty sets
    table = [[set() for _ in range(n - i)] for i in range(n)]

    # Fill the table for substrings of length 1
    for i, char in enumerate(input_string):
        for lhs, productions in cfg.items():
            for production in productions:
                if production == [char]:
                    table[0][i].add(lhs)

    # Fill the table for substrings of length >1
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            for partition in range(1, length):
                left_cell = table[partition - 1][start]
                right_cell = table[length - partition - 1][start + partition]

                for lhs, productions in cfg.items():
                    for production in productions:
                        if len(production) == 2:
                            B, C = production
                            if B in left_cell and C in right_cell:
                                table[length - 1][start].add(lhs)

    is_in_language = 'S' in table[-1][0]
    return is_in_language, table

def generate_derivation_sequence(parse_table, input_string, cfg):
    n = len(input_string)
    if 'S' not in parse_table[-1][0]:
        return None

    def backtrack(symbol, start, length):
        if length == 1:
            return [(symbol, input_string[start])]

        for partition in range(1, length):
            left_cell = parse_table[partition - 1][start]
            right_cell = parse_table[length - partition - 1][start + partition]

            for production in cfg.get(symbol, []):
                if len(production) == 2:
                    B, C = production
                    if B in left_cell and C in right_cell:
                        left_derivation = backtrack(B, start, partition)
                        right_derivation = backtrack(C, start + partition, length - partition)
                        return [(symbol, B + C)] + left_derivation + right_derivation

        return []

    derivation_sequence = backtrack('S', 0, n)
    return derivation_sequence

cfg = {
    'S': [['A', 'B'], ['B', 'C']],
    'A': [['B', 'A'], ['a']],
    'B': [['c'], ['C', 'B'], ['b']],
    'C': [['A', 'B'], ['a']]
}

input_string = input("Enter the string to check: ")

is_in_language, parse_table = cyk_parse(cfg, input_string)

if is_in_language:
    print("The string is in the language.")
    derivation_sequence = generate_derivation_sequence(parse_table, input_string, cfg)

    if derivation_sequence:
        print("Derivation sequence:")
        for step in derivation_sequence:
            print(f"{step[0]} -> {step[1]}")
    else:
        print("No derivation sequence found.")
else:
    print("The string is not in the language.")
