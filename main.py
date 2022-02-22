class User :
    def __init__(self,username , userid ):
        self.username = username 
        self.userid = userid
        self.followers = 0
        self.following = 0
    
    def follow(self, user) :
        self.following += 1
        user.followers += 1

# an attribute is a variable associated with a class
user_1 = User("Pratik", "12")
user_2 = User("Pratik1", "20")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.followers)
print(user_2.following)