# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""


import re
from pprint import pprint
regex = (r"interface +(?P<int>\S+)\n+ (?P<desc>description) .+")
#?P<descr>.+)")
regex1 = (r"interface +(?P<int>\S+)\n")

def get_ints_without_description(file):
   with open(file) as f:
      config = re.split(r"!\n", f.read())
      result = []
      for line in config:
          if line.startswith('interface'):
              match = re.match(regex, line)             
              if not match:
                   match1 = re.match(regex1, line)
                   result.append(match1.group(1))
      return result


print(get_ints_without_description('config_r1.txt'))
