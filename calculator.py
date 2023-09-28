import re

print("Master Calculator")
print('Type "exit" to exit')

previous = 0
run = True


def perform_math():
    global run, previous
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == "exit":
        print("Goodbye, human.")
        run = False
    else:
        equation = re.sub("[a-zA-Z,.:;`() ]", "", equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()
