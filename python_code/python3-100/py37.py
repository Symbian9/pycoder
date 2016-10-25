if __name__ == '__main__':
    N = 10
    print('please input ten num')
    lst = []
    for i in range(N):
        lst.append(int(input('input a number: ')))
    for i in range(N):
        print(lst[i])



    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            if lst[min] > lst[j]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    print('after sorted')

    for i in range(N):
        print(lst[i], end=' ')