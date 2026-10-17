def merge(A, left, mid, right):
    T = [0] * len(A)
    i = left
    j = mid + 1
    target = left

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            T[target] = A[i]
            i += 1
        else:
            T[target] = A[j]
            j += 1
        target += 1

    while i <= mid:
        T[target] = A[i]
        i += 1
        target += 1

    while j <= right:
        T[target] = A[j]
        j += 1
        target += 1

    for k in range(left, right + 1):
        A[k] = T[k]

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

A = [64, -12, 25, -12, 22, 90, 12, 3, 5]
merge_sort(A, 0, len(A) - 1)
print("Sorted array:", A)
