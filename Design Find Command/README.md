# Find Command Design

Design a `find` command-line utility. This utility should support various filtering criteria.


## Questions

1. Does it need to support more than one filter ? 
2. What are the types of the filter that I need to support for eg. filter by size, filter by name, etc
3. Does it need to support combined filters (AND , OR) ? 

## Designing

> The **Strategy Design Pattern** enables defining a family of algorithms, encapsulating each in a separate class, and making them interchangeable. [Link](https://refactoring.guru/design-patterns/strategy)

## Why Strategy Pattern?

- Allows adding new filters without changing existing code.
- Delegates filtering logic to filter classes, keeping file management and filtering concerns separate.
- Supports combining multiple filters flexibly.

## Design Steps

### 1. Core Entity: `File`

Represents a file with `name` and `size`.

```python
class File: 
    def __init__(self, name: str, size: int) -> None:
        pass

    def __str__(self) -> str: 
        pass
```

### 2. Filter Interface

Abstract base class for all filters.

```python
from abc import ABC, abstractmethod

class Filter(ABC): 
    @abstractmethod 
    def check(self, file: File) -> bool:
        pass
```

### 3. Filter Strategies

#### FileNameFilter

Filters by file extension.

```python
class FileNameFilter(Filter): 
    def __init__(self, extension: str) -> None:
        self.extension = extension

    def check(self, file: File) -> bool:
        file_name = file.name
        extension = file_name.split(".")[-1]
        return self.extension == extension
```

#### FileSizeFilter

Filters by file size.

```python
class FileSizeFilter(Filter): 
    def __init__(self, size: int) -> None: 
        self.size = size

    def check(self, file: File) -> bool:
        return file.size > self.size
```

### 4. FileSystemService

Manages files and delegates filtering to filter classes.

> **Reasoning:**  
> `FileSystemService` separates file management from filtering logic. It delegates filtering to filter strategies, making it easy to add new filters without changing this class.

```python
class FileSystemService: 
    def __init__(self, files: list[File]) -> None:
        self._files = files

    def search(self, filters: list[Filter]) -> list[File]:
        result = []
        for file in self._files:
            if all(filter.check(file) for filter in filters):
                result.append(file)
        return result
```

### 5. Usage Example

```python
files = [
    File("Picture1.txt", 234),
    File("Picture2.jpg", 132),
    File("Picture2.png", 45),
    File("Picture3.png", 78),
    File("Picture1.jpg", 43)
]

file_system = FileSystemService(files)

# Search by file name
print("Search by file name:")
search_result = file_system.search([FileNameFilter("txt")])
for file in search_result:
    print(file)

# Search by file size
print("----------------------")
print("Search by file size:")
search_result = file_system.search([FileSizeFilter(50)])
for file in search_result:
    print(file)

# Composite search
print("----------------------")
print("Composite search by file name and size:")
search_result = file_system.search([FileNameFilter("jpg"), FileSizeFilter(50)])
for file in search_result:
    print(file)
```


