#!/usr/bin/env python3
import argparse


def list_to_sort():
    """
    Return a list with 3 elements:
    0. the algorithm required to sort
    1. the list of intergers need to be sorted
    2. true if gui is specified, else return false
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the list to sort')
    parser.add_argument('--algo', metavar='ALGO',
                        choices=['bubble', 'insert',
                                 'quick', 'merge'], default='bubble',
                        help='''specify which algorithm to use for sorting
                        among [bubble | insert | quick | merge],
                        default bubble''')
    parser.add_argument('--gui', action='store_true',
                        help='visualise the algorithm in GUI mode')
    args = parser.parse_args()
    list = [args.algo, args.integers, args.gui]
    return list


def bubble_sort(list):
    """
    Bubble Sort algorithm
    """
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                print(*list)


def insertion_sort(list):
    """
    Insertion Sort algorithm
    """
    for i in range(1, len(list)):
        value = list[i]
        for j in range(i-1, -1, -1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        if value == list[i]:
            pass
        else:
            print(*list)


def partition(list, left, right):
    """
    Choose the last number as pivot and sort list into left and right
    Return the right update position of that pivot to continue divine sublists
    """
    pivot = list[right]
    print('P: ' + str(pivot))
    i = left - 1
    for j in range(left, right):
        if list[j] < pivot:
            i += 1
            list[j], list[i] = list[i], list[j]
    list[right], list[i+1] = list[i+1], list[right]
    return (i+1)


def quick_sort(list, left, right):
    """
    Quick Sort algorithm
    """
    if left < right:
        piv = partition(list, left, right)
        print(*list)
        quick_sort(list, left, piv-1)
        quick_sort(list, piv+1, right)


def merge_sort(list):
    if len(list) > 1:
        middle = len(list)//2
        Left = list[:middle]
        Right = list[middle:]
        merge_sort(Left)
        merge_sort(Right)
        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                list[k] = Left[i]
                i += 1
            else:
                list[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            list[k] = Left[i]
            i += 1
            k += 1
        while j < len(Right):
            list[k] = Right[j]
            j += 1
            k += 1
        print(*list)


def main():
    list = list_to_sort()
    if list[0] == 'insert':
        insertion_sort(list[1])
    elif list[0] == 'quick':
        quick_sort(list[1], 0, len(list[1])-1)
    elif list[0] == 'merge':
        merge_sort(list[1])
    else:
        bubble_sort(list[1])


if __name__ == '__main__':
    main()
