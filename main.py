from diaries.DiarySample import DiarySample
from diaries.Diaryk19051 import Diaryk19051

diaries = [DiarySample(),Diaryk19051(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
