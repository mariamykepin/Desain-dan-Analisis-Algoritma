import numpy as np

def getBagi(numbers):
  hasil = numbers[0]

  for i in range(1, len(numbers)):
    hasil /= numbers[i]

  return hasil

angka_list = [10, 2, 5]
hasil_bagi = getBagi(angka_list)
print("Hasil pembagian seluruh angka : ", hasil_bagi)