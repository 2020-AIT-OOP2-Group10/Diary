from diaries.DiarySample import DiarySample
from diaries.KawaiDiaryNew import KawaiDiaryNew
from diaries.KawaDiary import KawaDiary
from diaries.Diaryk19051 import Diaryk19051

diaries = [DiarySample(),
    Diaryk19051(),
    KawaDiary(),
    KawaiDiaryNew(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
