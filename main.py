# create an object from a class User
from user import User
from post import Post


app_user_one = User("mm@pp.lv", "Martins Pluss", "qwerty", "programmer")
app_user_one.get_user_info()

app_user_two = User("aa@bb.lv", "Vita Plusina", "neteiksu", "secretary")
app_user_two.get_user_info()

app_user_one.change_password("123123")
app_user_one.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()