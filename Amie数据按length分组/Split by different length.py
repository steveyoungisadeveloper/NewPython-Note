import re

l2 = open('len2.txt', 'w', encoding='UTF-8')
l3 = open('len3.txt', 'w', encoding='UTF-8')
l4= open('len4.txt', 'w', encoding='UTF-8')
l5 = open('len5.txt', 'w', encoding='UTF-8')
with open('cleanrules.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        info = re.findall(r'<', line)
        print(info)
        if len(info) == 2:
            l2.writelines(line)
        elif len(info) == 3:
            l3.writelines(line)
        elif len(info) == 4:
            l4.writelines(line)
        elif len(info) == 5:
            l5.writelines(line)
        else:
            print("Wrong!!!!!!!")
l2.close()
l3.close()
l4.close()
l5.close()
