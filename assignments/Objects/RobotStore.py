import Product as p

p1 = p.Product('ultrasonic range finder', 2.50, 4)
p2 = p.Product('Servo motor', 14.00, 10)
p3 = p.Product('Servo controller', 44.95, 5)
p4 = p.Product('Micro controller board', 34.99, 7)
p5 = p.Product('Laser range finder', 149.99, 2)
p6 = p.Product('Lithium polymer battery', 8.99, 8)

storeInventory = [p1, p2, p3, p4, p5, p6]


def print_stock():
    print("\nAvailable Products")
    print("------------------")
    for i in range(0, len(storeInventory)):
        # access the quantity member of the Product object
        if storeInventory[i]._quantiy > 0:
            print(str(i) + ")",
                  storeInventory[i]._name, "$", storeInventory[i]._price)
            print()


def main():
    cash = float(input("How much money do you have?"))
    while cash > 0:
        print_stock()
        vals = input(
            "Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit":
            break

        prod_id = int(vals[0])
        count = int(vals[1])

        # if there is enough in inventory
        if storeInventory[prod_id]._quantiy >= count:
            if cash >= storeInventory[prod_id]._price:
                storeInventory[prod_id]._price * count
                cash -= storeInventory[prod_id]._price * count
                print("You purchased", count, " ",
                      storeInventory[prod_id]._price, ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")

        # handle if product is sold out
        else:
            print("Sorry, we are sold out of", storeInventory[prod_id]._name)


main()
