# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""


import re
from pprint import pprint

regex = (
         r"interface (?P<intf>\S+)"
         r" ip address (?P<ip_add>\S+) (?P<ip_mask>(\S+))"
         r"| ip address (?P<ip_sec>\S+) (?P<mask_sec>\S+) \S+"
        )
result = {}
#def get_ip_from_cfg(file):
with open('config_r2.txt') as f:
       for line in f:
          match = re.search(regex, line)
          if match:
#             print(match.group(2))
             if match.lastgroup == 'intf':
                interface = match.group(match.lastgroup)
                result[interface] = {}
#             elif match.lastgroup == 'ip_sec':
#                result[interface] == match.group(5)
             else: 
                 result[interface] =  match.group(match.lastgroup)
       pprint(result)


#def clear_ip(config_file):
#  data = get_ip_from_cfg(config_file)
#  result = {}
#  for key, value in data.items():
#      if  data[key]:
#         result[key] = value
#  return result

#if __name__ == "__main__":

#   pprint(get_ip_from_cfg("config_r2.txt"))

