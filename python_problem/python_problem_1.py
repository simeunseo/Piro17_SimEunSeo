def checkInput(num):
    if num.isdigit(): #입력값이 숫자라면
        #정수인지 확인한다
        if float(num) - int(num) != 0: #정수가 아니라면
            print('정수를 입력하세요')
            return 1
        else : #정수라면
            if int(num)<1 or int(num)>3 : #정수이지만 범위에 맞지 않는다면
                print('1,2,3 중 하나를 입력하세요')
                return 2
            else : #정수이면서 범위에 맞는다면
                return 0
    else : #입력값이 숫자가 아니라면
        print('정수를 입력하세요')
        return 1
    


def brGame(player):
    global currentNum
    global gameEndFlag
    global winner
    winner = 'none'
    num=0

    #입력 받기
    while True :
        num=input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')
        if checkInput(num)==0: #입력값이 올바르다면
            num=int(num)
            break
    #숫자 부르기
    for i in range(currentNum, currentNum+num):
        print('player%s : %d' %(player, i))
        currentNum+=1
        if i == 31 : #31을 부르면
            gameEndFlag = 1 #게임 종료
            if player== 'A' :
                winner = 'B'
            else :
                winner = 'A'
            return
                


gameEndFlag = 0
currentNum = 1
while True:
    if gameEndFlag == 0 : 
        brGame('A')
    else :
        break
    if gameEndFlag == 0 :
        brGame('B')
    else :
        break

print('player%s win!' %winner)
