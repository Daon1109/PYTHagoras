
def prime(num):
    
    i=1
    cnt=0
    while i<num:
        dvd=num/i
        if (dvd-int(dvd))==0:
            cnt=cnt+1
        i=i+1
    if cnt==1:
        return 1
    else:
        return 0