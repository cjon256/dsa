#  Category: algorithms
#  Level: Easy
#  Percent: 63.505096%


#  An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#
#  You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
#
#  To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
#
#  Return the modified image after performing the flood fill.
#
#
#  Example 1:
#
#  Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
#  Output: [[2,2,2],[2,2,0],[2,0,1]]
#  Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
#  Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
#
#
#  Example 2:
#
#  Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
#  Output: [[0,0,0],[0,0,0]]
#  Explanation: The starting pixel is already colored 0, so no changes are made to the image.
#
#
#
#  Constraints:
#
#
#  	m == image.length
#  	n == image[i].length
#  	1 <= m, n <= 50
#  	0 <= image[i][j], color < 2¹⁶
#  	0 <= sr < m
#  	0 <= sc < n
#

import unittest
from typing import List


#  start_marker
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] is color:
            return image
        original_color = image[sr][sc]

        def recursively_fill(cr: int, cc: int):
            image[cr][cc] = color
            if cc > 0:
                if image[cr][cc - 1] == original_color:
                    recursively_fill(cr=cr, cc=cc - 1)
            if cc < (len(image[0]) - 1):
                if image[cr][cc + 1] == original_color:
                    recursively_fill(cr=cr, cc=cc + 1)
            if cr > 0:
                if image[cr - 1][cc] == original_color:
                    recursively_fill(cr=cr - 1, cc=cc)
            if cr < (len(image) - 1):
                if image[cr + 1][cc] == original_color:
                    recursively_fill(cr=cr + 1, cc=cc)

        recursively_fill(sr, sc)
        return image


#  end_marker
class TestSolution(unittest.TestCase):
    def test_floodFill_1(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        color = 2
        self.assertEqual(
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
            Solution().floodFill(image, sr, sc, color),
        )

    def test_floodFill_2(self):
        image = [[0, 0, 0], [0, 0, 0]]
        sr = 0
        sc = 0
        color = 0
        self.assertEqual(
            [[0, 0, 0], [0, 0, 0]], Solution().floodFill(image, sr, sc, color)
        )


if __name__ == "__main__":
    unittest.main()
