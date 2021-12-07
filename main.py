# opcodes assignment
opcode = {

    "MOV": "00000",
    "ADD": "00001",
    "SUB": "00010",
    "MUL": "00011",
    "DIV": "00100",
    "REM": "00101",
    "AND": "00110",
    "OR": "00111",
    "INV": "01000",
    "INC": "01001",
    "DEC": "01010",
    "SL": "01011",
    "SR": "01100",
    "CLR": "01101",
    "PUSH": "01110",
    "POP": "01111",
    "PUSHAD": "10000",
    "POPAD": "10001",
    "WRITEINT": "10010",
    "RET": "10011"
}

# register addresses
register = {

    "R0":	"0000",
    "R1":	"0001",
    "R2":	"0010",
    "R3":	"0011",
    "R4":	"0100",
    "R5":	"0101",
    "R6":	"0110",
    "R7":	"0111",
    "R8":	"1000",
    "R9":	"1001",
    "R10":	"1010",
    "R11":	"1011",
    "R12":	"1100",
    "R13":	"1101",
    "R14":	"1110",
    "R15":	"1111"

}

# memory register addresses
memoryRegister = {

    "[R0]":	"0000",
    "[R1]":	"0001",
    "[R2]":	"0010",
    "[R3]":	"0011",
    "[R4]":	"0100",
    "[R5]":	"0101",
    "[R6]":	"0110",
    "[R7]":	"0111",
    "[R8]":	"1000",
    "[R9]":	"1001",
    "[R10]":	"1010",
    "[R11]":	"1011",
    "[R12]":	"1100",
    "[R13]":	"1101",
    "[R14]":	"1110",
    "[R15]":	"1111"

}

# o1 values
operand1 = {
    "R": "0",
    "[": "1"

}

isRun = True

# opcode o1 o2 reg1 reg2 data
commandList = ["MOV",
               "ADD",
               "SUB",
               "MUL",
               "DIV",
               "REM",
               "AND",
               "OR",
               "INV",
               "INC",
               "DEC",
               "SL",
               "SR",
               "CLR",
               "PUSH",
               "POP",
               "PUSHAD",
               "POPAD",
               "WRITEINT",
               "RET"
               ]

# start up prompt
print("Welcome To RISC simulator by Mujtaba")
print("Command list")
for i in commandList:
    print("\t"+i)

# main loop
while isRun == True:
    # convert input to uppercase
    print("Enter -1 in command to exit")
    commandInput = input("Enter command: ").upper()

    # break if exit
    if commandInput == "-1":
        print("Program Ended")
        break
    # databits set to empty string by default
    dataBits = ""

    # if command requires no operand
    if commandInput == "PUSHAD" or commandInput == "POPAD" or commandInput == "RET" or commandInput == "WRITEINT":
        print("Instruction in bits: " + opcode[commandInput] + "000 0000 0000")

        resultBin = opcode[commandInput]+"00000000000"
        print("Instructions in hex: " + hex(int(resultBin, 2))[2:])

    # else , command requires atleast one operand
    else:

        listCMDOP = commandInput.split(" ")
        operandList = listCMDOP[1].split(",")
        command = listCMDOP[0]

        opcodeBits = opcode[command]


        # assignming o1 and o2
        o1Bit = operand1[operandList[0][0]]

        if (command == "MOV" or command == "ADD" or command == "SUB" or command == "AND" or command == "OR"):
            # assigning o2 in binary operations
            if operandList[1][0] == "R":
                o2Bits = "00"
            elif operandList[1][0] == "[":
                o2Bits = "01"
            elif operandList[1][0].isnumeric():
                o2Bits = "10"
            else:
                o2Bits = "11"
        else:
            # if empty operand 2
            o2Bits = "11"

        if o1Bit == "0": # operand 1 is register
            firstOperandBits = register[operandList[0]]
        else:
            firstOperandBits = memoryRegister[operandList[0]]

        # assign second operand address
        if o2Bits == "00":
            secondOperandBits = register[operandList[1]]
        elif o2Bits == "01":
            secondOperandBits = memoryRegister[operandList[1]]
        elif o2Bits == "10":

            # convert decimal data to binary and store in string
            # padding of 0s till 16 bits
            decNumber = int(operandList[1])
            binNumber = str(bin(int(decNumber))[2:].zfill(16))
            secondOperandBits = "0000"
            dataBits = binNumber

        else:
            secondOperandBits = "0000"

        # make one binary string of all result

        # opcode o1 o2 reg1 reg2 data
        resultBin = opcodeBits+o1Bit+o2Bits+firstOperandBits+secondOperandBits+dataBits

        resultString = "Instruction in bits: " + opcodeBits + " " + o1Bit + \
            " " + o2Bits + " " + firstOperandBits + " " + secondOperandBits + " " + dataBits

        #print in bianry and hex
        print(resultString)

        # if no data bits dont append 0s
        if dataBits == "":
            print("Instructions in hex: " +
                  hex(int(resultBin, 2))[2:])
        else:
            print("Instructions in hex: " +
                  hex(int(resultBin, 2))[2:].zfill(8))
