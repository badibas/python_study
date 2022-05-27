# -*- coding: utf-8 -*-
access_config = {
     'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/16': 17
     }

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

def generate_access_config(intf_vlan_mapping, access_template):
   for  intf, vlan  in intf_vlan_mapping.items():
         print('interface ' +intf)
         for interface_config in access_template:     
            if interface_config.endswith('access vlan'):
                print("{} {}".format(interface_config, vlan))
            else:
                print(f'{interface_config}')

generate_access_config(access_config_2, access_mode_template)

#def  generate_access_config(intf_vlan_mapping, access_template):
"""
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
"""
