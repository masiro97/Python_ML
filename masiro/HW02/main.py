#main.py
#2017.04.04 제출
#학번: 2015041703
#이름: 신혜영
#학생 성적 관리 프로그램 만들기
#신규 입력, 전체 출력, 정력, 전체 삭제, 선택 삭제, 파일 입출력
#프로그램 종료 시, 리스트의 전체를 파일로 저장
#프로그램 실행 시, 파일에 있는 리스트를 모두 불러와서 리스트에 입력

import func

print("학생 성적 관리 프로그램입니다.")

while True:
    print("1.신규 입력 2.전체 출력 3.정렬 4.전체 삭제 5.선택 삭제 0.종료")
    e_input = input("입력: ")

    if(e_input.isdigit() and 0 <=int(e_input) <=5):

        select = int(e_input)
        if select == 1:
            print("데이터를 신규로 입력받습니다")
            func.NewInput()
        elif select == 2:
            print("데이터를 모두 출력합니다")
            func.EntirePrint()
        elif select == 3:
            func.SortStudent()
            print("데이터를 정렬했습니다")
        elif select == 4:
            print("데이터가 모두 삭제되었습니다")
            func.DelEntire()
        elif select == 5:
            print("데이터를 선택삭제합니다")
            func.DelSelect()
        elif select == 0:
            print("프로그램을 종료합니다.")
            break
        else:
            print("다시 입력해주세요")
    else:
        print("잘못된 입력입니다")
        print("숫자를 입력해주세요 (0 ~ 5)")


