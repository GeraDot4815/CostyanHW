import myfunctions as mf
from product import Product
from myfunctions import *
from tabulate import tabulate

class CustomOutput:
    LS = '-' #line symbol
    #LL = 20 #line length

    def print_with_lines(self, text: str, linelen=-1, symbol=LS, needspace=True) -> str:
        if linelen==-1 : linelen=len(text)

        output = (symbol * linelen + '\n' +
              text
              + '\n' + symbol * linelen
              + '\n'*needspace)

        return output

co=CustomOutput()

def view_menu():
    print("lovi menu")

def wait_comand_input():
    menutip=co.print_with_lines("Menu - показать доступные команды")
    inputtip="Введите команду --> "
    wronginp=co.print_with_lines("Команда введена неверно", symbol="!")

    print(menutip)
    inp = input(inputtip)
    while not inp.lower() in mf.VALIDINPUTS.values():
        print('\n'+wronginp)

        print(menutip)
        inp = input(inputtip)

    inp=inp.lower()
    process_input(inp)

def process_input(inp: str):

    if inp==mf.VALIDINPUTS.get(0):
        view_menu()
    elif inp==mf.VALIDINPUTS.get(1):
        pass
    elif inp==mf.VALIDINPUTS.get(1):
        pass
    elif inp==mf.VALIDINPUTS.get(1):
        pass
    elif inp==mf.VALIDINPUTS.get(1):
        pass
    elif inp==mf.VALIDINPUTS.get(1):
        pass
    elif inp==mf.VALIDINPUTS.get(1):
        pass
    elif inp==mf.VALIDINPUTS.get(1):
        pass



if __name__ == '__main__':
    wait_comand_input()
    cheese = Product(0, "сыр", 15)
    create_element()


