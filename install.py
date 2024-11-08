import os
os.system ("clear")
print ("\033[34;m")
os.system ("figlet install Tools on Termux")
print ("\033[31;m")
print ("install  nmap   [1]")
print ("install python2 [2]")
print ("install python3 [3]")
print ("install  php    [4]")
print ("install cmatrix [5]")
print ("install  git    [6]")
print ("install  wget   [7]")
print ("install  ruby   [8]")
print ("install   go    [9]")
print ("install   C     [10]")
print ("install figlet  [11]")
print (".......................")
print (" \033[34;m      back   [99]")
print ("\033[33;m")
name=input ("Enter...")
if name == "1":
    import os
    os.system ("pkg install nmap")
if name == "2":
    import os
    os.system ("pkg install python2")
if name == "3":
    import os
    os.system ("pkg install python")
if name == "4":
    import os
    os.system ("pkg install php -y")
if name == "5":
    import os
    os.system ("pkg install cmatrix")
if name == "6":
    import os
    os.system ("pkg install git")
if name == "7":
    import os
    os.system ("pkg install wget")
if name == "8":
    import os
    os.system ("pkg install ruby -y")
if name == "9":
    import os
    os.system ("apt install golang -y")
if name == "10":
    import os
    os.system ("apt install clang -y")
if name == "11":
    import os
    os.system ("pkg install figlet")
if name == "99":
    import os
    os.system ("python back.py")
