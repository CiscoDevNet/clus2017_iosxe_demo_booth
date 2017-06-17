import os
import sys
from cli import cli
import time
import difflib
from spark import *

SPARK_ROOM = "Catalyst OnBox"

my_token = "ODY1ZWE3ZTUtY2JhNS00Njc2LWI1MDYtMTAwY2EwM2FkNzFmYTM4YzdhMjgtODI5"
bot_token = "Mjg3ZWVjMTYtYzc2NC00ZDc2LTg5ZWMtYjJlMmYyYTllZjA5YzlhM2ZhYmMtZTAy"

def save_config():

	output = cli('show run')

	timestr = time.strftime("%Y%m%d-%H%M%S")
	filename = "/home/guestshell/configs/" + timestr + "_shrun"

	f = open(filename,"w")
	f.write(output)
	f.close

	f = open('/home/guestshell/configs/current_config_name','w')
	f.write(filename)
	f.close

	return filename

def get_cfg_fn():

	try:
		f = open('/home/guestshell/configs/current_config_name','r')
	except:
		return None
	fn = f.read()
	f.close()
	return fn

def compare_configs(cfg1,cfg2):

	d = difflib.unified_diff(cfg1, cfg2)

	diffstr = ""

	for line in d:
		if line.find('Current configuration') == -1:
			if line.find('Last configuration change') == -1:
				if (line.find("+++")==-1) and (line.find("---")==-1):
					if (line.find("-!")==-1) and (line.find('+!')==-1):
						if line.startswith('+'):
							diffstr = diffstr + "\n" + line
						elif line.startswith('-'):
							diffstr = diffstr + "\n" + line

	return diffstr

if __name__ == '__main__':

	old_cfg_fn = get_cfg_fn()

	if not old_cfg_fn:
		#  First time we are running
		save_config()
		sys.exit()

	new_cfg_fn = save_config()

	f = open(old_cfg_fn)
	old_cfg = f.readlines()
	f.close

	f = open(new_cfg_fn)
	new_cfg = f.readlines()
	f.close

	os.remove(old_cfg_fn)

	text = "Configuration change detected:" + "\n" + compare_configs(old_cfg,new_cfg)

	room = get_room_id(SPARK_ROOM, my_token)

	post_message(text, room, bot_token)