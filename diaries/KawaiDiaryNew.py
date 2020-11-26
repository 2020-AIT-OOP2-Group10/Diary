from diaries.AbstractDiary import AbstractDiary


class KawaiDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "普通の一日だった"

    def get_author(self):
        return "Kawai"
