import easyProve as ep
import fact

# a49b5
a=ep.variable('a')
b=ep.variable('b')
ep.addRule(fact.AddEq(9,a,b))
a.val=5 # tik
mid=ep.variable('')
ep.addRule(fact.MulEq(mid,b,10))
ep.addRule(fact.AddEq(45,a,mid))

ep.infer()
print(a.val)
print(b.val)
print(mid.val)