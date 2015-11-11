#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "blu3b0lt"
__copyright__ = "Copyright (c) 2015 blu3b0lt"
__credits__ = ["Forismatic.com"]



import requests
import json
import subprocess
import time
import os

while True:
	response = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json")
	responseJson = json.loads(response.text)
	author = responseJson['quoteAuthor']
	quote = responseJson['quoteText']
	currentDirectory = os.getcwd()
	iconPath = currentDirectory + "/icon.png"
	subprocess.call(["notify-send", "-u", "normal", "-t", "10000", "-c", "Quotes", "-i", iconPath, author+" says" , '" '+quote+' "'])
	time.sleep(2400)