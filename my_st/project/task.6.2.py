ip_add = input('Enter ip-address:' )

if     int(ip_add.split('.')[0]) in range(1, 223):
       print(f'IP_address {ip_add} is unicast')
elif   int(ip_add.split('.')[0]) in range(224,239):
       print(f'IP_address {ip_add} is multicast')
elif   int(ip_add.split('.')[0]) == 255  and int(ip_add.split('.')[1]) == 255  and int(ip_add.split('.')[2]) == 255  and int(ip_add.split('.')[3]) == 255:
        print(f'IP_address {ip_add} is  local_broadcast')
elif    int(ip_add.split('.')[0]) == 0  and   int(ip_add.split('.')[1]) == 0  and  int(ip_add.split('.')[2]) == 0  and int(ip_add.split('.')[3]) == 0:
 print(f'IP_address {ip_add} is  unassigned')
else:  
         print(f'IP_adress {ip_add} is other IP')


