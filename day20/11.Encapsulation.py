class PostViewer:
    
    def __init__(self, owner_name, private_account=False):
        self.owner_name = owner_name 
        self.__private_account = private_account  
        self.posts = []  
        self.followers = []
    
    def add_post(self, photo_url):
        self.posts.append(photo_url)
        print(f"{self.owner_name} added a new post.")

    def set_privacy(self, private_status):
        self.__private_account = private_status

        if private_status:
            print(f"{self.owner_name}'s account is now Private.")
        else:
            print(f"{self.owner_name}'s account is now Public.")

    def follow(self, follower_name):
        if follower_name not in self.followers:
            self.followers.append(follower_name)
            print(f"{follower_name} is now following {self.owner_name}.")
        else:
            print(f"{follower_name} is already following {self.owner_name}.")
        

    def view_posts(self, viewer_name):
        if not self.__private_account or viewer_name in self.followers:
            print(f"Posts by {self.owner_name}:")
            for post in self.posts:
                print(post)
        else:
            print(f"{self.owner_name}'s account is private. Follow them to view posts.")
   
sanjay=PostViewer("sanjay",True)
sanjay.add_post("python course")
sanjay.add_post("flask course")
sanjay.add_post("sql course")
sanjay.add_post("softskills course")


dinesh=PostViewer("dinesh")
post=['candid pic','professional pic']
for i in post:
    dinesh.add_post(i)

dinesh.follow("sanjay")
sanjay.follow("dinesh")  

sanjay.view_posts("dinesh")
dinesh.view_posts("sanjay")


       
