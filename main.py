from diaries.DiarySample import DiarySample
from diaries.KawaiDiaryNew import KawaiDiaryNew

diaries = [DiarySample(), KawaiDiaryNew()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
