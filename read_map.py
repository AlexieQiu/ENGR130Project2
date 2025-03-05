from collections import deque
def map(txt):
    fp = open(txt, "r")
    map = []
    cnt = list.count(fp.readlines())
    fp.close()
    fp = open(txt, "r")
    num_line = 0
    while True:
        if num_line == cnt - 1:
            break
        map.append(fp.readline().split(","))
        num_line += 1

    return map


def BFS(map):
    i = len(map)
    j = len(map[0])

    start = None
    for row in map:
        if "S" in row:
            start = (map.index(row), row.index("S"))
            break

    if not start:
        return "None"
    q = deque([(start[0], start[1], [])])
    visited = set()
    visited.add(start)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        r, c, path = q.popleft()
        if map[r][c] == "X":
            return path + [(r, c)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < i and 0 <= nc < j and (nr, nc) not in visited:
                if map[nr][nc] in ("0", "X"):  # Can move to empty space or 'X'
                    q.append((nr, nc, path + [(r, c)]))  # Store path
                    visited.add((nr, nc))

    return "None"


# if __name__ == '__main__':
