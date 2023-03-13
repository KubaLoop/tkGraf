from scipy import interpolate as inp
import pylab as lab

x = "0 0.3 0.5 0.8 1 2 3".split()
y = "0 0.1 0.5 1 3 10 30".split()

x = list(map(float, x))
y = list(map(float, y))

newX = lab.linspace(0,3, 333)#stribrnych strikacek strikalo pres 333 stribrnych strech
spl = inp.CubicSpline(x,y)
#spl = inp.UnivariateSpline(x,y)
newY = spl(newX)

lab.plot(x,y,"o", label = "Měřící body")
lab.plot(newX, newY,":", label = "Interpolace")
lab.grid()
lab.legend()
lab.show()
