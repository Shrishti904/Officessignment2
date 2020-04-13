lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 

# iterating till the range 
print("Enter no. seperated by lines")
for i in range(0, n): 
       
    ele = int(input()) 
    lst.append(ele) # adding the element 
      
print(lst) 

f= list(filter(lambda x:x%2==0,lst))
print("Even no. in a list",f)
g=list(filter(lambda y:y%2!=0,lst)) 
print("Odd no's in a list",g)