def x (words):
    ctr = 0
    empty_list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            empty_list.append(word)
    print (empty_list)
    return ctr

count = x(['abc', '101', 'tgh', 'oho', '150'])
print('the number of words that have the first and last characters equivelent to each other are: ', count)
