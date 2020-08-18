from random import randint
from sort_funcs import (
    bubble_sort, selection_sort, insertion_sort,
    merge_sort, quick_sort
)



def create_array(length=10, maxint=50) -> list:
    new_arr = [randint(0, maxint) for _ in range(length)]
    return (new_arr)


def benchmark(sort_func, n=[10, 100, 1000, 10000]) -> None:
    """
    Compare execution time with build-in `sorted` function
    """

    from time import time
    b0 = []
    b1 = []
    print("In progress...")
    for length in n:
        lst = create_array(length, length)
        t0 = time()
        sorted(lst)
        t1 = time()
        b1.append(t1 - t0)
        t0 = time()
        sort_func(lst)
        t1 = time()
        b0.append(t1 - t0)
    print("Done!")
    print(f"\nn \tBuilt-In\t{sort_func.__doc__}")
    print("_" * 50)
    for i, cur_n in enumerate(n):
         print("%d\t%0.5f \t%0.5f"%(cur_n, b1[i], b0[i]))


def test_sort_funcs(sort_func_list, test_lst=None, bmark=False) -> None:
    """
    Prove ability to sort of custom sort functions
    """

    for sort_func in sort_func_list:
        if test_lst == None: lst = create_array()
        else: lst = test_lst.copy()
        print(sort_func.__doc__)
        print("-" * (len(sort_func.__doc__) + 2))
        print(f"before: {lst}")
        if sort_func.__annotations__['return']:
            lst = sort_func(lst)
        else:
            sort_func(lst)
        print(f"after : {lst}\n")
        if bmark: benchmark(sort_func)
        print('\n')


sort_func_list = [
 #   bubble_sort, selection_sort, insertion_sort,
    merge_sort, quick_sort
]

test_sort_funcs(sort_func_list, test_lst=[9,7,5,4,3,2,1,-1], bmark=True)

