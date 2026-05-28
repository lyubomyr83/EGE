"""
Сеть задана IP-адресом 106.184.0.0 и маской сети 255.248.0.0.
Сколько в этой сети IP-адресов, для которых сумма единиц в двоичной записи IP-адреса не кратна 2?
В ответе укажите только число.
"""

from ipaddress import ip_network

net = ip_network('106.184.0.0/255.248.0.0', 0)

col = 0
for ip in net:
    ip = ip.__str__().split('.')
    ip = list(map(int, ip))
    ip = list(map(lambda n: bin(n)[2:].zfill(8), ip))
    ip = ''.join(ip)

    if ip.count('1') % 2 != 0:
        col += 1

print(col)
