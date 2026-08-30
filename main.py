"""나만의 프롬프트 관리 프로그램

터미널에서 메뉴 번호를 입력해 프롬프트를 추가하고, 목록·카테고리 조회·
검색·상세 보기·즐겨찾기까지 관리할 수 있는 콘솔 프로그램.
"""


# 기본 프롬프트 데이터 — 이전 미션에서 작성한 프롬프트 4개를 미리 등록
# 리스트 + 딕셔너리로 저장 (제목, 내용, 카테고리, 즐겨찾기 여부)
PROMPTS = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": True,
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝고 깨끗한 배경, 중앙에 제품 배치, 부드러운 그림자, 심플한 포인트 텍스트 포함. 16:9 비율.",
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 20년 경력의 시니어 IT 컨설턴트입니다. 고객의 질문에 대해 실무 경험을 바탕으로 구체적이고 현실적인 조언을 해주세요. 기술적 용어는 쉬운 비유로 설명하고, 마지막에 다음 액션 아이템 3가지를 요약해 주세요.",
        "category": "페르소나",
        "favorite": False,
    },
    {
        "title": "뉴스 요약 프롬프트",
        "content": "주어진 뉴스 기사 내용을 핵심만 3줄로 요약해주세요. 1) 사건 요약, 2) 주요 숫자/팩트, 3) 독자가 알아야 할 영향.",
        "category": "자동화",
        "favorite": False,
    },
]

# 카테고리 목록 — 추가 시 선택 목록으로 사용
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


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


def add_prompt():
    """새 프롬프트 추가 — 제목·내용·카테고리 입력, 빈 입력 시 재입력 요청"""
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ").strip()
    while not title:
        print("제목은 비워둘 수 없습니다.")
        title = input("제목: ").strip()
    content = input("내용: ").strip()
    while not content:
        print("내용은 비워둘 수 없습니다.")
        content = input("내용: ").strip()

    print("\n카테고리 선택:")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}) {category}")
    print(f"{len(CATEGORIES) + 1}) 직접 입력")
    choice = input("선택: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        category = CATEGORIES[int(choice) - 1]
    elif choice.isdigit() and int(choice) == len(CATEGORIES) + 1:
        category = input("새 카테고리: ").strip() or "기타"
    else:
        print("카테고리를 선택하지 않아 '기타'로 등록합니다.")
        category = "기타"

    PROMPTS.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print("\n프롬프트가 추가되었습니다!")


def show_by_category():
    """카테고리 선택 → 해당 카테고리 프롬프트만 출력"""
    print("\n=== 카테고리별 조회 ===")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}) {category}")
    choice = input("선택: ").strip()
    if not choice.isdigit() or not 1 <= int(choice) <= len(CATEGORIES):
        print("존재하지 않는 카테고리입니다.")
        return
    category = CATEGORIES[int(choice) - 1]
    results = [p for p in PROMPTS if p["category"] == category]
    print(f"\n[{category}] 카테고리 프롬프트:")
    if not results:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(results, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star}")
    print(f"\n총 {len(results)}개의 프롬프트")


def search_prompt():
    """키워드 검색 — 제목 또는 내용에 포함된 프롬프트 출력"""
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    if not keyword:
        print("검색어를 입력해 주세요.")
        return
    results = [p for p in PROMPTS if keyword in p["title"] or keyword in p["content"]]
    print("\n검색 결과:")
    if not results:
        print(f"'{keyword}'에 해당하는 프롬프트가 없습니다.")
        return
    for i, p in enumerate(results, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")
    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


def show_detail():
    """번호 입력 → 해당 프롬프트 전체 내용 표시"""
    print("\n=== 프롬프트 상세 보기 ===")
    number = input("번호 입력: ").strip()
    if not number.isdigit() or not 1 <= int(number) <= len(PROMPTS):
        print("존재하지 않는 번호입니다.")
        return
    prompt = PROMPTS[int(number) - 1]
    line = "\u2500" * 28
    print(f"\n{line}")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {'⭐' if prompt['favorite'] else '아니요'}")
    print(line)
    print("내용:")
    print(prompt["content"])
    print(line)


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
        if choice == "1":
            add_prompt()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        else:
            print("이 기능은 아직 개발 중입니다.")
        input("\n메뉴로 돌아가려면 Enter를 누르세요")


if __name__ == "__main__":
    main()
