userName = input("Enter name:")
userAge = input("Enter age:")
try:
    userAgeInt = int(userAge)
    print("Wellcome " + userName + ", you have " + str(100 - userAgeInt) + " years to become 100 years old")
except ValueError:
    print("Invalid age input. Please enter a valid integer.")
