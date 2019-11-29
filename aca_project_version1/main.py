import file_parser
from file_parser import file_parser, list1

cycle = 0
instruction = None
def instruction_decode(inst):
    instruction = inst
    print("Decoding instruction ", inst)

def instruction_fetch():
    print("Fetching an instruction")
    print(list1)
    for i in range(len(list1)):
        inst = list1[i]
        print(inst)
        instruction_decode(inst)

def main():
    global cycle
    i = 1
    # file_parser()
    while i == 1:
        cycle += 1
        print("cycle = ", cycle)
        intstruction = instruction_fetch()
        break
main()