import itertools

# Function to input values for a 3-variable Karnaugh map
def input_karnaugh_map():
    k_map = {}
    for i in range(2):
        for j in range(2):
            for k in range(2):
                value = int(input(f"Enter the value at ({i}, {j}, {k}): "))
                k_map[(i, j, k)] = value
    return k_map

# Function to simplify a 3-variable Karnaugh map
def simplify_karnaugh_map(k_map):
    simplified_terms = []

    for minterm, value in k_map.items():
        if value == 1:
            simplified_terms.append(minterm)

    simplified_expression = []
    
    for term in simplified_terms:
        variables = []
        for i, value in enumerate(term):
            if value == 1:
                variables.append(chr(ord('A') + i))
            elif value == 0:
                variables.append(f"~{chr(ord('A') + i)}")
        simplified_expression.append(" . ".join(variables))

    return " + ".join(simplified_expression)

def main():
    print("Enter values for the 3-variable Karnaugh map (0 or 1):")
    k_map = input_karnaugh_map()
    
    simplified_expression = simplify_karnaugh_map(k_map)
    
    print("\nSimplified Boolean Expression:")
    print(simplified_expression)

if __name__ == "__main__":
    main()

