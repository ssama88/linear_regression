import pandas as pd

data = pd.read_csv('player_stats.csv')
salaries = pd.read_csv('salaries.csv')
parsed_data = {'name': [], 'pts': [], 'ast': [], 'reb': [], 'blk': [], 'stl': [], 'sal': [], 'age': [], 'mp': [], 'fga': []}
num = 0
for idx, row in data.iterrows():

    for _, salary_row in salaries.iterrows(): 
        if row[30] == salary_row[10]: 
            if isinstance(salary_row[3], float): break
            parsed_data['name'].append(row[1])
            parsed_data['pts'].append(row[29])
            parsed_data['ast'].append(row[24])
            parsed_data['reb'].append(row[23])
            parsed_data['blk'].append(row[26])
            parsed_data['stl'].append(row[25])
            parsed_data['sal'].append(float(salary_row[3][1:]))
            parsed_data['age'].append(row[3])
            parsed_data['mp'].append(row[7])
            parsed_data['fga'].append(row[9])
            
    
    num+=1
    


output = pd.DataFrame(parsed_data)

output.to_csv("Output.csv", index = False)

