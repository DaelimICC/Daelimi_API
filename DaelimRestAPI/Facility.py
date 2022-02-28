class Facility:
    def __init__(self):
        self.FacilityNames = (
        '수암도서관',
        '도서관',
        'WCC홀',
        '방송실',
        '체육관관람석',
        '체육관',
        '언어치료센터',
        '글로벌잡스테이션',
        '잡스테이션',
        '대림아트홀',
        '에이스스테이션',
        '대림학보사',
        '학보사',
        '입학팀',
        '교육행정팀',
        '산학협력단',
        '링크사업단',
        '보건실',
        '스마트스테이션'
    )

    def checkVailed(self, code):
        if code in self.FacilityNames:
            return True
        else:
            return False
