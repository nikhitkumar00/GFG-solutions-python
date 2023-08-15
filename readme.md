## Table of Contents

-   [Sorting Elements using `arr.sort()`](#sorting-elements-using-arrsort)
-   [Checking for Power of 2](#checking-for-power-of-2)
-   [Creating a Dictionary with Default Values](#creating-a-dictionary-with-default-values)
-   [Applying Functions to Create Dictionary Values](#applying-functions-to-create-dictionary-values)
-   [Return Values of `list.sort()` and `sorted()` in Functions](#return-values-of-listsort-and-sorted-in-functions)
-   [Using `enumerate` to Get Index-Value Pairs](#using-enumerate-to-get-index-value-pairs)
-   [Using `enumerate` with Arrays](#using-enumerate-with-arrays)
-   [Finding the Index of an Element using `arr.index()`](#finding-the-index-of-an-element-using-arrindex)

---

## Sorting Elements using `arr.sort()`

```python
arr.sort(key=function, reverse=True)
```

-   Sorts elements in `arr` using `function` and sorts in descending order when `reverse=True`.

**Example:**

```python
data = [(1, 4), (3, 2), (2, 7)]
data.sort(key=lambda x: x[1], reverse=True)
print(data)  # Output: [(2, 7), (1, 4), (3, 2)]
```

---

## Checking for Power of 2

```python
n & (n - 1) == 0
```

-   Checks if `n` is a power of 2.
-   Ensure `n > 0`.

**Example:**

```python
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_2(4))  # Output: True
print(is_power_of_2(5))  # Output: False
```

---

## Creating a Dictionary with Default Values

```python
d = dict.fromkeys(keys, default_value)
```

-   Creates a dictionary using `keys`, all having the same `default_value`.

**Example:**

```python
keys = ['a', 'b', 'c']
default_value = 0
result_dict = dict.fromkeys(keys, default_value)
print(result_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
```

---

## Applying Functions to Create Dictionary Values

```python
d = {ele: is_even(ele) for ele in a}
```

-   Uses `is_even()` to determine dictionary values.
-   Uses dictionary comprehension.

**Example:**

```python
def is_even(n):
    return 1 if n % 2 == 0 else 0

a = [1, 2, 3, 4, 5]
d = {ele: is_even(ele) for ele in a}
print(d)  # Output: {1: 0, 2: 1, 3: 0, 4: 1, 5: 0}
```

---

## Return Values of `list.sort()` and `sorted()` in Functions

When using `list.sort()` or `sorted()` inside a function, remember:

-   `list.sort()` sorts the list in-place and returns `None`.
-   `sorted()` returns a new sorted list.

```python
def sort_list_and_return(l):
    l.sort()   # Returns None

def sorted_list_and_return(l):
    return sorted(l)  # Returns a new sorted list
```

---

## Using `enumerate` to Get Index-Value Pairs

To get index-value pairs from a list, use `enumerate`:

```python
dic = {x: index for index, x in enumerate(A2)}
```

-   `enumerate` returns both the index and value as a tuple for each element in the list.
-   Useful for creating dictionaries with elements as keys and their respective indices as values.

**Example:**

```python
A2 = [10, 20, 30, 40, 50]
dic = {x: index for index, x in enumerate(A2)}
print(dic)  # Output: {10: 0, 20: 1, 30: 2, 40: 3, 50: 4}
```

---

## Using `enumerate` with Arrays

You can use `enumerate` with arrays to get both index and value for each element:

```python
for index, value in enumerate(arr):
    print(f"Element at index {index}: {value}")
```

-   `enumerate` returns both the index and value as tuples, allowing you to iterate over arrays with index information.

---

## Finding the Index of an Element using `arr.index()`

To find the index of an element in an array, use the `arr.index()` method:

```python
index = arr.index(element)
```


-   Returns the index of the first occurrence of `element` in the array.
-   Raises a `ValueError` if `element` is not found in the array.

**Example:**

```python
arr = [10, 20, 30, 40, 20, 50]
index = arr.index(20)
print(index)  # Output: 1
```