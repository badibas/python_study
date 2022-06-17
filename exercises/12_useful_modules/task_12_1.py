# -*- coding: utf-8 -*-

from pprint import pprint
import ipaddress
import subprocess

def ping_ip_address(ip):
      reply = subprocess.run(
              ['ping', '-c', '2', '-n', ip],
               stdout=subprocess.DEVNULL
               )
      if reply.returncode == 0:
           return True  
      else:
           return None

if __name__ == "__main__":

  ip_list = ("8.8.8.8", "192.168.160.1", "8.8.4.4", "10.178.255.10")
  ip_ok = []
  ip_no_ok = []  
  for ip in ip_list:
      status = ping_ip_address(ip)
      if status:
         ip_ok.append(ip)
      else:
         ip_no_ok.append(ip)
  pprint("Доступные адреса {} Не доступные адреса {}".format(ip_ok, ip_no_ok))
