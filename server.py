import random
import socket
from _thread import start_new_thread



def fb(a):
    b=bytes()
    for i in gmap:
        b+=str(i).encode('utf-8')
    if a:
        for i in range(10):
            for i1 in range(10):
                print(gmap[i*10+i1], end=' ')
            print('/n')
    return b

def flg(i):
    if gmap[i]=='#':
        gmap[i]='f'
    elif gmap[i]=='f':
        gmap[i]='#'

def f_chk(i):
    try:
        if gmap[i]=="f": 
            return 1
        else: 
            return 0
    except IndexError:
        return 0

def restart():
    a=[]
    for i in range(100):
        a.append("#")
    b=[]
    for i in range(100):
        b.append(0)
    c=[]
    for i in range(100):
        c.append(0)
    d=[]
    for i in range(100):
        a.append(0)
    return a, b, c, d 


def opn(i):
    try:
        print(i)
        if gmap[i]=='#':
            gmap[i]=field[i];
            #if gmap[i]==0:
            #    if fopn[i-11]==0:
            #        opn(i-11)
            #        fopn[i-11]=1
            #    if fopn[i-10]==0:
            #        opn(i-10)
            #        fopn[i-10]=1
            #    if fopn[i-9]==0:
            #        opn(i-9)
            #        fopn[i-9]=1
            #    if fopn[i-1]==0:
            #        opn(i-1)
            #        fopn[i-1]=1
            #    if fopn[i+1]==0:
            #        opn(i+1)
            #        fopn[i+1]=1
            #    if fopn[i+11]==0:
            #        opn(i+11)
            #        fopn[i+11]=1
            #    if fopn[i+9]==0:
            #        opn(i+9)
            #        fopn[i+9]=1
            #    if fopn[i+10]==0:
            #        opn(i+10)
            #        fopn[i+10]=1
            if field[i]==0:
               if i%10!=0:
                   opn(i-1)
                   if i>9:
                       opn(i-11)
                   if i<90:
                       opn(i+9)
               if i%10!=9:
                   opn(i+1)
                   if i>9:
                       opn(i-9)
                   if i<90:
                       opn(i+11)
               if i>9:
                    opn(i-10)
               if i<90:
                   opn(i+10)
        elif gmap[i]!='f':
            k=0
            k+=f_chk(i-11)
            k+=f_chk(i-10)
            k+=f_chk(i-9)
            k+=f_chk(i-1)
            k+=f_chk(i+1)
            k+=f_chk(i+10)
            k+=f_chk(i+11)
            k+=f_chk(i+9)
            print(k)
            #if k==field[i]:
            #    if fopn[i-11]==0:
            #        opn(i-11)
            #        fopn[i-11]=1
            #    if fopn[i-10]==0:
            #        opn(i-10)
            #        fopn[i-10]=1
            #    if fopn[i-9]==0:
            #        opn(i-9)
            #        fopn[i-9]=1
            #    if fopn[i-1]==0:
            #        opn(i-1)
            #        fopn[i-1]=1
            #    if fopn[i+1]==0:
            #        opn(i+1)
            #        fopn[i+1]=1
            #    if fopn[i+11]==0:
            #        opn(i+11)
            #        fopn[i+11]=1
            #    if fopn[i+9]==0:
            #        opn(i+9)
            #        fopn[i+9]=1
            #    if fopn[i+10]==0:
            #        opn(i+10)
            #        fopn[i+10]=1
            #if i%10!=0:
            #    k+=f_chk(i-10)
            #    if i>9:
            #        k+=f_chk(i-11)
            #    if i<90:
            #        k+=f_chk(i+9)
            #if i%10!=9:
            #    k+=f_chk(i+1)
            #    if i>9:
            #        k+=f_chk(i-9)
            #    if i<90:
            #        k+=f_chk(i+11)
            #if i>9:
            #     k+=f_chk(i-10)
            #if i<90:
            #    k+=f_chk(i+10)
            if k==field[i]:
                if i%10!=0:
                    if fopn[i-1]==0:
                        fopn[i-1]+=1
                        opn(i-1)
                    if i>9:
                        if fopn[i-11]==0:
                            fopn[i-11]+=1
                            opn(i-11)
                    if i<90:
                        if fopn[i+9]==0:
                            fopn[i+9]+=1
                            opn(i+9)
                if i%10!=9:
                    if fopn[i+1]==0:
                        fopn[i+1]+=1
                        opn(i+1)
                    if i>9:
                        if fopn[i-9]==0:
                            fopn[i-9]+=1
                            opn(i-9)
                    if i<90:
                        if fopn[i+11]==0:
                            fopn[i+11]+=1
                            opn(i+11)
                if i>9:
                    if fopn[i-10]==0:
                        fopn[i-10]+=1
                        opn(i-10)
                if i<90:
                    if fopn[i+10]==0:
                        fopn[i+10]+=1
                        opn(i+10)
    except IndexError:
        pass
