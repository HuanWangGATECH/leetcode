# input 1226#24# 
# output 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 


def decode(array):
    result=[0]*26
    i=len(array)-1
    
    #print (i)
    #print (result)
    while i>=0:
        print (i)

        if array[i]=="#":
            number=int(array[i-2:i])
            result[number-1]+=1 
            i-=3
        elif array[i]==")":
            count=int(array[i-1])
            if array[i-3]=="#":
                number=int(array[i-5:i-3])
                i-=6
            else:
                number=int(array[i-3:i-2])
                i-=4
            result[number-1]+=count
        else:
            number=int(array[i])
            result[number-1]+=1
            i-=1

    #print (result)
    return result 





array="1226#24#(2)"
print (decode(array))

array="1"
print (decode(array))

array="1(2)23(3)"
print (decode(array))

array="2110#(2)"
print (decode(array))

array="23#(2)24#25#26#23#(3)"

print (decode(array))
