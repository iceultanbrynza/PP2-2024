def filter_prime(list):
    ints = []
    cnt = 0
    for i in list:
        for j in range(1, i+1):
            if(i%j==0):
                cnt+=1
            if(j==i):
                if(cnt==2):
                    ints.append(i)
                    cnt = 0
                else:
                    cnt = 0
    print(ints)
ints = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filter_prime(ints)