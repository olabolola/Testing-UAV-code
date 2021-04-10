import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns




colors = ['#727272', '#599ad3']
no_customer_values = (50, 100, 200, 500)
drone_capacity_values = (1, 2, 3, 4)

def get_battery_strategy_vs_noc_and_dc(mean_value_col, by, save = False):
    mean_values = {}

    mean_values['launch immediately'] = []
    mean_values['wait for capacity'] = []

    if by == 'no_customers':
        for no_customers in no_customer_values:
            mean_values['launch immediately'].append(df_bad[(df_bad.no_customers == no_customers) & (df_bad.strategy == 'FPF_MPA')][mean_value_col].mean())
            mean_values['wait for capacity'].append(df_good[(df_good.no_customers == no_customers) & (df_good.strategy == 'FPF_MPA')][mean_value_col].mean())
    elif by == 'drone_capacity':
        for drone_capacity in drone_capacity_values:
            mean_values['launch immediately'].append(df_bad[(df_bad.drone_capacity == drone_capacity) & (df_bad.strategy == 'FPF_MPA')][mean_value_col].mean())
            mean_values['wait for capacity'].append(df_good[(df_good.drone_capacity == drone_capacity) & (df_good.strategy == 'FPF_MPA')][mean_value_col].mean())

    if by == 'no_customers':
        df_plot = pd.DataFrame(mean_values, index = no_customer_values)
    elif by == 'drone_capacity':
        df_plot = pd.DataFrame(mean_values, index = drone_capacity_values)
    df_plot.plot(kind='bar', rot=0, color = colors)
    plt.ylabel(mean_value_col)
    plt.xlabel(by)
    plt.legend(loc='lower right')
    if save:
        path = 'figures/'
        filename = f'{by} vs {mean_value_col} for each strategy'
        plt.savefig(path + filename)
    else:
        plt.show()

    




df_bad = pd.read_csv('results/results - launch immediately.csv')

df_bad.strategy = df_bad.strategy.replace('farthest_package_first', 'FPF')
df_bad.strategy = df_bad.strategy.replace('closest_package_first', 'CPF')
df_bad.strategy = df_bad.strategy.replace('most_packages_first', 'MPF')
df_bad.strategy = df_bad.strategy.replace('farthest_package_first_MPA', 'FPF_MPA')
cols = ['total_time', 'package_delivery_time', 'drone_travel_distance', 'utilization', 'avg_package_wait_time', 'avg_customer_wait_time', 'total_delay_time', 'avg_span_2', 'avg_span_3', 'avg_span_4', 'avg_nodropoffs_2', 'avg_nodropoffs_3', 'avg_nodropoffs_4', 'no_preventions']
# bies = ['drone_capacity', 'no_customers']
df_bad.avg_span_2 = df_bad.avg_span_2.replace([-10], np.nan)
df_bad.avg_span_3 = df_bad.avg_span_3.replace([-10], np.nan)
df_bad.avg_span_4 = df_bad.avg_span_4.replace([-10], np.nan)
df_bad.avg_nodropoffs_2 = df_bad.avg_nodropoffs_2.replace([-10], np.nan)
df_bad.avg_nodropoffs_3 = df_bad.avg_nodropoffs_3.replace([-10], np.nan)
df_bad.avg_nodropoffs_4 = df_bad.avg_nodropoffs_4.replace([-10], np.nan)


df_good = pd.read_csv('results/results - wait for capacity.csv')

df_good.strategy = df_good.strategy.replace('farthest_package_first', 'FPF')
df_good.strategy = df_good.strategy.replace('closest_package_first', 'CPF')
df_good.strategy = df_good.strategy.replace('most_packages_first', 'MPF')
df_good.strategy = df_good.strategy.replace('farthest_package_first_MPA', 'FPF_MPA')
cols = ['total_time', 'package_delivery_time', 'drone_travel_distance', 'utilization', 'avg_package_wait_time', 'avg_customer_wait_time', 'total_delay_time', 'avg_span_2', 'avg_span_3', 'avg_span_4', 'avg_nodropoffs_2', 'avg_nodropoffs_3', 'avg_nodropoffs_4', 'no_preventions']
# bies = ['drone_capacity', 'no_customers']
df_good.avg_span_2 = df_good.avg_span_2.replace([-10], np.nan)
df_good.avg_span_3 = df_good.avg_span_3.replace([-10], np.nan)
df_good.avg_span_4 = df_good.avg_span_4.replace([-10], np.nan)
df_good.avg_nodropoffs_2 = df_good.avg_nodropoffs_2.replace([-10], np.nan)
df_good.avg_nodropoffs_3 = df_good.avg_nodropoffs_3.replace([-10], np.nan)
df_good.avg_nodropoffs_4 = df_good.avg_nodropoffs_4.replace([-10], np.nan)

strategies = ['FPF', 'FPF_MPA', 'CPF', 'MPF']


for col in cols:
    for by in ('no_customers', 'drone_capacity'):
        get_battery_strategy_vs_noc_and_dc(col, by = by, save=False)


# for col in cols:
#     print(df_bad.total_time.mean())
#     print(df_good.total_time.mean())

# get_battery_strategy_vs_noc_and_dc('total_time', 'drone_capacity', save=False)