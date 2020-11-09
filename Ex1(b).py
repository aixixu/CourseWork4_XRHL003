import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# generate data and store in numpy array, put into histogram

numVal = 10000
nBins = 100
rMin = 0.
rMax = 1.
r = []
r_exact = []
r_variance = []
r_standard_deviation = []

for i in range(12):
    r.append(np.random.uniform(rMin, rMax, numVal))
    r_exact.append(np.mean(r[i]))
    r_variance.append(np.mean(r[i]))
    r_standard_deviation.append(np.mean(r[i]))

xData_1 = r[0] + r[1] - 1
xData_2 = r[0] + r[1]+ r[2] + r[3] - 2
xData_3 = -6
for i in range(12):
    xData_3 = xData_3 + r[i]
exact_1 = np.mean(xData_1)
variance_1 = np.var(xData_1)
standard_deviation_1 = np.std(xData_1)

exact_2 = np.mean(xData_2)
variance_2 = np.var(xData_2)
standard_deviation_2 = np.std(xData_2)

exact_3 = np.mean(xData_3)
variance_3 = np.var(xData_3)
standard_deviation_3 = np.std(xData_3)

xHist1, bin_edges1 = np.histogram(xData_1, bins=nBins, range=(2*rMin-1, 2*rMax-1))
xHist2, bin_edges2 = np.histogram(xData_2, bins=nBins, range=(4*rMin-2, 4*rMax-2))
xHist3, bin_edges3 = np.histogram(xData_3, bins=nBins, range=(12*rMin-6, 12*rMax-6))
# make plot and save in file

# for xData_1 the plot as follow
binLo1, binHi1 = bin_edges1[:-1], bin_edges1[1:]
xPlot1 = np.array([binLo1, binHi1]).T.flatten()
yPlot1 = np.array([xHist1, xHist1]).T.flatten()
fig1, ax1= plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
plt.title('Histogram of x = r1+ r2− 1')
ax1.set_xlim((2*rMin-1, 2*rMax-1))
ax1.set_ylim((0., 300))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot1, yPlot1)
# output information
plt.text(-0.75, 250, f'exact = {exact_1}\nvariance = {variance_1}\nstandard_deviation = {standard_deviation_1}')
fig1 = plt.gcf()
plt.show()
fig1.savefig("uniformHist1.png")
print(f'E[r1]+E[r2]-1 = {r_exact[0] + r_exact[1] - 1}')
print(f'E[r1+r2-1] = {exact_1}')
print(f'V[r1]+V[r2] = {r_variance[0] + r_variance[1]}')
print(f'V[r1 + r2] = {variance_1}')

# for xData_2 the plot as follow
binLo2, binHi2 = bin_edges2[:-1], bin_edges2[1:]
xPlot2 = np.array([binLo2, binHi2]).T.flatten()
yPlot2 = np.array([xHist2, xHist2]).T.flatten()
fig2, ax2= plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
plt.title('Histogram of x =  r1+ r2+ r3+ r4− 2')
ax2.set_xlim((4*rMin-2, 4*rMax-2))
ax2.set_ylim((0., 400))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot2, yPlot2)
# output information
plt.text(-1.50, 320, f'exact = {exact_2}\nvariance = {variance_2}\nstandard_deviation = {standard_deviation_2}')
fig2 = plt.gcf()
plt.show()
fig2.savefig("uniformHist2.png")
print(f'E[r1]+E[r2]+E[r3]+E[r4]-2 = {r_exact[0] + r_exact[1] + r_exact[2] + r_exact[3] -2}')
print(f'E[r1+r2+r3+r4-2] = {exact_2}')
print(f'V[r1]+V[r2]+V[r3]+V[r4] = {r_variance[0] + r_variance[1] + r_variance[2] + r_variance[3]}')
print(f'V[r1+r2+r3+r4] = {variance_2}')

# for xData_3 the plot as follow
binLo3, binHi3 = bin_edges3[:-1], bin_edges3[1:]
xPlot3 = np.array([binLo3, binHi3]).T.flatten()
yPlot3 = np.array([xHist3, xHist3]).T.flatten()
fig3, ax3= plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
plt.title('Histogram of x =  r1+ r2+ r3+ ...+ r12 −6')
ax3.set_xlim((12*rMin-6, 12*rMax-6))
ax3.set_ylim((0., 650))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot3, yPlot3)
# output information
plt.text(-4.0, 540, f'exact = {exact_3}\nvariance = {variance_3}\nstandard_deviation = {standard_deviation_3}')
fig3 = plt.gcf()
plt.show()
fig3.savefig("uniformHist3.png")
print(f'E[r1]+E[r2]+....E[r12]-6 = {sum(r_exact) - 6}')
print(f'E[r1+r2+...r12-6] = {exact_3}')
print(f'V[r1]+V[r2]+...+V[12] = {sum(r_variance)}')
print(f'V[r1+r2+...+r12] = {variance_3}')
