# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_addr=input('Введите IP-адрес:')
a = 0
l=0 # for .
a=0 # for error
for k in ip_addr:
    if (k.isdigit() or k == '.'):
        a = a + 0
    else:
        a = a + 1
if ip_addr.count('.') != 3:
    a = a + 1
for k in ip_addr.split('.'):
    if len(k) == 0:
        a = a + 1
if (a == 0):
    ip = ip_addr.split('.')
    for k in ip:
        if (int(k)>=0 and int(k)<=255):
            a = a + 0
        else:
            a = a + 1
if a == 0:
    if (int(ip[0])>=1 and int(ip[0])<=223):
        print('unicast')
    elif (int(ip[0])>=224 and int(ip[0])<=239):
        print('multicast')
    elif (ip_addr == '255.255.255.255'):
        print('local broadcast')
    elif (ip_addr == '0.0.0.0'):
        print('unassigned')
    else:
        print('unused')
else:
    print ('Неправильный IP-адрес')