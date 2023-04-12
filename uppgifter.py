import beepy as beep
import time

mening = input("Skriv något!: ").lower()
morselist = ["kl", "lkkk", "lklk", "lkk", "k", "kklk", "llk", "kkkk", "kk", "klll", "lkl", "klkk", "ll", "lk", "lll", "kllk", "llkl", "klk", "kkk", "l", "kkl", "kkkl", "kll", "lkkl", "lkll", "llkk"]
morsestr = ""
i = 0
alfabetet = "abcdefghijklmnopqrstuvwxyz"

for i in range(0, len(mening)):
    morsestr = morsestr + morselist[alfabetet.find(mening[i])]

print(morsestr)

for i in range(0, len(morsestr)):
    if morsestr[i] == "k":
        beep.beep(1)
    else:
        time.sleep(0.25)
        beep.beep(3)
        time.sleep(0.25)
