H='Find and replace'
A=False
import npyscreen as B,os,argparse as I,signal as C
def D(file):
	with open(file,'r')as A:return A.read()
def E(file,text):
	with open(file,'w')as A:A.write(text)
F=I.ArgumentParser(prog='context',description='Edit files in your console.',epilog='(c) 2025 AzureTecDevs  |  Updated: 1-1-2025')
F.add_argument('--file','-f',help='file to open by default')
G=F.parse_args()
def handler(signum,frame):exit(code=0)
C.signal(C.SIGINT,handler)
def J(message,title='Message',form_color='STANDOUT',wide=A):
	E=form_color;D=title;C=message;C=B.utilNotify._prepare_message(C)
	if wide:A=B.utilNotify.fmPopup.PopupWide(name=D,color=E)
	else:A=B.utilNotify.fmPopup.Popup(name=D,color=E)
	F=A.add(B.TitleText,name='Replace:',value='');G=A.add(B.TitleText,name='With:',value='');A.edit();return[F.value,G.value]
class K(B.FormBaseNewWithMenus):
	def create(A):
		A.title=A.add(B.FixedText,value='new',color='LABEL');A.menu1=A.new_menu('Menu');A.editor=A.add(B.MultiLineEdit,value='');A.menu1.addItem('Open',onSelect=A.spawn_file_dialog,shortcut='^O');A.menu1.addItem('Save as',onSelect=A.spawn_file_dialog_save,shortcut='^N');A.menu1.addItem('Save',onSelect=A.spawn_file_dialog_savecur,shortcut='^S');A.menu1.addItem(H,onSelect=A.frep,shortcut='^F');A.menu1.addItem('Quit',onSelect=A.exitg,shortcut='^C');A.menu1.addItem('Close menu')
		if not G.file==None:A.open_file(G.file)
	def exitg(A):print('Exit');exit(code=0)
	def spawn_file_dialog(C):E=B.selectFile(confirm_if_exists=A);C.editor.value=D(E);C.title.value=E
	def frep(A):B=J('',title=H);A.editor.value=A.editor.value.replace(B[0],B[1])
	def open_file(A,file):B=os.path.abspath(file);A.editor.value=D(B);A.title.value=B
	def spawn_file_dialog_save(C):D=B.selectFile(confirm_if_exists=A);E(D,C.editor.value);C.title.value=D
	def spawn_file_dialog_savecur(A):E(A.title.value,A.editor.value)
class L(B.NPSAppManaged):
	def onStart(A):A.addForm('MAIN',K,name='conText 0.1.0')
if __name__=='__main__':M=L().run()