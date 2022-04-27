ip_add = input('Enter ip address and prefix: ')

ip_add1 = ip_add.split('/')

ip1 = ip_add1[0].split('.')
a = int(ip1[0])
b = int(ip1[1]) 
c = int(ip1[2])
d = int(ip1[3])
mask = int(ip_add1[-1])

ip_template = '''
              {0:<8} {1:<8} {2:<8} {3:<8}
              {0:08b} {1:08b} {2:08b} {3:08b}
              '''

m = 32 - mask
mas = '1' * mask + '0' * m
e = int(mas[0:8], 2)
f = int(mas[8:16], 2)
i = int(mas[16:24], 2)
j = int(mas[24::], 2)

print('\n' + '-' * 50)
print('Network:' '\n' + ip_template.format(a,b,c,d))
print('Mask:' '\n' + ip_template.format(e,f,i,j))
