from product import Product
import customoutput as co
productlist: list[Product]=[]

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

    print("*Данные упешно соранены*")
def load_data():
    print("*Данные упешно загружены*")