voted = {}

def check_voter(name):
    if voted.get(name):
        print("Kick them out")
    else:
        voted[name] = True
        print("Let them vote")

check_voter("Pratik")
check_voter("Ravi")
check_voter("Pratik")

# the above code is descriptioon to show the use of the hash rtables