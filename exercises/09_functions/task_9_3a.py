# -*- coding: utf-8 -*-
from pprint import pprint

result = {}


with open("config_sw2.txt", "r") as f:
     list_file = f.read()
     cfg_section = list_file.split("!\n")
#     pprint(output)
     for section in cfg_section:
#         pprint(section)
         if section.startswith("interface Fast"):
            section_lines = section.split("\n")
            for line in section_lines:
                if line.startswith("interface"):
                   intf = line.split()[1]
                   result[intf] = "VLAN1"
#                   print(intf)
                elif "allowed vlan" in line:
                   trunk = line.split()[-1]
                   result[intf] = trunk
#                   print(trunk)
                elif "access vlan" in line:
                   access = line.split()[-1]
                   result[intf] = access
#                   print(access)

pprint(result)

"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
