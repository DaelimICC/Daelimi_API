import re


class Location:
    def __init__(self):
        pass

    global buildCodes
    global wrongCode

    wrongCode = "찾을 수 없는 강의실 코드"

    # 학관 딕셔너리
    buildCodes = {
        'M': '다산관',
        'N': '수암관',
        'P': '홍지관',
        'Y': '수의실',
        'A': '대학본부',
        'B': '한림관',
        'C': '골프연습장',
        'D': '정보통신관',
        'E': '퇴계관',
        'F': '율곡관',
        'G': '학생회관',
        'H': '임곡관',
        'J': '전산관',
        'K': '생활관',
        'L': '자동차관'
    }

    # 강의실 코드 검증 메서드
    def checkBuildCode(self, buildCode):
        # 영문 판별 정규식
        reg = re.compile(r'[a-zA-Z]')

        if not reg.match(buildCode):
            return False

        if buildCode not in buildCodes.keys():
            return False

        return True

    # 강의실 코드 -> 강의실 위치 변환
    def classroomfinder(self, roomcode):
        if len(roomcode) != 5:
            return wrongCode

        # 코드 파싱
        buildCode = roomcode[0].upper()
        stair = roomcode[1:3]

        if not self.checkBuildCode(buildCode):
            return wrongCode

        # 층 코드 필터
        if not stair.isdigit():
            return wrongCode
        if int(stair) >= 9 or int(stair) < 0:
            return wrongCode

        return buildCodes[buildCode] + ' ' + str(int(stair)) + '층'
