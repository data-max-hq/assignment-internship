array_a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
array_b = [100, 90, 80, 70, 60, 50]
# Expected output should contain: [9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 90, 80, 70, 60, 50]


def duplicate_remover_1(list1, list2):
    """duplicate remover is used to remove duplicates in a list while maintaining the source list unchanged,
    it uses as an input 2 lists (array_a, array_b) and outputs a list with unique values"""

    # this equation is used to create a list by attaching one list to the other
    list3 = list1 + list2

    # this is an empty list which will be used to collect the unique values of the list3
    output = []

    # this code represents the elegance and simplicity of python
    # it is self-explanatory but in other words it appends to the "output" list an item from the list3
    # with the condition that this item must not be present on "output", while iterating through every item of "list3"
    for x in list3:
        if x not in output:
            output.append(x)

    # prints "output" list
    print(output)


duplicate_remover_1(array_a, array_b)