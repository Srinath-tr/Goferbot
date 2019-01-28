phonebook = {}
phonebook["John"] = 938277566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

a=phonebook.pop("John")
del phonebook["Jill"]
print(phonebook)
print a
