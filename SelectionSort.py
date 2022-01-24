def selection_sort(list_sort):
    for i in range(0, len(list_sort)):
        for j in range(0, len(list_sort)):
            if list_sort[j] == min(list_sort):
                sorted_list.append(list_sort[j])
                list_sort.pop(j)
                break

    return sorted_list


sorted_list = []
sort = [19, 18, 22, 97, 8, 9]
print(selection_sort(sort))