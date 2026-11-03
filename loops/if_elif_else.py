#IF-ELIF-ELSE STATEMENT
# Grade Calculator
score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")   
elif score >= 70:
    print("You got a C!")
elif score >= 60:
    print("You got a D!")
else:
    print("You got an F!")



#Multiplication Table Generator
num = float(input("Enter any number to gernerate its multiplication table: "))
for i in range(1, 11):
    print(f"{num} ❌ {i} = {num*i} ")
            