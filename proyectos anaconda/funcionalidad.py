import pandas as pd
import matplotlib.pyplot as plot
from scipy import stats
import UIgraficas as ug
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

archivo="abalone.csv"
datos=pd.read_csv(archivo)
datos.columns=["sex","length","diameter","heigth","whole heigth","shucked weight","viscera weight","shell weight","rings"]
#plot.hist(x=datos["length"])
#plot.title("Histograma de la segunda columna")
#plot.xlabel("Valor de los datos")
#plot.ylabel("Cantidad de los datos")
#plot.show()

x=0
y=""
z=""

def graficarData():
    ug.fig.clear()
    global x
    global y
    plot.subplots()
    if(x==1):
        plot.hist(datos[y])
        plot.title("Histograma de la variable "+y)
        plot.xlabel("Valor de los datos")
        ug.canvas.draw()
        ug.canvas.get_tk_widget().pack()
    elif(x==2):
        plot.boxplot(x=datos[y])
        ug.canvas.draw()
        ug.canvas.get_tk_widget().pack()
    elif(x==3):
        fig=plot.figure()
        ax=fig.add_subplot(111)
        stats.probplot(datos[y],dist=stats.norm, sparams=(6,),plot=ax)
        ug.canvas.draw()
        ug.canvas.get_tk_widget().pack()
    elif(x==4):
        plot.subplot()
        plot.scatter(datos[y],datos[z])
        ug.canvas.draw()
        ug.canvas.get_tk_widget().pack()



#plot.subplots()
#plot.boxplot(x=datos["length"])
#plot.xlabel("Valor de los datos")
#plot.ylabel("Cantidad de los datos")
#plot.show()


#fig=plot.figure()
#ax=fig.add_subplot(111)
#res=stats.probplot(datos["length"],dist=stats.norm, sparams=(6,),plot=ax)
#plot.show()


#plot.subplots()
#plot.scatter(datos["Shell weight"],datos["Shucked weight"])
#plot.show()

#matriz=datos.corr()


    