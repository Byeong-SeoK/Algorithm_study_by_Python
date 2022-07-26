import heapq as h
def solution(scoville, K):
    answer = 0
    
    h.heapify(scoville)
    
    while True:
        item1 = h.heappop(scoville)        
        if(item1 >= K):
            break
            
        if(len(scoville) == 0):
            answer = -1
            break
        
        item2 = h.heappop(scoville)
        sum = item1 + item2*2
        answer = answer + 1
        
        h.heappush(scoville, sum)
    
    
    
        
    return answer
