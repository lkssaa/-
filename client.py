import customtkinter
import socket

hostname, port = '', 0

def connect():
    global hostname, port
    hostname, port = entry.get(), int(entry2.get())
    app.quit()

app = customtkinter.CTk()
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")
app.geometry("400x150")
frame = customtkinter.CTkFrame(master=app, width=400, height=100)
frame.grid(row=0, column=0) 
entry = customtkinter.CTkEntry(master=frame, placeholder_text="IP", width=300, text_color="#556B2F")

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="PORT", width=300, text_color="#556B2F")

entry.grid(row=0, column=0, padx=50, pady=10) 
entry2.grid(row=1, column=0, padx=50, pady=10) 

conn_b=customtkinter.CTkButton(master=app, text = 'connect', command=connect, width=380, height=50, hover_color='#556B2F', corner_radius=0)
conn_b.grid(row = 1, column = 0)

app.mainloop()
print(hostname, port)
print('aaaaaaaaaaaaa')

mess_b=[0,1]

#hostname = "127.0.0.1"
#port = 11111


b=[]

for i in range(100):
    b.append([[0, 1], [0, 1]])

def snd(a):
    client = socket.socket()                    
    client.connect((hostname, port))
    client.send(a.encode())      
    data = client.recv(1024)
    client.close()
    return data.decode() 

def f_bind(event, s):
    b[s][1].reverse()
    #j="button%s['bg'] = 'gray'" %(s)
    #exec(j)

    



def dmap():
    #if mess_b[0]:
    #    snd('r')
    #    mess_b.reverse()
    mess='a'
    for i in range(100):
        if b[i][0][0]:
            mess='o'+str(i)
            b[i][0].reverse()
            break
        if b[i][1][0]:
            mess='f'+str(i)
            b[i][1].reverse()
            break
    rec_m=snd(mess)
    for i in range(100):
        if rec_m[i]=='#':
            exec("button%s.configure(text='%s')" % (i,'|||||||'))
        elif rec_m[i]=='f':
            exec("button%s.configure(text='%s')" % (i,'flag')) 
        elif rec_m[i]=='9':
            exec("button%s.configure(text='%s')" % (i,'<+>')) 
        else:
            exec("button%s.configure(text='%s')" % (i, rec_m[i]))
    app.after(100, dmap)


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


app = customtkinter.CTk()
app.geometry("700*700")
frame = customtkinter.CTkFrame(master=app, width=500, height=500)
frame.grid(row=0, column=0, padx=5, pady=5)
bl=[]
for i in range(100):
    k = "button%s = customtkinter.CTkButton(master=frame, text = '%s', command=b[%s][0].reverse, width=50, height=50, hover_color='#20B2AA', corner_radius=0)" % (i, "#", i)
    k1 = "button%s.grid(row=%s, column=%s)" % (i, i//10, i%10)
    k2 = """button%s.bind('<Button-3>', 
    lambda e, f=%s: f_bind(e, f))""" % (i, i) 
    bl.append(k)
    bl.append(k1)
    bl.append(k2)
for i in bl:
    exec(i)
#r_button = customtkinter.CTkButton(master=app, text = 'restart', command=mess_b.reverse, width=500, height=30, hover_color='#20B2AA', corner_radius=0)
#r_button.grid(row=1, column=0, padx=5, pady=5)
dmap()

app.mainloop()
print(b)







