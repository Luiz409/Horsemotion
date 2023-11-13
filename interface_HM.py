import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

path = 'dados.txt'

data = np.loadtxt(path, delimiter=",")

acel_x = data[:,0]
acel_y = data[:,1]
acel_z = data[:,2]

giro_x = data[:,3]
giro_y = data[:,4]
giro_z = data[:,5]

rate = 10
mode = 'same'

acel_x = np.convolve(acel_x, np.ones((rate,))/rate, mode=mode)
acel_y = np.convolve(acel_y, np.ones((rate,))/rate, mode=mode)
acel_z = np.convolve(acel_z, np.ones((rate,))/rate, mode=mode)

giro_x = np.convolve(giro_x, np.ones((rate,))/rate, mode=mode)
giro_y = np.convolve(giro_y, np.ones((rate,))/rate, mode=mode)
giro_z = np.convolve(giro_z, np.ones((rate,))/rate, mode=mode)

def plot_graph(arr):
    plt.plot(arr)
    plt.show()

def plot_3d(arr1, arr2, arr3):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(arr1,arr2,arr3, c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def generate_analysis():
    meanAx = round(np.mean(acel_x), 3)
    meanAy = round(np.mean(acel_y), 3)
    meanAz = round(np.mean(acel_z), 3)

    meanGx = round(np.mean(giro_x), 3)
    meanGy = round(np.mean(giro_y), 3)
    meanGz = round(np.mean(giro_z), 3)
    
    label_rax.config(text=meanAx)
    label_ray.config(text=meanAy)
    label_raz.config(text=meanAz)

    label_rgx.config(text=meanGx)
    label_rgy.config(text=meanGy)
    label_rgz.config(text=meanGz)

# Cria uma win
win = tk.Tk()
win.title("Horse motion analysis")

win.geometry("600x650")

# Cria rótulos e botões para aceleração
label_ax = tk.Label(win, text="Aceleração em X (m/s²):")
label_ax.grid(row=0, column=0, padx=10, pady=10)

botton_ax = tk.Button(win, text="Gerar gráfico", command=lambda:plot_graph(acel_x))
botton_ax.grid(row=1, column=0, padx=10, pady=10)  

label_ay = tk.Label(win, text="Aceleração em Y (m/s²):")
label_ay.grid(row=2, column=0, padx=10, pady=10)

botton_ay = tk.Button(win, text="Gerar gráfico", command=lambda:plot_graph(acel_y))
botton_ay.grid(row=3, column=0, padx=10, pady=10)

label_az = tk.Label(win, text="Aceleração em Z (m/s²):")
label_az.grid(row=4, column=0, padx=10, pady=10)

botton_az = tk.Button(win, text="Gerar gráfico", command=lambda:plot_graph(acel_z))
botton_az.grid(row=5, column=0, padx=10, pady=10)

label_gx = tk.Label(win, text="Giroscópio em X (º/s):")
label_gx.grid(row=0, column=2, padx=10, pady=10)

botton_gx = tk.Button(win, text="Gerar gráfico", command=lambda:plot_graph(giro_x))
botton_gx.grid(row=1, column=2, padx=10, pady=10)

label_gy = tk.Label(win, text="Giroscópio em Y (º/s):")
label_gy.grid(row=2, column=2, padx=10, pady=10)

botton_gy = tk.Button(win, text="Gerar gráfico", command=lambda:plot_graph(giro_y))
botton_gy.grid(row=3, column=2, padx=10, pady=10)

label_gz = tk.Label(win, text="Giroscópio em Z (º/s):")
label_gz.grid(row=4, column=2, padx=10, pady=10)

botton_gz = tk.Button(win, text="Gerar gráfico", command=lambda:plot_graph(giro_z))
botton_gz.grid(row=5, column=2, padx=10, pady=10)

label_3da = tk.Label(win, text="Gerar gráfico 3D da Aceleração:")
label_3da.grid(row=6, column=0, padx=10, pady=10)

botton_3da = tk.Button(win, text="Gerar gráfico", command=lambda:plot_3d(acel_x, acel_y, acel_z))
botton_3da.grid(row=7, column=0, padx=10, pady=10)

label_3dg = tk.Label(win, text="Gerar gráfico 3D do Giroscópio:")
label_3dg.grid(row=6, column=2, padx=10, pady=10)

botton_3dg = tk.Button(win, text="Gerar gráfico", command=lambda:plot_3d(giro_x, giro_y, giro_z))
botton_3dg.grid(row=7, column=2, padx=10, pady=10)

label_gr = tk.Label(win, text="Gerar análise:")
label_gr.grid(row=9, column=1, padx=10, pady=10)

botton_gr = tk.Button(win, text="Gerar", command=lambda:generate_analysis())
botton_gr.grid(row=10, column=1, padx=10, pady=10)

label_dax = tk.Label(win, text="Valor médio da aceleração em X:")
label_dax.grid(row=11, column=0, padx=10, pady=0)

label_rax = tk.Label(win, text="(__)")
label_rax.grid(row=12, column=0, padx=10, pady=0)

label_day = tk.Label(win, text="Valor médio da aceleração em Y:")
label_day.grid(row=11, column=1, padx=10, pady=0)

label_ray = tk.Label(win, text="(__)")
label_ray.grid(row=12, column=1, padx=10, pady=0)

label_daz = tk.Label(win, text="Valor médio da aceleração em Z:")
label_daz.grid(row=11, column=2, padx=10, pady=0)

label_raz = tk.Label(win, text="(__)")
label_raz.grid(row=12, column=2, padx=10, pady=0)

label_dgx = tk.Label(win, text="Valor médio do giroscópio em X:")
label_dgx.grid(row=13, column=0, padx=10, pady=0)

label_rgx = tk.Label(win, text="(__)")
label_rgx.grid(row=14, column=0, padx=10, pady=0)

label_dgy = tk.Label(win, text="Valor médio do giroscópio em Y:")
label_dgy.grid(row=13, column=1, padx=10, pady=0)

label_rgy = tk.Label(win, text="(__)")
label_rgy.grid(row=14, column=1, padx=10, pady=0)

label_dgz = tk.Label(win, text="Valor médio do giroscópio em Z:")
label_dgz.grid(row=13, column=2, padx=10, pady=0)

label_rgz = tk.Label(win, text="(__)")
label_rgz.grid(row=14, column=2, padx=10, pady=0)

def main():
    win.mainloop()
    win.deiconify()

if __name__ == "__main__":
    main()
