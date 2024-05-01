def generate_pool_table(source_code):
    pool_table = []
    literal_count = 0

    for line in source_code:
        parts = line.split()

        if len(parts) == 0:
            continue

        if 'LTORG' in parts:
            pool_table.append((literal_count, literal_count + 1))
            literal_count += 1

        for part in parts:
            if part.startswith('='):
                literal_count += 1

    return pool_table

source_code = [
    "START 100",
    "READ A",
    "MOVER AREG, ='1'",
    "MOVEM AREG, B",
    "MOVER BREG, ='6'",
    "ADD AREG, BREG",
    "COMP AREG, A",
    "BC GT, LAST",
    "LTORG",
    "NEXT SUB AREG, ='1'",
    "MOVER CREG, B",
    "ADD CREG, ='8'",
    "MOVEM CREG, B",
    "PRINT B",
    "LAST STOP",
    "A DS 1",
    "B DS 1",
    "END"
]

pool_table = generate_pool_table(source_code)

print("Pool Table:")
for index, (start, end) in enumerate(pool_table, start=1):
    print(f"Pool {index}: From Literal {start} to Literal {end}")
