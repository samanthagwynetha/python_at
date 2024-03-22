print("Enter your grade: ")
grade = input().upper()

if grade == "A":
    print("Score range: 95-100")
elif grade == "B":
    print("Score range: 90-94")
elif grade == "C":
    print("Score range: 85-89")
elif grade == "D":
    print("Score range: 80-84")
elif grade == "E":
    print("Score range: 75-79")
else:
    print("Invalid Input!")