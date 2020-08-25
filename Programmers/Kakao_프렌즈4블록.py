import sys

sys.stdin = open('Programmers/inputs/Kakao_프렌즈4블록.txt', 'r')


def solution(m, n, board):
    for y in range(m):
        board[y] = list(board[y])

    dy = [1, 0, 1]
    dx = [1, 1, 0]

    count = 0
    while True:
        toDrop = set()
        for y in range(m-1):
            for x in range(n-1):
                index = board[y][x]
                confirm = []
                coords = []
                if index != 0:
                    for i in range(3):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if index == board[ny][nx]:
                            confirm.append(board[ny][nx])
                            coords.append((ny, nx))

                    if confirm.count(index) == 3:
                        for coord in coords:
                            toDrop.add(coord)
                        toDrop.add((y, x))

        for el in toDrop:
            board[el[0]][el[1]] = 0

        count += len(toDrop)

        for x in range(n):
            column = []
            for y in range(m):
                column.append(board[y][x])

            zero_counter = column.count(0)
            for i in range(zero_counter):
                column.remove(0)
            for i in range(zero_counter):
                column.insert(0, 0)

            for i in range(len(column)):
                board[i][x] = column[i]

        if len(toDrop) == 0:
            return count


for tc in range(int(input())):
    m, n = map(int,input().split())
    board = []
    for i in range(m):
        board.append(list(input()))

    print(solution(m, n, board))

    
    
