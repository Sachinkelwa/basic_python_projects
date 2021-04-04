def love(name_male,name_female):
    sum1 = 0
    for i in name_male:
        for j in name_female:
            if i == j:
                sum1 += 5
    if sum1 < 100:
        print(f"your love parsent is : {sum1} % ")
        print("keep loving")
    else:
        print(f"your love prasent is : 100% ")
        print("your love is beyond science")
a = input("Enter he's name : ")
b = input("Enter her name : ")
love(a,b)
    