# PISA 2022 Data Cleaning and Descriptive Statistics

This project, co-authored by Yao Zhang and Zengyi Yu, focuses on the cleaning and descriptive statistical analysis of the PISA 2022 dataset. The aim is to uncover insights into educational trends and student performance across different regions and genders.
## Code Snippet

Below is a snippet of the code used for data cleaning and descriptive statistical analysis:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data loading
data_path = '/path/to/data.xlsx'
data = pd.read_excel(data_path)

# Data transformation and analysis here...
# (Include your code)

# Plotting the results
# (Include your plotting code)
```
### 3. 使用说明
如果需要，提供如何在本地环境中运行代码的说明。


## How to Run

To run this analysis on your local machine, follow these steps:
1. Clone the repository: `git clone https://github.com/your-repository.git`
2. Navigate to the repository directory: `cd your-repository`
3. Ensure that you have Python installed with required packages: `pandas`, `seaborn`, and `matplotlib`.

## Results and Conclusion

Our analysis revealed significant educational trends... (Briefly describe your findings)
## Contributing

Feel free to fork the repository and submit pull requests.

## Acknowledgments

Thanks to Zhang Yao and Yu Zengyi for their collaboration on this project.

## 2.1.1 字段解释

针对研究问题，需要对PISA大数据集进行数据筛选，以获取与研究主题相关的变量和测量量表。对数据集进行分析，可以看到数学焦虑的测量量表提供各类信息，包括学生在数学课堂中的焦虑水平、对数学作业的紧张程度等。自我效能感的测量量表提供学生在数学领域中的自我效能感水平、自主学习自我效能感以及数字能力自我效能感等信息。此外获取学生基本信息，如国家和地区、性别。最终获得21个变量字段，11339条数据。

### 表1 字段解释

| 变量分类 | 字段名称   | 字段含义                                   |
|------|--------|----------------------------------------|
| 基本信息 | CNT    | 参与PISA评估的国家或地区                        |
|      | ST004D01T | 性别，1代表女生，2代表男生                       |
| 数学焦虑 | JLQ1   | 我经常担心在数学课上对我来说会很困难                    |
|      | JLQ2   | 当我必须做数学作业时，我会非常紧张                    |
|      | JLQ3   | 我在做数学题时会非常紧张                         |
|      | JLQ4   | 做数学题时我感到无助                           |
|      | JLQ5   | 我担心我的数学成绩会很差                         |
|      | JLQ6   | 我对数学失败感到焦虑                           |
| 自我效能感 | MATHEFF | 形式数学和应用数学                           |
|      | MATHEF21 | 数学推理和21世纪技能                         |
|      | SDLEFF | 社会比较对数学自我效能感的影响程度                  |
|      | ICTEFFIC | 信息和通信技术对数学自我效能感的影响程度             |
| 数学成绩和数学素养分维度 | MCCR   | 变化与关系                                 |
|      | MCQN   | 数量认知                                 |
|      | MCSS   | 空间与形状                                 |
|      | MCUD   | 不确定性与数据                              |
|      | MPEM   | 运用数学概念、事实和程序                         |
|      | MPFS   | 用数学方法表述情境                             |
|      | MPIN   | 数学成果的解释、应用和评价                       |
|      | MPRE   | 数学推理                                  |

## 2.1.2 数学焦虑评估量表

PISA数据集在数学领域中考察了学生的态度和情感方面的数据。通过问卷调查，PISA收集了学生对数学学习的态度、兴趣、自信心等数学焦虑的相关信息。我们在此基础上构建数学焦虑评估量表。考虑到PISA中原始数据是选项序号越小越焦虑，所以将其转换成四点量表(美国社会心理学家李克特设计的一种心理学评分加总式量表)，0-4分别代表“未选择”、“反对”、“强烈反对”、“赞同”、“强烈赞同”。

## 2.1.3 自我效能感

数学自我效能中的形式数学和应用数学（MATHEFF）是学生对于进行形式和应用数学任务的自信程度评级。数学自我效能中的数学推理和21世纪数学（MATHEF21）是学生对于进行数学推理和21世纪数学任务的自信程度评级。自主学习自我效能（SDLEFF）是学生在未来学校再次关闭时进行自主学习任务的自信程度评级。数字能力自我效能（ICTEFFIC）是学生对于使用数字资源进行各种任务的能力自信程度评级。

## 2.2 数据预处理

在数据清洗阶段，利用SPSS Modeler的“选择”节点筛选出需要的三个地区的数据字段。对于问卷中存在个别问题未作答的学生进行删除，由于这三个地区在CREATEFF创造性自我效能感列出现缺失，故删除此列。数学焦虑的量表中有六道题目，学生会选择5道题目作答，满分为20分，我们将其等比转化为1000分，与数学得分相统一，再分别将数学素养九个分维度的十个数据取平均值，得到数学素养分维度的评估数据。这样能够提供一个简单的指标来衡量学生在不同分维度上的表现，得到一个更全面的数学素养评估，以更好地了解学生在数学方面的能力和知识水平。

