#Plot 1
#Demonstration of many plots with same axis in single figure

import numpy as np
import matplotlib.pyplot as plt

def P(T,V):
    a,b=4.225,0.0371  #unit of 'a' in atm litre^2 per mol^2, unit of 'b' in litre per mole
    R=0.082           #unit of 'R' in litre atm per Kelvin per mole
    return (R*T/(V-b))-(a/V**2)

V=np.linspace(0.05,0.5,1000)

plt.title(r'P-V Diagram of vanderwaals eqn for $NH_3$ gas with $T_c=405.5~K$')
plt.xlabel('V in litre')
plt.ylabel('P in atm')
plt.plot(V,P(200.0,V),label=r'$T=200K$')
plt.plot(V,P(250.0,V),label=r'$T=250K$')
plt.plot(V,P(325.0,V),label=r'$T=325K$')
plt.plot(V,P(450.0,V),label=r'$T=450K$')
plt.plot(V,P(550.0,V),label=r'$T=550K$')

plt.legend(loc='best',prop={'size':12})

plt.savefig('S:\\Documents\\Github\\Computational-Physics-UG\\Methods of graph plotting\\Function_plot\\Python Files\\fig_legend_1.png')
plt.show()

