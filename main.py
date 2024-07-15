import controller as c
menuOptions = """
1. Add Product Data
2. View All Product
3. View Individual Product
4. Delete Product
5. Update Product
6. Close Menu
Please Choose one from (1-6) : """
while True:
    userChoice = int(input(f"{menuOptions}"))
    if userChoice == 1:
        c.addproduct()

    elif userChoice == 2:
        c.viewproduct()

    elif userChoice == 3:
        c.viewSingle()

    elif userChoice == 4:
        c.deleteByid()
    elif userChoice == 5:
        c.updateProduct()