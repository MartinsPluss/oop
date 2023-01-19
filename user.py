# OOP

# create a class
class User:
    def __init__(self, user_email, name, user_password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = user_password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def add_new_skill(self, new_job_tilte):
        self.current_job_title = new_job_tilte

    def get_user_info(self):
        print(f"User {self.name} currently works as {self.current_job_title}. You can contact him at {self.email} ")







