import sys
import os
import time
from epics import *


class LiberaRFCLK:
	
	def __init__(self):
		self.freqget = PV('LRFCLK:RF:getFREQ.VAL')
		self.freqset = PV('LRFCLK:RF:setFREQ')
		self.mcget = PV('LRFCLK:RF:getMCFREQ.VAL')
		self.mcset = PV('LRFCLK:RF:setMCFREQ')
		self.powget = PV('LRFCLK:RF:getPOW.VAL')
		self.powset = PV('LRFCLK:RF:setPOW')
		self.harmset = PV('LRFCLK:RF:getHARMONICNUM')
		self.harmget = PV('LRFCLK:RF:setHARMONICNUM.VAL')
		self.gateget = PV('LRFCLK:RF:getGATE.VAL')
		self.gateset = PV('LRFCLK:RF:setGATE')
		self.gatemodeget = PV('LRFCLK:GATE:getMODE.VAL')
		self.gatemodeset = PV('LRFCLK:GATE:setMODE')
		self.gatefillget = PV('LRFCLK:GATE:getFILL.VAL')
		self.gatefillset = PV('LRFCLK:GATE:setFILL')
		self.gatepattget = PV('LRFCLK:GATE:getPATT.VAL')
		self.gatepattset = PV('LRFCLK:GATE:setPATT')
		self.confoutsget = PV('LRFCLK:CONFIG:getOUTS.VAL')
		self.confoutsset = PV('LRFCLK:CONFIG:setOUTS')
		self.rfmodeget = PV('LRFCLK:RF:getMODE.VAL')
		self.rfmodeset = PV('LRFCLK:RF:setMODE')

	def __setRF(self):
		if  self.rfmodeget.get() != 'RF':#TODO:correct ir on IOC!
			self.rfmodeset.value = 'RF'
	

	def setFREQ(self,value):
		self.__setRF()
		conv_value = str(value)
		conv_value = conv_value.replace('.',',')
		self.freqset.value = conv_value

	def setPOW(self,value):
		self.__setRF()
		conv_value = str(value)
		conv_value = conv_value.replace('.',',')
		self.powset.value = conv_value


if __name__ == '__main__':

	c = LiberaRFCLK()
	c.setFREQ(3.2)
