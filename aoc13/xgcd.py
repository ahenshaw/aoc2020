def xgcd(a, b):  
    # Base Case  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = xgcd(b%a, a)  
     
    # Update x and y using results of recursive  
    # call  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 

if __name__ == '__main__':
    print(1425*638)
    ans = 754018
    for x, y, m in ((67, 7, 6), (67, 59, 57), (67, 61, 58)):
        # a, b, c = xgcd(x, y)

        print(gcd(x, y))
    print(((67*7-6)*59 - 57)*61-58)
