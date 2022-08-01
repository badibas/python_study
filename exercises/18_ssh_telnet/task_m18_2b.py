import netmiko
from pprint import pprint
import yaml
import logging

cor = {}
incor = {}

def  send_config_commands(device, config_commands, log = True):
   host = device['host']
#   logging.info(f"Подключаюсь к  {host}")
#   if log == True:
#      print(f"Подключаюсь к {host}")
#   else:
#     pass
   with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
#        cor = {}
#        incor = {}
    # for config_commands in com:
        command = ssh.send_config_set(config_commands)
        if '%' in command:
           incor[config_commands] = command
           if "% Invalid input" in command:
               print(f"Команда \'{config_commands}\' выполнилась с ошибкой <<Invalide input detection>> на устройстве \'{host}\'") 
           elif "% Incomplet" in command:
               print(f"Команда \'{config_commands}\' выполнилась с ошибкой <<Incomplete command>> на устройстве \'{host}\'")
           elif "% Ambiguous" in command:
               print(f"Команда \'{config_commands}\' выполнилась с ошибкой <<Ambiguous command>> на устройстве \'{host}\'")
        else:
           cor[config_commands] = command
#        return (cor, incor)
#pprint((cor, incor))  

if __name__ == "__main__":
    
   # commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    commands = ['logging 0255.255.1',
                 'logging',
                 'a',
                 'logging buffered 20010',
                 'ip http server']
    r1 = {'device_type': 'cisco_ios',
     'host': '192.168.100.1',
     'username': 'cisco',
     'password': 'cisco',
     'secret': 'cisco'}


#    with open("devices.yaml") as f:
#        devices = yaml.safe_load(f)       
#        for dev in devices:
#    for com in commands:
    host = r1['host']
 #  if log == True:
    print(f"Подключаюсь к {host}")
    for com in commands:
         send_config_commands(r1, com)
pprint(cor, incor)
