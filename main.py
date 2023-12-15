import myfunctions as mf
import storage
from product import Product
import customoutput as co

def wait_comand_input():
    menutip=co.print_with_lines("Menu - показать доступные команды")
    inputtip="Введите команду --> "
    wronginp=co.print_with_lines("Команда введена неверно", symbol="!")

    print(menutip)
    inp = co.liminput(inputtip)
    while not inp.lower() in mf.VALIDINPUTS.values():
        print('\n'+wronginp)

        print(menutip)
        inp = co.liminput(inputtip)

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
        mf.view_all_table()
    elif inp==mf.VALIDINPUTS.get(4):
        mf.category_sort_settings()
    elif inp==mf.VALIDINPUTS.get(5):
        mf.date_sort_settings()
    elif inp==mf.VALIDINPUTS.get(6):
        mf.cost_sort_settings()
    elif inp==mf.VALIDINPUTS.get(7):
        storage.save_data()
    elif inp==mf.VALIDINPUTS.get(8):
        mf.exit_app()
    elif inp==mf.VALIDINPUTS.get(9):
        mf.auto_view_settings()

    wait_comand_input()



if __name__ == '__main__':
    cheese = Product(0, "сыр", 15, "молочная")
    storage.add_product(cheese)
    ch = Product(1, "чипсы", 30, "вкусняха")
    storage.add_product(ch)
    fh = Product(2, "рыба", 100, "буэээ", "11.03.02")
    storage.add_product(fh)
    kl = Product(3, "колбаса", 1, "вкусняха", "23.09.12")
    storage.add_product(kl)
    wait_comand_input()



