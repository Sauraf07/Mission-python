contacts =[]
for i in range(4):
    contacts.append(input("Enter the contects names : "))
print("total contact are :",contacts)
remove = input(" remove the names : ")
contacts.remove(remove)
print(contacts)