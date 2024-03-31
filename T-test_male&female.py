import pandas as pd
from scipy import stats

# 读取Excel文件
# 替换'your_file_path.xlsx'为你的Excel文件路径，例如 'data.xlsx'
df = pd.read_excel('Test_male_female.xlsx')

# 分离男性和女性的数据
women = df[df['gender'] == 1]  # 假设gender 1代表女性
men = df[df['gender'] == 2]    # 假设gender 2代表男性

# 对每个变量进行独立样本t检验
for column in ['jiaolv', 'MATH', 'ziwo']:
    # 假设两组方差不相等
    t_stat, p_val = stats.ttest_ind(women[column], men[column], equal_var=False)
    print(f'{column}: t统计量={t_stat}, p值={p_val}')
