def solution(s):
    answer = ''
    
    temp = ''
    s = s.lower()

    for i in range(0, len(s)):
        if(s[i] == " "):
            temp = temp + s[i]
            
            answer = answer + temp.capitalize()
            temp = ''
        else:
            temp = temp + s[i]
    
    answer = answer + temp.capitalize() 
    #파이썬에서는 문자 끝을 인식하지 못하므로 따로 예외처리하여 밖에서 그 경우를 더해줄 수 있도록 한다.
        
    return answer
