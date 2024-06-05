import pandas as pd

data = pd.read_csv('player_stats.csv')
salaries = pd.read_csv('salaries.csv')
parsed_data = {'name': [], 'pts': [], 'ast': [], 'reb': [], 'blk': [], 'stl': [], 'sal': [], 'age': [], 'mp': [], 'fga': []}

salaryDict = {}
for idx, salary_row in salaries.iterrows():
    if idx == 0: continue
    if isinstance(salary_row[3], float): continue 
    salaryDict[salary_row[10]] = float(salary_row[3][1:])
for idx, row in data.iterrows():
    if row[30] not in salaryDict: continue
    salary = salaryDict[row[30]]
    parsed_data['name'].append(row[1])
    parsed_data['pts'].append(row[29])
    parsed_data['ast'].append(row[24])
    parsed_data['reb'].append(row[23])
    parsed_data['blk'].append(row[26])
    parsed_data['stl'].append(row[25])
    parsed_data['sal'].append(salary)
    parsed_data['age'].append(row[3])
    parsed_data['mp'].append(row[7])
    parsed_data['fga'].append(row[9])

output = pd.DataFrame(parsed_data)

output.to_csv("Output.csv", index = False)
