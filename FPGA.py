import sys
import os
import time
from epics import *


class FPGA:
	def __init__(self):
		self.waveformAcqChannel0ADC = PV('BPM:FPGA3:ADC:channel0.VAL')
		self.waveformAcqChannel1ADC = PV('BPM:FPGA3:ADC:channel1.VAL')
		self.waveformAcqChannel2ADC = PV('BPM:FPGA3:ADC:channel2.VAL')
		self.waveformAcqChannel3ADC = PV('BPM:FPGA3:ADC:channel3.VAL')

		self.numSamplesADCget = PV('BPM:FPGA2:ADC:numSAMPLES:getValue.VAL')
		self.numSamplesADCset = PV('BPM:FPGA2:ADC:numSAMPLES:setValue.VAL')
		self.acqVARget = PV('BPM:FPGA2:acqVAR:getValue.VAL')
		self.acqVARset = PV('BPM:FPGA2:acqVAR:setValue.VAL')

		self.waveformAcqChannelATBTAMP = PV('BPM:FPGA3:TBTAMP:channelA.VAL')
		self.waveformAcqChannelBTBTAMP = PV('BPM:FPGA3:TBTAMP:channelB.VAL')
		self.waveformAcqChannelCTBTAMP = PV('BPM:FPGA3:TBTAMP:channelC.VAL')
		self.waveformAcqChannelDTBTAMP = PV('BPM:FPGA3:TBTAMP:channelD.VAL')

		self.waveformAcqChannelXTBTPOS = PV('BPM:FPGA3:TBTPOS:channelX.VAL')
		self.waveformAcqChannelYTBTPOS = PV('BPM:FPGA3:TBTPOS:channelY.VAL')
		self.waveformAcqChannelQTBTPOS = PV('BPM:FPGA3:TBTPOS:channelQ.VAL')
		self.waveformAcqChannelSUMTBTPOS = PV('BPM:FPGA3:TBTPOS:channelSUM.VAL')


	def acqTBTPOSPoints(self,numPoints):
		self.numSamplesADCset.value = numPoints
		self.acqVARset.value = str("TBTPOSAcquisition")
		time.sleep(10)
		#while True:TODO:check correctly
		#	if self.acqVARget.get() == 2:
		#		break

	def acqTBTAMPPoints(self,numPoints):
		self.numSamplesADCset.value = numPoints
		self.acqVARset.value = str("TBTAMPAcquisition")
		time.sleep(10)
		#while True:TODO:check correctly
		#	if self.acqVARget.get() == 2:
		#		break
    	

	def acqADCPoints(self,numPoints):
		self.numSamplesADCset.value = numPoints
		self.acqVARset.value = str("ADCAcquisition")
		time.sleep(10)
		#while True:
		#	if self.acqVARget.get() == 0:
		#		break
    	
		return True

	def getTBTPOSPointsChannelX(self):
		return self.waveformAcqChannelXTBTPOS.get()
	def getTBTPOSPointsChannelY(self):
		return self.waveformAcqChannelYTBTPOS.get()
	def getTBTPOSPointsChannelQ(self):
		return self.waveformAcqChannelQTBTPOS.get()
	def getTBTPOSPointsChannelSUM(self):
		return self.waveformAcqChannelSUMTBTPOS.get()


	def getTBTAMPPointsChannelA(self):
		return self.waveformAcqChannelATBTAMP.get()
	def getTBTAMPPointsChannelB(self):
		return self.waveformAcqChannelBTBTAMP.get()
	def getTBTAMPPointsChannelC(self):
		return self.waveformAcqChannelCTBTAMP.get()
	def getTBTAMPPointsChannelD(self):
		return self.waveformAcqChannelDTBTAMP.get()


	def getADCPointsChannel0(self):	
		return self.waveformAcqChannel0ADC.get()
	def getADCPointsChannel1(self):	
		return self.waveformAcqChannel1ADC.get()
	def getADCPointsChannel2(self):
		return self.waveformAcqChannel2ADC.get()
	def getADCPointsChannel3(self):
		return self.waveformAcqChannel3ADC.get()
