def cmb(N1,r,mod):
    ncr=1
 
    for i in range(N1-r+1,N1+1):
        ncr*=i
        ncr%=mod
 
    for i in range(1,r+1):
        ncr*=pow(i,-1,mod)
        ncr%=mod
 
 
    return ncr
