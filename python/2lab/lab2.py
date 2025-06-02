import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


df = pd.read_csv('company_sales_data.csv', sep = ',')
column_list = df.columns
sales_columns = df.columns[1:-1]
#1-2 задание
plt.xlabel('Month number')
plt.ylabel('Total units')
plt.title('Company Sales Data of last year')
plt.plot(df[column_list[0]], df[column_list[-1]], 
         lw = 3, color = 'red', ls = '--', marker = 'o', markerfacecolor = 'black', label = 'Profit data of last year')
plt.legend(loc='lower right', bbox_to_anchor=(1, 0)) #коор-ы отн-о фигуры, а не осей
plt.grid(ls = ':', lw = 0.7)
plt.show()

#3 задание
y1 = df[column_list[1]]
x = df[column_list[0]]
y2 = df[column_list[2]]
y3 = df[column_list[3]]
y4 = df[column_list[4]]
y5 = df[column_list[5]]
plt.plot(x, y1, marker = 'o', lw = 3, label = 'facecream sales data')
plt.plot(x, y2, marker = 'o', lw = 3, label = 'facewash sales data')
plt.plot(x, y3, marker = 'o', lw = 3, label = 'toothpaste sales data')
plt.plot(x, y4, marker = 'o', lw = 3, label = 'bathing soap sales data')
plt.plot(x, y5, marker = 'o', lw = 3, label = 'shampoo sales data')
plt.legend(loc = 'upper left')
plt.show()

fig, axs = plt.subplots(5)
axs[0].plot(x, y1, marker = '.', label = 'facecream', color = '#b00000', lw = 2)
axs[1].plot(x, y2, color = '#b02323', lw = 2)
axs[2].plot(x, y3, color = '#b04646', lw = 2)
axs[3].plot(x, y4, color = '#b06a6a', lw = 2)
axs[4].plot(x, y5, color = '#b08d8d', lw = 2) #а можно через for чтобы индексы счтались и доставались нужные надписи??
plt.show()

# #4 задание
plt.scatter(df['month_number'], df['toothpaste'], marker='o')
plt.xticks(np.arange(min(df['month_number']), max(df['month_number'])+1, 1.0))
plt.xlabel('Month')
plt.ylabel('Number of units sold')
plt.title('Tooth paste Sales data')
plt.legend(['Tooth paste sales data'], loc=0)
plt.grid( linestyle='--')
plt.show()

# #5 задание
face_cream = df['facecream']
face_wash = df['facewash']
width = 0.3
x = df['month_number']
plt.xticks(np.arange(min(df['month_number']), max(df['month_number'])+1, 1.0))
plt.bar(x-0.3/2, face_cream, width)
plt.bar(x+0.3/2, face_wash, width)
plt.grid(linestyle="--")
plt.legend(["Face cream sales data","Face wash cales data"])
plt.xlabel('Month')
plt.ylabel('Sales units in number')
plt.show()

#6 задание
cmap = plt.get_cmap('viridis')
colors = cmap(np.linspace(0, 1, len(sales_columns)))
total = []
for col in sales_columns:
  total.append(df[col].sum())
plt.title("Sales data")
plt.pie(total, labels=sales_columns, autopct='%1.1f%%',colors=colors)
plt.legend(sales_columns, loc=4)
plt.show()

# #7 задание
cmap = plt.get_cmap('inferno')
colors = cmap(np.linspace(0, 1, len(sales_columns)))
plt.title("All product sales data using stack plot")
plt.xlabel("Month number")
plt.ylabel("Sales units in Number")
plt.xticks(np.arange(min(df['month_number']), max(df['month_number'])+1, 1.0))
plt.stackplot(df['month_number'], [df[col] for col in sales_columns], colors=colors)
plt.legend(sales_columns)
plt.show()

# #8 задание
fig = plt.figure()
ax1 = plt.subplot2grid((2,3), (0,0), rowspan=1, colspan=3)
ax2 = plt.subplot2grid((2,3), (1,0))
ax3 = plt.subplot2grid((2,3), (1,1))
ax4 = plt.subplot2grid((2,3), (1,2))
fig.tight_layout()
plt.show()