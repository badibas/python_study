from pprint import pprint

with open('ospf.txt', 'r') as f:
     for line in f:
         Prefix = line.split()[1]
         Metric = line.split()[2]
         Next_Hop = line.split()[4]
         Last_update = line.split()[5]
         Out_int = line.split()[6]
         print(f'''
                  Prefix {Prefix}
                  AD/Metric {Metric}
                  Next-Hop {Next_Hop}
                  Last update {Last_update}
                  Outboud Interface {Out_int}
                 ''')
         print('=' * 40)
 


