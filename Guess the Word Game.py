num=178;
print("\n Guess the number : " )
inp= int(input());
count = 8;

while True:
    count=count-1;
    print(" counts remaining : ", count);
    if count:

        if num==inp:
            print("\n CONGRATULATION.. You Have Win The Game .REMAINING COUNTS:",count);
            break
        elif inp !=num:
            if inp>num:
                print("\n enter less than", inp,",try another number...");
                inp=int(input())
                continue
            else:
                print("\n enter greater than", inp,",try another number...");
                inp = int(input())
                continue
    else:
        print("Game Over");
        break



