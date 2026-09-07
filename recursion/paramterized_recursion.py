def func(x,N):
    if N==0:
        return
    print(x)
    func(x,N-1)
x=input("Print a value to be printed N times: ")
N=int(input("Enter number of times to print: "))
func(x,N)
# basic example of parameterized recursion

def fn(i,x):
    if i>x:
        return
    print(i)
    fn(i+1,x)
fn(1,8)
# example of parameterized recursion to print numbers from 1 to x - head recursion

def fn2(i,N):
    if i>N:
        return
    fn2(i+1,N)
    print(i)
fn2(1,7)
# example of parameterized recursion to print numbers from 1 to N - tail recursion