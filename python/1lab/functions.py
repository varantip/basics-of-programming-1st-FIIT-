import numpy as np
import os

#1. чтение файла
def read_file(filename, method='np.loadtxt'):
    #читает файл с числами, возвращает список чисел
    if method == 'open':
        with open(filename, 'r') as f:
            return [float(line.strip()) for line in f]
    else:  #метод numpy по умолчанию
        return np.loadtxt(filename)

#2. расчет стат. показателей (среднее, максимум, минимум)
def calculate_stats(y):
    return {
        'mean': np.mean(y),  #среднее значение
        'max': np.max(y),    #максимальное
        'min': np.min(y)     #минимальное
    }

#3. расчет производной
def calculate_derivative(x, y):
    #пр-я в каждой точке
    return np.gradient(y, x)  

#4. расчет интеграла методом прямоугольников
def calculate_integral(x, y):
    total = 0
    for i in range(len(x)-1):
        width = x[i+1] - x[i]  #ширина прямоугольника
        height = y[i]          #высота прямоугольника
        total += width * height #площадь + к сумме
    return total

#5. сохранение результатов в файл
def save_results(out_folder, original_file, stats, derivative, integral):
    # Создаем папку, если её нет
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    
    #имя нового файла (добавляем out_ к исходному имени)
    new_filename = f"out_{os.path.basename(original_file)}"
    full_path = os.path.join(out_folder, new_filename)
    
    #запись данных в новый файл (все на англ, потому что utf-8 настраивать лень)
    with open(full_path, 'w') as f:
        f.write(f"Original file: {original_file}\n\n")
        f.write("Statistics:\n")
        f.write(f"Average: {stats['mean']:.3f}\n")
        f.write(f"Maximum: {stats['max']:.3f}\n")
        f.write(f"Minimum: {stats['min']:.3f}\n\n")
        f.write("Derivative:\n")
        np.savetxt(f, derivative, fmt='%.3f')  #записываем массив
        f.write(f"\nIntegral: {integral:.3f}\n")
    
    print(f"File {new_filename} save is succesfull!")