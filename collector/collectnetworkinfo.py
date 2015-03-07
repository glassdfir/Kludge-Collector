import cmdlnr as cmdlnr
import logger as log
import csv, win32netcon

def Collect(self):
	arrayOfCommands = [
	["netstat -bona", "Network\\netstat.txt"],
	["ipconfig \/displaydns | findstr \"Name Live Host\"", "Network\\dns.txt"],
	["ipconfig \/all", "Network\\ipconfig.txt"],
	["arp -a", "Network\\arp.txt"],
	["route print", "Network\\routes.txt"],
	["netsh.exe firewall show state", "Network\\firewall.txt"],
	["netsh firewall show service", "Network\\firewall-state.txt"],
	["net use", "Network\\netbios.txt"],
	["nbtstat -nrSsc", "Network\\NBTStat.txt"],
	["net sessions", "Network\\netbios-sessions.txt"]
	]
	command = cmdlnr.CmdLnr()
	for i in range(len(arrayOfCommands))
		try:
			command.run_acmd(arrayOfCommands[i][0],arrayOfCommands[i][1])
		except:
			log.exception
			pass