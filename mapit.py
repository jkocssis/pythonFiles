#! python3
# mapit.py 
import webbrowser,sys,pyperclip
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) 
else:
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)



''' webbrowser.open('http://inventwithpython.com/')
webbrowser.open('http://siga.cps.sp.gov.br/aluno/') '''