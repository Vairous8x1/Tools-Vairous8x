import os
os.system("clear")
print ("\033[32;m")
os.system ("figlet Tools-Vairous 8x")
print ("   \033[31;mRoot on Termux       [1]")
print ("   Hack-Email           [2] ")
print ("   Ip-Target or DNS     [3]")
print ("   Install Tools-Termux [4]")
print ("\033[33;m")
name = input ("    Enter...")
if name=="1":
    print ("one")
    import os
    os.system ("clear")
    print ("\033[31;m")
    os.system ("figlet V8xRoot")
    print ("\033[34;m")
    print(" Root [1]")
    print (" back [99]\033[34;m")
    name = input ("Enter ...")
    if name=="99":
        import os
        os.system("python back.py")
    if name == "1":


#import os
#emprator color
        m = '\033[81;36m'#سمائي
        E = '\x1b[1;31m'#ابيض
        G = '\x1b1;32m'#ابيض
        S = '\x1b[1;33m'#اصفر
        Z = '\x1b[1;31m'#احمر
        X = '\x1b[1;33m'#اصفر
        Z1 = '\x1b[2;31m'#احمر
        F = '\x1b[2;32m'#اخضر طوخ
        A = '\x1b[2;39m'#ابيض
        C = '\x1b[2;35m'#بنفسجي
        B = '\x1b[2;36m'#اخضر
        Y = '\x1b[1;34m'#الازرق
################
        logo = '''
        ──────────────────────────────────────────────
        ─██████████████─██████████████─██████████████─
        ─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
        ─██▒▒██████▒▒██─██▒▒██████▒▒██─██▒▒██████████─
        ─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██─────────
        ─██▒▒██──██▒▒██─██▒▒██████▒▒██─██▒▒██████████─
        ─██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
        ─██▒▒██──██▒▒██─██▒▒██████▒▒██─██████████▒▒██─
        ─██▒▒██──██▒▒██─██▒▒██──██▒▒██─────────██▒▒██─
        ─██▒▒██████▒▒██─██▒▒██──██▒▒██─██████████▒▒██─
        ─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
        ─██████████████─██████──██████─██████████████─
        ──────────────────────────────────────────────'''
        os.system('clear')
        print(logo)
        print(X+'━─━─━─━─◈─━─━─━─━'*3)
        print(B+'.               #   Vairous8x  #')
        print(' ')
        print(B+'.               #  Password = Vairous8x         #')
        print(F+'━─━─━─━─◈─━─━─━─━'*3)
        print('')
        pas = input(B+'َ         pass ==> ')
        if pas == 'Vairous8x' :
            os.system('apt-get update -y')
            os.system('apt-get upgrade -y')
            os.system('pkg install proot-distro')
            os.system('proot-distro install ubuntu')
            os.system('clear')
            logoroot = '''
        ██████╗░░█████╗░░█████╗░████████
        ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
        ██████╔╝██║░░██║██║░░██║░░░██║░░░
        ██╔══██╗██║░░██║██║░░██║░░░██║░░░
        ██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░
        ╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░'''
            print(B+logoroot)
            print(X+'━─━─━─━─◈─━─━─━─━'*3)
            print(X+'━─━─━─━─◈─━─━─━─━'*3)
            print('')
            print(F+'َ             Run the root again, write it')
            print('')
            print(X+'  #         proot-distro login ubuntu  #')
            print('')
            print(X+'━─━─━─━─◈─━─━─━─━'*3+F)
            os.system('proot-distro login ubuntu')
if name=="2":
    import os
    os.system("clear")
    os.system("pkg install figlet")
    os.system("pkg install python")
    os.system("pkg install python2")
    print ("\x1b[2;31mhack-email")
    os.system("clear")
    os.system("figlet HACK-EMAIL")
    print ("\x1b[1;34mhack-email [1]")
    print ("back [99]\x1b[1;33m")
    name=input ("Enter...")
    if name == "1":
        os.system("python2 hack.py")
    if name == "99":
        import os
        os.system("python back.py")

if name=="3":
    print ("Vairous8x")
    import os
    os.system("clear")
    os.system("figlet ip-Target")
    print ("ip-Target or DNS [1]")
    print ("back [99]")
    name = input ("Enter...")
    if name=="99":
        import os
        os.system("python back.py")
    if name=="1":
        import os
        import socket
        import sys
        os.system("clear")
        os.system ("pkg install toilet -y ")
        os.system ("clear")
        os.system ("toilet -f mono12 -F gay Vairous8x")
        print ("\x1b[1;33mEnter Your Dns or Target: \x1b[1;34m")
        hostname=input()
        ip=socket.gethostbyname(hostname)
        print ("\x1b[2;31mHost Name Is : ",hostname,'/n' 'Target Ip Is',ip)



if name=="4":
    import os
    os.system("python install.py")

else:
    print (" ")