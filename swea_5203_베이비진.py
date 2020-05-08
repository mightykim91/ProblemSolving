def shuffle(player, lst, output, level, used):
    #exit
    if level == len(lst):
        babygin(player, output)
        return

    for i in range(len(lst)):
        if not used[i]:
            used[i] = True
            shuffle(player, lst, output+[lst[i]], level+1, used)
            used[i] = False
            if triplet_flag_one or triplet_flag_two or run_flag_one or run_flag_two:
                return



def babygin(player, lst):
    global triplet_flag_one, run_flag_one, triplet_flag_two, run_flag_two
    #check run
    run_cnt = 1
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1] + 1:
            run_cnt += 1

        else:
            run_cnt = 1

        if run_cnt == 3:
            #print(lst)
            if player == 1:
                run_flag_one = True

            else:
                run_flag_two = True

            break

    #check triplet
    for i in range(len(lst)):
        if lst.count(lst[i]) >= 3:
            if player == 1:
                triplet_flag_one = True
            else:
                triplet_flag_two = True
            break


for tc in range(1, int(input())+1):
    #무승부 = 0, 플레이어1 = 1 플레이어2 = 2
    triplet_flag_one, triplet_flag_two = False, False
    run_flag_one, run_flag_two = False, False
    player_one = []
    player_two = []
    given_cards = list(map(int, input().split()))
    for i in range(len(given_cards)):
        if i % 2 == 0:
            player_one.append(given_cards[i])
        elif i % 2 != 0:
            player_two.append(given_cards[i])
            if len(player_one) >= 3 and len(player_two) >= 3:
                used = [False]*len(player_one)
                shuffle(1, player_one, [], 0, used)
                shuffle(2, player_two, [], 0, used)
                if triplet_flag_one or triplet_flag_two or run_flag_one or run_flag_two:
                    break
    if triplet_flag_one or run_flag_one:
        print("#{} 1".format(tc))
    elif triplet_flag_two or run_flag_two:
        print("#{} 2".format(tc))
    else:
        print("#{} 0".format(tc))
