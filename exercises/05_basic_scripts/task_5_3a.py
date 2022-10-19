#!/usr/bin/env python3.10
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
int_dict = {
    'quest': {
        'access': 'Введите номер VLAN: ',
        'trunk': 'Введите разрешенные VLANы:'
        },
    'mode': {
        'access': access_template,
        'trunk': trunk_template
        }
    }
int_mode = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: ')
int_vlan = input(int_dict.get('quest').get(int_mode))
print('interface {}\n'.format(interface) + '\n'.join(int_dict.get('mode').get(int_mode)).format(int_vlan))
### Сортировка вланов в трнке и удаление дублей ###
#print('interface {}\n'.format(interface) + '\n'.join(int_dict.get('mode').get(int_mode)).format(str(sorted(set(int_vlan.split(',')))).strip('{}').replace("'",'').replace(' ','').strip('[]')))