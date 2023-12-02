class PynstaUser:

    # Initializer / Instance attributes
    def __init__(self, name: str, posts: list, friends: list):
        self.name = name
        self.posts = posts
        self.friends = friends

    def add_friend(self, friend):
        self.friends.append(friend)
        print("You have added: " + friend)

    def post(self, post):
        self.posts.append(post)
        print("You have posted: " + post)

if __name__ == "__main__":
    testuser = PynstaUser("Admin", ["Test post! Testing123"], ["Bob"])
    print(testuser.name)
    print(testuser.posts)
    print(testuser.friends)   
