
a=[28,31,24,25,30,32,20,30,31,26,31]
total=0

#평균

def mMean():
    for i in a:
        total+= j
    return total/len(a)


print("평균 mMean() : %d" %mMean())


def mMedian():
    for i in range(len(a)-1):
        for j in range(i,len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    if len(a) % 2 == 0:
        return (a[int(len(a)/2)] + a[int(len(a)/2)-1])/2
    else:
        return a[int(len(a)/2)]
    