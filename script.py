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




# write youtube subs here if you need a quick place to write

# david hoffman
# fresh and fit 
# Andrew Huberman

while i < total:
  # long click for hover over
  long_click(691, 1030, duration=2000)


  

  # Example short click on unsub
  short_click(346, 1309)



  time.sleep(1)


  # update i 
  i+=1
  print(i)


