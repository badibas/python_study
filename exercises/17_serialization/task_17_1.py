# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
from pprint import pprint
import csv
import re

regex = (r"(?P<mac>\S+) +(?P<ip>(?:\d+.){3}\d+) +.+ +(?P<port>\S+)")

def write_dhcp_snooping_to_csv(file):
    sw = file.split('_')[0]
    with open(file) as f:
        result = []
        for line in f:
            match = re.search(regex, line)
            if match:
#               print(match.groups())
              mac, ip, port = match.groups() 
              
              result1 = "{}, {}, {}, {}".format(sw, mac, ip, port).split(",")
              
              result.append(result1)
               
        return result

if __name__ == "__main__":

#  result = []
#  for config in sh_dhcp:
#    result.append(write_dhcp_snooping_to_csv(config))
#  pprint(result)

   config_files = ('sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt')

   with open('output.csv', 'w') as f:
      write = csv.writer(f, delimiter = ';')
      write.writerow(['switch','mac','ip','interface'])
      for config in config_files:
        result = write_dhcp_snooping_to_csv(config)
#        print(result)
        for row in result:
            write.writerow(row)

