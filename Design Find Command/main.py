# // File Systems 
from abc import ABC, abstractmethod
from typing import Optional

class File : 
    def __init__(self, name: str , size : int) -> None:
        self.name = name 
        self.size = size

    def __str__(self) -> str : 
        return f"{self.name} : {self.size}"

class Filter(ABC): 
    @abstractmethod 
    def check(self, file : File) -> bool:
        pass

class FileNameFilter(Filter): 

    def __init__(self, extension : str) -> None :
        self.extension = extension

    def check(self, file : File) -> bool:
        
        file_name = file.name
        extension = file_name.split(".")[-1]

        if self.extension == extension:
            return True
        else:
            return False


class FileSizeFilter(Filter): 
    def __init__(self, size : int) -> None : 
        self.size = size

    def check(self, file: Filter) -> bool:
        size = file.size
        if size > self.size: 
            return True
        else: 
            return False

class FileSystemService: 
    def __init__(self, files : list[File]) -> None:
        self._files = files

    def search(self, filters: list[Filter]) -> list[File]:
        result = []
        for file in self._files:
            if all(filter.check(file) for filter in filters):
                result.append(file)
        return result
                



files = []
files.append(File("Picture1.txt" , 234))
files.append(File("Picture2.jpg" , 132))
files.append(File("Picture2.png" , 45))
files.append(File("Picture3.png" , 78))
files.append(File("Picture1.jpg" , 43))


file_system = FileSystemService(files)

print("Search by file name:")
search_result = file_system.search([FileNameFilter("txt")])
for file in search_result:
    print(file)

print("----------------------")
print("Search by file size:")
search_result = file_system.search([FileSizeFilter(50)])
for file in search_result:
    print(file)

print("----------------------")
print("Composite search by file name and size:")
search_result = file_system.search([FileNameFilter("jpg"), FileSizeFilter(50)])
for file in search_result:
    print(file)