def username_generator(first_name,last_name):
  username = ""
  if len(first_name) >= 3:
    username = first_name[:3]
  else:
    username = first_name
  if len(last_name) >= 4:
    username += last_name[:4]
  else:
    username += last_name
  return username
def password_generator(username):
  password = ""
  for i in range(-1,len(username)-1):
    password += username[i]
  return password


