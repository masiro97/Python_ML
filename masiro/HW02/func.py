#func.py
#Define Functions

def NewInput():
    s_file = open("Student_Grade.txt","a")
    name = input("학생 이름을 입력해주세요: ")
    eng = int(input("영어 성적을 입력해주세요: "))
    math = int(input("수학 성적을 입력해주세요: "))
    mean = (eng + math)/2
    data  = "이름 : %s 수학: %d 영어: %d 평균:%.1f\n" %(name,math,eng,mean)
    s_file.write(data)
    s_file.close()
    return

def EntirePrint():
    s_file = open("Student_Grade.txt", "r")
    data = s_file.readlines()
    if len(data) == 0:
        print("데이터가 없습니다")
    else:
        for i in data:
            print(i)
        s_file.close()
    return

def SortStudent():
    # readlines로 파일의 모든 데이터를 불러온 뒤 정렬
    s_file = open("Student_Grade.txt", "r")
    data = s_file.readlines()
    data.sort()
    s_file.close()

    # 파일을 w모드로 열어서 모두 삭제 한뒤 정렬된 데이터를 다시 작성
    s_file = open("Student_Grade.txt","w")
    for i in data:
        s_file.write(i)
    s_file.close()
    return

def DelEntire():
    # w모드로 열어서 모든 데이터 삭제
    s_file = open("Student_Grade.txt", "w")
    s_file.close()
    return

def DelSelect():
    num =0            #데이터의 순서를 나타내는 변수

    # 읽기 모드로 열은 뒤에 데이터의 순서와 함께 프린트
    s_file = open("Student_Grade.txt", "r")
    data = s_file.readlines()
    for i in data:
        num += 1
        print("%d. %s"%(num,i))
    s_file.close()

    while True:
        temp = input("삭제할 데이터의 번호를 입력해주세요")
        if not(temp.isdigit()):
            print("숫자를 입력해주세요")
        elif (0>int(temp) or int(temp)>num):
            print("없는 데이터 번호입니다")
            stop = int(input("선택삭제를 계속 하시겠습니까? (계속:1 중지:0)"))
            if stop == 1:
                print("선택 삭제를 계속 합니다")
            else:
                print("선택삭제를 중지합니다")
                break
        else:
            DelData = int(temp)
            del data[DelData-1]
            s_file = open("Student_Grade.txt","w")
            for i in data:
                s_file.write(i)
            s_file.close()
            print("%d번째 데이터를 삭제했습니다." %DelData)
            break
    return