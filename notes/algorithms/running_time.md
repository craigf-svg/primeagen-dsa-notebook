## Running Time and Big O Notation

_Running time_ is the number of steps an algorithm takes to finish. _Big O notation_ describes how an algorithm's running time will grow as the size of the input increases. In short, Big O is a way to describe different __growth rates__ of algorithms.

### Library as a Metaphor

The books and aisles in a library are a perfect metaphor for understanding how the time of a task changes depending on input size.

### Touching Every Book in a Library Aisle

If the goal is to touch every book while walking down an aisle of a library, it would probably take a lot longer for an aisle of 100 books compared to an aisle of 10 books. 

Does this task take more time as the number of books increase? Answer: The time it takes scales proportionally with the increase in number of books in that aisle.

It follows that touching every book in an aisle has a Big O of $O(n)$ or __linear__ time complexity.

It's called __linear__ because the running time grows in direct proportion as the number of books. Doubling the number of books would double the amount of time it takes. __n__ shows this by representing for the number of books in the aisle.



```python
# O(n): Touching every book in an aisle
def touch_books(books):
    for book in books:
        print("Touched", book)
```

Next is an operation time where the time doesn't depend on the input size (the amount of books).

### Scenario 2: Adding a Book to the End of a Shelf

Add a book to the end of a library shelf.

Does it scale? Answer: No, the time it takes doesn't depend on how many books are already on that shelf.

Adding a book to the end of a shelf has a Big O of $O(1)$ or runs in __constant__ time.

An operation like this is called __constant__ because the amount of time this task takes doesn't change or grow at all based on the size of the input.¹

```python
# O(1): Adding a book to the end of a shelf
def add_book(shelf, new_book):
    shelf.append(new_book)
```
<br />

| Scenario                                 | What You Do                                 | How Time Scales                | Big O Notation | Time Type   |
|-------------------------------------------|---------------------------------------------|-------------------------------|----------------|---------|
| Touching every book in a library aisle    | Walk down the aisle and touch each book     | More books = more time         | O(n)           | Linear  |
| Adding a book to the end of a shelf       | Place a book at the end of the shelf        | Same time no matter the size  | O(1)           | Constant|

<br />

### How to Determine Big O of an Algorithm

The three step process to determine Big O of any algorithm: 

$\text{Counting} \ \text{Number} \ \text{of} \ \text{Operations} \rightarrow \text{Focus} \ \text{on} \ \text{Worst} \ \text{Case} \rightarrow \text{Simplify}$

1. _Count number of operations_: Count how many times an algorithm’s main steps run as the input grows. In a linear search that checks every element (n) and logs 3 messages: $O(n + 3)$

1. _Focus on the worst case scenario._<sup>2</sup> Big O focuses on the worst case scenario, so if a searching algorithm visits each element searching for a value and logs 3 messages we would use $O(n + 3)$ for finding the element.
    a. Best Case: The search checks and find the value in the first item and logs 3 messages - $O(1 + 3)$
    b. Worst case: The search checks all elements and could not find the value, and logs 3 messages. $O(n + 3)$

2. _Simplify_: It corresponds to the growth rate that is _approached_ with high enough sizes. This means to always drop constants and lower exponents. In the case of our linear search we have determined the Big O through our 3 step process.
$O(n + 3) \rightarrow O(n)$
Some other examples of simplifying number of operations to Big O are below.  
    a. $O(2n)$ → $O(n)$  
    b. $O(n² + n)$ → $O(n²)$  
    c. $O(n + 10)$ → $O(n)$  


### So Which is Better, O(n) or O(1)?

The less an algorithm scales with input size, the more desirable the algorithm. This means that the closer an algorithm gets to O(1), the better. 

If sorting a 100 books in alphabetical order could be as time efficient as adding a book to the end of a shelf that would be highly desirable.

O(n) is generally very good for sorting and searching tasks, since the work grows in a straight line with the amount of data. But not all algorithms are this efficient. 

Some algorithms like bubble sort have a running time of $O(n^2)$, meaning that as input size grows the running time grows much faster.

### Quadratic Time Complexity

An example of __quadratic__ time, or $O(n^2)$, would be writing down the names of books on a shelf, but with every new book you reach, you rewrite the entire list of names from the beginning up until the new book, so a single additional book could cost an hour of time.

```python
# O(n^2): For each new book, write the list # and book title
def rewrite_names(books):
    total_operations = 0
    for i in range(len(books)):
        # Rewrite the list
        for j in range(i + 1):
            print(f"List #{i}: {books[j]}")
            total_operations += 1
    print(f"Total number of operations: {total_operations}")
```

### Common Time Complexities

Big O notation helps describe how an algorithm’s running time or space requirements grow as the input size increases. Below is a quick overview and python examples of the most common growth rates.

O(1): Constant time where the operation does not depend on input size.

O(log n): Logarithmic time, includes operations like binary search.

O(n): Linear time where the operation grows directly with input size.

O(n log n): Linearithmic time, includes sorting algorithms like merge sort and heap sort.

O(n²): Quadratic time, includes bubble sort.

![Most common Big O Notations Graphed](bigo_graph.svg) [<sup>3</sup>]

Time Complexity Examples in Python
```python
arr = [9,6,7,8,5,3,2,1,4]
n = len(arr)

# O(1) - Constant¹
arr.append(10)

# O(log n) - Logarithmic
i = 1
while i < n:
    print(i)
    i *= 2

# O(n) - Linear
for i in range(n):
    print(i)

# O(n log n) - Linearithmic
for i in range(n):
    j = 1
    while j < n:
        print(i, j)
        j *= 2

# O(n^2) - Quadratic
for i in range(n):
    for j in range(n):
        print(i, j)
```

<br />

### The ability to determine and understand time complexities of algorithms helps in creating solutions that are efficient even when handling very large amounts of data. 

Thanks for reading!

<br />

#### Notes / Citations

 [¹] A small exception is that if the aisle is a true array and "adding a book to end of the shelf" refers to adding a value to an unallocated space, appending can become O(n) time. Here, we assume the shelf is pre-allocated.

 [²] Even though it is hinted later in the paragraph, Big O notation can describe average case or best case time too, but it’s most commonly used to express worst case.

 [³] _Source: [Cooervo Big O Notation](https://cooervo.github.io/Algorithms-DataStructures-BigONotation/index.html)_

 [⁴] _Source: [GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)_