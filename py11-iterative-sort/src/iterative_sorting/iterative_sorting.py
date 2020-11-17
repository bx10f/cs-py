# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    if len(arr) < 2:
        return arr
    # loop through n-1 elements
    for idx in range(0, len(arr) - 1):
        smallest_idx = idx
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(idx + 1, len(arr)):
            # TO-DO: swap
            if arr[j] < arr[smallest_idx]:
                smallest_idx = j

        arr[smallest_idx], arr[idx] = arr[idx], arr[smallest_idx]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # for i in range(len(arr) - 1):
    #     for j in range(i + 1, len(arr)):
    #         if arr[i] > arr[j]:
    #             arr[i], arr[j] = arr[j], arr[i]
    swap = True
    while swap:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True

    return arr


"""
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def counting_sort(arr, maximum=None):

    return arr