def solution(n):
    answer = []

    coordinate = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            temp.append(0)
        coordinate.append(temp)

    x = 0  # x축 좌표
    y = 0  # y축 좌표
    num = 1  # 실제로 블록안에 들어갈 값
    repeat = n  # loop 횟수 (6, 5, 4, 3 순으로 점점 작게 반복)
    count = 0  # while문이 각각 몇번씩 반복했는지 확인하기 위한 변수
    pattern = 0  # y++ / x++ / x--,y-- 이렇게 3가지 방법을 %3으로 구분

    while(repeat != 0):
        if(pattern % 3 == 0): #y++
            coordinate[y][x] = num #파이썬에서 첫번째 index가 행이므로 이는 y축에 해당
            num = num+1
            count = count+1

            if(count != repeat): #아직 repeat 만큼 반복문이 돌지 않은 상황
                y = y+1
            else:
                count = 0
                x = x+1 
                #이것을 해주지 않으면 다음 상황에서 현재 값이 변경된다.
                #즉, 이 과정을 해줌으로서 시작점을 현재 값이 있는 공간이 아니라
                #실제로 시작해야하는 공간으로 옮겨줄 수 있다.
                
                repeat = repeat-1
                #repeat횟수는 위에서 언급했듯이 계속 감소한다.
                
                pattern = 1

        elif(pattern % 3 == 1): #x++
            coordinate[y][x] = num
            num = num+1
            count = count+1

            if(count != repeat):
                x = x+1
            else:
                count = 0
                x = x-1
                y = y-1
                repeat = repeat-1
                pattern = 2

        else: #x--, y--
            coordinate[y][x] = num
            num = num+1
            count = count+1

            if(count != repeat):
                x = x-1
                y = y-1
            else:
                count = 0
                y = y+1
                repeat = repeat-1
                pattern = 0


    for p in range(0, n): #answer에 값을 넣는 과정
        for q in range(0, n):
            if (coordinate[p][q] != 0):
                answer.append(coordinate[p][q])
            else:
                continue

    return answer
