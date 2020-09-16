import pysftp
import threading
import time, sys
import os
import webbrowser

host = ""
username = "****"
password = "****"
remote_path = ""
local_path = "" 
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


def connectionFTP(host,username,passowrd,cnopts):
    return pysftp.Connection(host, username=username,password=password,cnopts=cnopts);

def ftpLoja(host):

    host = 'qql'+f'{loja:03}'+'00.qq';  
    try: 
        sftp = connectionFTP(host,username,password,cnopts);
        with sftp:
           with sftp.cd("/Moodle"):
                if sftp.lexists("/Moodle/cob/") :
                   sftp.put('arquivos/'+f'{loja}.pdf','/Moodle/cob/teste.pdf')
                else :
                   sftp.mkdir('cob')
                   sftp.put('arquivos/'+f'{loja}.pdf','/Moodle/cob/teste.pdf')
                
                
            
    except:
        print("Erro: ->>>> "+str(loja)+" <<<<-         host: "+host)
    else:
        print("Succeso: ->>>> "+str(loja)+" <<<<-         host: "+host)

if __name__ == '__main__':

    files = os.listdir('arquivos_loja/');
    
    for filename in files :
        host = int(filename.split('.')[0]);
        threading.Thread(target=ftpLoja,args=[loja]).start()

        #//teste via toolkit
        #host = 'qql'+f'{host:03}'+'00.qq';   
        #webbrowser.open('http://'+f'{host}'+'/cob/carta.pdf', autoraise=True)
     
   
