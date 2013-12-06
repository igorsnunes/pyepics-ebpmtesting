from RFFE import *
from LiberaRFCLK import *
from FPGA import *

RFFEcontroller = RFFE(1)
LRFCLK = LiberaRFCLK()

RFFEcontroller.setATTENUATOR(31.5,1)
RFFEcontroller.setATTENUATOR(31.5,2)

LRFCLK.setFREQ(489.6)

n_times_measure = 0
	PowerLevel = -60
	while PowerLevel < 20:
		LRFCLK.setPOW(PowerLevel)
		FPGA.acqireData()
		PowerLevel+= 1
	n_times_measure += 1

