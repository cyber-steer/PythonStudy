from matplotlib import pylab as plt

y=[5,3,7,10,9,5,3.5,8]
x=range(len(y))
plt.bar(x,y,width=0.7, color="blue")
plt.plot(x,y,color="red")
plt.scatter(x,y,linewidths=5,color="red")
# plt.grid(True)
plt.show()
