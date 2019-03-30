import eel
from eel import sleep
import sys
import subprocess
from subprocess import PIPE
import os
from config import *

eel.init('web')
web_app_options = {
    'mode': "chrome-app", #or "chrome"
    'port': 8080,
    'chromeFlags': ["--aggressive-cache-discard  --allow-file-access-from-files"]
}

#Load Tokens
if os.path.exists('tokens.txt'):
    userToken = open("tokens.txt").read().splitlines()

if os.path.exists('proxies.txt'):
    proxy_list = open("proxies.txt").read().splitlines()
else:
    proxy_list = []
    for token in userToken:   
        proxy_list.append('localhost')

@eel.expose
def save_token(s):
    file = open('tokens.txt','a')
    file.write(s+'\n')
    file.close()



@eel.expose
def tokenRun():
    for token in userToken:
        eel.log(token);

@eel.expose
def sv_textSpam():
    proxy_number = 0
    if os.path.exists('text.txt'):
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots\server\discord_text_spam.py',token,'null',proxy_list[proxy_number]],shell=True)
            proxy_number += 1
            sleep(1)
    else:
        #spam_text = input("Write spam text : ")
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots\server\discord_text_spam.py',token,spam_text,proxy_list[proxy_number]],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE, bufsize=1)
            proxy_number += 1
            sleep(1)
    for line in p.stdout:
        line = line.decode("utf-8").rstrip()
        eel.log(line);
    #p.wait()

def sv_imgSpam_F():
    proxy_number = 0    
    for token in userToken:
        p = subprocess.Popen([pythonCommand, 'bots\server\discord_image_spam.py', token,proxy_list[proxy_number]],shell=True)
        proxy_number += 1
    p.wait()
            
def sv_insult_F():
    proxy_number = 0
    for token in userToken:
        p = subprocess.Popen([pythonCommand,'bots\server\discord_insult_spam.py', token,proxy_list[proxy_number]],shell=True)
        proxy_number += 1
    p.wait()

#DM Spammers
def dm_spamText_F(spam_text):
    proxy_number = 0
    if os.path.exists('text.txt'):
        if not os.path.exists('dm_spam_text.txt'):
            file = open('dm_spam_text.txt','w')
            file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
            file.close()
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots\DM\discord_text_spam_dm.py',token,'null',proxy_list[proxy_number]],shell=True)
            proxy_number += 1
            sleep(2.5)
    else:
        if not os.path.exists('dm_spam_text.txt'):
            file = open('dm_spam_text.txt','w')
            file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
            file.close()
        spam_text = input("Write spam text : ")
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots\DM\discord_text_spam_dm.py',token,spam_text,proxy_list[proxy_number]],shell=True)
            proxy_number += 1
            sleep(2.5)
    p.wait()

def dm_imgSpam_F():
    proxy_number = 0
    if not os.path.exists('dm_spam_image.txt'):
        file = open('dm_spam_image.txt','w')
        file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
        file.close()
    for token in userToken:
        p = subprocess.Popen([pythonCommand, 'bots\DM\discord_image_spam_dm.py', token,proxy_list[proxy_number]],shell=True)
        proxy_number += 1
    p.wait()

def dm_insult_F():
    proxy_number = 0
    if not os.path.exists('dm_spam_insult.txt'):
        file = open('dm_spam_insult.txt','w')
        file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
        file.close()
    for token in userToken:
        p = subprocess.Popen([pythonCommand,'bots\DM\discord_insult_spam_dm.py', token,proxy_list[proxy_number]],shell=True)
        proxy_number += 1
    p.wait()

def joinServer_F():
    proxy_number = 0
    for token in userToken:
        if userToken == False:
            enp = token.split(':')
            p = subprocess.Popen([pythonCommand,'bots\misc\joinServer.py',enp[0],enp[1],inviteLink,useBrowser,proxy_list[proxy_number]],shell=True)
            proxy_number += 1        
            sleep(joinSpeed)
        else:
            p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,proxy_list[proxy_number]],shell=True)
            proxy_number += 1        
            sleep(joinSpeed)
    p.wait()

eel.start('gui.html')
