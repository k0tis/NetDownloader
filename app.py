#python sosi moi 4len
import requests as req
from time import sleep
from os import system

system("title NetDownload.exe - Working.")
url = input("Url: ")

def wait():
	system("title NetDownload.exe - Closing.")
	sleep(3)
	exit()

try:
	resp = req.get(url)
	open(filename, "wb").write(resp.content)
	print("File " +filename+ "successfully downloaded.")
	wait()

except:
	print("An error occurred while downloading.")
	wait()
