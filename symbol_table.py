# class Assembler:
#     def __init__(self):
#         self.symbol_table = {}
#         self.literal_table = {}
#         self.pool_table = []
#         self.intermediate_code = []
#     def pass_one(self, source_code):
#         lines = source_code.split('\n')
#         location_counter = 0
#         pool_index = 0
#         for line in lines:
#             tokens = line.split()
#             if len(tokens)==0:
#                 continue
#             if tokens[0]=='START':
#                 location_counter = int(tokens[1])
#                 self.intermediate_code.append(f"{location_counter} (AD,01) (C, (C, {tokens[1]})")
#                 continue
#             if tokens[0]=="END":
#                 self.intermediate_code.append(f"{location_counter} (AD, 02)")
#                 break
#             if tokens[0] == "LTORG":
#                 self.intermediate_code.append(f"{location_counter} (AD, 03)")
#                 for i in range(pool_index, len(self.pool_table)):
#                     self.literal_table[self.pool_table[i]] = location_counter
#                     location_counter+=1
#                 self.pool_table = []
#                 pool_index = len(self.literal_table)
#                 continue
#             if tokens[1] == 'DS':

#                 self.symbol_table[tokens[0]]==location_counter
#                 size = int(tokens[2])
#                 location_counter += size
#             elif tokens[1] == 'DC':
#                 self.symbol_table[tokens[0]]==location_counter
#                 location_counter += 1
#             elif tokens[1] == 'LT':
#                 self.pool_table.append(tokens[0])
#             else:
#                 self.symbol_table[tokens[0]] = location_counter
#                 location_counter += 1
#             self.intermediate_code.append(f"{location_counter}({tokens[1]},{tokens[0]})")

#     def pass_two(self, source_code):
#         lines = source_code.split('\n')
#         location_counter = 0
#         for line in lines:
#             tokens = line.split()
#             if len(tokens) == 0:
#                 continue
#             if tokens[0]=='START':
#                 location_counter = int(tokens[1])
#                 continue
#             if tokens[0]=='END':
#                 break
#             if tokens[1] == 'DS' or tokens[1] == 'DC':
#                 location_counter += int(tokens[2])
#             else:
#                 location_counter +=1

#     def print_tables(self):
#         print("Symbol Table:")
#         print(self.symbol_table)
#         print("Literal Table:")
#         print(self.literal_table)
#         print("Pool Table:")
#         print(self.pool_table)
#         print("Intermediate Code:")
#         for code in self.intermediate_code:
#             print(code)
# if __name__ == "__main__":
#         assembler = Assembler()
#         source_code = """
#         START 100
#         MOV A, 10
#         ADD B, A
#         LT 5

#         DS C, 1
#         END
#          START 180
#  READ M
#  READ N
# LOOP MOVER AREG, M
#  MOVER BREG, N
#  COMP BREG, =’200’
#  BC GT, LOOP
# BACK SUB AREG, M
#  COMP AREG, =’500’
#  BC LT, BACK
#  STOP
# M DS 1
# N DS 1
#  END
#         """
#         assembler.pass_one(source_code)
#         assembler.pass_two(source_code)
#         assembler.print_tables()
def first_pass(source_code):
    symbol_table = {}
    location_counter = 0

    for line in source_code:
        parts = line.split()

        if len(parts) == 0:
            continue

        if parts[0] == 'START':
            location_counter = int(parts[1])
        elif parts[0] != 'END':
            if parts[0] != 'DS':
                symbol_table[parts[0]] = location_counter
                location_counter += 1
            elif parts[0] == 'DS':
                symbol_table[parts[1]] = location_counter
                location_counter += int(parts[2])

    return symbol_table

def second_pass(source_code, symbol_table):
    symbol_table_with_address = {}

    for line in source_code:
        parts = line.split()

        if len(parts) == 0:
            continue

        if parts[0] != 'START' and parts[0] != 'END':
            if parts[0] != 'DS':
                address = symbol_table[parts[0]]
                symbol_table_with_address[parts[0]] = address
            elif parts[0] == 'DS':
                address = symbol_table[parts[1]]
                symbol_table_with_address[parts[1]] = address

    return symbol_table_with_address

def generate_symbol_table(source_code):
    symbol_table = first_pass(source_code)
    symbol_table_with_address = second_pass(source_code, symbol_table)
    return symbol_table_with_address

source_code = [
    "START 180",
    "READ M",
    "READ N",
    "LOOP MOVER AREG, M",
    "MOVER BREG, N",
    "COMP BREG, =’200’",
    "BC GT, LOOP",
    "BACK SUB AREG, M",
    "COMP AREG, =’500’",
    "BC LT, BACK",
    "STOP",
    "M DS 1",
    "N DS 1",
    "END"
]

symbol_table = generate_symbol_table(source_code)

print("Symbol Table:")
for symbol, address in symbol_table.items():
    print(f"{symbol} : {address}")

