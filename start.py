import threading , time , os

open("check.txt","w").write("False")

def st():
  while True:
    time.sleep(2)
    print("Starting...")
    os.system("python bot.py")

t = threading.Thread(target=st)


t.start()
while True:
  time.sleep(3)
  f = open("check.txt","r").read()
  os.system("pkill python")
    
print("End")
