from snap import *

#v = TIntV.GetV(TInt(11),TInt(12),TInt(13),TInt(14),TInt(15))
v = TIntV.GetV(11,12,13,14,15)

print v[2].Val

try:
    print v[5].Val
except:
    print "*** PYTHON CATCH"

print "--------- 1"
for item in v:
    print item.Val

print "--------- 2"
for i in range(0, v.Len()):
    print v[i].Val

print "--------- 3"
for i in range(0, v.Len()):
    print v.GetVal(i).Val

