#Question 3
#Write a program to calculate the speed of a planet at aphelion, the distance between the planet and the Sun at aphelion, the semi-major axis of the orbit, the orbital period, and the eccentricity of the orbit. The program should ask the user to input the distance between the planet and the Sun at perihelion and the velocity of the planet at perihelion. The program should then calculate and output the speed of the planet at aphelion, the distance between the planet and the Sun at aphelion, the semi-major axis of the orbit, the orbital period, and the eccentricity of the orbit. The program should be written in Python and should be well commented. The program should be submitted as a single file named Q3.py.

import numpy as np
G=6.6738*10**(-11)    # Universal Gravitatiuonal Constant in N-m**2/kg**2
M=1.9891*10**30       # Mass of the Sun in kg

flag='Y'
while flag=='Y' or flag=='y':

    print('Enter the distance between planet and Sun at perihelion in scientific notation in m')
    x1=eval(input('Enter the coefficient : '))
    n1=eval(input('Enter the exponent in powers of 10: '))
    l1=x1*10**n1

    print('Enter the velocity of planet at perihelion in scientific notation in m/s')
    x2=eval(input('Enter the coefficient : '))
    n2=eval(input('Enter the exponent in powers of 10: '))
    v1=x2*10**n2


    b=-2*G*M/(v1*l1)
    c=-(v1**2-2*G*M/l1)
    v2=(-b-np.sqrt(b**2-4*c))/2      # velocity of planet at aphelion

    if v2<=0:
        print('Bounded orbit is not possible')
        flag=input('Do you wish to retry? (Y/N) : ')
        print(flag)
    else:
        l2=l1*v1/v2                                 # distance between planet and Sun at aphelion
        a=(l1+l2)/2                                 # semi-major axis
        b=(l1*l2)**(0.5)
        T=(2*(np.pi)*a*b)/(l1*v1*365*24*3600)       # Orbital Period in years
        e=(l2-l1)/(l2+l1)                           # eccentricity of orbit

        print('The speed of planet at aphelion is (in m/s) : ',format(v2,'0.4f'))
        print('The semi-major axis is (in m) : ',format(l2,'0.4f'))
        print('The orbital time period in years is : ',format(T,'0.4f'))
        print('The orbital eccentricity is : ',format(e,'0.4f'))
        break

