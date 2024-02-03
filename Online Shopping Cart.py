def shop():
    ''' Welcome to the Online Shopping Cart!
        1. Add Products
        2. Display Cart
        3. Remove Product
        4. Calculate Total Price
        5. Checkout
        6. Exit
    '''

def addProduct(name):
    userCart.append(name)
    print(name , "is added to your cart.")

def displayCart():
    if len(userCart) == 0:
        print("cart is empty!!")
    else:
        print("Your Cart has following items: ")
        for item in userCart:
            print(item)

def removeProduct(name):
    userCart.remove(name)
    print(name , "is removed from cart.")

def calculateTotal():
    total = 0
    for item in userCart:
        price = int(productList[item])
        if price is not None:
            total += price
        else:
            print(f"Warning: {item} not found in the product list.")

    print("Total Price: ", total)


def checkout():
    print("Your Cart has following items: ")
    for item in userCart:
        print(item,":", productList[item])
    calculateTotal()
    userCart.clear()

    print("Your cart products are checkout")

    
def doTask(choice):
    if choice == '1':
        name = input("Enter product name: ")
        addProduct(name)
    elif choice == '2':
        displayCart()
    elif choice == '3':
        name = input("Enter product name which you want to remove: ")
        removeProduct(name)
    elif choice == '4':
        calculateTotal()
    elif choice == '5':
        checkout()
    else:
        exit()
    

def main():
    global userCart
    global productList
    userCart = []
    productList = {'Laptop': 1200, 'SmartPhone': 600, 'Earphone': 200}

    print(shop.__doc__)
    while True:
        choice = input("Enter your Choice (1-6): ")
        doTask(choice)


main()
