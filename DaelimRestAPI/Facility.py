class Facility:
    def __init__(self):
        self.FacilityNames = {
            '수암도서관' : '수암관 4, 5층',
            '도서관' : '수암관 4, 5층',
            'WCC홀' : '수암관 1층',
            '방송실' : '한림관 4층',
            '체육관관람석' : '한림관 4층',
            '체육관' : '한림관 3층',
            '언어치료센터' : '홍지관 3층',
            '글로벌잡스테이션' : '홍지관 3층',
            '잡스테이션' : '퇴계관 5층',
            '대림아트홀' : '홍지관 1층',
            '에이스스테이션' : '퇴계관 5층',
            '대림학보사' : '퇴계관 1층',
            '학보사' : '퇴계관 1층',
            '입학팀' : '대학 본부 1층',
            '교육행정팀' : '대학 본부 1층',
            '산학협력단' : '대학 본부 3층',
            '링크사업단' : '대학 본부 4층',
            '보건실' : '임곡관 2층',
            '스마트스테이션' : '전산관 4층',
            '매점' : '학생회관 1층, 생활관 1층',
            '교내 서점' : '생활관 1층',
            '안경점' : '생활관 1층'
        }

    def checkVailed(self, code):
        if code in self.FacilityNames.keys():
            return True
        else:
            return False

    def FindLocation(self, FacilityName):
        return self.FacilityNames[FacilityName]
