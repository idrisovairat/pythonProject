def int_func(slovo):
    slovov = 'sdfsdfasdfasgfhghjfghsdfASDfsf'
    return slovo.title() if not set(slovo).difference(slovov) else False

print(int_func(slovov))