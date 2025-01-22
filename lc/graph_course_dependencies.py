from typing import Dict, List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_map: Dict[int, List[int]] = {}

        for i in range(numCourses):
            prerequisites_map.setdefault(i, [])

        for ctgt, csrc in prerequisites:
            prerequisites_map[ctgt].append(csrc)

        completable_courses = set()

        # print(f"{prerequisites_map=}")

        while len(completable_courses) < numCourses :
            completable_now = []

            for c, deps in prerequisites_map.items():
                if c in completable_courses:
                    continue

                if all([d in completable_courses for d in deps]):
                    completable_now.append(c)

            if not completable_now:
                return False

            completable_courses.update(completable_now)
            # print(f"{completable_courses=}, {completable_now=}, unresolved={[c for c in prerequisites_map.keys() if c not in completable_courses]}")

        return True

s = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(f"{numCourses=}, {prerequisites=}")
print(s.canFinish(numCourses, prerequisites))


numCourses = 2
prerequisites = [[1,0],[0,1]]
print(f"{numCourses=}, {prerequisites=}")
print(s.canFinish(numCourses, prerequisites))

numCourses = 20
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
print(f"{numCourses=}, {prerequisites=}")
print(s.canFinish(numCourses, prerequisites))
