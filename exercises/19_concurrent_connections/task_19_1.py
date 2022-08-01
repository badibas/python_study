# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import subprocess


def ping_ip(ip_list):
#    valid = []
#    invalid = [] 
    result = subprocess.run(['ping', '-c', '2', '-n', ip_list], stdout=subprocess.DEVNULL)
#    if result.returncode == 0:
#       valid.append(ip_list)
#    else:
#       invalid.append(ip_lis)
    return result.returncode

def ping_ip_addresses(ip_list, limit=3):   
   valid = []
   invalid = []
   with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_ip, ip_list)
        for ip, code in zip(ip_list, result):
            if code == 0:
               valid.append(ip)
            else:
               invalid.append(ip)
   print(valid, invalid)        

if __name__ == "__main__":
   ping_ip_addresses(['192.168.100.1', '192.168.100.2', '192.168.100.12'])
