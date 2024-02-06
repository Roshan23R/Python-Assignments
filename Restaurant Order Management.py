products = {
    "A": 10,
    "B": 10,
    "C": 10,
    "D": 10,
    "E": 10,
    "F": 10,
    "G": 10,
    "H": 10
}
 
orders = []
 
def placeOrder(*prod):
    print(prod)
    for a, b in prod:
        if a not in products:
            print("this item is not served")
        else:
            orders.append({
                "name": a,
                "quantity": int(b),
                "price": products[a]
            })
 
def displayCart():
    print(orders)
       
def removeProduct(*prod):
    print(prod)
    for item in prod[0]:
        print(item)
        for dict in orders:
            if item == dict["name"]:
                orders.remove(dict)
 
def totalPrice():
    cost = 0
    for dict in orders:
        cost += dict["price"]
    return cost
 
print("Welcome to Restaurant Order Management System!")
 
choices = {
    1: "Place Order",
    2: "Display Order Details",
    3: "Remove Items from Order",
    4: "Calculate Total Cost",
    5: "Exit"
}
 
print(choices)
 
 
while True:
    num = int(input("Enter your choice "))
 
    if num == 1:
        prod = input("enter the name and quantity of the product ")
        placeOrder(prod.split(","))
 
    elif num == 2:
        displayCart()
 
    elif num == 3:
        prod = input("enter the name of the product to remove ")
        removeProduct(prod.split(", "))
 
    elif num == 4:
        print(totalPrice())
 
    else:
        break