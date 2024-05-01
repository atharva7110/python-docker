def first_pass(source_code):
    literal_table = {}
    location_counter = 0

    for line in source_code:
        parts = line.split()

        if len(parts) == 0:
            continue

        if parts[0] == 'START':
            location_counter = int(parts[1])
        elif parts[0] != 'END':
            for i in range(1, len(parts)):
                if parts[i][0] == '=':
                    if parts[i] not in literal_table:
                        literal_table[parts[i]] = location_counter
                        location_counter += 1

    return literal_table

def second_pass(source_code, literal_table):
    literal_table_with_address = {}

    for line in source_code:
        parts = line.split()

        if len(parts) == 0:
            continue

        for i in range(1, len(parts)):
            if parts[i][0] == '=':
                address = literal_table[parts[i]]
                literal_table_with_address[parts[i]] = address

    return literal_table_with_address

def generate_literal_table(source_code):
    literal_table = first_pass(source_code)
    literal_table_with_address = second_pass(source_code, literal_table)
    return literal_table_with_address

source_code = [
    "START 100",
    "READ A",
    "READ B",
    "MOVER AREG, ='50'",
    "MOVER BREG, ='60'",
    "ADD AREG, BREG",
    "LOOP MOVER CREG, A",
    "ADD CREG, ='10'",
    "COMP CREG, B",
    "BC LT, LOOP",
    "NEXT SUB AREG, ='10'",
    "COMP AREG, B",
    "BC GT, NEXT",
    "STOP",
    "A DS 1",
    "B DS 1",
    "END"
]

literal_table = generate_literal_table(source_code)

print("Literal Table:")
for literal, address in literal_table.items():
    print(f"{literal} : {address}")

# Let's go through the code line by line, explaining each part:

# ```python
# def first_pass(source_code):
#     literal_table = {}
#     location_counter = 0
# ```

# - We define a function `first_pass` that takes the source code of the assembly program as input.
# - We initialize an empty dictionary `literal_table` to store literals and their addresses.
# - `location_counter` is initialized to 0, which will keep track of the memory addresses.

# ```python
#     for line in source_code:
#         parts = line.split()

#         if len(parts) == 0:
#             continue
# ```

# - We iterate through each line of the source code.
# - `parts` is obtained by splitting the line using whitespace.
# - If the length of `parts` is 0 (empty line), we skip to the next iteration.

# ```python
#         if parts[0] == 'START':
#             location_counter = int(parts[1])
# ```

# - If the line starts with "START", we set the `location_counter` to the specified starting address.

# ```python
#         elif parts[0] != 'END':
#             for i in range(1, len(parts)):
#                 if parts[i][0] == '=':
#                     if parts[i] not in literal_table:
#                         literal_table[parts[i]] = location_counter
#                         location_counter += 1
# ```

# - For lines other than "END", we loop through each part of the line.
# - If a part starts with '=', it indicates a literal.
# - We check if the literal is not already in the `literal_table`. If not, we add it to the `literal_table` with the current `location_counter` and increment `location_counter`.

# ```python
#     return literal_table
# ```

# - After iterating through all lines, we return the `literal_table` generated in the first pass.

# The second pass follows a similar structure, but instead of generating the `literal_table`, it populates it with addresses obtained from the first pass.

# The `generate_literal_table` function orchestrates the two-pass process and returns the final literal table.

# Finally, we have the source code provided as a list of strings, and we call the `generate_literal_table` function with this source code. The resulting literal table is printed out.
