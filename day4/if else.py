products = ['heels','shirts','hand bags','laptops','facewash']
search = input("enter the item")

if search in products:
    print(f"{search} in found!\ngo and shop now!!!")
else:
    print(f"{search} not found!\nlook for other things")
