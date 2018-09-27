person = {'Name': 'Zdzichu Kowalski',
          'Gender': 'Male',
          'Occupation': 'Researcher',
          'Home Planet': 'Betelgeuse Seven',
          'Age': 5}


person['Age'] = 6

print(person['Age'])

person['City'] = "Rotmanka"

print(person)

person2 = {}
for key, val in person.items():
    person2[key + "1"] = str(val) + "1"

print(person2)