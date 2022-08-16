import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pandas as pd
import matplotlib.pyplot as plot
from scipy import stats
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import numpy as np
from statistics import mode
from scipy.stats import kurtosis
from scipy import stats

#Funcionalidad de la aplicacion
###############################################################################
archivo="abalone.csv"
datos=pd.read_csv(archivo)
datos.columns=["sex","length","diameter","heigth","whole heigth","shucked weight","viscera weight","shell weight","rings"]

#variables globales
x=0
y=""
z=""
a=0
moda=0
media=0
mediana=0
simetria=0
ckurtosis=0


#ventana master
ventana=tk.Tk()
ventana.geometry("1020x1020")
ventana.title("Graficador")
vcheck=tk.IntVar()

fig = Figure(figsize=(5, 5),dpi=100)
canvas = FigureCanvasTkAgg(fig, master=ventana)

def conseguirAlfa():
    global a
    a=float(txt1.get())
    print(a)
    
def resolverAtipicos(datos,a,DF):
    D=DF
    #si la version 1.2 o en adelante utilizar method en vez de interpolation
    Q1=np.percentile(D[datos], 25, method = 'midpoint')
    Q3=np.percentile(D[datos], 75, method = 'midpoint')
    IQR=Q3-Q1
    
    lsuperior = np.where(DF[datos] >= (Q3 + a * IQR))
    linferior = np.where(DF[datos] <= (Q1 - a * IQR))
    
    D.drop(lsuperior[0], inplace = True)
    D.drop(linferior[0], inplace = True)
    return D

def graficarData():
    copiaDatos=datos.copy()
    global a
    global fig 
    global x
    global y
    global z
    global moda
    global media
    global mediana
    global simetria
    global kurtosis
    fig.clear()
    
    if(a!=0):
        copiaDatos=resolverAtipicos(y, a, copiaDatos)
        
        if(z!=""):
            copiaDatos=resolverAtipicos(z, a, copiaDatos)
    
    if(x==1):
        plot = fig.add_subplot(111)
        plot.hist(copiaDatos[y])
        canvas.draw()
        canvas.get_tk_widget().place(x=400, y=50)
        moda = mode(copiaDatos[y])
        mediana = copiaDatos[y].median()
        simetria = copiaDatos[y].skew()
        media = copiaDatos[y].mean()
        ckurtosis = copiaDatos[y].kurtosis()

        lbl6.config(text="Moda: " + str(moda))
        lbl6.place(x=400, y=550)
        lbl7.config(text="Mediana: " + str(mediana))
        lbl7.place(x=400, y=570)
        lbl8.config(text="Media: " + str(media))
        lbl8.place(x=400, y=590)
        lbl9.config(text="Asimetria: " + str(simetria))
        lbl9.place(x=400, y=610)
        lbl10.config(text="Kurtosis: " + str(ckurtosis))
        lbl10.place(x=400, y=630)

    elif(x==2):
        plot = fig.add_subplot(111)
        plot.boxplot(x=copiaDatos[y])
        canvas.draw()
        canvas.get_tk_widget().place(x=400, y=50)
        moda = mode(copiaDatos[y])
        mediana = copiaDatos[y].median()
        simetria = copiaDatos[y].skew()
        media = copiaDatos[y].mean()
        ckurtosis = copiaDatos[y].kurtosis()

        lbl6.config(text="Moda: " + str(moda))
        lbl6.place(x=400, y=550)
        lbl7.config(text="Mediana: " + str(mediana))
        lbl7.place(x=400, y=570)
        lbl8.config(text="Media: " + str(media))
        lbl8.place(x=400, y=590)
        lbl9.config(text="Asimetria: " + str(simetria))
        lbl9.place(x=400, y=610)
        lbl10.config(text="Kurtosis: " + str(ckurtosis))
        lbl10.place(x=400, y=630)

    elif(x==3):
        ax = fig.add_subplot(111)
        stats.probplot(copiaDatos[y],dist=stats.norm, sparams=(6,),plot=ax)
        canvas.draw()
        canvas.get_tk_widget().place(x=400, y=50)
        moda = mode(copiaDatos[y])
        mediana = copiaDatos[y].median()
        simetria = copiaDatos[y].skew()
        media = copiaDatos[y].mean()
        ckurtosis = copiaDatos[y].kurtosis()

        lbl6.config(text="Moda: " + str(moda))
        lbl6.place(x=400, y=550)
        lbl7.config(text="Mediana: " + str(mediana))
        lbl7.place(x=400, y=570)
        lbl8.config(text="Media: " + str(media))
        lbl8.place(x=400, y=590)
        lbl9.config(text="Asimetria: " + str(simetria))
        lbl9.place(x=400, y=610)
        lbl10.config(text="Kurtosis: " + str(ckurtosis))
        lbl10.place(x=400, y=630)

    elif(x==4):
        if(y!=z):
            try:
                plot = fig.add_subplot(111)
                plot.scatter(copiaDatos[y],copiaDatos[z])
                canvas.draw()
                canvas.get_tk_widget().place(x=400, y=50)
                moda = mode(copiaDatos[y])
                mediana = copiaDatos[y].median()
                simetria = copiaDatos[y].skew()
                media = copiaDatos[y].mean()
                ckurtosis = copiaDatos[y].kurtosis()

                lbl6.config(text="Moda: " + str(moda))
                lbl6.place(x=400, y=550)
                lbl7.config(text="Mediana: " + str(mediana))
                lbl7.place(x=400, y=570)
                lbl8.config(text="Media: " + str(media))
                lbl8.place(x=400, y=590)
                lbl9.config(text="Asimetria: " + str(simetria))
                lbl9.place(x=400, y=610)
                lbl10.config(text="Kurtosis: " + str(ckurtosis))
                lbl10.place(x=400, y=630)
            except:
                print("hola")
                tkinter.messagebox.showinfo("Error al graficar","NO se puede hacer un diagrama con 2 variables que no presentan la misma cantidad de densidad")
        else:
            tkinter.messagebox.showinfo("Error al graficar",
                                        "NO se puede hacer un diagrama con 2 variables que sean iguales")

