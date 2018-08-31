#Add on for PyCharm

import appModuleHandler
#import NVDAObjects.JAB
import ui
import api
import tones
from keyboardHandler import KeyboardInputGesture


class AppModule(appModuleHandler.AppModule):
#start at foreground to get same navigation
	def script_lineNum(self, gesture):
		splitNum = self.lineInfo()
		loneNum = splitNum[0]
		ui.message("line" + loneNum)
	
	def script_lineCol(self, gesture):
		splitNum = self.lineInfo()
		colNum = splitNum[1]
		ui.message("column" + colNum)
		
	def lineInfo(self):
		possibleNum = api.getForegroundObject()
		lineNum = possibleNum.firstChild.getChild(1).lastChild.getChild(1).getChild(2).firstChild
		nextName = lineNum.next.name
		if nextName.startswith('CRLF'):
			lineNum = lineNum.name

		else:
			lineNum = nextName

		splitNum = lineNum.split(':')
		return splitNum

		
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
			tones.beep(500, 100)

			
	def script_runComm(self, gesture):
		gesture.send()
		ui.message("run")
		KeyboardInputGesture.fromName("f12").send()

	def script_stopComm(self, gesture):
		gesture.send()
		ui.message("stop")
		
	
	__gestures = {
		"kb:nvda+shift+f3": "lineNum",
		"kb:nvda+shift+f4": "lineCol",
		"kb:nvda+shift+f7": "errorSpeak",
		"kb:shift+f10": "runComm",
		"kb:control+f2": "stopComm",
	}
