print("\033c")
print("in deze opdracht vragen ze om een percentage")

percentage=101

while percentage < 0 or percentage > 100:
    percentage= int(input("Enter a number between 0 to 100:"))

    print("het antwoord is: ",percentage,"%")