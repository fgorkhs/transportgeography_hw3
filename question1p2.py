import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

with open("schooldata_parsed.csv", "r") as file:
    df = pd.read_csv(file).set_index('seat')

file = open("separate_reports.txt", "w")
def fwr(title, obj):
    file.write(title+'\n')
    file.write(str(obj)+'\n')
    file.write(("-"*63)+'\n')

# Sex difference
fwr('boys', df[df['sex'] == 'male'].describe())
fwr('girls', df[df['sex'] == 'female'].describe())
# boys 2.17
# girls 4.11

# Income difference
fwr('low income', df[df['household_income'] == 1].describe())
fwr('mid income', df[df['household_income'] == 2].describe())
fwr('high income', df[df['household_income'] == 3].describe())
# low 3.38
# mid 2.42
# high 2.89

# Do they pay tuition?
fwr('paying', df[df['tuition'] == True].describe())
fwr('nonpaying', df[df['tuition'] == False].describe())
# paying 3.04
# nonpaying 3.06

fig, axs = plt.subplots(1,2,sharey=False, sharex=False)
fig.set_figheight(4)
fig.set_figwidth(10)

axs[0].plot(df['school_distance'], df['grade'], linewidth=0, marker='o', color='black')
axs[0].set_yticks(np.arange(len(set(df['grade']))+1))
axs[0].set_ylim(axs[0].get_ylim()[::-1])
axs[0].set_yticklabels(['', "Jia", "Yi", "Bing", "Ding", "Wu"])
axs[0].set_xlabel("Distance from School")
axs[0].set_ylabel("Grade")

axs[1].plot(df['attitude'], df['grade'], linewidth=0, marker='o', color='black')
axs[1].set_yticks(np.arange(len(set(df['grade']))+1))
axs[1].set_ylim(axs[1].get_ylim()[::-1])
axs[1].set_yticklabels(['', "Jia", "Yi", "Bing", "Ding", "Wu"])
axs[1].set_xlabel("Attitude")
axs[1].set_ylabel("Grade")


plt.savefig("secondlook.png")
print(df)