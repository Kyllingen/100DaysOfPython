# class tests. Review constructors and class variables

class User:
    
    def __init__(self, id, name):
        ''' constructor '''
        print("User being created...")
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        ''' follow another user '''
        user.followers += 1
        self.following += 1

user1 = User("001", "joe")

print(user1.id)