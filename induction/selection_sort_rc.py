import copy


def selection_sort(li):
    A = copy.deepcopy(li)
    n = len(A)
    i = 0
    if i < n:
        k = i
        for j in range(i + 1, n):
            if A[j] < A[k]:
                k = j
        if k != i:
            A[i], A[k] = A[k], A[i]
        A = A[:1] + selection_sort(A[1:])
    return A


def main():
    t = [1, 2, 7, 3, 6, 1, 7, 3, 6, 9, 23, 8, 1, 7, 4, 2]
    print(selection_sort(t))


if __name__ == '__main__':
    main()
