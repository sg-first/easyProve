import easyProve as ep
import typeCheck as tc

def setVal(v, n): # n肯定是数字，v不知道
    if tc.isVariable(v):
        v.val=n
        return v
    else:
        return n

_result = 0
_op1 = 1
_op2 = 2
def getValNum(i):
    num = 0
    for j in i:
        if not tc.isNotKnow(j):
            num = num + 1
    return num

def inferAddEq():
    for i in ep.allRule['AddEq']:
        if getValNum(i)==2:
            if tc.isNotKnow(i[_result]):
                i[_result]=setVal(i[_result], i[_op1] + i[_op2])
            elif tc.isNotKnow(i[_op1]):
                i[_op1]=setVal(i[_op1], i[_result] - i[_op2])
            elif tc.isNotKnow(i[_op2]):
                i[_op2]=setVal(i[_op2], i[_result] - i[_op1])

def inferDivEq():
    for i in ep.allRule['DivEq']:
        if getValNum(i)==2:
            if tc.isNotKnow(i[_result]):
                i[_result]=setVal(i[_result], i[_op1] / i[_op2])
            elif tc.isNotKnow(i[_op1]):
                i[_op1]=setVal(i[_op1], i[_result] * i[_op2])
            elif tc.isNotKnow(i[_op2]):
                i[_op2]=setVal(i[_op2], i[_result] * i[_op1])

def inferIsContray():
    for i in ep.allRule['IsContray']:
        if getValNum(i)==1:
            if tc.isNotKnow(i[0]):
                i[0]=setVal(i[0],i[1]*-1)
            elif tc.isNotKnow(i[1]):
                i[1]=setVal(i[1],i[0]*-1)

def inferIsReciprocal():
    for i in ep.allRule['IsReciprocal']:
        if getValNum(i)==1:
            if tc.isNotKnow(i[0]):
                i[0]=setVal(i[0],1/i[1])
            elif tc.isNotKnow(i[1]):
                i[1]=setVal(i[1],1/i[0])

_point=0
_x=1
_y=2
def findPointPos(point):
    for i in ep.allRule['Pos']:
        if i[_point]==point:
            return (i[_x],i[_y])
    return (None,None)