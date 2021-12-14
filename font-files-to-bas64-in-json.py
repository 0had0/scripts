#!/usr/bin/python

import sys
import os
import json
import subprocess

if len(sys.argv) > 1:
	directory=sys.argv[1]
	json_array=[]

	for file in os.listdir(directory):
		if file.endswith('.ttf') or file.endswith('.otf'):
			path = os.path.join(directory, file)
			base64 = subprocess.run(['openssl', 'base64', '-in', path], stdout=subprocess.PIPE).stdout.decode('utf-8')
			[name, type] = file.split('.')
			json_array.append({"name": name, "base64": base64, "type": type})
	with open(f"{file.split('-')[0]}.json", "w") as output:
		output.write(json.dumps(json_array, indent=4, sort_keys=True))
else:
	print("please specify a directory")
