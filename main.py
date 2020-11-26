from diaries.DiarySample import DiarySample
from diaries.LongMineDiary import LongMineDiary


diaries = [DiarySample(), LongMineDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
