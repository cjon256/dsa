#  Category: algorithms
#  Level: Hard
#  Percent: 48.2%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# Design a data structure that simulates an in-memory file system.
#
# Implement the FileSystem class:
#
#     FileSystem() Initializes the object of the system.
#     List<String> ls(String path)
#         If path is a file path, returns a list that only contains this file's name.
#         If path is a directory path, returns the list of file and directory names in this directory.
#     The answer should in lexicographic order.
#     void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
#     void addContentToFile(String filePath, String content)
#         If filePath does not exist, creates that file containing given content.
#         If filePath already exists, appends the given content to original content.
#     String readContentFromFile(String filePath) Returns the content in the file at filePath.
#
#
#
# Example 1:
#
# Input
# ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
# [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
# Output
# [null, [], null, null, ["a"], "hello"]
#
# Explanation
# FileSystem fileSystem = new FileSystem();
# fileSystem.ls("/");                         // return []
# fileSystem.mkdir("/a/b/c");
# fileSystem.addContentToFile("/a/b/c/d", "hello");
# fileSystem.ls("/");                         // return ["a"]
# fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
#
#
#
# Constraints:
#
#     1 <= path.length, filePath.length <= 100
#     path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".
#     You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
#     You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.
#     1 <= content.length <= 50
#     At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.
#
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

import unittest
from typing import List


#  start_marker
class FileSystem:

    def __init__(self):
        self.root = {}

    def ls(self, path: str) -> List[str]:
        hier = filter(None, path[1:].split("/"))
        cwd = self.root
        for d in hier:
            cwd = cwd[d]
        if type(cwd) is str:
            return [d]
        return sorted(cwd.keys())

    def mkdir(self, path: str) -> None:
        hier = list(filter(None, path[1:].split("/")))
        cwd = self.root
        for d in hier:
            cwd = cwd.setdefault(d, {})

    def addContentToFile(self, filePath: str, content: str) -> None:
        hier = list(filter(None, filePath[1:].split("/")))
        cwd = self.root
        fn = hier.pop()
        for d in hier:
            cwd = cwd[d]
        cwd[fn] = cwd.get(fn, "") + content

    def readContentFromFile(self, filePath: str) -> str:
        hier = list(filter(None, filePath[1:].split("/")))
        cwd = self.root
        fn = hier.pop()
        for d in hier:
            cwd = cwd[d]
        return cwd[fn]

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        fs = FileSystem()
        self.assertEqual(fs.ls("/"), [])

    def test_case_2(self):
        fs = FileSystem()
        fs.mkdir("/a/b/c")
        self.assertEqual(fs.ls("/"), ["a"])

    def test_case_3(self):
        fs = FileSystem()
        fs.mkdir("/a/b/c")
        fs.addContentToFile("/a/b/c/d", "hello")
        self.assertEqual(fs.readContentFromFile("/a/b/c/d"), "hello")

    def test_case_4(self):
        fs = FileSystem()
        fs.mkdir("/a/b/c")
        fs.addContentToFile("/a/b/c/d", "hello")
        self.assertEqual(fs.ls("/a"), ["b"])

    def test_case_5(self):
        fs = FileSystem()
        fs.mkdir("/a/b/c")
        fs.addContentToFile("/a/b/c/d", "hello")
        self.assertEqual(fs.ls("/a/b"), ["c"])

    def test_case_6(self):
        fs = FileSystem()
        fs.mkdir("/a/b/c")
        fs.addContentToFile("/a/b/c/d", "hello")
        self.assertEqual(fs.ls("/a/b/c"), ["d"])


if __name__ == "__main__":
    unittest.main()
