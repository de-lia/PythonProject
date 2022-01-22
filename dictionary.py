item = []
item1 = {
    "name": " ",
    "price": " ",
    "quantity": " "
}
print("Available commands: ")
print("(A) Add\n(E) Edit\n(V) View\n(Q) Quit")

command = " "
while True:
    command = input("Enter a command: ")
    if command.upper() == "A":
        print("You are in add mode")

        item_name = input("Enter the name of the product: ")
        item_price = int(input("What is the unit price of your product?: "))
        item_quantity = int(input("How many products do you want to add?: "))

        new_item = {"name": item_name, "price": item_price, "quantity": item_price}
        item.append(new_item)

    elif command.upper() == "E":
        print("You are in edit mode.")

    elif command.upper() == "V":
        print("Name\t Price\t Quantity\t")
        for i in item:
            print(i["name"] + "\t" + str(i["price"]) + "\t" + str(i["quantity"]))
    elif command.upper() == "Q":
        break
    else:
        print("You have entered a wrong command.")
