import easyProve as ep
import fact

A = ep.point('A')
B = ep.point('B')
C = ep.point('C')
ABC = ep.triangle('ABC', A, B, C)

B_ = ep.point("B'")
C_ = ep.point("C'")

angle_BAB_= ep.angle("BAB'", B, A, B_)
angle_CAC_= ep.angle("CAC'", C, A, C_)

ep.addRule(fact.AddEq(180, angle_BAB_, angle_CAC_))
D = ep.point('D')
ep.addRule(fact.IsMidPoint(D, B_, C_))

AD = ep.lineSeg('AD', A, D)
BC = ep.lineSeg('BC', B, C)

ep.infer()
ep.ask(fact.DivEq(ep.what, AD, BC))
