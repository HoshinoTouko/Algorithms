import copy


def insertion_sort(li):
    A = copy.deepcopy(li)
    n = len(A)

    if n > 1:
        x = A[n-1]
        A = insertion_sort(A[:n-1]) + A[n-1:]
        j = n - 1
        while j > 1 and A[j-1] > x:
            A[j] = A[j-1]
            j -= 1
        A[j] = x

    return A


def main():
    t = [1, 2, 7, 3, 6, 1, 7, 3, 6, 9, 23, 8, 1, 7, 4, 2, 7, 123, 54, 7, 2]
    print(insertion_sort(t))


if __name__ == '__main__':
    main()
