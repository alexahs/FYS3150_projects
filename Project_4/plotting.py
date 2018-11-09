import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# import seaborn as sns
# sns.set()
# sns.set_style('white')
# plt.xkcd();
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')

filename = "cycleComparison.dat"
dat = np.loadtxt(filename)
anal = np.loadtxt("analytical.dat")


E = dat[:, 1]
M = dat[:, 5]
Cv = dat[:, 7]
chi = dat[:, 6]
cyc = dat[:, -1]

anal = anal/4.0

# errors = np.zeros((len(E), 4))
errE = np.zeros(len(E))
errM = np.zeros(len(E))
errCv = np.zeros(len(E))
errChi = np.zeros(len(E))



# vals = np.array([E, M, Cv, chi])*4.0

def absE(A, S):
    # print A
    # print S
    return abs((A - S)/A)

errE = absE(anal[0], E)
errM = absE(anal[4], M)
errCv = absE(anal[5], Cv)
errChi = absE(anal[6], chi)

figname = "errors_Cv_X.png"
# plt.loglog(cyc, errE)
# plt.loglog(cyc, errM)
plt.loglog(cyc, errCv)
plt.loglog(cyc, errChi)
plt.legend([r"$C_v$", r"$\chi$"])
plt.xlabel("No. of MC Cycles")
plt.ylabel("Absolute error")
plt.savefig(figname)


plt.show()