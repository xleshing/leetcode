class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]):

        def dfs_path(graph: dict[int:list], start: int) -> set:
            visited = set([start])
            stack = [start]
            while stack:
                node = stack.pop()
                for nbr in graph[node]:
                    if nbr not in visited:
                        visited.add(nbr)
                        stack.append(nbr)
            return visited

        restrictions_dict = {i: [] for i in range(n)}
        friend_dict = {i: [] for i in range(n)}
        solutions = []

        for res in restrictions:
            restrictions_dict[res[0]].append(res[1])
            restrictions_dict[res[1]].append(res[0])

        for req in requests:
            req_status = True
            f_path = dfs_path(friend_dict, req[0])
            l_path = dfs_path(friend_dict, req[1])
            for f_link in f_path:
                for f_res in restrictions_dict[f_link]:
                    if f_res in l_path:
                        req_status = False
                        break

            if req_status:
                for l_link in l_path:
                    for l_res in restrictions_dict[l_link]:
                        if l_res in f_path:
                            req_status = False
                            break

            if req_status:
                friend_dict[req[0]].append(req[1])
                friend_dict[req[1]].append(req[0])
            solutions.append(req_status)
        print(solutions)

sol = Solution()
sol.friendRequests(5, [[0, 1], [1, 2], [2, 3]], [[0, 4], [1, 2], [3, 1], [3, 4]])

# 最優解: 使用 DSU(disjoint set union) 並查集
# class DSU:
#     def __init__(self,n):
#         self.n = n
#         self.p = list(range(n+1))
#         self.size = [1]*(n+1)
#         self.restrictions = [set() for _ in range(n+1)]
#     def find(self,u):
#         if self.p[u] == u:
#             return u
#         self.p[u] = self.find(self.p[u])
#         return self.p[u]
#     def add_restriction(self,a,b):
#         pa,pb = self.find(a),self.find(b)
#         if pa != pb:
#             self.restrictions[pa].add(pb)
#             self.restrictions[pb].add(pa)
#     def can_unite(self,a,b):
#         pa,pb = self.find(a),self.find(b)
#         if pa == pb:
#             return True
#         return pb not in self.restrictions[pa]
#     def unite(self,a,b):
#         if not self.can_unite(a,b):
#             return False
#         pa,pb = self.find(a),self.find(b)
#         if pa != pb:
#             if self.size[pa] < self.size[pb]: pa,pb = pb,pa
#             self.restrictions[pa].update(self.restrictions[pb])
#             for other_parent in self.restrictions[pb]:
#                 self.restrictions[other_parent].remove(pb)
#                 self.restrictions[other_parent].add(pa)
#             self.size[pa] += self.size[pb]
#             self.p[pb] = pa
#         return True
#
#
# class Solution:
#     def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
#         dsu = DSU(n)
#         for u,v in restrictions:
#             dsu.add_restriction(u,v)
#         return [dsu.unite(u,v) for u,v in requests]