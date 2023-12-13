import customoutput as co
import storage
from product import Product
from tabulate import tabulate

TABHEADERS=["ID", "Название", "Цена", "Категория", "Дата"]

VALIDINPUTS={0:"menu", #Menu
             1:"add", #Add
             2:"delete", #Delete
             3:"view", #View
             4:"sortk", #SortK
             5:"sortd", #SortD
             6:"sortc", #SortC
             7:"save", #Save
             8:"exit"} #Exit

def view_menu():
    viewtip=co.print_with_lines("View - вывести всю таблицу ваших продуктов", symbol="=")

    sorttip = co.print_with_lines("SortC - сортировать по цене"+
                                  '\n'+"SortD - сортировать по дате"+
                                  '\n'+"SortK - сортировать по категории")

    crdeltip = co.print_with_lines("Add - добавить новый продукт в таблицу"+
                                   '\n'+"Delete - удалить какой-то продукт из таблицы",
                                   symbol='*')

    saveexittip=co.print_with_lines("Save - сохранить данные"+
                                    '\n'+"Exit - выйти из приложения, сохранив данные",
                                    symbol='!')

    advice = "Подсказка: Регистр при вводе НЕ учитывается!"
    print(viewtip)
    print(crdeltip)
    print(sorttip)
    print(saveexittip)
    print(advice)

def add_element():
    def check_cost_format(cost: str):
        digits = "0123456789"
        dots = ".,"

        dcost = ""
        for i in cost:
            if i in digits or i in dots: dcost = dcost + i

        chkcost=""
        if(dcost!=""): chkcost = dcost.replace(dots[0], "")
        if(dcost!=""): chkcost = chkcost.replace(dots[0], "")

        if chkcost == "":
            return False
        else:
            return True

    nametip="Ведите название товара --> "

    costtip="Введите цену товара --> "
    wrongcosttip=("!Цена введена неправильно!"+'\n'+
                  "Введите цену в одном из указанных форматов"+'\n'+
                  "000"+'\n'+
                  "00.00"+'\n'+
                  "00,00"+'\n')

    categorytip="Введите категорию товара (Enter - пропустить) --> "
    datetip = "Введите дату покупки товара (Enter - сегодня) --> "

    name = input(nametip)
    cost = input(costtip)
    while not check_cost_format(cost):
        print(wrongcosttip)
        cost = input(costtip)
        check_cost_format(cost)

    cost=cost.replace(",", ".")
    cost=float(cost)

    category = input(categorytip) or None
    date = input(datetip) or None

    idx=len(storage.productlist)
    pr = Product(idx, name, cost, category, date)
    storage.add_product(pr)

    print(co.print_with_lines("Товар успешно добавлен!"))
def delete_element():
    pass

def view_table():
    table=[]
    for pr in storage.productlist:
        el=[pr.id, pr.name, pr.cost, pr.category, pr.date]
        table.append(el)
    print(tabulate(table, headers=TABHEADERS))

def sort_cost():
    pass
def sort_date():
    pass
def sort_category():
    pass

def save_data():
    pass
def exit_app():
    pass