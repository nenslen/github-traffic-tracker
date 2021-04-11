import requests
import pandas as pd
import credentials as creds
import os
from datetime import datetime


token = creds.TOKEN
owner = creds.OWNER
headers = {
    'Content-Type': 'application/vnd.github.v3+json',
    'Authorization': f'token {token}'
}
request_string = 'https://api.github.com/'


def get_public_repos():
    query = f'users/{owner}/repos'
    r = requests.get(request_string + query, headers=headers)
    
    return r.json()
    
    
def get_clones_for_repo(repo):
    query = f'repos/{owner}/{repo}/traffic/clones'
    r = requests.get(request_string + query, headers=headers)
    
    return r.json()['clones']


def get_views_for_repo(repo):
    query = f'repos/{owner}/{repo}/traffic/views'
    r = requests.get(request_string + query, headers=headers)
    
    return r.json()['views']
    

def get_clone_and_view_data(repos):
    clone_df = pd.DataFrame(columns=['repo_name', 'date', 'total_clones', 'unique_clones'])
    view_df = pd.DataFrame(columns=['repo_name', 'date', 'total_views', 'unique_views'])
    today = datetime.today().strftime('%Y-%m-%d')
    
    
    for repo in repos:
        name = repo['name']
        
        clones = get_clones_for_repo(name)
        views = get_views_for_repo(name)
    
    
        # Get clone data
        for clone in clones:
            timestamp = clone['timestamp'].split('T')[0]
            if timestamp == today:
                continue # Skip today's data because it can still change
                
            new = {
                'repo_name': name,
                'date': timestamp,
                'total_clones': clone['count'],
                'unique_clones': clone['count']
            }
            clone_df = clone_df.append(new, ignore_index=True)
                
            
        # Get view data
        for view in views:
            timestamp = view['timestamp'].split('T')[0]
            if timestamp == today:
                continue # Skip today's data because it can still change
                
            new = {
                'repo_name': name,
                'date': timestamp,
                'total_views': view['count'],
                'unique_views': view['count']
            }
            view_df = view_df.append(new, ignore_index=True)
    
    return (clone_df, view_df)


def create_data_files_if_not_exist(clone_filename, view_filename):
    if not os.path.exists(clone_filename):
        with open(f'{clone_filename}', 'w') as file:
            file.write('repo_name,date,total_clones,unique_clones')
            
    if not os.path.exists(view_filename):
        with open(f'{view_filename}', 'w') as file:
            file.write('repo_name,date,total_views,unique_views')


def update_clone_and_view_data(clone_data, view_data):
    clone_filename = 'clone_data.csv'
    view_filename = 'view_data.csv'
    
    create_data_files_if_not_exist(clone_filename, view_filename)
    
    clone_df = pd.read_csv(clone_filename)
    view_df = pd.read_csv(view_filename)
    
    
    # Update clone data
    for index, data in clone_data.iterrows():
        repo_name = data['repo_name']
        date = data['date']
        
        match = clone_df.loc[(clone_df['repo_name'] == repo_name) & (clone_df['date'] == date)]
    
        # Add this clone data if it's not already present
        if match.shape[0] == 0:
            clone_df = clone_df.append(data)
            
            
    # Update view data
    for index, data in view_data.iterrows():
        repo_name = data['repo_name']
        date = data['date']
        
        match = view_df.loc[(view_df['repo_name'] == repo_name) & (view_df['date'] == date)]
    
        # Add this clone data if it's not already present
        if match.shape[0] == 0:
            view_df = view_df.append(data)
    
    # Save to csv
    clone_df.to_csv(clone_filename, index=False)
    view_df.to_csv(view_filename, index=False)
    
    
repos = get_public_repos()
clone_data, view_data = get_clone_and_view_data(repos)
update_clone_and_view_data(clone_data, view_data)
