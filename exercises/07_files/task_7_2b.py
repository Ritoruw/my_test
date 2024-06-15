# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

filename = argv[1]
ignore = ["duplex", "alias", "configuration"]
q = argv[2]
fq = open(q,'w')
listq = []
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
                listq.append(line)
#                 print(line)

fq.writelines(listq)
fq.close()
