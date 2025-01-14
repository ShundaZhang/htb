import pandas as pd
import re

# 文件路径
file_path = 'data.txt'

# 定义权重
weights = {
    "health_weight": 0.2,
    "agility_weight": 0.3,
    "charisma_weight": 0.1,
    "knowledge_weight": 0.05,
    "energy_weight": 0.05,
    "resourcefulness_weight": 0.3
}

# 技能列表和对应权重
skills = ["Health", "Agility", "Charisma", "Knowledge", "Energy", "Resourcefulness"]
skill_weights = [weights[f"{skill.lower()}_weight"] for skill in skills]

# 预处理文件，移除分隔符行和标题行
with open(file_path, 'r') as file:
    lines = file.readlines()

# 提取有效数据行
data_lines = [
    line for line in lines
    if re.match(r"\s+\w+", line) and not any(header in line for header in ["Health", "Agility", "Charisma", "Knowledge", "Energy", "Resourcefulness"])
]

# 定义列名
columns = ["First Name", "Last Name", "Health", "Agility", "Charisma", "Knowledge", "Energy", "Resourcefulness"]

# 解析数据行
parsed_data = []
for line in data_lines:
    fields = re.split(r'\s{2,}', line.strip())
    if len(fields) == len(columns):
        parsed_data.append(fields)

# 将数据加载到 DataFrame 中
data = pd.DataFrame(parsed_data, columns=columns)

# 将技能列转换为数值型
for skill in skills:
    data[skill] = pd.to_numeric(data[skill])

# 计算每个技能的得分
for skill, weight in zip(skills, skill_weights):
    data[f"{skill}_score"] = round(6 * (data[skill] * weight)) + 10

# 计算总分
data["overall_value"] = round(
    5 * ((data["Health_score"] * 0.18) +
         (data["Agility_score"] * 0.20) +
         (data["Charisma_score"] * 0.21) +
         (data["Knowledge_score"] * 0.08) +
         (data["Energy_score"] * 0.17) +
         (data["Resourcefulness_score"] * 0.16))
)

# 转换总分为整数
data["overall_value"] = data["overall_value"].astype(int)

# 按总分排序，获取前 14 名
top_candidates = data.nlargest(14, "overall_value")[["First Name", "Last Name", "overall_value"]]

# 格式化输出
formatted_output = ', '.join([
    f"{row['First Name']} {row['Last Name']} - {row['overall_value']}"
    for _, row in top_candidates.iterrows()
])

print(formatted_output)
#All code generated by ChatGPT!
#HTB{t3xT_p4rS1ng_4nD_maTh_f0rmUl4s...}
