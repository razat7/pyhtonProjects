from product import Product
import csv

#--------------add product----------------   
def addproduct():
    pData = Product(id="", name="", price=0, qty=0)
    pData.id = int(input("Enter the ID for Product :"))
    pData.name = input(f"Enter the name of Product {pData.id} : ")
    pData.price = float(input(f"Enter the price of {pData.name} : "))
    pData.qty = float(input(f"Enter the {pData.name}'s quantity : "))

    file = open("product.csv", 'a') #a = append data
    file.write(f"{pData.id},{pData.name},{pData.price},{pData.qty}\n")
    file.close() 

#--------------view product----------------
def viewproduct():
    print("----------------All Product Details---------------------")
    openFile = open("product.csv", "r") #r = read data
    viewdata = openFile.read() 
    print(viewdata)
    print("-----------------------------------------------")

#--------------view single product----------------
def viewSingle():
    # Allproductlists = []
    id = input("Enter the ID Number : ")
    product_lists = csv_to_list()
    # with open("product.csv", "r")as file:
    #     productData = csv.reader(file)
    #     for row in productData:
    #         Dataslist = Product(id=row[0], name=row[1], price=float(row[2]), qty=float(row[3]))
    #         Allproductlists.append(Dataslist)
    idFound = False
    dataSingle = Product(id="", name="", price=0, qty=0)

    for p in product_lists:
        if p.id == id:
            idFound = True
            dataSingle = p
            print("Data Found")
            break
        else:
            idFound = False
    if idFound == True:
        dataSingle.display_product()
    else:
        print("No Matching Data Found*")


#--------------Convert Product into Csv ---------------
def product_to_csv(listofproduct):
    f = open ("product.csv", 'w')
    f.write("")
    f.close()
    for p in listofproduct:
        file = open("product.csv", "a")
        file.write(f"{p.id},{p.name}, {p.price}, {p.qty}\n")
        file.close()

#--------------Convert CSV into Product List ---------------
def csv_to_list():
    Allproductlists = []
    with open("product.csv", "r")as file:
            productData = csv.reader(file)
            for row in productData:
                Dataslist = Product(id=row[0], name=row[1], price=float(row[2]), qty=float(row[3]))
                Allproductlists.append(Dataslist)
    return(Allproductlists)

#--------------Delete Product ---------------
def deleteByid():
    del_id = input("Enter the id to delete : ")
    data_lists = csv_to_list()
    update_products = []

    recordfound = False
    for product in data_lists:
        if product.id == del_id:
            recordfound = True
        else:
          update_products.append(product)
    
    if recordfound == True:
        product_to_csv(update_products)
        print(f"Deleted Successfully")
    else:
        print("Something is wrong")

#--------------Update Product ---------------
def updateProduct():
    productlists = csv_to_list()
    updateID = input("Enter the ID to Update")
    datafound = False
    founddata = Product(id="", name="", price="", qty="")

    index = 0
    for i in range(len(productlists)):
        if productlists[i].id == updateID:
            datafound = True
            founddata = productlists[i]
            index = i
            break
        else:
            datafound = False

    if datafound == True:
        print("Record Found")
        founddata.display_product()
        print("Enter New Details : ")
        np = founddata
        np.id = input("Enter the New ID : ")
        np.name = input("Enter the New Name : ")
        np.price = input("Enter the New Price : ")
        np.qty = input("Enter the Quantity : ")
        productlists[index] = np
        product_to_csv(productlists)
        print("Record Updated Successfully")
    else:
        print("Data not matched with provided ID*")

