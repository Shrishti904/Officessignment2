'''Create a module/Function which has Function GCD that accepts two parameters
 and import this in you main code and pass two values'''


def GCDofNum(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            GCDvalue=i
    return i