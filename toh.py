def toh(n,s,t,d):
    global count
    if n>0:
        toh(n-1,s,d,t)
        print(f"Move Disk{n}   {s}-->{d}")
        count+=1
        toh(n-1,t,s,d)
        
#main code
s='S'
t='T'
d='D'
count=0
n=int(input("enter the number of disks:"))
print("sequence is:")
toh(n,s,t,d)
print("the number of moves:",count)