from numpy import linspace
import matplotlib.pyplot as plt
from pyit2fls import tri_mf,trapezoid_mf

domain = linspace(0., 3., 1001)

trapezoid = trapezoid_mf(domain, [-0.1, 0, 0.25, 0.5, 1.])
tri2 = tri_mf(domain,[0.5,1.,1.5,1.])
tri3 = tri_mf(domain,[1.,1.5,2.,1.])
tri1 = tri_mf(domain, [1.5, 2, 2.5, 1.])
trapezoid2 = trapezoid_mf(domain, [2.5, 2.75, 3, 3.5, 1.])
 
plt.figure()

plt.plot(domain,trapezoid,label = "HI")
plt.plot(domain, tri1,label="NM")
plt.plot(domain,tri2,label = "NS")
plt.plot(domain,tri3,label = "ZE")
plt.plot(domain,trapezoid2,label = "HE")

plt.legend()
plt.xlabel("Domain")
plt.ylabel(" Degreee of Membership")
plt.show()