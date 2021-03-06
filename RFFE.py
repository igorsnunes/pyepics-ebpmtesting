import sys
import os
import time
from epics import *
import time

class RFFE:
	
	def __init__(self,number):
		self.swiget = PV("BPM:FRONTEND"+str(number)+":channel1:switchState:read" )
		self.swiset = PV("BPM:FRONTEND"+str(number)+":channel1:switchState:write")
		self.att1get = PV("BPM:FRONTEND"+str(number)+":attenuator1:getValue")
		self.att1set = PV("BPM:FRONTEND"+str(number)+":attenuator1:setValue")
		self.att2get = PV("BPM:FRONTEND"+str(number)+":attenuator2:getValue")
		self.att2set = PV("BPM:FRONTEND"+str(number)+":attenuator2:setValue")
	def setSWITCH(self,state):
		if state=="DIRECT" or state=="INVERT" or state=="MATCHED" or state=="SWITCHING":
			self.swiset.value = str(state)
			time.sleep(5.0)#TODO:if record is passive, still necessary?
			new_state = self.swiget.get(as_string=True)
			print state + " and " + new_state
			if state == new_state:
				return True
			return False
		else:
			return False

	def setATTENUATOR(self,value,att_num):
		if att_num == 1:
			if value < 31.5 and value > 0.0:
				self.att1set.value = float(value)
				time.sleep(5.0)#TODO:if record is passive, still necessary?
				new_value = self.att1get.get()
				if new_value == value:
					return True
				return False
			else:
				return False
		elif att_num == 2:
			if value < 31.5 and value > 0.0:
				self.att2set.value = float(value)
				time.sleep(5.0)#TODO:if record is passive, still necessary?
				new_value = self.att2get.get()
				if new_value == value:
					return True
				return False
			else:
				return False


if __name__ == '__main__':
	c = RFFE(0)
