for i in range(1, 101):
    #    test1 = str(i).find("7")
    #    if int(i)%7!=0 and test1 == -1:
    #       print(i)
    #    else:
    #       continue
    if i % 7 == 0 or i % 10 == 7:
        continue
    else:
        print(i)
