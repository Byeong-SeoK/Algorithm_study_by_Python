def solution(m, musicinfos):
    answer = ''
    
    length = [] #런타임이 들어가는 배열
    title = [] #곡 제목이 들어가는 배열
    melody = [] #음 정보가 들어가는 배열
    

    for i in range(0, len(musicinfos)):# ,으로 split해서 info에 넣는다.
        info = musicinfos[i].split(',')
        
        if(int(info[0][:2]) < int(info[1][:2])):#0이 시작 시간, 1이 끝나는 시간
            hour = int(info[1][:2]) - int(info[0][:2])
            
            if(int(info[0][3:]) > int(info[1][3:])):#12:40 13:00 --> 20
                minute = int(info[1][3:]) - int(info[0][3:])
            else:
                minute = int(info[1][3:]) - int(info[0][3:])
            
            time = hour*60+minute
        
        elif(int(info[0][:2]) == int(info[1][:2])):
            
            if(int(info[0][3:]) > int(info[1][3:])):#12:40 13:00 --> 20
                minute = int(info[1][3:]) - int(info[0][3:])
            else:
                minute = int(info[1][3:]) - int(info[0][3:])
            time = minute
        
        else: #23:50 00:10같이 시작 시간의 hour값이 더 큰 경우
            hour = int(info[1][:2]) - int(info[0][:2]) + 24
            
            if(int(info[0][3:]) > int(info[1][3:])):#12:40 13:00 --> 20
                minute = int(info[1][3:]) - int(info[0][3:])
            else:
                minute = int(info[1][3:]) - int(info[0][3:])
            
            time = hour*60+minute
            
        
        length.append(time)
        print(time)
        title.append(info[2])
        melody.append(info[3])
        
    
    temp1 = []
    index1 = 0
    for j in range(0, len(m)): #m의 #부분 숫자로 교체
        if(m[j] != '#'):
            temp1.append(m[j])
            index1 = index1+1
        else:
            if(temp1[index1-1] == 'C'):
                temp1[index1-1] = '1'
            elif(temp1[index1-1] == 'D'):
                temp1[index1-1] = '2'
            elif(temp1[index1-1] == 'F'):
                temp1[index1-1] = '3'
            elif(temp1[index1-1] == 'G'):
                temp1[index1-1] = '4'
            elif(temp1[index1-1] == 'A'):
                temp1[index1-1] = '5'
            else:
                continue
    
    m_str = ''
    for k in range(0, len(temp1)):
        m_str = m_str + temp1[k]
    m = m_str
    #print("after : ", m)
    
    
    for a in range(0, len(melody)): #melody의 #부분 숫자로 교체
        temp2 = []
        index2 = 0
        for b in range(0, len(melody[a])):
            if(melody[a][b] != '#'):
                temp2.append(melody[a][b])
                index2 = index2+1
            else:
                if(temp2[index2-1] == 'C'):
                    temp2[index2-1] = '1'
                elif(temp2[index2-1] == 'D'):
                    temp2[index2-1] = '2'
                elif(temp2[index2-1] == 'F'):
                    temp2[index2-1] = '3'
                elif(temp2[index2-1] == 'G'):
                    temp2[index2-1] = '4'
                elif(temp2[index2-1] == 'A'):
                    temp2[index2-1] = '5'
                else:
                    continue
        
        mus_str = '' #배열의 값을 string으로 만드는 변수이다.
        for c in range(0, len(temp2)):
            mus_str = mus_str + temp2[c]
        melody[a] = mus_str
    
    #print("after melody : ", melody)
        
    num = 0
    l_index = 0 #length에 접근하는 index
    
    for p in range(0, len(melody)):
        if(len(melody[p]) > length[l_index]):#멜로디 길이 > 재생시간, 재생시간 만큼만 재생
            meo_str = melody[p][:length[l_index]]
            melody[p] = meo_str #새로운 음 정보로 교체
            l_index = l_index+1
            
        elif(len(melody[p]) == length[l_index]):#멜로디 길이 == 재생시간
            l_index = l_index+1
            
        else:#멜로디 길이 < 재생시간, 멜로디를 재생시간에 맞추어서 반복 재생
            remain = length[l_index] % len(melody[p])
            share = length[l_index] // len(melody[p])
            
            meo_str = melody[p]*share + melody[p][:remain]
            
            melody[p] = meo_str
            #print(melody[p])
            
            l_index = l_index+1
            
    #print(melody)
    
    print("length : ", length)
    print("title : ", title) 
    print("melody : ", melody)
    print("m : ", m)
    
    
    run_time = 0 #재생 시간 비교를 위한 변수
    found = False
    
    for k in range(0, len(melody)):
        find = melody[k].find(m) #음 정보가 존재하는지 검색
        #print(find)
        
        if(find == -1): #음 정보가 없을 때
            continue
        else:
            found = True
            
            if(run_time < length[k]): #재생 시간이 더 긴 것으로 title 교체
                run_time = length[k]
                answer = title[k]
            else:
                continue
    
    if(not found): #찾고자하는 곡을 못 찾았을 때
        answer = '(None)'
    
    return answer
