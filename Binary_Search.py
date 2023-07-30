# a function that contains two paras => a list and a target
# variables => start, end, middle, no of steps
# while loop
# increasing the steps each ime, a split is done
# if conditions to track the target element
# calling a function

def binary_Search(list, element):
    start = 0
    end = 0
    middle = 0
    steps = len(list)

    while(start <= end):
        print("Step no", steps, ":", list[start:end+1])

        steps = steps + 1
        middle = (start + end)//2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

        return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target_element = 12

binary_Search(my_list, target_element)

