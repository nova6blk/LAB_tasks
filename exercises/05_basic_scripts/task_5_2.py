#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


enter = input('Введите IP адрес и префикс в формате Х.Х.Х.Х/XX: ')
### IP-address ###
octet_1 = int(enter.split('/')[0].split('.')[0])
octet_2 = int(enter.split('/')[0].split('.')[1])
octet_3 = int(enter.split('/')[0].split('.')[2])
octet_4 = int(enter.split('/')[0].split('.')[3])
### Prefix\mask ###
prefix = int(enter.split('/')[1]) ### /24
prefixbin = '1' * prefix + '0' * (32 - prefix) ### 11111111111111111111111100000000
maskbin_1 = prefixbin[0:8]
maskbin_2 = prefixbin[8:16]
maskbin_3 = prefixbin[16:24]
maskbin_4 = prefixbin[24:]
mask_1 = int(maskbin_1, 2)
mask_2 = int(maskbin_2, 2)
mask_3 = int(maskbin_3, 2)
mask_4 = int(maskbin_4, 2)

template = """
Network:
{0:<10} {1:<10} {2:<10} {3:<10}
{0:>08b}   {1:>08b}   {2:>08b}   {3:>08b}

Mask:
/{4}
{5:<10} {6:<10} {7:<10} {8:<10}
{9:10} {10:10} {11:10} {12:10}
"""
print(template.format(octet_1,octet_2,octet_3,octet_4,prefix,mask_1,mask_2,mask_3,mask_4,maskbin_1,maskbin_2,maskbin_3,maskbin_4))
######################
### Хуевое решение ###
######################
#prefix = int(enter.split('/')[1])
#prefixbin = '1' * prefix + '0' * (32 - prefix)
#octet_1 = '{:08b}'.format(int(enter.split('/')[0].split('.')[0])) + ' ' * 2
#octet_2 = '{:08b}'.format(int(enter.split('/')[0].split('.')[1])) + ' ' * 2
#octet_3 = '{:08b}'.format(int(enter.split('/')[0].split('.')[2])) + ' ' * 2
#octet_4 = '{:08b}'.format(int(enter.split('/')[0].split('.')[3]))
#
#maskbin_1 = prefixbin[0:8] + ' ' * 2
#maskbin_2 = prefixbin[8:16] + ' ' * 2
#maskbin_3 = prefixbin[16:24] + ' ' * 2
#maskbin_4 = prefixbin[24:] + ' ' * 2
#mask_1 = int(prefixbin[0:8], 2)
#mask_2 = int(prefixbin[8:16], 2)
#mask_3 = int(prefixbin[16:24], 2)
#mask_4 = int(prefixbin[24:], 2)
#
#print('Network:\n' + (' ' * 9).join(enter.split('/')[0].split('.')))
#print(octet_1, octet_2, octet_3, octet_4)
#print('\nMask:\n/' + str(prefix))
#print(mask_1, '      ',mask_2,'      ',mask_3,'      ',mask_4)
#print(maskbin_1, maskbin_2,maskbin_3,maskbin_4)
