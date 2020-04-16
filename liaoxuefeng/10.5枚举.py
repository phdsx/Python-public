from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.__members__.items())
'''
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
'''
