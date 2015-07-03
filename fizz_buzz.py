def fb(i):    
        def fb_a(): 
                print ("Fizz")
        def fb_b(): 
                print ("Buzz")
        def fb_c(): 
                print ("FizzBuzz")
        def fb_d(): 
                print ("")
        r = i % 3 
        s = i % 5 
        t = i % 15 
        d = {True:fb_a,False:fb_d}
        e = {True:fb_b,False:fb_d}
        f = {True:fb_c,False:fb_d}
        d[r == 0 and s != 0]()
        e[s == 0 and r != 0]()
        f[t == 0]() 

i = 1 
while i <= 20:
           print i, fb(i)
        i = i+1

