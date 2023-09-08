import numpy as py

def getKali(numbers):
  hasil = 1
  for angka in numbers:
    hasil *= angka

  return hasil

angka_list = [2, 3, 4, 5]
hasil_kali = getKali(angka_list)
print("Hasil perkalian seluruh angka : ", hasil_kali)