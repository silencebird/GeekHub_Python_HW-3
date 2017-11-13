import random
import time

n = 1000
k = 99


# function will generate 100 000 integer numbers
def int_random(n):
    a = ()
    for i in range(0, n):
        a = a + ((random.randint(0, k)),)
    return a


# function will generate 100 000 float numbers
def float_random(n):
    b = ()
    for i in range(0, n):
        b = b + ((random.uniform(0, k)),)
    return b


int_list = int_random(n)
float_list = float_random(n)


# python sorting
def python_sort(num_list):
    num_list.sort()
    return num_list


python_sort_intlist = python_sort(list(int_list))
python_sort_floatlist = python_sort(list(float_list))
##############SORTING ALGORITHMS###################

# Bubble sorting
# timer start
sttime = time.time()


def bubble_sorting(num_list):
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


# sort lists with integer and float numbers

sort_int_list = bubble_sorting(list(int_list))
sort_float_list = bubble_sorting(list(float_list))
# timer finish
fntime = time.time()
# Report in a private message that task is done
print("Bubble sort: time = " + "%.3f" % (fntime - sttime) + ", the list is sorted correctly = " + \
      str((sort_int_list == python_sort_intlist) and (sort_float_list == python_sort_floatlist)))

# Selection  sorting
# timer start
sttime = time.time()


def selection_sorting(num_list):
    for i in range(0, n):
        min = num_list[i]
        index = i
        for j in range(i + 1, n):
            if num_list[j] < min:
                min = num_list[j]
                index = j
        num_list[i], num_list[index] = num_list[index], num_list[i]
    return num_list


# sort lists with integer and float numbers
sort_int_list = selection_sorting(list(int_list))
sort_float_list = selection_sorting(list(float_list))

# timer finish
fntime = time.time()


# Report in a private message that task is done
print("Selection  sort: time = " + "%.3f" % (fntime - sttime) + ", the list is sorted correctly = " + \
      str((sort_int_list == python_sort_intlist) and (sort_float_list == python_sort_floatlist)))

# Insertion  sorting
def insertion_sorting(num_list):
    for i in range(0, n):
        j = i - 1
        while ((num_list[j+1] < num_list[j]) and (j >= 0)):
            num_list[j+1], num_list[j] = num_list[j], num_list[j+1]
            j -= 1
    return num_list


# sort lists with integer and float numbers
sort_int_list = insertion_sorting(list(int_list))
sort_float_list = insertion_sorting(list(float_list))
# timer finish
fntime = time.time()

# Report in a private message that task is done
print("Insertion sort: time = " + "%.3f" % (fntime - sttime) + ", the list is sorted correctly = " + \
      str((sort_int_list == python_sort_intlist) and (sort_float_list == python_sort_floatlist)))
