def backtrack(station, charged, battery_left):
    global min_charge
    if charged >= min_charge:
        return

    if station == N-1:
        min_charge = min(charged, min_charge)
        return

    if battery_left >= 


for tc in range(1, int(input())+1):
    battery = list(map(int, input().split()))
    N = len(battery)
    min_charge = 987654321
    battery_left = battery[0]
