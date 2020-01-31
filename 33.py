# fraction in the form of ab/cd
import time
t=time.time()
 
num=1
den=1
for ab in range(10,100):
    for cd in range(11,100):
        if ab%10!=0 and ab<cd:
            a=ab/10
            b=ab%10
            c=cd/10
            d=cd%10
            if a==c and ab*d==b*cd:
                print ab,"/",cd
                num*=ab
                den*=cd
            if b==c and ab*d==a*cd:
                print ab,"/",cd
                num*=ab
                den*=cd
            if a==d and ab*c==b*cd:
                print ab,"/",cd
                num*=ab
                den*=cd
            if b==d and ab*c==a*cd:
                print ab,"/",cd
                num*=ab
                den*=cd
print num,"/",den
print time.time()-t

"""for y in range(1,10):
    for z in range(y,10):
        x=float(9)*y*z/(10*y-z)
        if int(x) == x and y/z < 1 and x<10:
            print x, y, z, str(10*y+x)+'/'+str(z+10*x), str(y)+'/'+str(z)"""

