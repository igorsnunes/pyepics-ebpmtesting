import numpy as np
import matplotlib.pyplot as plt
from FPGA import *

dbe_fpga = FPGA()

n = np.arange(0,4096,1)

#dbe_fpga.acqADCPoints(4096)
#c0array = dbe_fpga.getADCPointsChannel0()
#c1array = dbe_fpga.getADCPointsChannel1()
#c2array = dbe_fpga.getADCPointsChannel2()
#c3array = dbe_fpga.getADCPointsChannel3()

#plt.plot(n,c0array,'b',n,c1array,'r',n,c2array,'g',n,c3array,'r')
#plt.show()

#dbe_fpga.acqTBTAMPPoints(4096)
#c0array = dbe_fpga.getTBTAMPPointsChannelA()
#c1array = dbe_fpga.getTBTAMPPointsChannelB()
#c2array = dbe_fpga.getTBTAMPPointsChannelC()
#c3array = dbe_fpga.getTBTAMPPointsChannelD()

#plt.plot(n,c0array,'b',n,c1array,'r',n,c2array,'g',n,c3array,'r')
#plt.show()


#plt.plot(n,c2array,'g',n,c3array,'r')
#plt.show()

dbe_fpga.acqTBTPOSPoints(4096)
c0array = dbe_fpga.getTBTPOSPointsChannelX()
c1array = dbe_fpga.getTBTPOSPointsChannelY()
c2array = dbe_fpga.getTBTPOSPointsChannelQ()
c3array = dbe_fpga.getTBTPOSPointsChannelSUM()

plt.plot(n,c0array,'b',n,c1array,'r',n,c2array,'g',n,c3array,'r')
plt.show()
