def zzs(list):
    i = 0
    string = ""
    while i < len(list):
        if(list[i] == 0 or list[i] == 7):
            string = string + str(list[i])
        i+=1
    if(string == "007"):
        print("True")
    else:
        print("False")
lists = [2, 5,3,3,7, 6,4,5,0,0,433]
zzs(lists)
