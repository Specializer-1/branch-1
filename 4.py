print('\033c') 

print("Dit programma vraagt om een percentage totdat het goed is")

percentage = 101

while percentage < 0 or percentage > 100:
    percentage = int(input("Geef een percentage dat ligt tussen 0 en 100: "))

print("Het percentage is: " + str(percentage) + "%")






