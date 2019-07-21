def xor(list1, list2):
    list3=list1+list2
    for i in range(0, len(list3)):
        x=list3[i]
        y=i
        while y>0 and x<list3[y-1]:
            list3[y]=list3[y-1]
            y=y-1
        list3[y]=x

        last=list3[-1]
    for i in range(len(list3) -2, -1, -1):
        if last==list3[i]:
            del list3[i]
        else:
            last=list3[i]

    return list3 



with open('clientsn1.txt', 'rU') as in_file:
    li1 = in_file.read().split('\n')

with open('clientsn2.txt', 'rU') as in_file:
    li2 = in_file.read().split('\n')

data = xor(li1,li2)


with open('clientsNew.txt', 'w') as out_file:
    out_file.write('\n'.join(data))