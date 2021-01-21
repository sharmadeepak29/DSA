# Write a program to reverse an array or string
def reverseListIterative(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

def reverseListRecursive(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseListRecursive(A, start+1, end-1)

A = [1,2,3,4,5,6,7,8,9]
B = [1,2,3,4,5,6,7,8,9]
print(A)
reverseListIterative(A, 0, 8)
print(A)
print(B)
reverseListRecursive(B, 0, 8)
print(B)
