# 3. Provide a program to calculate the time and distance based on
# below problem.
# • We have a 100-meter rod.
# • At both ends, 1-1 cockroach is place.
# • The left cockroach moves at 1 meter per second forward, and every 10 seconds moves 2
# meters backward.
# • The right cockroach moves at 2 meters per second forward, and every 5 seconds moves 1
# meter backward.
# • When both cockroaches meet, we have to calculate the time and distance. Calculate the total
# time to complete the 100 meter rod.

 


# Speed of cockroach 1 - 1 metre per sec fwd and 2 metres back for every 10 sec, ie 9 metres per 10sec
# similarly for cockroach 2 - spedd is 8 metres per 5 sec
# we know, avg time to meet = tot distance between the two / total relative speed of the two
# and speed = distance/time

var =input('To proceed with default problem enter - D \nTo enter new prblm values enter - N  ')

try:
    if var == 'D' or var =='d':
        dist=100
        s1=8/10
        s2=9/5


    elif var == 'N' or var =='n':
        dist=float(input('Enter distance between cockroaches - '))
        a1=float(input('Enter speed of cockroache1 in meters per sec  - '))
        b1=float(input('Enter rate of getting back for cockroache1 in meters per sec  - '))
        
        a2=float(input('Enter speed of cockroaches2 in meters per sec - '))
        b2=float(input('Enter rate of getting back for cockroaches2 in meters per sec - '))
        s1=a1-b1
        s2=a2-b2

    time=dist/(s1+s2)

    d1=s1*time
    d2=s2*time
    print("Distance covered by cockroach1 =",d1,"\nDistance covered by cockroach2 =",d2,"\nTime to meet =",time)

except Exception as e:
    print(e)