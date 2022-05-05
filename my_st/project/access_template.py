access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotion',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('\n'.join(access_template).format(5))

