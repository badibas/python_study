type  = input("Введите рижим работы интерфейса (access/trunk): ")
interface_number  = input("Введите тип и номер интерфейса: ")
r1 = {'access':"Введите номер VLAN: ", 'trunk':"Введите список разрешенных VLANs: "}
vlan = input(r1[type])


access_template = [
       "switchport mode access", "switchport access vlan {}",
       "switchport nenegotiate", "spanning-tree portfast",
       "spaning-tree bpduguard enable"
       ]

trunk_template = [
       "switchport trunk encapsulation dot1q", "switchport mode trunk",
       "switchport trunk allowed vlan {}"
      ]
ac = dict(access = access_template, trunk = trunk_template)
 
ac1 = ac[type]

print('\n'+ '-' * 50)
print ('interface {}'.format(interface_number))
print ('\n'.join(ac[type]).format(vlan))
# print ('\n'.join().format(vlan))
