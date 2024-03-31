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

## 3.拟合度分析
分析模型各拟合度指标是否符合理想值。RMSEA需小于0.08，GFI、AGFI、NFI、IFI、TLI、CFI需大于0.9，PGFI、PNFI需大于0.5。

### 表1 中介模型拟合指标

| 性别 | GFI  | AGFI | RMSEA | NFI  | TLI  | CFI  | IFI  | PGFI | PNFI |
|----|------|------|-------|------|------|------|------|------|------|
| 男  | 0.946 | 0.93 | 0.06  | 0.977 | 0.974 | 0.978 | 0.978 | 0.73 | 0.843 |
| 女  | 0.951 | 0.936 | 0.057 | 0.977 | 0.975 | 0.978 | 0.978 | 0.734 | 0.843 |

注: GFI为拟合优度指数，AGFI为调整的拟合优度指数，RMSEA为近似误差均方根，NFI为标准拟合指数，IFI为增值拟合指数，TLI为非规范拟合指数，CFI为比较拟合指数，PGFI为精简拟合指数，PNFI为精简规范拟合指数（方杰,张敏强,邱皓政.，2012）

实际的拟合度指标均满足条件。而CMIN/DF（卡方自由度之比）为21.723，不满足小于3的理想值，原因是本次研究样本数量较大，大样本难以满足卡方值检验，因此主要参考其他指标来判断模型的优劣。**因此，可以认为模型的适配度和拟合度都表现出较好的水平。**

### 参考文献

[1] 《深化新时代教育评价改革总体方案》印发 [EB/OL]. (2020-10-13) [2023-03-23]. https://www.chinacourt.org/article/detail/2020/10/id/5523152.shtml.  
[2] Richardson, Frank C.; Suinn, Richard M. The Mathematics Anxiety Rating Scale: Psychometric data. [J]. Journal of Counseling Psychology, 1972(6).  
[3] 陈英和, 耿柳娜. 数学焦虑研究的认知取向 [J]. 心理科学, 2002(06): 653-655+648-764. DOI: 10.16719/j.cnki.1671-6981.2002.06.004.  
[4] BANDURA A. Self-efficacy: toward a unifying theory of behavioral change [J]. Psychological Review, 1977, 84(2): 191-215.  
[5] USHER E L, PAJARES F. Sources of self-efficacy in mathematics: A validation study [J]. Contemporary Educational Psychology, 2009, 34(1): 89-101.  
[7] 崔志翔, 徐斌艳. 数智时代国际基础学科计算思维教育发展的策略、方向与启示——《PISA 2022数学框架》之思考 [J]. 远程教育杂志, 2022, 40(06): 13-21. DOI: 10.15881/j.cnki.cn33-1304/g4.2022.06.001.  
[8] 方杰, 张敏强, 邱皓政. 中介效应的检验方法和效果量测量: 回顾与展望 [J]. 心理发展与教育, 2012, 28(1): 105-111.  
[9] HAYES A F. Beyond Baron and Kenny: Statistical Mediation Analysis in the New Millennium [J]. Communication Monographs, 2009, 76(4): 408-420.  
[10] Usher E L, Pajares F. Sources of SelfEfficacy in School: Critical Review of the Literature and Future Directions [J]. Review of Educational Research, 2008, 78(4): 751-796.
