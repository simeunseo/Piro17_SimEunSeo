##############  menu 1
def Menu1(studentInfo, userInput) :
    #사전에 학생 정보 저장하는 코딩
    studentInfo[userInput[0]] = [userInput[1],userInput[2]]
    
'''
##############  menu 2
def Menu2(#매개변수가 필요한지 판단 후 코딩할 것) :
    #학점 부여 하는 코딩

##############  menu 3
def Menu3(#매개변수가 필요한지 판단 후 코딩할 것) :
    #출력 코딩

##############  menu 4
def Menu4(#매개변수가 필요한지 판단 후 코딩할 것):
    #학생 정보 삭제하는 코딩
'''

#학생 정보를 저장할 변수 초기화
studentInfo = {'David':[10, 20]}


print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출
        userInput = input("Enter name mid-score final-score : ").split(' ')
        if len(userInput) != 3 :
            #데이터 입력 갯수가 맞지 않을 경우
            print('Num of data is not 3!')
        elif userInput[0] in studentInfo:
            #이미 입력된 학생일 경우
            print('Already exist name!')
        elif not userInput[1].isdigit() or not userInput[2].isdigit():
            #숫자가 아닐 경우
            print('Score is not positive integer!')
        elif int(float(userInput[1])) != float(userInput[1]) or int(float(userInput[2])) != float(userInput[2]) or int(userInput[1])<0 or int(userInput[2])<0 :
            #숫자이지만 양의 정수가 아닐 경우
            print('Score is not positive integer!')
        else :
            Menu1(studentInfo, userInput)
            print(studentInfo)
'''
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료

    else :
        #"Wrong number. Choose again." 출력
'''
