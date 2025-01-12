def merge_sort(arr_: list) -> list:
    if len(arr_) <= 1:
        return arr_

    middle = len(arr_) // 2

    left = merge_sort(arr_[:middle])
    right = merge_sort(arr_[middle:])

    return merge_arrays(left, right)


def merge_arrays(left: list, right: list) -> list:
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else :
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])

    return result



if __name__ == "__main__":
    arr = [3, 6, 4, 3, 1, 2, 12]
    print(merge_sort(arr))
