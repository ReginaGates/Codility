# Codility Array Lesson - Rotating through a list
# Solution by Regina Gates
# November 11, 2017
#
# I am glad it works, even with the all of the test cases on Codility,
# However, I've thought of several other ways that may be better. I think I don't
# quite have the patience to try those to the point of making them work, yet, absent
# more complete knowledge of Python, to know from the get-go that those ideas would work.

# I think the goal of this challenge was to have a loop that does the work in stages, for
# the number of rotations needed. I did not do that. If I get the bug, I'll revisit that
# option and update.

# Please don't cheat.

import random

def rotate(A, K):
    N = len(A)

    # If there is no input, avoid crashing the program; return empty list.
    if N == 0:
        slice_A = []
        return slice_A

    # If there is only one element, no rotation can be performed. Return identity.
    elif N == 1:
        slice_A = A
        return slice_A

    # If there are only 2 elements...
    elif N == 2:
        # if we must rotate an even number of times, we return the same list.
        if K%2 == 0:
            slice_A = A
        # if the rotation is an odd number of times, we exchange the items in the list.
        else:
            slice_A = A
            slice_A[0], slice_A[1] = slice_A[1], slice_A[0]
        return slice_A

    elif K == 0 or K == N:
        # We return the original list
        slice_A = A
        return slice_A

    else:
        if K > N:
            # Bring K to a manageable number, especially if super-large.
            rem_K = K % N
            # print(rem_K)  # Debug
            # n is the range of the region of the original list, excluded from the slice.
            n = N-rem_K
        else:  # K < N
            n = N-K
            # print(n) # Debug

        slice_A = A[n:]
        # print(slice_A) # Debug
        # add excluded portion back in, on the front-end.
        for i in range(0, n):
            slice_A.insert(N-1, A[i])
        return slice_A

# Test cases
list_A = [random.randrange(-1000, 1000) for i in range(0, 100)]
# print(list_A)
slice_Index = 16
print(rotate(list_A, slice_Index))
print("-"*40)

list_B = [3, 8, 9, 7, 6]
# print(list_B)
slice_Index = 8
print(rotate(list_B, slice_Index))
print("-"*40)

list_C = [1, 2, 3, 4, 5, 6, 7]
# print(list_C)
slice_Index = 2
print(rotate(list_C, slice_Index))
