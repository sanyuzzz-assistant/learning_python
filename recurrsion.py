'''def factorial(x):
    if x == 1 or x==0:
        f=1
    else:
        f=x*factorial(x-1)
    return f        

n=int(input("enter a number:"))
res=factorial(n)
print(f"factorial of {n} is {res}")'''

def summ(x):
    if x==5:
        s=5
    else:
        s=x+summ(x+1)
    return s    