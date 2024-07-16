import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,1,50)

print(x)
y1=2*x+1
y2=x**2

plt.figure()
plt.plot(x,y1)
plt.show()

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1,linestyle='--')

plt.xlim((-2,3))
plt.xlim((-3,3))
plt.xlabel("I am x")
plt.ylabel("I am y")
new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-1,-0.75,0.5,1],[r'$really\ bad$',r'$bad$',r'$godd$',r'$really god$'])
print(new_ticks)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',-1))
plt.show()
