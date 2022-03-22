import datetime
from datetime import datetime, timedelta

basla = input("Gün Ay Yıl olacak şekilde bir tarih yazınız: ")  # 14 02 2022
basla = datetime.strptime(basla, "%d %m %Y")                    # 2022-02-14 00:00:00
basla = basla.date()                                            # 2022-02-14

baslangictarihi = basla.strftime("%d %m %Y")                    # 14 02 2022
bitis = basla + timedelta(days=120)                             # 2022-06-14
bitistarihi = bitis.strftime("%d %m %Y")                        # 14 06 2022

simdi = datetime.now().date()                                   # 2022-02-14
fark = bitis - simdi                                            # 120 days, 0:00:00

print(f"Virdin başlangıç tarihi {baslangictarihi} bitiş tarihi: {bitistarihi}. Virdin bitmesine {fark.days} gün var.")