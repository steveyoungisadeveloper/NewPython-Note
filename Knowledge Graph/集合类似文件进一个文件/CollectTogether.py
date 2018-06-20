import re

l2 = open('len2.txt', 'w', encoding='UTF-8')
l3 = open('len3.txt', 'w', encoding='UTF-8')
l4= open('len4.txt', 'w', encoding='UTF-8')
l5 = open('len5.txt', 'w', encoding='UTF-8')
with open('RlesTogether.txt', 'w', encoding='UTF-8') as outPut:
    for i in range(37):
        with open('PouyaYAGOoutput/transrules_d12_%d.txt' % (i), "r",  encoding='UTF-8') as inPut:
            for line in inPut:
                if line.startswith('ruleidx'):
                    print()
                elif line.startswith('R'):
                    outPut.writelines(line)
                    info = re.findall(r'and', line)
                    if len(info) == 1:
                        l2.writelines(line)
                    elif len(info) == 2:
                        l3.writelines(line)
                    elif len(info) == 3:
                        l4.writelines(line)
                    elif len(info) == 4:
                        l5.writelines(line)
                    else:
                        print("Wrong!!!!!!!")

l2.close()
l3.close()
l4.close()
l5.close()
