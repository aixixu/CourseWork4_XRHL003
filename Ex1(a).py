# simpleMC.py -- simple Monte Carlo program to make histogram of uniformly
# distributed random values and plot
# G. Cowan, RHUL Physics, October 2019

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# generate data and store in numpy array, put into histogram

numVal = 10000
nBins = 100
xMin = 0.
xMax = 1.
r = []
for i in range(12):
    r.append(np.random.uniform(xMin, xMax, numVal))

xData_1 = r[0] + r[1] - 1
xData_2 = r[0] + r[1]+ r[2] + r[3] - 2
xData_3 = -6
for i in range(12):
    xData_3 = xData_3 + r[i]

xHist1, bin_edges1 = np.histogram(xData_1, bins=nBins, range=(xMin-1, xMax))
xHist2, bin_edges2 = np.histogram(xData_2, bins=nBins, range=(xMin-2, xMax+1))
xHist3, bin_edges3 = np.histogram(xData_3, bins=nBins, range=(xMin-6, xMax+5))
# make plot and save in file

# for xData_1 the plot as follow
binLo1, binHi1 = bin_edges1[:-1], bin_edges1[1:]
xPlot1 = np.array([binLo1, binHi1]).T.flatten()
yPlot1 = np.array([xHist1, xHist1]).T.flatten()
fig1, ax1= plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
plt.title('Histogram of x = r1+ r2− 1')
ax1.set_xlim((xMin-1, xMax))
ax1.set_ylim((0., 300))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot1, yPlot1)
fig1 = plt.gcf()
plt.show()
fig1.savefig("uniformHist1.png")

# for xData_2 the plot as follow
binLo2, binHi2 = bin_edges2[:-1], bin_edges2[1:]
xPlot2 = np.array([binLo2, binHi2]).T.flatten()
yPlot2 = np.array([xHist2, xHist2]).T.flatten()
fig2, ax2= plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
plt.title('Histogram of x =  r1+ r2+ r3+ r4− 2')
ax2.set_xlim((xMin-2, xMax+1))
ax2.set_ylim((0., 350))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot2, yPlot2)
fig2 = plt.gcf()
plt.show()
fig2.savefig("uniformHist2.png")

# for xData_3 the plot as follow
binLo3, binHi3 = bin_edges3[:-1], bin_edges3[1:]
xPlot3 = np.array([binLo3, binHi3]).T.flatten()
yPlot3 = np.array([xHist3, xHist3]).T.flatten()
fig3, ax3= plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
plt.title('Histogram of x =  r1+ r2+ r3+ ...+ r12 −6')
ax3.set_xlim((xMin-6, xMax+5))
ax3.set_ylim((0., 550))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot3, yPlot3)
fig3 = plt.gcf()
plt.show()
fig3.savefig("uniformHist3.png")