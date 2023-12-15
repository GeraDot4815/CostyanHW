import datetime
import maya
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

COSTSORTS = ["min", "max"]

def enter_date_with_check(inptip="Введите дату покупки --> "):
    tip = co.print_with_lines("Рекомендуемый формат ввода даты: ДД.ММ.ГГГГ")
    errortip = "!Неверный формат ввода даты!"

    print(tip)
    inp = co.liminput(inptip) or None
    if inp==None: return datetime.date.today().strftime("%d.%m.%Y")

    date = datetime.date
    errorflag = True

    while errorflag:
        try:
            date = maya.parse(inp).datetime().date().strftime("%d.%m.%Y")
            errorflag = False
            break
        except:
            print(errortip)
            print(tip)
            inp = co.liminput(inptip)
    return date
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
    date = enter_date_with_check(datetip)

    idx=len(storage.productlist)
    pr = Product(idx, name, cost, category, date)
    storage.add_product(pr)

    print(co.print_with_lines("Товар успешно добавлен!"))
    if (storage.autotab[0]): auto_view_tab(storage.autotab)
def delete_element():
    view_all_table()
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
    if (storage.autotab[0]): auto_view_tab(storage.autotab)

def view_all_table():
    table=[]
    for pr in storage.productlist:
        el=[pr.id, pr.name, pr.cost, pr.category, pr.date]
        table.append(el)
    print(tabulate(table, headers=TABHEADERS))

def cost_sort_settings():
    tip=co.print_with_lines("Min - сортировать по возрастанию цены"+'\n'+
                            "Max - сортировать по убыванию цены")
    inptip="Введите команду --> "
    errortip="!Команда введена неверно!"

    print(tip)
    inp=co.liminput(inptip, 3).lower()

    while not inp in COSTSORTS:
        print(errortip)
        print(tip)
        inp = co.liminput(inptip, 3).lower()

    storage.filtercost=inp

    view_sort_cost(storage.filtercost)
def view_sort_cost(filter): #Min/max
    idxs=[]
    for pr in storage.productlist:
        idxs.append([pr.id, pr.cost])

    if filter==COSTSORTS[0]: #Min
        idxs.sort(key=lambda x:x[1], reverse=False)
    elif filter==COSTSORTS[1]:
        idxs.sort(key=lambda x:x[1],reverse=True)

    table=[]
    for i in idxs:
        pr=storage.productlist[i[0]]
        el=[pr.id, pr.name, pr.cost, pr.category, pr.date]
        table.append(el)
    print(tabulate(table, headers=TABHEADERS))
def date_sort_settings():
    dates=[]
    for pr in storage.productlist:
        dates.append(pr.date)
    noresult = "Введенная дата не найдена"
    date=enter_date_with_check()
    if date in dates:
        storage.filterdate=date
    else:
        print(noresult)
        return
    view_sort_date(storage.filterdate)
def view_sort_date(date):
    prs = []
    for pr in storage.productlist:
        if pr.date == date:
            prs.append(pr)
    noresult=co.print_with_lines("В указанную дату не было совершено покупок"+'\n'+
                                 "Введите 'SortD', чтобы изменить настройки сортировки по дате", symbol="*",
                                 linelen=len("Введите 'SortD', чтобы изменить настройки сортировки по дате"))

    if(len(prs)==0):
        print(noresult)
        return

    table = []
    for pr in prs:
        el = [pr.id, pr.name, pr.cost, pr.category, pr.date]
        table.append(el)
    print(tabulate(table, headers=TABHEADERS))

def category_sort_settings():
    EXITCMDS=["x","х"]
    categories=[]
    for pr in storage.productlist:
        categories.append(pr.category)
    def print_all_cats(categories):
        linelen=10
        print("Доступные для сортировки категории:"+'\n'+
              '-'*linelen)
        for ct in categories:
            print(ct)
        print('-'*linelen)
        print('\n'+"Для выхода из функции введите 'X'")

    inptip="Введите команду --> "
    errortip="!Введенная категория не найдена!"

    print_all_cats(categories)
    inp=co.liminput(inptip)

    if inp.lower() in EXITCMDS: return

    while not inp in categories:
        print(errortip)
        print_all_cats(categories)
        inp = co.liminput(inptip)

    storage.filtercategory=inp

    view_sort_category(storage.filtercategory)
def view_sort_category(category):
    prs = []
    for pr in storage.productlist:
        if pr.category==category:
            prs.append(pr)

    table = []
    for pr in prs:
        el = [pr.id, pr.name, pr.cost, pr.category, pr.date]
        table.append(el)
    print(tabulate(table, headers=TABHEADERS))

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
    inp=co.liminput(inptip, 1).lower()
    while not inp in valids:
        print(wrongtip)
        inp=co.liminput(inptip, 1).lower()
    canview=False if inp=="f" else True

    storage.autotab=(canview, inp)
    auto_view_tab(storage.autotab)
def auto_view_tab(settings):
    if settings[0]==False: return
    elif settings[1]=="a":
        view_all_table()
    elif settings[1]=="c":
        view_sort_cost(storage.filtercost)
    elif settings[1]=="k":
        view_sort_category(storage.filtercategory)
    elif settings[1]=="d":
        view_sort_date(storage.filterdate)

def exit_app():
    storage.save_data()
    exit()