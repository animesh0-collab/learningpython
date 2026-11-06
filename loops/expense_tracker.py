# A program where the user can continuously type in their daily expenses one by one. The program stores them in a list.
print("-----Welcome to the Expense Tracker!-----")
items_name=[]
items_quantity = []
items_rate = []
work = True
while work:
    names= input("Enter the name of the item (or type 'exit' to finish): \n").lower()
    if  not names.isalpha() and names != "exit":
        print("Enter valid data")
        break
    else:
        if names == "exit":
            work = False
            total_expenses = 0
            for i in range(len(items_name)):
                total_expenses += items_quantity[i] * items_rate[i]
            print(f"Your total expenses will be: {total_expenses}")



            break
        else:
            items_name.append(names)
            quantity = float(input(f"Enter the quantity of {names} purchased: \n"))
            items_quantity.append(quantity)
            rate = float(input(f"Enter the rate of a single {names} : \n"))
            items_rate.append(rate)




    
    
