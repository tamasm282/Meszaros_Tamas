# Jövedelemszámítás
print("Jövedelemszámítás\n")
kor = int(input("Hány éves vagy?"))
gyerek = ""
if kor > 25:
    gyerek = input("Van 3 gyereked és nő vagy (y/n)?")
    if gyerek not in ["y", "yes", "igen", "Igen", "i"]:


brutto = int(input("Mennyi a bruttód:"))
if kor <= 25 or gyerek in ["y", "yes", "igen", "Igen", "i"]:
    if brutto > 500000:
        szja = (brutto-500000) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15
print("Adók".center(40))
print("SZJA:".ljust(30, "_"), str(int(szja)).rjust(10, "_"), sep="")
print("Nyugdíj:".ljust(30,"_"), str(int(brutto * 0.1)).rjust(10, "_"), sep="")
print("TB:".ljust(30, "_"),str(int(brutto * 0.07)).rjust(10,"_"), sep="")
print("Munkanélkül:".ljust(30, "_"),str(int(brutto * 0.015)).rjust(10,"_"), sep="")
print("\nNettó:".ljust(30, "_"),str(int(brutto-brutto * 0.185-szja)).rjust(10,"_"), sep="")
