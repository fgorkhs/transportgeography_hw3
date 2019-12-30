import numpy as np 
import pandas as pd
from collections import OrderedDict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import make_scorer
from mord import LogisticAT
import matplotlib.pyplot as plt
from matplotlib import rcParams

with open("school_data.csv", 'r') as file:
    df = pd.read_csv(file).set_index('seat')

# converts data to ASCII
heavenly_stems = dict(zip([n for n in '甲乙丙丁戊己'], list(range(1,7))))
df['grade'] = [heavenly_stems[x] for x in list(df['grade'])]
hh_levels = {'低':'low', '中':'mid', '高':'high'}
df['household_income'] = [hh_levels[x] for x in df['household_income']]
sex_class = {'男':'male', '女':'female'}
df['sex'] = [sex_class[x] for x in df['sex']]
tuition_class = {'無':False, '有':True}
df['tuition'] = [tuition_class[x] for x in df['tuition']]

gradecounts = dict((pd.Index(df['grade']).value_counts()))
distancecounts = dict(df['school_distance'])
distancecounts = {k:v for k, v in sorted(distancecounts.items(), key=lambda item: item[1])}
attitudecounts = pd.Index(df['attitude']).value_counts()

fig, axs = plt.subplots(1,3,sharey=False, sharex=False)
fig.set_figheight(5)
fig.set_figwidth(15)

gradevals = [float(gradecounts[g]) for g in sorted(list(gradecounts.keys()))]
axs[0].bar(range(len(gradevals)), gradevals, align='center', color='black')
axs[0].set_xticks(np.arange(len(gradevals)))
axs[0].set_xticklabels(["Jia", "Yi", "Bing", "Ding", "Wu"])
axs[0].set_xlabel("Grade")
axs[0].set_ylabel("Student Count")

distancevals = [float(distancecounts[g]) for g in list(distancecounts.keys())]
axs[1].bar(range(len(distancevals)), distancevals, align='center', color='black')
axs[1].set_xticks(np.arange(len(distancevals)))
axs[1].set_xticklabels(list(distancecounts.keys()), rotation=-90, size=4)
axs[1].set_xlabel("Student Number")
axs[1].set_ylabel("Distance from School")

attitudevals = [float(attitudecounts[g]) for g in sorted(list(attitudecounts.keys()))]
axs[2].bar(range(len(attitudevals)), attitudevals, align='center', color='black')
axs[2].set_xticks(np.arange(len(attitudevals)))
axs[2].set_xticklabels(sorted(list(attitudecounts.keys())))
axs[2].set_xlabel("School Atttitude")
axs[2].set_ylabel("Student Count")

plt.savefig("firstlook.png")

print(dict((pd.Index(df['sex']).value_counts())))
print(dict((pd.Index(df['tuition']).value_counts())))
print(dict((pd.Index(df['household_income']).value_counts())))

with open("schooldata_parsed.csv", "w") as file:
    df.to_csv(file)

heavenly_stems_eng = dict(zip(list(range(1,6)), ["jia", "yi", "bing", "ding", "wu"]))
df['grade'] = [heavenly_stems_eng[x] for x in list(df['grade'])]
with open("schooldata_parsed_for_r.csv", "w") as file:
    df.to_csv(file)
print(df)




'''
model_linear = LinearRegression()
model_single_logir = LogisticRegression(multi_class='ovr',
    class_weight='balanced')
model_multi = LogisticRegression(multi_class='multinomial',
    solver='lbfgs',
    class_weight='balanced')
model_ordinal = LogisticAT(alpha=0)

features = df.iloc[:, :-1]  #all except quality
target = df['quality']
'''