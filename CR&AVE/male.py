import numpy as np

# 定义函数计算CR和AVE
def calculate_cr_ave(loading_estimates):
    # 计算负载的平方和和负载的四次方和
    lambda_square_sum = np.sum(np.square(loading_estimates))
    lambda_fourth_power_sum = np.sum(np.power(loading_estimates, 4))

    # 计算平均方差提取(AVE)
    ave = lambda_square_sum / len(loading_estimates)

    # 计算复合可靠性(CR)
    cr = (lambda_square_sum ** 2) / ((lambda_square_sum ** 2) + (len(loading_estimates) - lambda_square_sum))

    return cr, ave


# 数学焦虑的估计值
math_anxiety_loadings = np.array([0.322, 0.199, 0.427, 0.385, 0.392, 0.408])

# 自我效能感的估计值
self_efficacy_loadings = np.array([.899, .800, .367, .270])
#self_efficacy_loadings = np.array([.812, .801, .824, .853])
# 数学素养的估计值
math_literacy_loadings = np.array([.975, .979, .972, .959, .978, .980, .973, .979])

# 计算CR和AVE
cr_math_anxiety, ave_math_anxiety = calculate_cr_ave(math_anxiety_loadings)
cr_self_efficacy, ave_self_efficacy = calculate_cr_ave(self_efficacy_loadings)
cr_math_literacy, ave_math_literacy = calculate_cr_ave(math_literacy_loadings)

print("数学焦虑的CR和AVE值: CR =", cr_math_anxiety, ", AVE =", ave_math_anxiety)
print("自我效能感的CR和AVE值: CR =", cr_self_efficacy, ", AVE =", ave_self_efficacy)
print("数学素养的CR和AVE值: CR =", cr_math_literacy, ", AVE =", ave_math_literacy)
