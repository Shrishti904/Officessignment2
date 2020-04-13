'''If you pass immutable arguments like integers, strings or tuples to a function, 
the passing acts like call-by-value. The object reference is passed to the function parameters. 
They can't be changed within the function, because they can't be changed at all, i.e. they are immutable. 
It's different, if we pass mutable arguments. They are also passed by object reference, 
but they can be changed in place in the function.
 If we pass a list to a function, we have to consider two cases: 
 Elements of a list can be changed in place, i.e. the list will be changed even in the caller's scope.
  If a new list is assigned to the name, the old list will not be affected, i.e. the list in the caller's scope will remain untouched.'''

def EvenorOdd(N):
        if(N%2==0):
            print("Even")
            print(N*2)
        else:
            print("Odd")
            print(N*2)
Num=int(input("Enter a no."))
EvenorOdd(Num)  
print(Num)
