type  = input("Введите рижим работы интерфейса (access/tunk): ")
interface_number  = input("Введите тип и номер интерфейса: ")
vlan  = input("Введите номер VLAN(s): ")



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
