#  Category: algorithms
#  Level: Medium
#  Percent: 39.21767%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring
#
#
#  There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#
#  You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
#
#
#  Example 1:
#
#  Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
#  Output: 700
#  Explanation:
#  The graph is shown above.
#  The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
#  Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
#
#
#  Example 2:
#
#  Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
#  Output: 200
#  Explanation:
#  The graph is shown above.
#  The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
#
#
#  Example 3:
#
#  Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
#  Output: 500
#  Explanation:
#  The graph is shown above.
#  The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
#
#
#
#  Constraints:
#
#
#  	1 <= n <= 100
#  	0 <= flights.length <= (n * (n - 1) / 2)
#  	flights[i].length == 3
#  	0 <= fromi, toi < n
#  	fromi != toi
#  	1 <= pricei <= 10⁴
#  	There will not be any multiple flights between two cities.
#  	0 <= src, dst, k < n
#  	src != dst
#


import heapq
import unittest
from collections import defaultdict
from typing import List, NamedTuple


#  start_marker
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Define named tuples for flights and hops
        Flt = NamedTuple("Flt", [("cost", int), ("hops", int), ("dest", int)])
        Hop = NamedTuple("Hop", [("cost", int), ("city", int)])

        # Define a maximum distance (greater than 99 * 10⁴
        MAX_DIST = 100 * 10**4 + 1

        # Initialize distances and minimum distance
        distances: List[List[int]] = [[MAX_DIST] * n for _ in range(k + 1)]
        min_dist: int = MAX_DIST

        # Create a dictionary to store next hops for each city
        next_hops_dict: defaultdict[int, List[Hop]] = defaultdict(lambda: [])
        for flight in flights:
            from_, to, price = flight
            next_hops_dict[from_].append(Hop(cost=price, city=to))

        # Initialize the heap with the starting point
        init = Flt(0, 0, src)
        heap = [init]

        # Dijkstra's algorithm, I mean kinda?
        while heap:
            np = heapq.heappop(heap)

            # Skip if the number of hops exceeds the limit
            if np.hops - 1 > k:
                continue

            # Update the minimum distance if the destination is reached
            if np.dest == dst:
                min_dist = min(min_dist, np.cost)

            # Get the next hops from the current city
            next_hops: List[Hop] = next_hops_dict[np.dest]
            for hop in next_hops:
                # Skip if the number of hops exceeds the limit for the next city
                if hop.city != dst and np.hops + 1 > k:
                    continue

                # Update the distance if it is shorter than the current distance
                if np.hops <= k:
                    if np.cost + hop.cost >= distances[np.hops][hop.city]:
                        continue
                    distances[np.hops][hop.city] = np.cost + hop.cost
                    if hop.city == dst:
                        min_dist = min(min_dist, distances[np.hops][hop.city])

                # Add the next hop to the heap
                if np.hops < k:
                    heapq.heappush(heap, Flt(np.cost + hop.cost, np.hops + 1, hop.city))

        # Return -1 if there is no valid path, otherwise return the minimum distance
        if min_dist == MAX_DIST:
            min_dist = -1
        return min_dist
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        src = 0
        dst = 3
        k = 1
        expected = 700
        result = Solution().findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, expected)

    def test_case_2(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        expected = 200
        result = Solution().findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, expected)

    def test_case_3(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        expected = 500
        result = Solution().findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, expected)

    def test_case_4(self):
        n = 3
        flights = [[0, 1, 100], [2, 0, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 2
        expected = 500
        result = Solution().findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, expected)

    def test_case_5(self):
        n = 5
        flights = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
        src = 0
        dst = 2
        k = 2
        expected = 7
        result = Solution().findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, expected)

    def test_case_6(self):
        n = 17
        # fmt: off
        flights = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
        # fmt: on
        src = 13
        dst = 4
        k = 13
        expected = 47
        result = Solution().findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
