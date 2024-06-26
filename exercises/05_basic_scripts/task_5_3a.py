# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
mydict = {'access' : access_template + ['Введите номер VLAN:'],
          'trunk' : trunk_template + ['Введите разрешенные VLANы:']}
type_port = input('ведите режим работы интерфейса (access/trunk):')
a = mydict[type_port]
type_int = input('ведите тип и номер интерфейса: Fa0/7')
type_vlan = input(a[-1])
a.pop(-1)
a = '\n'.join(a).format(type_vlan)
print('interface {}'.format(type_int))
print(a)