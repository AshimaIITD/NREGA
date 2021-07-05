from csv import reader
import numpy as np
import csv

def normlze(l):
    try:
        tt = [(k - min(l))/(max(l) - min(l)) for k in l]
        return tt
    except:
        # print(l)
        # print(max(l))
        # print(min(l))
        return [0 for k in l]


    # return [(k - min(l))/(max(l) - min(l)) for k in l]

def minmaxnorm(lis):
    ret = []
    ret.append(lis[0])
    for k in range(1, len(lis)):
        ret.append(normlze(lis[k]))
    return ret

def addlist(l1, l2):
    return [sum(x) for x in zip(l1, l2)]

def superadd(l1, l2):
    ret = []
    ret.append(l1[0])

    # ll2 = floatify(l2)
    ll2 = minmaxnorm(floatify(l2))

    for i in range(1, len(l1)):
        ret.append(addlist(l1[i], ll2[i]))
    return ret

def floatify(ee):
    ret = []
    ret.append(ee[0])
    for i in range(1, len(ee)):
        ret.append([float(k) for k in ee[i]])
    return ret


# print(minmaxnorm(check))
# for hh in minmaxnorm(check):
#     print(hh)

# '''
res = []

with open('2.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    r = np.array(list_of_rows).T.tolist()
    res.append(r[0])
    for k in range(1, len(r)):
        res.append(np.zeros(len(r[0])))

for x in res:
    print(len(x))
    print(x)
# '''

for num in range(1,11):
# for num in range(1,3):
    filename = str(num) + ".csv"

    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        r = np.array(list_of_rows).T.tolist()
        # for k in range(1, len(r)):
        res = superadd(res, r)

        # for x in np.array(list_of_rows).T.tolist():
        #     print(x)

print("++++++++++++++++++++")

slope = []
for x in np.array(res).T.tolist():
    stemp = [x[0]]
    sigma_xy = 0
    sigma_x = 0
    sigma_y = 0
    sigma_xx = 0
    nn = len(x) - 1
    for y in range(1, len(x)):
        # print(type(x[y]))
        # print(x[y])
        sigma_xy += y*float(x[y])
        sigma_x += y
        sigma_xx += y*y
        sigma_y += float(x[y])

    tempslope = (nn*sigma_xy - sigma_x*sigma_y)/(nn*sigma_xx - sigma_x*sigma_x)
    stemp.append(tempslope)
    slope.append(stemp)

# for i in range(1, len(res)):

with open("result.csv", 'w', newline="") as myfile:
    wr = csv.writer(myfile, delimiter=",")
    # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for word in np.array(slope).T.tolist():
        wr.writerows([word])




'''
for i in range(1, len(res)):

with open("result.csv", 'w', newline="") as myfile:
    wr = csv.writer(myfile, delimiter=",")
    # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for word in np.array(res).T.tolist():
        wr.writerows([word])
'''
