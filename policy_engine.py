
# Simple ZTNA policy engine

def check_access(username):
    allowed_users=["admin","user1","user2"]
    return username in allowed_users
