import tkinter as tk


def suma():
    valor1 = entrada_1.
    valor2= entrada_2.__getattribute__()
    suma = valor1+valor2
    tk.Label(main,f"el valor de la suma es --> {suma}")


main=tk.Tk()
main.title("Hola mundo")

etiqueta_1 = tk.Label(main,text="Vamos a sumar 2 numeros")
etiqueta_1.grid(column=0,row=0)
entrada_1= tk.Entry(main,"").grid(column=0,row=1)

entrada_2= tk.Entry(main).grid(column=0,row=2)

boton_suma = tk.Button(main,text="SUMA", command=suma).grid(column=0,row=3)



main.mainloop()