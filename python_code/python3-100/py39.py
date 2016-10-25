if __name__ == '__main__':
    a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
    print('original list is:')
    for i in range(len(a)):
        print(a[i])
    number = int(input('insert a new number: '))
    end = a[-1]
    if number > end:
        a.append(number)
    else:
        for i in range(len(a)):
            if a[i] > number:           # 如果number大于 a[i]
                temp1 = a[i]            # 取出a[i]放入 temp1
                a[i] = number           # 插入number 到 a[i]
                for j in range(i + 1, len(a)):  # 迭代a[i]之后的值，依次后移一个位置
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    for i in range(len(a)):
        print(a[i])
    #
    # code 2
    # number = int(input('input a number: '))
    # if number > a[len(a) - 1]:
    #     a.append(number)
    # else:
    #     for i in range(len(a)):
    #         if a[i] > number:
    #             a.insert(i, number)
    #             break
    # print(a)