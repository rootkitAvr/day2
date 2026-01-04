def reverse_list(listen):
    new_list = []
    lenlisten = len(listen)-1
    for i in range(lenlisten, -1, -1):
        new_list.append(listen[i])

    return new_list
