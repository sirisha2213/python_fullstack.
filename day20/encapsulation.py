#encapsulation 
class snapchat:
    def __init__(self,username,password,friends):
        self.username = username #public
        self.__password = password #private(__)
        self._friends = friends #for protected(_)

    def getpassword(self):
        return self.__password
    def setpassword(self,new_password):
        self.__password = new_password

    @property  #it is decorative
    def oprFriends(self):
        return self._friends
    @oprFriends.setter
    def oprFriends(self,newfriend):
        self._friends.append(newfriend)

sirisha = snapchat('sirisha','1322',['bhavana','sanjana'])

print(f' Name before modification: {sirisha.username}')
sirisha.username = 'siri'
print(f' Name after modification: {sirisha.username}')
        
print(f' password before modification: {sirisha.getpassword()}')

sirisha.setpassword('2213')
print(f' password after modification: {sirisha.getpassword()}')

print(f' friends before modification: {sirisha.oprFriends}')
sirisha.oprFriends = 'varsha'
print(f' friends after modification: {sirisha.oprFriends}')
89
