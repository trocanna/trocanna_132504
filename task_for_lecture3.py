#Написать программу, которая просит ввести температуру в [градусах цельсия или фаренгейта] (12C или 100F). 
#Программа должна проверить корректность ввода, а затем вывести значение в другой шкала: если ввод был в цельсиях, то вывод - в фаренгейтах и наоборот.

tempC = input("Введите температуру в градусах цельсия (максимум трёхзначное целое число, напр.: +16):")
zifri = "0123456789"
nachalniye_simvoli = "+-"
nolik = "0"

if tempC[0] in nolik:
  print("База")
elif tempC[0] in nachalniye_simvoli:
  #print("Проводится проверка")
  if len(tempC) > 1:
    #print(".") 
    if tempC[1] in zifri[1:]:
      #print("Вторая проверка")
      if len(tempC) > 2:
        #print(".")
        if tempC[2] in zifri:
          #print("Проверка номер три")
          if len(tempC) > 3:
            #print(".")
            if tempC[3] in zifri:
             print((9 / 5) * float(tempC) + 32)
            else: print("перечитай условие!")
          else: print((9 / 5) * float(tempC) + 32)  
        else: print("перечитай условие!")
      else: print((9 / 5) * float(tempC) + 32)
    else: print("перечитай условие!")
  else: print((9 / 5) * float(tempC) + 32)
else: print("перечитай условие!")
