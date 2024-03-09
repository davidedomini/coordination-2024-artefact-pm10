import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/simulation_pm10.csv', sep = ' ')
data = data[['time', 'TrainLoss[mean]', 'ValidationLoss[mean]']]
df_train = data[['time', 'TrainLoss[mean]']]
df_val = data[['time', 'ValidationLoss[mean]']]
df_train.rename(columns={'time':'Epoch', 'TrainLoss[mean]':'Loss'}, inplace=True)
df_val.rename(columns={'time':'Epoch', 'ValidationLoss[mean]':'Loss'}, inplace=True)
df_train['Type'] = 'Training loss'
df_val['Type'] = 'Validation loss'
df_all = pd.concat([df_train[1:60], df_val[1:60]], axis = 0 )


ax = sns.lineplot(
    data=df_all,
    x='Epoch',
    y='Loss',
    hue='Type'
)

ax.set_xlabel('Epoch', fontsize=18)
ax.set_ylabel('Loss', fontsize=18)
plt.savefig(f'charts/train_val_accuracy.png', dpi=500)
