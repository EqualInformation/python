# Custom python function to find longest substring of s in which the letters occur in 
# alphabetical order. In the case of ties, first substring is returned.
def lsubstr(s):
    lens = len(s)
    subs = ''
    subslist = []  
    longest=''
    for i in range(lens):
        tCount = 0
        for j in range(i,lens-1,1):
            if (s[j] <= s[j+1]):
                subs = subs + s[j]
                if(j == lens - 2):
                    subs=subs + s[j+1]
                    subslist.append(subs)
                    subs = ''
                    break
                tCount +=1
            elif (s[j] > s[j+1]):
                if(tCount >= 1 ):
                    subs = subs + s[j]
                elif(tCount < 1):
                    subs = subs + s[j]
                subslist.append(subs)
                subs = ''
                break 
    count = 0;
    for j in range(len(subslist)-1):
        if(count < 1):
            if(len(subslist[j]) < len(subslist[j+1])):
                longest = subslist[j+1]
            elif(len(subslist[j]) > len(subslist[j+1])):
                longest = subslist[j]
            elif(len(subslist[j]) == len(subslist[j+1])):
                longest = subslist[j]    
        elif(count >= 1):
            if(len(longest) < len(subslist[j+1])):
                longest = subslist[j+1]
        count += 1
    return longest

    
            