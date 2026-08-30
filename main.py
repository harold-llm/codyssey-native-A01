"""나만의 프롬프트 관리 프로그램

터미널에서 메뉴 번호를 입력해 프롬프트를 추가하고, 목록·카테고리 조회·
검색·상세 보기·즐겨찾기까지 관리할 수 있는 콘솔 프로그램.
"""


def show_menu():
    """메뉴 표시"""
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def main():
    """메인 루프 — 메뉴를 반복 표시하고 선택에 따라 기능을 실행"""
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "0":
            print("프로그램을 종료합니다. (Goodbye!)")
            break
        if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
            print("1~7 또는 0을 입력해 주세요.")
            continue
        print("이 기능은 아직 개발 중입니다.")
        input("\n메뉴로 돌아가려면 Enter를 누르세요")


if __name__ == "__main__":
    main()
