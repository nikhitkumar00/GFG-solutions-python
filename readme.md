# Study Material

Welcome to the Lookup Study Material project! This README provides essential information on how to use key concepts in Python.

## Table of Contents
- [Sorting Elements using `arr.sort()`](#sorting-elements)
- [Checking if a Number is a Power of 2](#power-of-2)

---

## Sorting Elements using `arr.sort()`

### Syntax
```python
arr.sort(key=function, reverse=True)
```

- The `key` parameter calls the provided `function` for each element `x` and sorts the main elements based on the return value of that function.
- Use the `reverse` parameter to specify the sorting order. Set it to `True` for descending order and `False` (default) for ascending.

**Example:**
```python
# Sort a list of tuples based on the second element in descending order
data = [(1, 4), (3, 2), (2, 7)]
data.sort(key=lambda x: x[1], reverse=True)
print(data)  # Output: [(2, 7), (1, 4), (3, 2)]
```

---

## Checking if a Number is a Power of 2

### Syntax
```python
n & (n - 1) == 0
```

- This expression checks if the value of `n` is a power of 2.
- Additionally, ensure that `n` is greater than 0, as the expression will incorrectly evaluate to true for `n <= 0`.

**Example:**
```python
# Check if a number is a power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_2(4))  # Output: True
print(is_power_of_2(5))  # Output: False
```