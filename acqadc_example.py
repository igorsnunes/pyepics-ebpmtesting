import numpy as np
import matplotlib.pyplot as plt
from FPGA import *

dbe_fpga = FPGA()

n = np.arange(0,4096,1)

dbe_fpga.acqADCPoints(4096)
c0array = dbe_fpga.getADCPointsChannel0()
c1array = dbe_fpga.getADCPointsChannel1()
c2array = dbe_fpga.getADCPointsChannel2()
c3array = dbe_fpga.getADCPointsChannel3()

plt.plot(n,c0array,'b',n,c1array,'r',n,c2array,'g',n,c3array,'r')
plt.show()
