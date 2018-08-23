#Add on for PyCharms

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
		#add split to get just num
		ui.message("line" + name)

	def script_errorSpeak(self, gesture):
		errorLoc = api.getForegroundObject()
		error = errorLoc.firstChild.getChild(1).getChild(2).getChild(1).firstChild.firstChild.firstChild.firstChild.firstChild
		#add split to get just num
		if error.firstChild is not None:
			errorMessage = error.name
			ui.message(errorMessage)
		else
			tones.beep(440, 1000)
		
	
	__gestures = {
		"kb:nvda+shift+f3": "lineNum",
		"kb:nvda+shift+f7": "errorSpeak"
	}