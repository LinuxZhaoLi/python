#   如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
class Student(object):

    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 -100")
        self._score = value

# class Student(object):

#     def get_score(self):
#          return self._score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# 得装饰器（decorator）可以给函数动态加上功能
# @property 把一个方法变成属性的调用
# 让调用者写出简短的代码，同时保证对参数进行必要的检查
# class Student1(object):

#     @property
#     def score(self):
#         return self.score 
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError("score must be an integer")
#         if value < 0 or value > 100:
#             raise ValueError("score must between 0 - 100")

#         self._score = value

class Student1(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    
if __name__ == "__main__":
    s = Student()
    s.set_score(60)
    c = s.get_score();
    print(c)
    try:
        s.set_score(1100);
        c = s.get_score();
    except Exception as e:
        print(e)
    print(c)
    print("****************分割线*********************")
    s1 = Student1()
    s1.score = 60
    print(s1.score)
    try: 
        s1.score = 1000
    except Exception as e:
        print(e)
