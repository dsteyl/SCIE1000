from pylab import *

array1 = array([1,43,7,12,3,9,2,23,4,5,6,2,3,65,7,43,2,3,4,5,67,8,3,2,345,456,8,2,21,34])
array2 = array([123,43,6467,12,234,68,2,4,5,5,5,23,543,4576,8678,4,2,3,4,34,53,4,4,4,68,8,8,21,5,67])
win_loss_draw = zeros(int(30))

i = 0
while i<30:
    if array1[i]>array2[i]:
        win_loss_draw[i] = 3
    elif array1[i]<array2[i]:
        win_loss_draw[i] = 1
    else:
        win_loss_draw[i] = 2

    i = i + 1
