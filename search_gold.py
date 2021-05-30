def travel_and_collect(arr, i, j, visited, bag):
    if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]) or arr[i][j] == 0 or visited[i][j] == 1:
        return

    visited[i][j] = 1
    bag.append(arr[i][j])
    travel_and_collect(arr, i - 1, j, visited, bag)
    travel_and_collect(arr, i, j + 1, visited, bag)
    travel_and_collect(arr, i + 1, j, visited, bag)
    travel_and_collect(arr, i, j - 1, visited, bag)


gm = [[1, 0, 4, 2, 8, 2], [4, 0, 6, 5, 0, 4], [1, 0, 4, 1, 4, 6], [2, 0, 7, 3, 2, 2], [3, 0, 5, 9, 2, 4],
      [2, 0, 0, 8, 5, 1]]
visited = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]
max_sum = 0

for i in range(len(gm)):
    for j in range(len(gm[0])):
        if gm[i][j] != 0 and visited[i][j] == 0:
            bag = []
            travel_and_collect(gm, i, j, visited, bag)
            if sum(bag) > max_sum:
                max_sum = sum(bag)

print(max_sum)
