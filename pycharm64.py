#Add on for PyCharm

import appModuleHandler
#import NVDAObjects.JAB
import ui
import api
import tones


class AppModule(appModuleHandler.AppModule):
#start at foreground to get same navigation
	def script_lineNum(self, gesture):
		possibleNum = api.getForegroundObject()
		name = possibleNum.firstChild.getChild(1).getChild(1).getChild(1).getChild(2).firstChild.next.name
		ui.message("line" + name)

		
	#f2 takes user to any problem areas
	#shift+f1 brings up the description
	#if gesture is pressed, desc is read
	#if there are no more errors to go through, a beep will sound
	def script_errorSpeak(self, gesture):
		errorLoc = api.getForegroundObject()
		
		try:
			error = errorLoc.firstChild.getChild(1).getChild(3).getChild(1).firstChild.firstChild.firstChild.firstChild.firstChild
			errorMessage = error.name
			ui.message(errorMessage)
		except IndexError:
			tones.beep(440, 1000)

			
	def script_runComm(self, gesture):
		gesture.send()
		ui.message("run")
		
	def script_stopComm(self, gesture):
		gesture.send()
		ui.message("stop")
		
	
	__gestures = {
		"kb:nvda+shift+f3": "lineNum",
		"kb:nvda+shift+f7": "errorSpeak",
		"kb:shift+f10": "runComm",
		"kb:control+f2": "stopComm",
	}
