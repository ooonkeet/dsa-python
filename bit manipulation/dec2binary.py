def cov2binary(num):
    result=""
    while num>0:
        if num%2==1:
            result+="1"
        else:
            result+="0"
        num=num//2
    result=result[::-1]
    return result
n=int(input("Enter a decimal number:- "))
print(n,"in binary format is",cov2binary(n))