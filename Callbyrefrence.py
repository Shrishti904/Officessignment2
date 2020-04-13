# list with EVEN and ODD number

# print original list


# loop to traverse each element in the list
# and, remove elements
# which are EVEN (divisible by 2)
def Toremoveeven(List1):
    
    for i  in List1:
        if(i%2 == 0):
            List1.remove(i)
            
    print("List after Removing even no.",List1)
            

# print list after removing EVEN elements
numberList = []
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)
Toremoveeven(numberList)
print("List after entering the main function ",numberList) #Value of List is changes globally


            
