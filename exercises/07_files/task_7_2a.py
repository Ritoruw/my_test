# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

filename = argv[1]
ignore = ["duplex", "alias", "configuration"]

with open(filename) as f:
    for line in f:
        if line[0] != '!':
            # Проверяем, содержит ли строка хоть одно из игнорируемых слов
            should_ignore = 0
            for i in range(len(ignore)):
                if ignore[i] in line:
                    should_ignore = 1
                    break
            if should_ignore == 0:
                print(line)
