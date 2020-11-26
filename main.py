from diaries.DiarySample import DiarySample
from diaries.KawaiDiaryNew import KawaiDiaryNew
from diaries.KawaDiary import KawaDiary
from diaries.Diaryk19051 import Diaryk19051
from diaries.LongMineDiary import LongMineDiary

diaries = [DiarySample(),
           Diaryk19051(),
           KawaDiary(),
           KawaiDiaryNew(),
           LongMineDiary(),]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
