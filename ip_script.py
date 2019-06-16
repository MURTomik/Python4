# 1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
# («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
# 2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
# Меняться должен только последний октет каждого адреса.
# По результатам проверки должно выводиться соответствующее сообщение.
# 3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера
# 2. Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
# (использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
# Reachable
# 10.0.0.1
# 10.0.0.2
#
# Unreachable
# 10.0.0.3
# 10.0.0.4

import ipaddress
# import socket
import subprocess
from tabulate import tabulate

def host_ping(list_ip):
    list_rezult = []
    for i in list_ip:
        if subprocess.call(f'ping {i}', shell=True, stdout=subprocess.PIPE):
            # print(f'{i} - доступен')
            list_rezult.append([i,'доступен'])
        else:
            # print(f'{i} - не доступен')
            list_rezult.append([i, 'не доступен'])
    return list_rezult

def spisok_ip(start, end):
    list_ip_next = []
    j = start
    while j <= end:
        list_ip_next.append(ipaddress.ip_address(f'10.0.0.{j}'))
        # list_ip_next.append(ipaddress.ip_address(f'213.180.204.{j}'))
        j += 1
    return list_ip_next

def host_range_ping(start, end):
    list = spisok_ip(start, end)
    list_rezult = host_ping(list)
    print(list_rezult)
    return list_rezult

def host_range_ping_tab(start, end):
    list = host_range_ping(start, end)
    print(tabulate(list, headers=['IP','Результат']))


# list_ip = []
# list_ip.append(socket.gethostbyname("www.goole.com"))
# list_ip.append(socket.gethostbyname("www.yandex.com"))
# list_ip.append(socket.gethostbyname("www.rp5.ru"))
#
# for i in range(5):
#     ip = ipaddress.ip_address(f'213.180.204.6{i}')
#     list_ip.append(ip)
# print(list_ip)
#host_ping(list_ip)

start = int(input('Введите начальное значение диапазона: '))
end = int(input('Введите конечное значение диапазона: '))

#host_range_ping(start, end)
host_range_ping_tab(start, end)






