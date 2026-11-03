#Multiplication Table Generator
num = float(input("Enter any number to gernerate its multiplication table: "))
work = True
while work:
    for i in range(1, 11):
        print(f"{num} ❌ {i} = {num*i} ")
    num = input("Enter another number or 'exit' to quit: ")
    if num != "exit":
        num = float(num)
    else:
        work = False
        print("Exiting the program...")
            