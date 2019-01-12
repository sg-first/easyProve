import infer as inf
import typeCheck as tc

class variable:
    def __init__(self, name, val=None):
        self.name = name
        self.val = val

    def __add__(self, other): # 参数只能是变量或数字
        if tc.isVariable(other):
            return self.val+other.val
        else:
            return self.val+other

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if tc.isVariable(other):
            return self.val-other.val
        else:
            return self.val-other

    def __rsub__(self, other):
        return self.__sub__(other)*-1

    def __truediv__(self, other):
        if tc.isVariable(other):
            return self.val/other.val
        else:
            return self.val/other

    def __rtruediv__(self, other):
        return 1/self.__truediv__(other)

    def __mul__(self, other):
        if tc.isVariable(other):
            return self.val*other.val
        else:
            return self.val*other

    def __rmul__(self, other):
        return self.__mul__(other)

class curve:
    def __init__(self,name, curType):
        self.name=name
        self.curType=curType

    def getType(self):
        return self.curType

class triangle:
    def __init__(self, name, point1, point2, point3):
        self.name = name
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

class point:
    def __init__(self, name):
        self.name = name

class angle(variable):
    def __init__(self,name, point1, pointKey, point2, val=None):
        super(angle, self).__init__(name, val)
        self.point1 = point1
        self.point2 = point2
        self.pointKey = pointKey
        allAngle.append(self)

class lineSeg(variable):
    def __init__(self, name, point1, point2, val=None):
        super(lineSeg, self).__init__(name, val)
        self.point1 = point1
        self.point2 = point2
        allLineSeg.append(self)

class paraCur(curve):
    def __init__(self, name):
        super(paraCur, self).__init__(name, 'paraCur')

class lineCur(curve):
    def __init__(self, name):
        super(lineCur, self).__init__(name, 'lineCur')

class _WHAT:
    pass

what=_WHAT()
allRule={'AddEq':[], 'DivEq':[], 'OnLine':[], 'isMidPoint':[], 'Pos':[], 'ParaCurPar':[],
         'LineCurPar':[], 'IsContray':[], 'IsReciprocal':[]}
allAngle=[]
allLineSeg=[]

def addRule(r):
    allRule[r[0]].append(r[1:])

def getRuleNum():
    num=0
    for i in allRule.values():
        num=num+len(i)
    return num+len(allAngle)+len(allLineSeg)

def infer():
    for _ in range(getRuleNum()):
        for _ in range(len(allRule['AddEq'])):
            inf.inferAddEq()
        for _ in range(len(allRule['DivEq'])):
            inf.inferDivEq()
        for _ in range(len(allRule['IsContray'])):
            inf.inferIsContray()
        for _ in range(len(allRule['IsReciprocal'])):
            inf.inferIsReciprocal()

def ask(r):
    pass
