print("Enter your math score: ")
math_score = int(input())

if 95 <= math_score <= 100:
    print("A")
elif 90 <= math_score < 95:
    print("B")
elif 85 <= math_score < 90:
    print("C")
elif 80 <= math_score < 85:
    print("D")
elif 75 <= math_score < 80:
    print("E")
else:
    print("Invalid Input!")