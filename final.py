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


# we generate res which is list of lists where first element of res is list of states and next 8 elements are zeroes
res = []
with open('7.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    r = np.array(list_of_rows).T.tolist()
    res.append(r[0])
    for k in range(1, len(r)):
        res.append(np.zeros(len(r[0])))
# print(res)

# Now we read individual parameter csv files from [a.csv to b.csv]. We normalise each of the parameters and add them together.
# res will thus contain score for a particular criteria [a.csv to b.csv]. First element is list of states, next 8 elements are yearwise scores.
# overall score of all parameters (0 to 10):-
for num in range(1,11):
# scheme support score (0 to 2):-
# for num in range(1,3):
# scheme utilisation score (0 to 4):-
# for num in range(3,7):
# scheme management score (0 to 4):-
# for num in range(7,11):
    filename = str(num) + ".csv"
    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        r = np.array(list_of_rows).T.tolist()
        res = superadd(res, r)
# print(res)

# print("++++++++++++++++++++")
slope = []
avg = 0; count = 0
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
    avg += tempslope
    count += 1

# avg = avg/count
# stemp = ["INDIA"]
# stemp.append(avg)
# slope.append(stemp)


# rev_slope = []
# state_list = []; val_list = []
# for elem in slope:
    # state_list.append(elem[0])
    # val_list.append(elem[1])
    # rev_slope.append(elem[0])
# rev_slope = []
# rev_slope.append(state_list)
# rev_slope.append(val_list)
# print(rev_slope)

# with open("overall_trend.csv", 'w', newline="") as myfile:
# with open("support_trend.csv", 'w', newline="") as myfile:
# with open("utilisation_trend.csv", 'w', newline="") as myfile:
# with open("management_trend.csv", 'w', newline="") as myfile:

# with open("overall_score.csv", 'w', newline="") as myfile:
# with open("support_score.csv", 'w', newline="") as myfile:
# with open("utilisation_score.csv", 'w', newline="") as myfile:
# with open("management_score.csv", 'w', newline="") as myfile:
    wr = csv.writer(myfile, delimiter=",")
    for word in np.array(slope).T.tolist():
        wr.writerows([word])
    # for word in np.array(res).T.tolist():
        # wr.writerows([word])
