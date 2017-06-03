import turtle as t
import tkinter as tk
import os

master = t.getcanvas().master

n_val = tk.IntVar(value=1)
n_str_val = tk.StringVar(value="1")
l_val = tk.DoubleVar(value=1)
alpha_val = tk.IntVar(value=1)
init_val = tk.StringVar(value="A")
replace_val = tk.StringVar(value="A")

def var_init():
    n_val.set(2)
    n_str_val.set("5")
    n_val.set(5)
    l_val.set(1)
    alpha_val.set(60)
    init_val.set("AddAddA")
    replace_val.set("AgAddAgA")

class Param(tk.Toplevel):
    def __init__(self, parent=master):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        
        self.init()

    def init(self):
        self.config(padx=10, pady=10)
        self.title="Paramètres"

        #On crée les boutons de sortie et de sauvegarde
        self.exit_button = tk.Button(self, text="Quitter",bg="White",command=self.destroy)
        self.save_button = tk.Button(self, text="Sauvegarder",bg="White", command=self.reload)
        
        #On crée le Spinbox pour entrer la valeur de n
        self.labeln = tk.Label(self, text="Nombre d'itérations")
        self.n_sel = tk.Spinbox(self, from_=1, to=10, textvariable=n_str_val)
        
        #On crée le Scale pour entrer la valeur de l
        self.labell = tk.Label(self, text="Longueur du trait")
        self.l_sel = tk.Scale(self,orient="horizontal", from_=0, to=100,tickinterval=25,length=200, resolution=0.1, variable=l_val)
        
        #on crée le Scale pour entrer la valeur d'alpha
        self.labelalpha = tk.Label(self, text="Angle de rotation (°)")
        self.alpha_sel = tk.Scale(self, orient="horizontal",from_=0, to=360, tickinterval = 60, resolution=1, length=200, variable=alpha_val)
        
        #On crée les champs d'entrée de la règle de création
        self.label_init = tk.Label(self, text="Règle initiale (A,g,d uniquement)")
        self.init_sel = tk.Entry(self, textvariable=init_val)
        self.label_replace = tk.Label(self, text="Règle de remplacement (A,g,d uniquement)")
        self.replace_sel = tk.Entry(self, textvariable=replace_val)

        #Affichage des objets sur la fenêtre
        self.exit_button.pack(side="right",anchor="s",padx=10,pady=10)
        self.save_button.pack(side="left",anchor="s",padx=10,pady=10)
        self.labeln.pack()
        self.n_sel.pack()
        self.labell.pack()
        self.l_sel.pack()
        self.labelalpha.pack()
        self.alpha_sel.pack()
        self.label_init.pack()
        self.init_sel.pack()
        self.label_replace.pack()
        self.replace_sel.pack()
        

    def reload(self):
        t.clearscreen()
        t.resetscreen()
        t_draw(int(n_str_val.get()), alpha_val.get(), l_val.get(), init_val.get(), replace_val.get())




def param():
    param = Param()

def main_win():
    menubar = tk.Menu(master)

    menu1 = tk.Menu(menubar,tearoff=0)
    menu1.add_command(label="Nouveau", command=new)
    menu1.add_command(label="Sauvegarder",command=save)
    menu1.add_command(label="Charger",command=load)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=master.destroy)
    menubar.add_cascade(label="Fichier", menu=menu1)

    menu2 = tk.Menu(menubar, tearoff=0)
    menu2.add_command(label="Paramètres",command=param)
    menubar.add_cascade(label="Éditer", menu=menu2)

    master.config(menu=menubar)

def t_init():
    t.title("Fractal Maker")
    t.screensize(10000,10000)
    t.ScrolledCanvas(master)
    

    t.delay(0)
    t.pu()
    t.setpos(-100,0)
    t.pd()

    t.color('red','yellow')
    t.speed(0)


def t_draw(n, alpha, l, init, replace):
    index=[]
    i=0
    inst=init
    t_init()
    
    while i<n:
        index=inst.split('A')
        inst = replace.join(index)
        i+=1

    inst= "A".join(index)

    for letter in inst:
        if letter == 'A':
            t.forward(l)
        elif letter == 'g':
            t.left(alpha)
        elif letter == 'd':
            t.right(alpha)

def new():
    alert= tk.messagebox.askokcancel(title="Nouveau fichier", message="Voulez-vous créer un nouveau fichier ?\nLa configuration actuelle sera perdue")
    
    if alert==True:
        t.clearscreen()
        t.resetscreen()
        var_init()
        t_draw(int(n_str_val.get()), alpha_val.get(), l_val.get(), init_val.get(), replace_val.get())


def save():
    path=tk.filedialog.asksaveasfilename(defaultextension=".frmk", filetypes=[("FRMK","*.frmk")], initialdir="Fractals" ,initialfile="My_Awesome_Fractal", title="Sauvegarder")
    
    if path!="":
        file = open(path, "w")
        write = n_str_val.get()+"\n"+str(alpha_val.get())+"\n"+str(l_val.get())+"\n"+str(init_val.get())+"\n"+str(replace_val.get())
        file.write(write)
        file.close()

def load():
    path=tk.filedialog.askopenfilename(defaultextension=".frmk", filetypes=[("FRMK","*.frmk")], initialdir="Fractals", title="Charger")
    if path!="":
        file = open(path, "r")
        read_i = file.read().split("\n")
        n_str_val.set(read_i[0])
        alpha_val.set(int(read_i[1]))
        l_val.set(float(read_i[2]))
        init_val.set(read_i[3])
        replace_val.set(read_i[4])
        file.close()

        t.clearscreen()
        t.resetscreen()
        t_draw(int(n_str_val.get()), alpha_val.get(), l_val.get(), init_val.get(), replace_val.get())


main_win()
var_init()
t_init()
t_draw(int(n_str_val.get()), alpha_val.get(), l_val.get(),init_val.get(), replace_val.get())

