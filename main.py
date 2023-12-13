import myfunctions as mf
import storage
from product import Product
import customoutput as co

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
        mf.view_menu()
    elif inp==mf.VALIDINPUTS.get(1):
        mf.add_element()
    elif inp==mf.VALIDINPUTS.get(2):
        mf.delete_element()
    elif inp==mf.VALIDINPUTS.get(3):
        mf.view_table()
    elif inp==mf.VALIDINPUTS.get(4):
        mf.sort_category()
    elif inp==mf.VALIDINPUTS.get(5):
        mf.sort_date()
    elif inp==mf.VALIDINPUTS.get(6):
        mf.sort_cost()
    elif inp==mf.VALIDINPUTS.get(7):
        mf.save_data()
    elif inp==mf.VALIDINPUTS.get(8):
        mf.exit_app()

    wait_comand_input()



if __name__ == '__main__':
    cheese = Product(0, "сыр", 15)
    storage.add_product(cheese)
    wait_comand_input()



