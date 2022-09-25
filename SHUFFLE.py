def maxaverage(l):
    d = {}
    for i in l:
        name, score = i
        if name in d:
            tot_score, num = d[name]
            d[name] = (tot_score+score, num+1)
        else:
            d[name] = (score, 1)
    max= -1
    for key in d:
        tot_score, num = d[key]
        ave = tot_score/num
        if(max < ave):
            max = ave
    l = []
    for key in d:
        tot_score, num = d[key]
        ave = tot_score/num
        if(max == ave):
            l.append(key)
    l.sort()
    return l
