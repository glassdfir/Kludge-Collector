import cmdlnr as cmdlnr
import logger as log

def Collect(self):
	arrayOfCommands = [
	["set", "System\\env.txt"],
	["schtasks.exe \/query", "Process\\schtasks.txt"],
	["at", "Process\\at.txt"],
	["tasklist", "Process\\tasklist.txt"],
	["doskey \/history", "System\\doskey.txt"],
	]
	command = cmdlnr.CmdLnr()
	for i in range(len(arrayOfCommands))
		try:
			command.run_acmd(arrayOfCommands[i][0],arrayOfCommands[i][1])
		except:
			log.exception
			pass

def EnumLocalUsers(self):
	with open('.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')