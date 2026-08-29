from math import sqrt

def factors_bruteforce(num):
    result=[]
    for i in range(1,num+1):
        if num%i==0:
            result.append(i)
    return result
# this is the brute force method to find the factors of a number with o(n) time complexity

def factors_semioptimized(num):
    result=[]
    for i in range(1,num//2):
        if num%i==0:
            result.append(i)
    result.append(num)
    return result
# this is a better approach with o(n/2) time complexity

def factors_optimized(num):
    result=[]
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            result.append(i)
            if i!=num//i:
                result.append(num//i)
    return sorted(result)

# this is the most optimized approach with o(sqrt(n))+o(nlogn) time complexity

def factors_variation(num):
    result=[]
    for i in range(1,int(sqrt(num))+1):
        if num%i==0:
            result.append(i)
            if i!=num//i:
                result.append(num//i)
    result.sort()
    return result

# this is another approach of optimized method
num=int(input("Enter a number: "))
print("Factors of",num,"are",factors_bruteforce(num)) 
print("Factors of",num,"are",factors_semioptimized(num))
print("Factors of",num,"are",factors_optimized(num))   
print("Factors of",num,"are",factors_variation(num))