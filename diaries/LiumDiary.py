from diaries.AbstractDiary import AbstractDiary


class LiumDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "リーダーになった"

    def get_author(self):
        return "Lium"
