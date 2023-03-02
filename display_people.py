from main import People

mypeople = People.select()
for person in mypeople:
    print(person.name, person.phone_number, person.email, person.county, person.gender, person.religion, person.password)