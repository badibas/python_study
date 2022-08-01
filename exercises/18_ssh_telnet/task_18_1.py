# -*- coding: utf-8 -*-
"""
Задание 18.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству
и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml
с помощью функции send_show_command (эта часть кода написана).

"""
import yaml
import netmiko

r1 = {
     'device_type': 'cisco.ios',
     'host': '192.168.100.1',
     'username': 'cisco',
     'password': 'cisco',
     'secret': 'cisco',
     }


def send_show_command(device, command):

    ssh = netmiko.Netmiko(**device)
    ssh.enable()
    return ssh.send_command(command)         
    



if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))

