#Question 1
#Write a program to calculate the transmission and reflection coefficients for an electron of energy E incident on a potential step of height V. The program should ask the user to input the energy of the incoming electron and the height of the potential step. The program should then calculate and output the transmission and reflection coefficients. The program should also output the sum of the transmission and reflection coefficients. The program should be able to handle the case where the energy of the incoming electron is less than the height of the potential step. In this case, the program should output an appropriate error message and ask the user to input the energy and height again. The program should continue to ask the user to input the energy and height until the energy is greater than the height of the potential step. The program should be written in Python and should be well commented. The program should be submitted as a single file named Q1.py.

import numpy as np
m=9.11*10**(-31)        #mass of an electron
hbar=6.626*10**(-34)/(2*np.pi)   # Reduced Plank's Constant

f='Y'
while f=='Y' or f=='y':
    E=eval(input('Enter the energy of incoming electron in eV : '))
    V=eval(input('Enter the height of the potential step in eV : '))
    if E<V:
        print('Energy of incoming electron has to be greater then height of potential well')
        f=input('Do you wish to retry? (Y/N) : ')
    else: 
        k1,k2=np.sqrt(2*m*(E))/hbar, np.sqrt(2*m*(E-V))/hbar
        T=4*k1*k2/(k1+k2)**2             #Transmission Coefficient
        R=((k1-k2)/(k1+k2))**2           #Reflection Coefficient
        print('The value of the Transmission and Reflection Coefficients are respectively : ',T,'and',R)
        print('Sum of Transmission and Reflection Coefficients is :',format(T+R,'0.2f'))
        break
