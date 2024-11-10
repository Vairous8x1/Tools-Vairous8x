import os
os.system ("clear")
print ("\033[34;m")
os.system ("figlet install Tools on Termux")
print ("\033[31;m")
print ("install  nmap                    [1]")
print ("install python2                  [2]")
print ("install python3                  [3]")
print ("install  php                     [4]")
print ("install cmatrix                  [5]")
print ("install  git                     [6]")
print ("install  wget                    [7]")
print ("install  ruby                    [8]")
print ("install   go                     [9]")
print ("install   C                      [10]")
print ("install figlet                   [11]")
print ("install neofetch                 [12]")
print ("install metasploit               [13]")
print ("install All the basics of Termux [14]")
print (".......................")
print (" \033[34;m      back   [99]")
print ("\033[33;m")
name=input ("Enter...")
if name == "1":
    import os
    os.system ("pkg install nmap")
    os.system ("python back.py")
if name == "2":
    import os
    os.system ("pkg install python2")
    os.system ("python back.py")
if name == "3":
    import os
    os.system ("pkg install python")
    os.system ("python back.py")
if name == "4":
    import os
    os.system ("pkg install php -y")
    os.system ("python back.py")
if name == "5":
    import os
    os.system ("pkg install cmatrix")
    os.system ("python back.py")
if name == "6":
    import os
    os.system ("pkg install git")
    os.system ("python back.py")
if name == "7":
    import os
    os.system ("pkg install wget")
    os.system ("python back.py")
if name == "8":
    import os
    os.system ("pkg install ruby -y")
    os.system ("python back.py")
if name == "9":
    import os
    os.system ("apt install golang -y")
    os.system ("python back.py")
if name == "10":
    import os
    os.system ("apt install clang -y")
    os.system ("python back.py")
if name == "11":
    import os
    os.system ("pkg install figlet")
    os.system ("python back.py")
if name == "13":
    import os
    os.system ("apt update && apt upgrade -y; apt install git -y; git clone https://github.com/sadamshr3be/metasploit_framework; cd metasploit_framework; -Metaspl*;bash setup;") 
    os.system ("msfconsole") 
#    os.system ("python back.py")
if name == "12":
    import os
    os.system ("pkg install neofetch")
    os.system ("python back.py")

if name=="14":
    import os
    os.system("clear")
    os.system("termux-setup-storage;cd;dpkg --configure -a;pkg update -y;pkg upgrade -y;pkg install python -y;pkg install python2 -y;pkg install python2-dev -y;pkg install python3 -y;pkg install pip -y;pkg install pip2;pip2 install requests;pkg install fish -y;pkg install ruby -y;pkg install git -y;pkg install dnsutils -y;pkg install php -y;pkg install perl -y;pkg install nmap -y;pkg install bash -y;pkg install clang -y;pkg install nano -y;pkg install w3m -y;pkg install figlet -y;pkg install cowsay -y;gem install lolcat;pkg install curl -y;pkg install tar -y;pkg install zip -y;pkg install unzip -y;pkg install tor -y;pkg install wget -y;pkg install wgetrc -y;pkg install wcalc -y;pkg install bmon -y;pkg install unrar -y;pkg install toilet -y;pkg install proot -y;pkg install golang -y;pkg install chroot -y;termux-chroot -y;pkg install openssl -y;pkg install cmatrix -y;pkg install openssh -y;apt update && apt upgrade -y")
    os.system ("python back.py")







if name == "99":
    import os
    os.system ("python back.py")
