def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1) #몫, 나머지 중 더 큰 값의 +1의 값을 answer에 넣는다.
    return answer
