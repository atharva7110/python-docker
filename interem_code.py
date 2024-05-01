def generate_intermediate_code(source_code):
    intermediate_code = []

    for line in source_code:
        parts = line.split()

        if len(parts) == 0:
            continue

        if parts[0] == 'START':
            intermediate_code.append(("START", int(parts[1])))
        elif parts[0] == 'READ':
            intermediate_code.append(("READ", parts[1]))
        elif parts[0] == 'MOVER':
            intermediate_code.append(("MOVER", parts[1], parts[2]))
        elif parts[0] == 'SUB':
            intermediate_code.append(("SUB", parts[1], parts[2]))
        elif parts[0] == 'STOP':
            intermediate_code.append(("STOP",))
        elif parts[0] == 'DS':
            intermediate_code.append(("DS", parts[1], int(parts[2])))
        elif parts[0] == 'END':
            intermediate_code.append(("END",))

    return intermediate_code

source_code = [
    "START 100",
    "READ A",
    "READ B",
    "MOVER AREG, A",
    "SUB AREG, B",
    "STOP",
    "A DS 1",
    "B DS 1",
    "END"
]

intermediate_code = generate_intermediate_code(source_code)

print("Intermediate Code:")
for instruction in intermediate_code:
    print(instruction)
