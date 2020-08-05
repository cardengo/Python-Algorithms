def bubble_sort(lst) -> None:
    """Bubble Sort"""

    swapped = True
    while swapped:
        swapped = False
        i = 0
        while i < len(lst) - 1:
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1]  = lst[i + 1], lst[i]
                swapped = True
            i += 1


def selection_sort(lst) -> None:
    """Selection Sort"""

    start = 0
    while start < len(lst):
        min_ind = None
        for i, el in enumerate(lst[start:]):
            if min_ind == None or el < lst[min_ind]:
                min_ind = start + i
        lst[start], lst[min_ind]  = lst[min_ind], lst[start]
        start += 1


def insertion_sort(lst) -> None:
    """Insertion Sort"""

    swapped = True
    while swapped:
        swapped = False
        i = 1
        while i < len(lst):
            if lst[i] < lst[i - 1]:
                swapped = True
                j = i
                while j > 0:
                    if lst[j] < lst[j - 1]:
                        lst[j], lst[j - 1] = lst[j - 1], lst[j]
                    j -= 1
            i += 1


def merge(a, b) -> list:
    c = []
    idx_a,idx_b = 0,0
    
    while (idx_a < len(a) and idx_b < len(b)):
        if (a[idx_a] < b[idx_b]):
            c.append(a[idx_a])
            idx_a += 1
        else:
            c.append(b[idx_b])
            idx_b += 1
    if (idx_a == len(a)): c.extend(b[idx_b:])
    else:                 c.extend(a[idx_a:])
    
    return c


def merge_sort(lst) -> list: 
    """Merge Sort"""
    
    if (len(lst) <= 1):
        return (lst)
    half_idx = int(len(lst) / 2)
    left,right = merge_sort(lst[:half_idx]), merge_sort(lst[half_idx:])
    
    return merge(left, right)


def quick_sort(lst) -> list:
    """Quicksort"""

    if len(lst) <= 1: return (lst)
    smaller,equal,bigger = [],[],[]
    pivot = lst[0]
    for el in lst:
       if el < pivot: smaller.append(el)
       if el == pivot: equal.append(el)
       if el > pivot: bigger.append(el)
    
    return (quick_sort(smaller) + equal + quick_sort(bigger))

