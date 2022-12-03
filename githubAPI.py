import requests
import json

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = 'ghp_VsPMBd8TgialGwLO8VEul5lUgKozRU2oCAyE'

    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+ username)
        return response.json()
    
    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    
    def createRepository(self, name):
        payload = {'name': name, 'description': 'REPO_ACIKLAMASI', 'auto_init': 'true'}
        response = requests.post('https://api.github.com/' + 'user/repos', auth=(username, self.token), data=json.dumps(payload))
        return response.json()
    
github = Github()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ')
    
    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} follower: {result['followers']}")
        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print('yanlış bir seçim')