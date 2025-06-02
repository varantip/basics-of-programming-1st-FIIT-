from functions import *

if __name__ == "__main__":
    #читаем данные по х
    x_data = read_file('data/xc.dat')
    
    for file in os.listdir('data'):
        if file.startswith('yc-') and file.endswith('.dat'):
            y_data = read_file(f'data/{file}')
            
            #вычисление данных
            statistics = calculate_stats(y_data)
            derivative = calculate_derivative(x_data, y_data)
            integral = calculate_integral(x_data, y_data)
            
            save_results('results', f'data/{file}', statistics, derivative, integral)