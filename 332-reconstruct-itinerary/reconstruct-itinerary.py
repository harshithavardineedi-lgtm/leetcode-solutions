from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for start, end in tickets:
            graph[start].append(end)

        for airport in graph:
            graph[airport].sort(reverse=True)

        route = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            route.append(airport)

        dfs("JFK")
        return route[::-1]    