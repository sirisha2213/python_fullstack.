#polymorphism
class hotstar:
    def __init__(self,username):
        print(f'hey {username}, welcome to hotstar')
    def playvideo(self):
        print('ads will be run')
        print('quality is low')
        print('no download options')
        print('no mltiple logins')

    def search(self):
        print('you can search for program')
    def watchlist(self):
        print(f'you can add movies to watch list')
    def notifications(self):
        print(f'you can get the push notifications')
    def login(self):
        print(f'you can login to hotstar')
        
class premiumhotstar:
    def __init__(self,username):
        print(f'hey {username}, welcome to  premium hotstar')
    def playvideo(self):
        print("ads won't run")
        print('quality is high')
        print(' download options')
        print(' mltiple logins')
    def search(self):
        print('you can search for program')
    def watchlist(self):
        print(f'you can add movies to watch list')
    def notifications(self):
        print(f'you can get the push notifications')
    def login(self):
        print(f'you can login to hotstar')  

bhavana = hotstar('bhavana')
bhavana.playvideo()
bhavana.search()
bhavana.notifications()
bhavana.watchlist()
bhavana.login()
print('\n\n')  
sanjana = premiumhotstar('sanjana')
sanjana.playvideo()
sanjana.search()
sanjana.notifications()
sanjana.watchlist()
sanjana.login()


        
