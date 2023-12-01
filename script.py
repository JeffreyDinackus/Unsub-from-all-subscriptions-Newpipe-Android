import subprocess
import time


# enter a number higher than all subscriptions
total = 400

i = 0




def adb_command(command):
    subprocess.run(['adb', 'shell', command])

def short_click(x, y):
    adb_command(f'input tap {x} {y}')

def long_click(x, y, duration=2000):
    adb_command(f'input touchscreen swipe {x} {y} {x} {y} {duration}')




while i < total:
  # long click for hover over
  long_click(300, 400, duration=3000)


  

  # Example short click on subsub
  short_click(100, 200)






  # click somewhere else on screen to reset the screen
  short_click(100, 200)

  # update i 
  i+=1


