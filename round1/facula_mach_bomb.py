def solution(x, y):
   ''' Google FooBar level 3.1'''
   
   # count steps while going from end-state -> initial-state
    count = 0
    x = int(x)
    y = int(y)
    
    while True:
        # initial state reached
        if x==1 and y==1:
            return str(count)
            
        # don't go below (1,1) & bomb-counts never equal except @ 1
        if x<1 or y<1 or x==y:
            return "impossible"
            
        # special case when one num == 1
        if x == 1:
            return str(count + (y-1))
        elif y == 1:
            return str(count + (x-1))
        
        # (n-1)th step reached by (BigNum -= SmallNum)
        if x>y:
            count += x//y
            x -= y*(x//y) # BigNum may be multiple-times bigger
        elif y>x:
            count += y//x
            y -= x*(y//x)
        
print(solution("2","12"))
