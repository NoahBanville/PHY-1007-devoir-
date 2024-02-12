#Devoir 1  d'onde : 
A = 0.1
E = 0.5
def integrand(x, a):
   return np.absolute(a*np.cos(10 * np.sqrt(2) * x))
for i in range(64): 
   Ef = 0.981 * (quad(integrand, 0, np.pi/16, args=(A)))[0]
   E = E - Ef
   A = np.sqrt((E*2)/100)
   if (i+1)*(1/16) %1 == 0 : 
      print("(",  (i+1)*(1/16), "pi, ", A, ")")