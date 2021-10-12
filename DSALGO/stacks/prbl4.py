# https://www.hackerrank.com/challenges/simple-text-editor/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())
stk = []
st = ""
while q>0:
    ip = input().split(" ")
    if int(ip[0]) == 1:
        stk.append(st)
        st = st + ip[1]
    elif int(ip[0]) == 2:
        stk.append(st)
        del_ch = int(ip[1])
        st = st[:-del_ch]
    elif int(ip[0]) == 3:
        k = int(ip[1])
        print(st[k-1])
    else:
        st = stk.pop(len(stk)-1)
        # stk.pop(len(stk)-1)
    q = q-1
