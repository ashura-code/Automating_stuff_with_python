import time
import sys

a = int(input("how many stars do you want ?: "))
def zigzag():
    i=a
    flag = True
    while i!=a+1:
      if flag==True:
        print(' '*i,end='')
        print('*****')
        i = i-1
        if i ==0:
            flag = False

      if flag==False:

            print(' ' * i, end='')
            print('*****')
            i = i + 1




while True:
    zigzag()
    time.sleep(0.5)
