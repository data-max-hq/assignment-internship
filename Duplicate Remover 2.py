array_a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
array_b = [100, 90, 80, 70, 60, 50]
#Expected output should contain: [9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 90, 80, 70, 60, 50]


def duplicate_remover_2(list1, list2):
    """duplicate remover 2 is used to remove duplicates in a list without creating a new list,
    it uses as an input 2 lists who may contain duplicates (list1, list2) and outputs a list with unique values"""

    # this equation is used to create a list by attaching one list to the other
    the_list = list1 + list2

    # from now on we will refer to j as the "compared" item of the list
    # from now on we will refer to i as the "compared to" item of the list

    # takes the first i element by its index = 0
    i = 0

    # this while iteration is used to loop through all i elements except the last element
    # which will be the last j
    while i < len(the_list)-1:

        # this command makes sure that the j elements index is at least 1 grater than the i element,
        # so we will not compare the same element
        j = i + 1

        # this while iteration is used to loop through all j elements
        while j < len(the_list):

            # while looping through every j this if statement compares the j and the i
            if the_list[i] == the_list[j]:

                # this command deletes the j element of the list if the condition of the if statement above is reached
                del the_list[j]
            else:

                # if the condition of the if statement is not reached, the index of the j element is
                # increased by 1 and so on until we break out the loop
                j += 1

        # when we break out of the loop we increase the i element index by 1 and start all over through the first loop
        i += 1

    # print the modified list who contains only the unique values
    print(the_list)


duplicate_remover_2(array_b, array_a)