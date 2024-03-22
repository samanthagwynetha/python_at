def calculate_sum(num1, num2):
    return num1 + num2
def calculate_def(num1, num2):
    return num1 / num2

print("1: Add")
print("2: Divide")

select = int(input("Select operation 1 or 2: "))
num1= int(input("num 1: "))
num2 = int(input("num 2: "))

if select == 1:
    print("The sum is: ",calculate_sum(num1, num2))
elif select == 2:
    print("The def is: ",calculate_def(num1, num2))
else:
    exit()
