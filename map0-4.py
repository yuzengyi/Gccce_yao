import pandas as pd

# 加载数据
data_path = 'mapped_data.xlsx'
data = pd.read_excel(data_path)

# 定义映射函数，将数据映射到[0, 4]区间
def map_to_range(column, new_min, new_max):
    min_val = column.min()
    max_val = column.max()
    return column.apply(lambda x: (new_max - new_min) * (x - min_val) / (max_val - min_val) + new_min)

# 定义要映射的列
columns_to_map = ['ST292', 'MATHEFF', 'MATHEF21', 'SDLEFF', 'ICTEFFIC',
                  'MATH_avg', 'MCCR_avg', 'MCQN_avg', 'MCSS_avg', 'MCUD_avg',
                  'MPEM_avg', 'MPFS_avg', 'MPIN_avg', 'MPRE_avg']

# 应用映射函数到指定的列
for col in columns_to_map:
    data[col] = map_to_range(data[col], 0, 4)

# 显示映射后的部分数据
mapped_data = data[columns_to_map].head()
print(mapped_data)
# 保存映射后的数据到新的Excel文件
output_path = 'data_final.xlsx'
data.to_excel(output_path, index=False)
