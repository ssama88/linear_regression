import requests
from bs4 import BeautifulSoup as soup

source = requests.get('https://www.basketball-reference.com/leagues/NBA_2024_per_game.html')


page = soup(source.content, features = 'html.parser')

# print(page.prettify())
players = []

for tag in page.find_all(class_ = "full_table"):
    playerStats = list(tag.children)
    player = {}
    player["name"] = playerStats[1].text
    
    print("player stats", playerStats)
    print("player attributes", player)
    # for idx, child in enumerate(tag.children): 
    #     new_Player = {}
    #     new_
        # if idx == 0: 
        #     print("hello", child.text)
        #     playerIdx = int(child.text)
        #     if players < playerIdx :
        #         players= playerIdx
        
    if(players > 3): break
    # players+=1
    # break

print("players", players)