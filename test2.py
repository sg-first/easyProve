import easyProve as ep
import fact
import math

# 第一问
A = ep.point('A')
ep.addRule(fact.Pos(A, -4, 0))
B = ep.point('B')
ep.addRule(fact.Pos(B, 4, 8))

p = ep.paraCur('p')
ep.addRule(fact.OnCurve(p, A))
ep.addRule(fact.OnCurve(p, B))

ep.infer()
ep.ask(fact.ParaCurPar(p, a=ep.what, b=ep.what, c=ep.what))

# 第二问
l = ep.lineCur('l')
k = ep.variable('k')
ep.addRule(fact.LineCurPar(l, k, 4))

p1 = ep.point('p1')
p2 = ep.point('p2')
ep.addRule(fact.OnCurve(l, p1))
ep.addRule(fact.OnCurve(l, p2))
ep.addRule(fact.OnCurve(p, p1))
ep.addRule(fact.OnCurve(p, p2))

aval = math.sqrt(2)/2
x1 = ep.variable('x1')
ep.addRule(fact.Pos(p1, x1, None))
x2 = ep.variable('x2')
ep.addRule(fact.Pos(p2, x2, None))
x1_re = ep.variable('')
x2_re = ep.variable('')
ep.addRule(fact.IsReciprocal(x1_re, x1))
ep.addRule(fact.IsReciprocal(x2_re, x2))
ep.addRule(fact.SubEq(aval, x1_re, x2_re))

ep.infer()
print(k.val)
