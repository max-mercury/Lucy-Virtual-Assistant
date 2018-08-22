import os
import sys

from SenseCells.tts import tts

	
def etrx_block():
	tts("directions for electronics department")
	link = "eog -f etrx.png"
	os.system(link)

def biom_block():
	tts("directions for bio medical department")
	link = "eog -f biom.png"
	os.system(link)


def library_block():
	tts("directions for library")
	link = "eog -f library.png"
	os.system(link)

def vlounge_block():
	tts("directions for v lounge")
	link = "eog -f vlounge.png"
	os.system(link)
	

#xdotool getactivewindow windowkill