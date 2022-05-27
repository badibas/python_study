# -*- coding: utf-8 -*-

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}
def generate_trunk_config(intf_config, trunk_mode):
   for  intf, vlans in intf_config.items():
        print(f'interface {intf}')
        for interface in trunk_mode:
             if  interface.endswith("allowed vlan"):
                print("{} {}".format(interface, str(vlans).strip('[]')))
             else:
                print(f"{interface}")

generate_trunk_config(trunk_config, trunk_mode_template)
generate_trunk_config(trunk_config_2, trunk_mode_template)
