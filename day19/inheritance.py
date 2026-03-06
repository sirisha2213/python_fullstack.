#inheritance
#single inheritance
'''
class Instagramv1:
    def __init__(self,username):
        self.username = username
        print(f'hey {self.username}, welcome to the instagram !!!!')

    def reels(self):
        print('you can upload and scroll the reels')

    def posts(self):
        print('you can post your pics')

class Instagramv2(Instagramv1):
    def __int__(self,username):
        super().__init__(usename)
    def story(self):
        print('ypu can upload the story')
        
            

sirisha = Instagramv1('sirisha')
sirisha.reels()
sirisha.posts()
print('\n')
varsha = Instagramv2('varsha')
varsha.reels()
varsha.posts()
varsha.story()

#multi level 

class Instagramv1:
    def __init__(self,username):
        self.username = username
        print(f'hey {self.username}, welcome to the instagram !!!!')

    def reels(self):
        print('you can upload and scroll the reels')

    def posts(self):
        print('you can post your pics')

class Instagramv2(Instagramv1):
    def __int__(self,username):
        super().__init__(usename)
    def story(self):
        print('ypu can upload the story')

class Instagramv3(Instagramv2):
    def __int__(self,username):
        super().__init__(usename)
    def note(self):
        print('ypu can add a note')

        
sirisha = Instagramv3('sirisha')
sirisha.reels()
sirisha.posts()
sirisha.story()
sirisha.note()

#multiple
class Instagramv1:
    def __init__(self,username):
        self.username = username
        print(f'hey {self.username}, welcome to the instagram !!!!')

    def reels(self):
        print('you can upload and scroll the reels')

    def posts(self):
        print('you can post your pics')

class Instagramv2(Instagramv1):
    def __int__(self,username):
        super().__init__(usename)
    def story(self):
        print('ypu can upload the story')

class Instagramv3(Instagramv2):
    def __int__(self,username):
        super().__init__(usename)
    def note(self):
        print('ypu can add a note')

class live:
    def launchlive(self):
        print('now you can launch live')
class verification:
    def verify(self):
        print('you can verify your account')

class Instagramv4(Instagramv3,live,verification):
    def __int__(self,username):
        super().__init__(username)
    


sirisha = Instagramv4('sirisha')
sirisha.reels()
sirisha.posts()
sirisha.story()
sirisha.note()
sirisha.launchlive()
sirisha.verify()
'''
#hierarichal
class Instagramv1:
    def __init__(self,username):
        self.username = username
        print(f'hey {self.username}, welcome to the instagram !!!!')

    def reels(self):
        print('you can upload and scroll the reels')

    def posts(self):
        print('you can post your pics')

class Instagramv2(Instagramv1):
    def __int__(self,username):
        super().__init__(usename)
    def story(self):
        print('ypu can upload the story')

class Instagramv3(Instagramv2):
    def __int__(self,username):
        super().__init__(usename)
    def note(self):
        print('ypu can add a note')

class live:
    def launchlive(self):
        print('now you can launch live')
class verification:
    def verify(self):
        print('you can verify your account')

class Instagramv4(Instagramv3,live,verification):
    def __int__(self,username):
        super().__init__(username)

class Instagramv5(Instagramv4):
    def __int__(self,username):
        super().__init__(username)
        
class creator(Instagramv4):
    def __init__(self,username):
        super().__init__(username)

    def insights(self):
        print('you can check your post insights')

class business(Instagramv4):
    def __init__(self,username):
        super().__init__(username)
    
    def buttons(self):
        print('you can contact the mail and number')
        
sirisha = Instagramv4('sirisha')
sirisha.reels()
sirisha.posts()
sirisha.story()
sirisha.note()
sirisha.launchlive()
sirisha.verify()
sirisha.insights()
sirisha.buttons()












































































        
