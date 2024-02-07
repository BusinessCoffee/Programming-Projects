import math

def commands(cmd):
    match cmd:
        case '?':
            print('''
                + → add a & b           \n
                - → subtract a & b      \n
                * → multiply a & b      \n 
                / → divide a & b        \n
                % → modulo a & b        \n
                ^ → a to the power of b \n
                s → square root a       \n
                | → absolute value of a \n\n
                ''')
        case _:
            print("⚠️ NOT A COMMAND ⚠️")

def errorHandler(userInput):
    inputList = userInput.split(" ")
    inputLength = inputList.__len__()
    match inputLength:
        case 1:
            commands(inputList[0])
        case 2:
            if inputList[0] == "s" or inputList[0] == "|":
                try:
                    print(calc(inputList[0], float(inputList[1]), None)+"\n")
                except:
                    print("⚠️ MUST BE A NUMBER ⚠️")
            else:
                print("⚠️ NOT A VALID ENTRY ⚠️")
        case 3:
            if inputList[2] == 0 and inputList[0] == "/":
                print("⚠️ DIVIDE BY ZERO ⚠️")
                return
            else:
                try:
                    print(calc(inputList[0], float(inputList[1]), float(inputList[2]))+"\n")
                except:
                    print("⚠️ MUST BE A NUMBER ⚠️")

def calc(op, a, b):
    match op:
        case '+':  
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case '%':
            return a % b
        case '^':
            return math.pow(a, b)
        case 's':
            return math.sqrt(a)
        case '|':
            return math.sqrt(a*a)
        
def main():
    print("? for help!")
    while True:
        userInput = input("Please choose an opperation and numbers for a & b    -   ")
        errorHandler(userInput)
    
main()