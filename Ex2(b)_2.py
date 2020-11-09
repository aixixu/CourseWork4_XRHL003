import matplotlib
import matplotlib.pyplot as plt
import numpy as np

numVal = 10000
nBins = 100
rMin = 0.
rMax = 1.
xMin = 0.
xMax = 1.

# use
r = np.random.uniform(rMin, rMax, numVal)
r_gauss=1/(np.sqrt(2*np.pi)*1)*np.exp(-np.power((r-0),2)/(2*1**2))
k=1
u=np.random.uniform(0,k*r_gauss)

xData=[]
for i in range(numVal):
    a=2*r[i]
    if a>u[i]:
        xData.append(r[i])

xHist1, bin_edges1 = np.histogram(xData, bins=nBins, range=(xMin, xMax))

# make plot and save in file

# for xData_1 the plot as follow
binLo1, binHi1 = bin_edges1[:-1], bin_edges1[1:]
xPlot1 = np.array([binLo1, binHi1]).T.flatten()
yPlot1 = np.array([xHist1, xHist1]).T.flatten()
fig1, ax1= plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
plt.title('Histogram of x = sqrt(r)')
ax1.set_xlim((xMin, xMax))
ax1.set_ylim((0,200))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot1, yPlot1)
fig1 = plt.gcf()
plt.show()
fig1.savefig("uniformHist2_2x.png")
