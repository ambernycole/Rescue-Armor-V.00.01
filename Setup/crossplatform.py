#!/usr/bin/python

#This file implements the code that makes Rescue Armor work cross platform in a way that I find sensible.
#If you don't, feel free to submit a pull request, fork or do whatever within the terms of the license agreement.

import os
import platform
import urllib.request

opersys = platform.system()

def dl_file(furl, fn=None):
	"""
	Download a file in a reusable way taking a file url and file name (optional)
	"""
	try:
		
		if fn == None:
			#There wasn't a filename specified, so let's figure out what to name it
			#To do that, let's take the URL, split it at / and get the string after the last slash
			fn = furl.split('/')[-1]
			urllib.request.urlretrieve(furl, fn)
			return fn
		else:
			#Somebody supplied their own file name for some reason, bleh but we can accomidate that
			urllib.request.urlretrieve(furl, fn)
			return fn
	except:
		#Oh shit, something went wrong
		print('le poop')

def get_operating_system():
	"""
	Returns the operating system, or in the case of linux, which distro
	"""
	match opersys:
		case "Windows":
			return 'windows'
		
		case 'Darwin':
			return 'macos'
		
		case "Linux":
			#We need to determine the distro now
			distro = platform.node()	
		
			match distro:
			
				case 'fedora':
					return 'fedora'
				
				case 'ubuntu':
					return 'ubuntu'
					
				case 'mint':
					return 'mint'
				
				case _:
					return 'generic-linux'
		case _:
			print('Unable to detect OS')
			exit()
			
def verify_signature(app):
	"""
	For the security consious, verifying the file they download is the correct one is probably important.
	There's many different ways that packages do this, from a simple MD5 hash (bad) to a digital signature (good)
	so we probably need a way to determine how to handle each app.
	"""
	opersys = get_operating_system()
	return 'bleh'
	
def find_file(fname, path='/'):
	"""
	Different operating systems install files in different places, so we need a way to see if a file exists. os.walk
	gives us that. It takes a file name (fname) and path (by default /, or the root directory) and looks for the file
	in question, returning the first result.
	"""	
	for root, dirs, files in os.walk(path):
	if name in files:
	    return os.path.join(root, name)




if __name__ == "__main__":
	#This really shouldn't do anything but, since I'm lazy, we're gonna test shit as needed instead of writing actual tests.
	url = 'https://stackoverflow.com/questions/24713597/urlretrieve-error-handling/boogers/xd/rox'
	dl_file(url)

