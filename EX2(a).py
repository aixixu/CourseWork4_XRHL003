import matplotlib
import matplotlib.pyplot as plt
import numpy as np

numVal = 10000
nBins = 100
rMin = 0.
rMax = 1.
r = np.random.uniform(rMin, rMax, numVal)
# cdf = x^2 inverse_cdf x = √r
xData_1 = np.sqrt(r)
xHist1, bin_edges1 = np.histogram(xData_1, bins=nBins, range=(rMin,rMax))

# make plot and save in file

# for xData_1 the plot as follow
binLo1, binHi1 = bin_edges1[:-1], bin_edges1[1:]
xPlot1 = np.array([binLo1, binHi1]).T.flatten()
yPlot1 = np.array([xHist1, xHist1]).T.flatten()
fig1, ax1= plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
plt.title('Histogram of x = sqrt(r)')
ax1.set_xlim((rMin,rMax))
ax1.set_ylim((0,300))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot1, yPlot1)
fig1 = plt.gcf()
plt.show()
fig1.savefig("uniformHist1_2x.png")