product_names = ["Ultrasonic range finder",
                 "Servo motor",
                 "Servo controller",
                 "Microcontroller board",
                 "Laser range finder",
                 "Lithium polymer battery"]
product_prices = [2.50, 14.99, 44.95, 34.95, 149.99, 8.99]
product_quantities = [4, 10, 5, 7, 2, 8]


def print_stock():
    print("\nAvailable Products")
    print("------------------")
    for i in range(0, len(product_names)):
        if product_quantities[i] > 0:
            print(
                f"{i}) {product_names[i]} ${product_prices[i]} {product_quantities[i]} left")
    print()


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input(
            "Enter product UD and quantity you wish to buy separated by a space: ").split(" ")

        if vals[0].lower() == "quit":
            break

        prod_id = vals[0]
        quantity = vals[1]

        if product_quantities[prod_id] >= quantity:
            price = product_quantities[prod_id] * quantity
            if cash >= price:
                cash -= price
                print(f"You purchased {quantity} {product_names[prod_id]}.")
                print("You have ${0:.2f} remaining".format(cash))
            else:
                print("Sorry you cannot afford that product.")
        else:
            print("Sorry we do not carry that product or we are out of stock.")


main()
