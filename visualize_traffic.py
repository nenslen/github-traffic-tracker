import matplotlib.pyplot as plt
import pandas as pd


plt.style.use('ggplot')


clone_df = pd.read_csv('clone_data.csv')
view_df = pd.read_csv('view_data.csv')

total_clones = clone_df['total_clones'].sum()
total_views = view_df['total_views'].sum()

view_repos = view_df['repo_name'].unique()


def print_clone_data():
    clone_repos = clone_df['repo_name'].unique()

    print ("{:<30} {:<10} {:<10}".format('Repo', 'Clones', 'Unique'))
    print('=' * 48)
    for repo in clone_repos:
        rows = clone_df.loc[clone_df['repo_name'] == repo]
        
        total_clones = rows['total_clones'].sum()
        unique_clones = rows['unique_clones'].sum()
        
        print ("{:<30} {:<10} {:<10}".format(repo, total_clones, unique_clones))
    print ("{:<30} {:<10} {:<10}".format('TOTAL', clone_df['total_clones'].sum(), clone_df['unique_clones'].sum()))
    print('')


def print_view_data():
    view_repos = view_df['repo_name'].unique()

    print ("{:<30} {:<10} {:<10}".format('Repo', 'Views', 'Unique'))
    print('=' * 48)
    for repo in view_repos:
        rows = view_df.loc[view_df['repo_name'] == repo]
        
        total_views = rows['total_views'].sum()
        unique_views = rows['unique_views'].sum()
        
        print ("{:<30} {:<10} {:<10}".format(repo, total_views, unique_views))
    print ("{:<30} {:<10} {:<10}".format('TOTAL', view_df['total_views'].sum(), view_df['unique_views'].sum()))
    print('')
        
        
print_clone_data()
print_view_data()
