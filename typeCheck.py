import easyProve as ep

def isVariable(v):
    return isinstance(v, ep.variable)

def isNotKnow(v):
    if v is None:
        return True
    elif isVariable(v):
        return v.val is None
    else:
        return False