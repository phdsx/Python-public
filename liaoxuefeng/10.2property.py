
class Screen(object):

    @property
    def width(self):
        return self.width1

    @width.setter
    def width(self,value):
        self.width1=value

    @property
    def height(self):
        return self.height1

    @height.setter
    def height(self, value):
        self.height1 = value



    @property
    def resolution(self):
        return self.width*self.height

'''
class Screen(object):

    @property
    def width(self):
        return self.width1

    @width.setter
    def width(self, value):
        self.width1 = value

    @property
    def height(self):
        return self.height1

    @height.setter
    def height(self, value):
        self.height1 = value

    @property
    def resolution(self):
        return int(self.width1)*int(self.height1)
'''
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
