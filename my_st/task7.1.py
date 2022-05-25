from pprint import pprint

with open('ospf.txt', 'r') as f:
     for line in f:
         Prefix = line.split()[1]
         Metric = line.split()[2].strip('[]')
         Next_Hop = line.split()[4].strip(',')
         Last_update = line.split()[5].strip(',')
         Out_int = line.split()[6]
         print(f'''
                 {'Prefix':20}{Prefix}
                 {'AD/Metric':20}{Metric}
                 {'Next-Hop':20}{Next_Hop}
                 {'Last update':20}{Last_update}
                 {'Outboud Interface':20}{Out_int}
                 ''')
         print('=' * 40)
 


