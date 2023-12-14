import datetime

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
             8:"exit",#Exit
             9:"autoview"}

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

    autotip=co.print_with_lines("AutoView - выводить таблицу после ее изменения")

    advice = "Подсказка: Регистр при вводе НЕ учитывается!"
    print(viewtip)
    print(crdeltip)
    print(sorttip)
    print(saveexittip)
    print(autotip)
    print(advice)

def add_element():
    def check_cost_format(cost: str):
        digits = "0123456789"
        dots = ".,"

        dcost = ""
        for i in cost:
            if i in digits or i in dots: dcost = dcost + i
        if dcost=="": return (False, -1)
        dcost = dcost.replace(",", ".")
        try:
            dcost=float(dcost)
        except ValueError:
            return (False, -1)
        return (True, dcost)

    nametip="Ведите название товара --> "

    costtip="Введите цену товара --> "
    wrongcosttip=("!Цена введена неправильно!"+'\n'+
                  "Введите цену в одном из указанных форматов"+'\n'+
                  "000"+'\n'+
                  "00.00"+'\n'+
                  "00,00"+'\n')

    categorytip="Введите категорию товара (Enter - пропустить) --> "
    datetip = "Введите дату покупки товара (Enter - сегодня) --> "

    name = co.liminput(nametip, 25)
    cost = co.liminput(costtip)
    check_result=check_cost_format(cost)
    while not check_result[0]:
        print(wrongcosttip)
        cost = co.liminput(costtip)
        check_result = check_cost_format(cost)


    cost=check_result[1]

    category = co.liminput(categorytip) or None
    date = co.liminput(datetip) or None

    idx=len(storage.productlist)
    pr = Product(idx, name, cost, category, date)
    storage.add_product(pr)

    print(co.print_with_lines("Товар успешно добавлен!"))
    if (autotab[0]): auto_view_tab(autotab)
def delete_element():
    view_table()
    tip="Введите ID или Название товара, который вы хотите удалить"
    print(tip)
    inp=co.liminput("--> ", 25)

    id=-1
    name="-"
    try:
        id=int(inp)
    except ValueError:
        name=inp
    storage.delete_product(id, name)
    if (autotab[0]): auto_view_tab(autotab)

def view_table():
    table=[]
    for pr in storage.productlist:
        el=[pr.id, pr.name, pr.cost, pr.category, pr.date]
        table.append(el)
    print(tabulate(table, headers=TABHEADERS))

filtercost="min"
def cost_sort_settings():
    global filtercost
    sort_cost(filtercost)
def sort_cost(filter): #Min/max
    pass

filterdate=datetime.date.today()
def date_sort_settings():
    global  filterdate
    sort_date(filterdate)
def sort_date(date):
    pass

filtercategory="none"
def category_sort_settings():
    global  filtercategory
    sort_category(filtercategory)
def sort_category(category):
    pass

def exit_app():
    pass

autotab=(False, "a")
def auto_view_settings():
    valids="ackdf"
    tip=co.print_with_lines("A - выводить всю таблицу"+'\n'+
                            "C - выводить с сортировкой по цене"+'\n'+
                            "K - выводить с сортировкой по категории"+'\n'+
                            "D - выводить с сортировкой по дате"+'\n'+
                            '\n'+"F - отключить автовывод", linelen=len("K - выводить с сортировкой по категории"))
    wrongtip="!Опция введена неверно!"+'\n'+"Для ввода доступны команды: A, C, K, D"
    inptip="Выберите одну из опций --> "
    print(tip)
    inp=co.liminput(inptip, 1)
    inp.lower()
    while not inp in valids:
        print(wrongtip)
        inp=co.liminput(inptip, 1)
    canview=False if inp=="f" else True
    global autotab
    autotab=(canview, inp)
    auto_view_tab(autotab)
def auto_view_tab(settings):
    if settings[0]==False: return
    elif settings[1]=="a":
        view_table()
    elif settings[1]=="c":
        cost_sort_settings()
    elif settings[1]=="k":
        category_sort_settings()
    elif settings[1]=="d":
        date_sort_settings()