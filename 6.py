print('\033c')
ListName = []
ListCard = []

Name = "Start"
while True:
    Name = input  ("Please enter a name: ")
    if Name == "Stop":
        print(ListName)
        break
    ListName.append(Name)

Card = "Start"
while True:
    Card = input ("Please enter a number:")
    if Card == "Stop":
        print(ListCard)
        break
    ListCard.append(int(Card))

def TotalCards(ListCard):
    total = 0 
    for number in ListCard:
        total += number 
    return total
print("You have", TotalCards(ListCard), "cards in total")