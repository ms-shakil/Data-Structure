#### print 1 to 10 and 10 to 1 with recursion function
def fun(n):
    if n > 10:
        return
    ## this print function print 1 to 10
    print(n) 
    fun(n+1)
    # this print function print 10 to 1
    print(n)
fun(1)    

#### factorial with recursion function

def Factorial(n):
    if n < 0 :
        return None
    if n in [1,0]:
        return 1
    return n * Factorial(n-1)
    
print(Factorial(5))        