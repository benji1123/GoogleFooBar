def solution(x, y):
    end = [int(x), int(y)] # end state
    count = 0

    # count genrations, while moving from end-state to initial
    while True:
        
        if end == [1,1]:
            return str(count)

        if end[0] < 1 or end[1] < 1 or end[0]==end[1] :
            return "impossible"

        # answer is known once either bomb reaches 1
        if end[0] == 1:
            return str(count + end[1] - 1)
        elif end[1] == 1:
            return str(count + end[0] - 1)
        
        '''
        the bomb with the larger count,
        must have had a lower count in the previous 
        generation.
        '''
        if end[0] > end[1]:
            count += end[0]//end[1]
            end[0] -= (end[0]//end[1])*end[1]
        else:
            count += end[1]//end[0]
            end[1] -= (end[1]//end[0])*end[0]

print(solution(4,7))
