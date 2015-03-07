import subprocess, os
import variables as var
import logger as log
import collectsysteminfo as sysinfo
import collectnetworkinfo as network
import collectmemoryinfo as memory

class CollectStuff(object):
    """ Start Collection of Data """
    def __init__(self):
        self = self
		#Determine the collection level and only make appropriate folders
        if var.level == 1:
			self.quickCollection()
		elif var.level == 2:
			self.fullCollection()
		elif var.level == 3:
			self.quickThenFullCollection()
	#Everything should be broken down into small groups of related evidence
	#This will allow for flexibility, granularity and ease of troubleshooting. 
	def quickCollection(self):
		sysinfo.collect()
		network.collect()
	
	def fullCollection(self):
		memory.collect()
		sysinfo.collect()
		network.collect()
	
	def self.quickThenFullCollection(self):
		self.quickCollection()
		memory.collect()
		
		
		
	
	

		
