# -*- coding: utf-8 -*-
"""
Задание 18.2a

Скопировать функцию send_config_commands из задания 18.2 и добавить параметр log,
который контролирует будет ли выводится на стандартный поток вывода информация о том
к какому устройству выполняется подключение.
По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства
из файла devices.yaml с помощью функции send_config_commands.
"""
import netmiko
from pprint import pprint
import yaml
#import paramiko
import logging

#logging.getLogger("paramiko").setLevel(logging.WARNING)
#logging.getLogger("netmiko").setLevel(logging.WARNING)

#logging.basicConfig(format="%(threadName)s %(name)s %(levelname)s: %(message)s",
#                    level=logging.INFO)


#logging.basicConfig(format="%(threadName)s %(name)s %(levelname)s: %(message)s", level=logging.INFO)
def  send_config_commands(device, config_commands, log = True):
    host = device['host']
    logging.info(f"Подключаюсь к  {host}")
    if log == True:
      print(f"Подключаюсь к {host}")
    else:
     pass
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        prompt = ssh.find_prompt()
        return ssh.send_config_set(config_commands)
   
if __name__ == "__main__":
    
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]

    r1 = {'device_type': 'cisco_ios',
     'host': '192.168.100.1',
     'username': 'cisco',
     'password': 'cisco',
     'secret': 'cisco'}


    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)       
        for dev in devices:
            print(send_config_commands(dev, commands))

