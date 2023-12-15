import json
import datetime
from product import Product
import customoutput as co
productlist: list[Product]=[]

filtercost="min"
filterdate=datetime.date.today().strftime("%d.%m.%Y")
filtercategory="none"

autotab=(False, "a")

def add_product(pr: Product):
    productlist.append(pr)

def delete_product(id=-1, name="-"):
    errortip = co.print_with_lines("Простите, товара с таким именем или индексом не найдено", symbol="?")
    if id!=-1:
        if id<0 or len(productlist)<id:
            print(errortip)
        else:
            productlist.pop(id)
            reset_idxs()
            return
    elif name!="-":
        for i in range(len(productlist)):
            if productlist[i].name==name:
                productlist.pop(i)
                reset_idxs()
                return
        print(errortip)
    else:
        print(errortip)
def reset_idxs():
    for i in range(len(productlist)):
        productlist[i].id=i

def save_data():
    data={}

    data['products']=[]
    for pr in productlist:
        (data['products'].append
        ({
        'id': pr.id,
        'name': pr.name,
        'cost': pr.cost,
        'category': pr.category,
        'date': pr.date
        }))

    data['costfilter']=filtercost
    data['datefilter']=filterdate
    data['catfilter']=filtercategory
    data['autotab']=autotab

    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

    print("*Данные упешно соранены*")
def load_data():
    global productlist
    global filtercost
    global filterdate
    global filtercategory
    global autotab

    with open('data.txt') as json_file:
        data = json.load(json_file)
        productlist=[]
        for spr in data['products']:
            npr=Product(spr['id'], spr['name'], spr['cost'], spr['category'], spr['date'])
            productlist.append(npr)
        filtercost = data['costfilter']
        filterdate = data['datefilter']
        filtercategory = data['catfilter']
        autotab = data['autotab']

    print("*Данные упешно загружены*")