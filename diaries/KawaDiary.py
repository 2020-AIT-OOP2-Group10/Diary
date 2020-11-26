from diaries.AbstractDiary import AbstractDiary


class KawaDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "朝に散歩をした"

    def get_author(self):
        return "Kawakami"
