from main import People

try:
    name = input("Enter your name\n")
    phone_number = input("Enter your phone number\n")
    email = input("Enter your email\n")
    county = input("Enter your county\n")
    gender = input("Enter your gender\n")
    religion = input("Enter your religion\n")
    password = input("Enter your password\n")

    People.create(name=name, phone_number=phone_number, email=email, county=county, gender=gender, religion=religion, password=password)
    print("Confirmed registration")

except:
 print("Failed registration")