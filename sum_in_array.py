# task 5
import time


def binary_search(sorted_array, elem_to_find):
    if sorted_array != []:
        mid = 0
        start = 0
        end = len(sorted_array)
        step = 0

        while start <= end:
            step = step+1
            mid = (start + end) // 2

            if elem_to_find == sorted_array[mid]:
                return mid

            if elem_to_find < sorted_array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    else:
        return -1


def cycle_and_bs(sorted_array, S):
    for i in range(len(sorted_array)):
        current_elem = sorted_array[i]
        need_elem = S - current_elem
        slice_lst = sorted_array[i+1:]
        find_index = binary_search(slice_lst, need_elem)
        if find_index != -1:
            print(current_elem, slice_lst[find_index])


start = time.time()
cycle_and_bs(list(range(-100, 10000, 1)), 50)
end = time.time()
print(end-start)  # 0.13796353340148926


def cycle_and_cycle(sorted_array, S):
    for i in range(len(sorted_array)-1):
        for j in range(i+1, len(sorted_array)):
            if sorted_array[i] + sorted_array[j] == S:
                print(sorted_array[i], sorted_array[j])


start = time.time()
cycle_and_cycle(list(range(-100, 10000, 1)), 50)
end = time.time()
print(end-start)  # 3.6050024032592773


def end_start(sorted_array, S):
    start = 0
    end = -1
    while sorted_array[start] != sorted_array[end]:
            summ = sorted_array[start] + sorted_array[end]
            if summ == S:
                print(sorted_array[start], sorted_array[end])
                start += 1
                end -= 1
            elif summ < S:
                start += 1
            elif summ > S:
                end -= 1

start = time.time()
end_start(list(range(-100, 10000, 1)), 50)
end = time.time()
print(end-start)  # 0.0029671192169189453
