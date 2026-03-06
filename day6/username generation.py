# username generation
name = input('eneter the name:')
dob = input('enter the dob[yyyy-mm-dd]')

username = name[:2]+name[-2:]+dob[-2:]+dob[2:4]

print(f"hi{name}!\nyour username: {username}")
