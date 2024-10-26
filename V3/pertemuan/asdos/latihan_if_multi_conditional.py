berat = 2
rasa = "manis"

if berat >= 2 and rasa == "manis":
    grade = "Grade A"
elif berat < 2 and rasa == "manis":
    grade = "Grade B"
elif berat >= 2 and rasa != "manis":
    grade = "Grade C"
else :
    grade = "Grade D"

print("Semangka dengan berat", berat, "kg dan rasa", rasa, "memiliki grade", grade)
