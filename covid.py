# cook your dish here
def check(l):
    # print("here")
    
    c = 0
    inf = 1
    res = []
    # print("len",len(l))
    for c in range(len(l)):
        # print(c,l[c])
        if c < len(l) - 1:
            diff = l[c + 1] - l[c]
            # print("dif",diff)
            if diff <= 2:
                inf += 1
                
            
            else:
                # print("cp 2")
                res.append(inf)
                inf = 1
                
        elif c == len(l) - 1:
            # print("cp 1")
            res.append(inf)

    return res
            
            
        
        
        
        

t = int(input())
# t= 3
# print("t",t)

for i in range(t):
    # print("i",i)
    n = int(input())
    # print("n",n)
    # ip = list(map(int,input().split(" ")))
    ip = list(map(int,input().split(" ")))
    # print("ip",ip)
    r = check(ip)
    if len(r) == 1:
        print(*r,*r)
    else:
        print(min(r),max(r))
        

    