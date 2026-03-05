# nested if statements in Python
age = int(input("Enter your Age: "))
weight = int(input("Enter your Weight: "))

# if condition 1
if age >= 15 :
    # if condition 2
    if weight >= 50:
        print("You can Donate")
    else:
        print("you are Underweight")
else:
    print("you are Underage")   