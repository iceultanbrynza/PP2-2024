def Histogram(*height):
    i = 0
    string = ""
    while(i < len(height)):
        for j in range(0, height[i]):
            string = string + '*'
        i+=1
        print(string)
        string = ""
Histogram(1, 5, 7, 9)
