import datetime
from datetime import datetime, timedelta

begin = input("Enter a date as day month year: ")  # 14 02 2022
begin = datetime.strptime(begin, "%d %m %Y")                    # 2022-02-14 00:00:00
begin = begin.date()                                            # 2022-02-14

beginningdate = begin.strftime("%d %m %Y")                    # 14 02 2022
end = begin + timedelta(days=120)                             # 2022-06-14

endingdate = end.strftime("%d %m %Y")                        # 14 06 2022

now = datetime.now().date()                                   # 2022-02-14
days = end - now                                            # 120 days, 0:00:00

print(f"Begins at {beginningdate} and ends at {endingdate}. {days.days} days left.")
