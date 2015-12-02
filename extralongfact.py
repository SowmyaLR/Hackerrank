# Enter your code here. Read input from STDIN. Print output to STDOUT
def facto(n):
    fact=1
    while n!=0:
        fact=fact*n
        n=n-1
    print fact

n=(int)(input())
facto(n)
