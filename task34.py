def rhythm(rhythm_get):
    rhythm_get = rhythm_get.split()
    list_1 = []
    for word in rhythm_get:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])


rhythm_get = input('Введите кричалку: ')
if rhythm(rhythm_get):
    print('Парам пам-пам')
else:
    print('Пам парам')