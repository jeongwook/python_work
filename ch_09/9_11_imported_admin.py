from users import Admin	


me = Admin('juan', 'yu', 'male', 30, ['can add post', 'can delete post', 'can ban user'])
me.describe_user()
me.greet_user()
me.privileges.show_privileges()
