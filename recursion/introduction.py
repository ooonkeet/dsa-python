# print my name 4 times
count = 0
def greet():
    global count
    if count == 4:
        return
    print("Ankit")
    count+=1
    greet()
greet()
# type 1 - use global var

def name(c=0):
    if c==4:
        return
    print("Amay")
    name(c+1)
name()
# type 2 - use default argument

# example of tail recursion