def capturadorEventox(event):
    global x
    if(combo1.get()=="Histograma"):       
        combo3.place_forget()
        x=1

    elif(combo1.get()=="Cajas y vigotes"):      
        combo3.place_forget()
        x=2

    elif(combo1.get()=="Normal"):   
        combo3.place_forget()
        x=3

    elif(combo1.get()=="Dispercion"):
        combo3.place(x=240,y=150,width=100,height=30)
        x=4

def capturadorEventoy(event):
    global y
    y=combo2.get()

    
def capturadorEventoz(event):
    global z
    z=combo3.get()

def checkAT():
    global atipicos
    global a
    if(vcheck.get()==1):
        txt1.place(x=70, y=350, width=100, height=30)
        btn2.place(x=70, y=400, width=100, height=30)
        lbl4.place(x=20, y=320, width=200, height=30)

    elif(vcheck.get()==0):
        txt1.place_forget()
        btn2.place_forget()
        lbl4.place_forget()
        a=0

#Diseño UI de la aplicacion
###############################################################################
fig = Figure(figsize=(5, 5),dpi=100)
canvas = FigureCanvasTkAgg(fig,master=ventana)

lbl1=tk.Label(ventana, text="Graficador", font=(50))
lbl1.place(x=10,y=40,width=100,height=30)

lbl2=tk.Label(ventana, text="Tipo de grafica")
lbl2.place(x=10,y=120,width=100,height=30)

lbl3=tk.Label(ventana, text="Datos")
lbl3.place(x=130,y=120,width=100,height=30)

lbl4=tk.Label(ventana, text="Digitar valor")


lbl5=ttk.Checkbutton(ventana,text="Resolver datos atipicos",command=checkAT,variable=vcheck,onvalue=1,offvalue=0)
lbl5.place(x=10,y=280,width=140,height=30)

lbl6=tk.Label(ventana, text="")
lbl7=tk.Label(ventana, text="")
lbl8=tk.Label(ventana, text="")
lbl9=tk.Label(ventana, text="")
lbl10=tk.Label(ventana, text="")

combo1=ttk.Combobox(ventana)
combo1.place(x=10,y=150,width=100,height=30)
combo1["values"]=("Histograma", "Cajas y vigotes", "Normal", "Dispercion")

combo2=ttk.Combobox(ventana)
combo2.place(x=130,y=150,width=100,height=30)
combo2["values"]=("length","diameter","heigth","whole heigth","shucked weight","viscera weight","shell weight","rings")

combo3=ttk.Combobox(ventana)
combo3.place(x=240,y=150,width=100,height=30)
combo3["values"]=("length","diameter","heigth","whole heigth","shucked weight","viscera weight","shell weight","rings")
combo3.place_forget()

txt1=tk.Entry(ventana)

btn3=tk.Button(ventana, text="Graficar", command=graficarData)
btn3.place(x=70,y=220,width=100,height=30)

btn2=tk.Button(ventana, text="Resolver atipicos", command=conseguirAlfa)


combo1.bind("<<ComboboxSelected>>",capturadorEventox)
combo2.bind("<<ComboboxSelected>>",capturadorEventoy)
combo3.bind("<<ComboboxSelected>>",capturadorEventoz)

ventana.mainloop()

