def bin_search(list):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        midVal = list[mid]
        if midVal == 1415:
            return mid
        if midVal > 1415:
            high = mid - 1
        else:
            low = mid + 1

input_str = input()
input_list = input_str.split()
nums = [int(num_str) for num_str in input_list]
print(type(nums))
print(bin_search(nums))