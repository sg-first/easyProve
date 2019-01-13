import easyProve as ep

def AddEq(result, op1, op2):
    return ['AddEq', result, op1, op2]

def SubEq(result, op1, op2):
    conOp2=ep.variable('')
    ep.addRule(IsContray(op2, conOp2))
    return ['AddEq', result, op1, conOp2]

def DivEq(result, op1, op2):
    return ['DivEq', result, op1, op2]

def MulEq(result, op1,op2):
    conOp2=ep.variable('')
    ep.addRule(IsReciprocal(op2,conOp2))
    return ['DivEq', result, op1, op2]

def OnCurve(curve, point):
    return ['OnLine', curve, point]

def IsMidPoint(pointKey, point1, point2):
    return ['isMidPoint', pointKey, point1, point2]

def Pos(point, x, y): # 这个和下面的曲线参数不能作为成员变量，因为可能会反向查询（如x1是不是点的x坐标）
    return ['Pos', point, x, y]

def ParaCurPar(curve, a, b, c):
    return ['ParaCurPar', curve, a, b, c]

def LineCurPar(curve, k, b):
    return ['LineCurPar', curve, k, b]

def IsContray(var1, var2):
    return ['IsContray', var1, var2]

def IsReciprocal(var1, var2):
    return ['IsReciprocal', var1, var2]