def compare(list1, list2):
    return set(list2) - set(list1)


with open('aboutN2.txt', 'rU') as in_file:
    li1 = in_file.read().split('\n')

with open('aboutN1.txt', 'rU') as in_file:
    li2 = in_file.read().split('\n')

data = compare(li1,li2)


with open('aboutNEW.txt', 'w') as out_file:
    out_file.write('\n'.join(data))