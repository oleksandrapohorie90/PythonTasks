from collections import deque

#Method 1
def is_palindrome(lst):
    return lst == list(reversed(lst))
example_list = [1, 2, 3, 2, 1]
print(is_palindrome(example_list))

#Method 2
def is_palindrome(lst):
    return lst == lst[::-1]
example_list = ['a', 'b', 'a']
print(is_palindrome(example_list))

#Method 3
def is_palindrome(lst):
    dq = deque(lst)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
example_list = [1, 'b', 'b', 1]
print(is_palindrome(example_list))