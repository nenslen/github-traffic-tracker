# github-traffic-tracker
 
 
## What is this project?
This project is a quick and simple way to keep a long-term history of your github repository traffic (views and clones). As of now (April 2021), github only lets you see the last 2 weeks of traffic for your repositories, which is unfortunate because 2 weeks is not a very long time. So, to keep a longer history, this project uses github's api to fetch traffic data for your public repositories and save it locally as a csv.

Note: The 2-week limit is a github limitation, this repo will not help you get traffic data that's already older than 2 weeks, it simply saves traffic data so it can be viewed later.


## Instructions
### 1) Create a personal access token on github
You can [create a token here](https://github.com/settings/tokens), and give it the public_repo permission.\
![image](https://user-images.githubusercontent.com/17073202/114321321-300d0700-9acf-11eb-8720-647ba306651a.png)

### 2) Create a credentials.py file in the same directory
You just need the TOKEN and OWNER variables defined:
```python
TOKEN = 'YOUR GITHUB TOKEN'
OWNER = 'YOUR GITHUB USERNAME'
```

### 3) Run get_traffic_data.py at least once every 2 weeks
This will create/update the clone_data.csv and view_data.csv files. I run mine once a day so the data is always up to date. Note that days with 0 clones/views are not recorded in these files, so if your files are still empty after running get_traffic_data.py, it's because none of your repos have any clones/views yet :(

### 4) Visualize your data
The traffic data is stored in clone_data.csv and view_data.csv, so you can visualize your data however you like using those files. Personally, I keep things simple and just run view_data.py, which outputs some very basic tables with the data I want to see.
