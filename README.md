# nvdaproj
In modern software development, IDEs (Integrated Development Environments) play a critical role in efficient workflow but rely heavily on visual cues. NVDA (Non-Visual Desktop Access) is an open-source screen reader offered for free, making it a popular choice for not only programming, but everyday use. My approach to accessibility in IDEs is creating an NVDA add-on for Pycharm Professional as it is a popular choice for professional use but falls behind many others in accessibility for blind programmers.


## add-on features
* **Line Numbers/Line Length (NVDA+Shift+F3):** This feature reads aloud line information. Understanding not only the location of lines of code, but in the context of the rest of the structure is important for development, especially for higher level projects and work. Line length gives insight to code style which is very much a visually focused detail important in keeping things clean and understandable by users. 

* **Error Descriptions (NVDA+Shift+F7):** Locating and understanding errors is somewhat accessible in Pycharms with keyboard shortcuts but this action gives no audio cues even with the Java Access Bridge and current screen reader support. This feature works with the existing process and lets the user know what is trying to be communicated when navigating through errors/warnings: f2 navigates through errors, shift+f1 brings up the description, and NVDA+Shift+F7 reads that information aloud. In the case there are none left to navigate through and no error description is presented, a beep will sound instead to notify this. 

* **Run/Stop:** This feature works with the existing PyCharm commands for running and stopping code as it is another process that gives no no support for accessibility other than silently executing. Using PyCharm's commands, Shift+F10 to run and Control+F2 to stop, speaks the action aloud and directs the carret focus to the respective windows.*


*Still in progress


## How to set up NVDA + PyCharm + Java Access Bridge
Java Access Bridge (JAB) is needed for this add-on to work. It allows many features to become visible to NVDA. Without it, PyCharm is completely inaccessible. 
1. Enable JAB: This can be done through the command prompt, using the command: (JRE_LOC)\bin\jabswitch -enable, where (JRE_LOC) is the path to JRE on your computer. 
2. Enable "Support Screen Readers" in Pycharm: This option is located in Settings/Preferences|Appearance & Behavior|System Settings
3. Add this file to NVDA add-ons: This version of the add-on is not packaged for installation. To test it as it is, place this file in the AppModules folder located in NVDA's Configuration Directory.

## Troubleshooting
* Check that the related files are in the correct places for the programs to work correctly together: WindowsAccessBridge-32.dll in C:\Windows\SysWOW64 and WindowsAccessBridge-64.dll in C:\Windows\System32.
* The name of this file which goes into NVDA's Configuration Directory should match the PyCharm's execution name. For example, pycharm.exe would make this file pycharm.py. Check for other versions of this name, like pycharm64.exe. 
