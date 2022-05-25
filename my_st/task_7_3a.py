# -*- coding: utf-8 -*-

from  pprint import pprint

path = "/home/python/first_repo/python_study/exercises/07_files/"

result = {}
fac =  []

with open(f"{path}CAM_table.txt", 'r') as f:

    for line in f:
        line = line.split()
        if line and  line[0].isdigit():
            if  str(int(line[1][:3], 16)).isdigit():
                 vlan, mac, *_, intf = line
                 fac.append(f"{int(vlan):<5} {mac:15} {intf:>9}")
#                 result[int(vlan)] = mac, intf
#                print(f"{line[0]:5} {line[1]:15} {line[3]:9}")
#                 result = '{:5} {:15} {:9}'.format(vlan, mac, intf)

#sorted(result)
#sorted(fac)
pprint(sorted(fac))
#print('{} {} {}'.format(sorted, sorted[0], sorted[1]))
#print(result[vlan])
#table = tuple(result)
#pprint(result)
#pprint(f"{result.keys()} {result.values()}")
#pprint(result.items())
#pprint(f"{result.key()} {result.values()}")
# {result.values[1]}")
            




"""
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
