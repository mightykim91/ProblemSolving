from collections import deque


def solution(board, moves):
    basket = deque()
    pop_count = 0
    for x in moves:
        y = 0
        while y < len(board):
            if board[y][x-1] != 0:
                if basket:
                    on_top = basket.popleft()
                    if on_top == board[y][x-1]:
                        pop_count += 2

                    else:
                        basket.appendleft(on_top)
                        basket.appendleft(board[y][x-1])
                else:
                    basket.append(board[y][x-1])
                board[y][x-1] = 0
                break
            else:
                y += 1

    answer = pop_count
    return answer