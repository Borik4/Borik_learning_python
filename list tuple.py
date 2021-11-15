# Խնդիր 1․
# Fill the array with random positive and negative numbers in such a way that all numbers are modulo different. This means that an array cannot contain only two equal numbers, but there cannot be two equal in absolute value. Find the largest modulo number in the resulting array.




# Խնդիր 2.
# Find the index of the modulo minimum element of the array. For example, in the array [10, -3, -5, 2, 5], the modulo element is the number 2.
from random import randint


def ex_2(lis):
    minimum = float('inf')
    for i in lis:
        if abs(i) < abs(minimum):
            minimum = i
    return minimum

print(ex_2([2, 34, 56, 7, 9, 9, -871]))
print(ex_2([2, 34, 56, 7, 9, 9, -871, -1]))

# Խնդիր 3.
# Calculate the sum of the absolute values of the array elements located after the first negative element.
# For example, in the array [5, 3, -1, 8, 0, -6, 1], the first negative element is the third in a row, and the sum of the modules of the array elements after it will be 8 + 0 + 6 + 1 = 15

def ex_3(l):
    sum = 0
    t = False
    for i in l:
        if t:
            sum += abs(i)
        elif i < 0:
            t = True

    return sum

print(ex_3([12, 3, -4, 1, 2, -3]))


# Խնդիր 4.
# Fill the array with random positive and negative integers. Display it on the screen. Remove all negative elements from the array and output again.

def ex_4(l):
    print(l)
    count = 0
    for i in range(len(l)):
        if l[i-count] < 0:
            l.pop(i-count)
            count += 1
    print(l)

ex_4([12,34 ,45,45, -56, 56, 56-566, 65, 76, -56, 56, -56 ])



# Խնդիր 5.
# In a one-dimensional array, find the sum of the elements between the minimum and maximum elements. The minimum and maximum elements themselves should not be included in the amount

def ex_5(l):
    maximum = l[0]
    minimum = l[0]
    sum = 0
    for i in l[1::]:
        if i < minimum:
            sum += minimum
            minimum = i
        elif i > maximum:
            sum += maximum
            maximum = i
        else:
            sum += i
    return sum

print(ex_5([12, 43, 45, 67, 567, 6]))


# Խնդիր 6.
# Find the sum of all digits of an integer array. For example, if the array [12, 104, 81] is given, then the sum of all its digits will be equal to 1 + 2 + 1 + 0 + 4 + 8 + 1 = 17.

def ex_6_1(l):
    return sum(l)

def ex_6_2(l):
    sum = 0
    for i in l:
        sum += i
    return sum

print(ex_6_1([12, 23, 23,4, 3,4 ]))
print(ex_6_2([12, 23, 23,4, 3,4 ]))

# Խնդիր 7.
# Shrink the array, removing from it all elements, the value of which is in the interval [a, b]. Fill the elements freed at the end of the array with zeros.

def ex_7(l, a, b):
    for i in range(len(l)):
        if a < l[i] < b:
            l[i] = 0
    return l


print(ex_7([1, 2, 3, 4, 5, -45,78, 8, 5], 1, 100))

# Խնդիր 8.
# Fill one array with random numbers, the other with numbers entered from the keyboard, write the sums of the corresponding cells of the first two in the cells of the third. Display the contents of the arrays on the screen.


def ex_8():
    l = [randint(-1000, 1000) for i in 10]
    l_1 = [int(input()) for i in 10]
    l_2 = [l[i]+l_1[i] for i in 10]
    print(l)
    print(l_1)
    print(l_2)



# Խնդիր 9.
# Fill an array of real numbers with keyboard input. Calculate the sum and product of the array elements. Display the array itself, the resulting sum and the product of its elements.

def ex_9():
    l = [int(input()) for i in 2]
    s = 0
    f = 1
    for i in l:
        s += i
        f *= i
    print(l)
    print(s)
    print(f)



# Խնդիր 10.
# Generate 20 random integers ranging from -5 to 4, write them to the array cells. Count how many of them are positive, negative and zero values. Display array elements and counted quantities.

def ex_10():
    l = [randint(-5, 4) for i in range(20)]
    positive = 0
    negative = 0
    zero = 0
    for i in l:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1

    print('zero  -> ', zero)
    print('positive  -> ', positive)
    print('negative   -> ', negative)



ex_10()