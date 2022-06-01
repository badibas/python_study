# -*- coding: utf-8 -*-
from pprint import pprint

def get_int_vlan_map(filename):
     access_port = {}
     trunk_port = {}
     with open(filename) as f:
         for  line in f:
             if "interface Fas" in line:
                intf = line.split()[-1]
                access_port[intf] = 1
             elif "access vlan" in line:
                access = line.split()[-1]
                access_port[intf] = int(access) 
             elif "allowed vlan" in line:
                trunk = line.split()[-1].split(",")
                items = []  
                for vlan in trunk:
                      vlan = int(vlan)
                      items.append(vlan) 
#                     trunk_port[intf].append(vlan)
                trunk_port[intf] = items
     return  access_port, trunk_port

result = get_int_vlan_map("config_sw2.txt")

pprint(result)
#pprint(block)



"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
