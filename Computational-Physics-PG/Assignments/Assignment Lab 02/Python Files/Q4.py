#Question 4
#Time taken for the yolk of an egg to reach a certain critical temperature after which the protein starts to coagulate

import numpy as np

M=67 #mass of the large egg in grams
p=1.038 #density of the egg in g/cm^3
c=3.7 #specific heat capacity of the egg in J/g-K
k=0.0054 #thermal conductivity of the egg in W/cm-K

Tw=100 #temperature of the boiling water in degree Celsius
Ty=70 #temperature of the centre of egg in degree Celsius
T0=eval(input('Enter refrigerator temperature : ')) #temperature of the egg in the refrigerator in degree Celsius

t=(M**(2/3)*c*p**(1/3)/(k*np.pi**2*(4*np.pi/3)**(2/3)))*np.log(0.76*(T0-Tw)/(Ty-Tw))
print("Time taken for the yolk of an egg to reach a certain critical temperature after which the protein starts to coagulate is",t,"seconds")