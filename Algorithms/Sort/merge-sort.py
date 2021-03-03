import random

def merge_sort(arr):
    if len(arr) > 1:
        
        # r: index of where the array is split
        r = len(arr) // 2

        # L: left half of the array
        L = arr[:r]
        
        # M: right half of the array
        M = arr[r:]

        merge_sort(L)
        merge_sort(M)

        # i: index of the left half of the array
        # j: index of the right half of the array
        # k: index of the whole array
        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1

    return arr


def main():
    array = random.sample(range(1000000), 1000000)

    array_sorted = merge_sort(array)

    # print(*array_sorted, sep="\n")
    print(array_sorted)


main()