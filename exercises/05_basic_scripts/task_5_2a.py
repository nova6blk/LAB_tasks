#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
enter = input('Введите IP адрес и префикс в формате Х.Х.Х.Х/XX: ')
prefix = int(enter.split('/')[1]) ### /24
### IP-address ###
octet_1bin = '{:08b}'.format(int(enter.split('/')[0].split('.')[0]),'b')
octet_2bin = '{:08b}'.format(int(enter.split('/')[0].split('.')[1]),'b')
octet_3bin = '{:08b}'.format(int(enter.split('/')[0].split('.')[2]),'b')
octet_4bin = '{:08b}'.format(int(enter.split('/')[0].split('.')[3]),'b')
new_ip_bin = (octet_1bin + octet_2bin + octet_3bin + octet_4bin)[:prefix] + '0' * (32 - prefix)
octet_1 = int(new_ip_bin[0:8],2)
octet_2 = int(new_ip_bin[8:16],2)
octet_3 = int(new_ip_bin[16:24],2)
octet_4 = int(new_ip_bin[24:],2)
### Prefix\mask ###
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