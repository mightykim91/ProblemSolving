for tc in range(1, int(input())+1):
    application_quantity = int(input())
    applications = []
    for i in range(application_quantity):
        start, end = map(int, input().split())
        if not 0 <= start < 24 or not 1<= end < 25:
            continue

        if (start,end) in applications:
            continue

        else:
            applications.append((start, end))

    #sort
    for i in range(len(applications)-1):
        for j in range(i+1, len(applications)):
            if (applications[j][1] - applications[j][0]) < (applications[i][1] - applications[i][0]):
                applications[i], applications[j] = applications[j], applications[i]

    print(applications)
    answer = 0
    #availabe = 0, not available = 1
    time_slot = [0]*25
    for j in range(application_quantity):
        validity_flag = True
        for i in range(applications[j][0],applications[j][1]+1):
            if time_slot[i] == 1:
                validity_flag = False
                break
            else:
                if i == application[0] or i == application[1]:
                    time_slot[i] = 1
                else:
                    time_slot[i] = 1
        if validity_flag:
            answer += 1

    print("#{} {}".format(tc,answer))




