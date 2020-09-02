permus = set()


def definePrime(num):
    if num == 1 or num == 0:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def permu(level, numbers, visited, nums):
    if level == len(numbers):
        permus.add(int(nums))
        return

    if nums != "":
        permus.add(int(nums))

    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            permu(level + 1, numbers, visited, nums + numbers[i])
            visited[i] = False


def solution(numbers):
    answer = 0
    visited = [False]*len(numbers)
    permu(0, numbers, visited, "")
    for prime in permus:
        if definePrime(prime):
            answer += 1
    return answer