def client_thread (conn):
    try:
        a=1
        #conn.sendall(fb()) 
        data = conn.recv(1024)           
        d = data.decode()
        if d[0]=="o":
           opn(int(d[1:3]))
        if d[0]=="f":
            flg(int(d[1:3]))
        if d[0]=="a":
            a=0
        #if d[0] =="r":
            #gmap, mines, field, fopn = restart()
        conn.sendall(fb(a))      
        conn.close()
    except ConnectionResetError:
        pass                     


gmap=[]
for i in range(100):
    gmap.append("#")
mines=[]
for i in range(100):
    mines.append(0)
field=[]
for i in range(100):
    field.append(0)
fopn=[]
for i in range(100):
    fopn.append(0)

for i in range(100):
    if random.randint(1, 5)==3:
        mines[i]=1;

for i in range(100):
    k=0
    if i%10!=0:
        k+=mines[i-1]
        if i>9:
            k+=mines[i-11]
        if i<90:
            k+=mines[i+9]
    if i%10!=9:
        k+=mines[i+1]
        if i>9:
            k+=mines[i-9]
        if i<90:
            k+=mines[i+11]
    if i>9:
         k+=mines[i-10]
    if i<90:
        k+=mines[i+10]
    if mines[i]:
        k=9
    field[i]=k


server = socket.socket()            
hostname = input('ip > ')    
port = int(input('port > '))                        
server.bind((hostname, port))       
server.listen(2)                    
 
print(f"{hostname}:{port}")
while True:
    client, _ = server.accept()
    start_new_thread(client_thread, (client, ))
    for i in range(100):
        if mines[i]==1:
            if gmap[i]!='f':
                break
        if i==99:
            gmap=[]
            for i in range(100):
                gmap.append("#")
            mines=[]
            for i in range(100):
                mines.append(0)
            field=[]
            for i in range(100):
                field.append(0)
            fopn=[]
            for i in range(100):
                fopn.append(0)
            for i in range(100):
                if random.randint(1, 5)==3:
                    mines[i]=1;

            for i in range(100):
                k=0
                if i%10!=0:
                    k+=mines[i-1]
                    if i>9:
                        k+=mines[i-11]
                    if i<90:
                        k+=mines[i+9]
                if i%10!=9:
                    k+=mines[i+1]
                    if i>9:
                        k+=mines[i-9]
                    if i<90:
                        k+=mines[i+11]
                if i>9:
                     k+=mines[i-10]
                if i<90:
                    k+=mines[i+10]
                if mines[i]:
                    k=9
                field[i]=k 
        if gmap[i]==9:
            gmap=[]
            for i in range(100):
                gmap.append("#")
            mines=[]
            for i in range(100):
                mines.append(0)
            field=[]
            for i in range(100):
                field.append(0)
            fopn=[]
            for i in range(100):
                fopn.append(0)
            for i in range(100):
                k=0
                if i%10!=0:
                    k+=mines[i-1]
                    if i>9:
                        k+=mines[i-11]
                    if i<90:
                        k+=mines[i+9]
                if i%10!=9:
                    k+=mines[i+1]
                    if i>9:
                        k+=mines[i-9]
                    if i<90:
                        k+=mines[i+11]
                if i>9:
                     k+=mines[i-10]
                if i<90:
                    k+=mines[i+10]
                if mines[i]:
                    k=9
                field[i]=k 

            
