access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

#for intf, vlan in access.items():
#   print("interface FastEthernet" + intf)
#    for command in access_template:
#        if command.endswith("access vlan"):
#            print(f" {command} {vlan}")
#        else:
#            print(f" {command}")
add = []
only = []
delet = []

for  intf, vlan in trunk.items():
     print("interface FastEthernet " + intf)
     for command in trunk_template:
         if command.endswith("allowed vlan"):
             if intf == "0/1":
                 for add in vlan():
                     add +=1
                 print(add)
 #                print(f"{command}" + " add " + f"{vlan[1]}"+ ', ' +f"{vlan[2]}")
             elif intf == "0/2":  
                 print(f"{command}" + ' ' + f"{vlan[1]}"+',' +f"{vlan[2]}")       
             elif intf == "0/4":
                 print(f"{command}" + " remove " + f"{vlan[1]}") 
         else:
             print(f"{command}")
