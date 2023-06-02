
def is_member(user):
    return user.groups.filter(name='Teacher').exists()