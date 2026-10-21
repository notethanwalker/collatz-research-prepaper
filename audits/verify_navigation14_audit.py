#!/usr/bin/env python3
"""Independent exact checks of N14; does not run the source archive or its long records."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib
BASE=Path(__file__).resolve().parent

def edges(B,d):
 return [e for e in range(1,B+1) if (e-d+9)%4==0 and (e-d+9)//4>=1]
def jr(d):return (d-1)//4,(d-1)%4+1
def coeff(d):
 j,r=jr(d);return F(2**j,5),F(2**(3 if r==1 else 2),5)
def policyvalue(B,d,policy):
 seen={};seq=[];x=d
 while x not in seen:
  seen[x]=len(seq);seq.append(x);x=policy[x]
 k=seen[x];cyc=seq[k:];off=F(0);mult=F(1)
 for x in cyc:
  a,b=coeff(x);off+=mult*a;mult*=b
 assert mult<1
 v=off/(1-mult)
 for x in reversed(seq[:k]):
  a,b=coeff(x);v=a+b*v
 return v
certs={};edgecount=0
for B in [4,5,8,16,17,18,24,32]:
 lo={d:min(edges(B,d)) for d in range(1,B+1)};hi={d:max(edges(B,d)) for d in range(1,B+1)}
 l={d:policyvalue(B,d,lo) for d in lo};u={d:policyvalue(B,d,hi) for d in hi}
 for d in lo:
  a,b=coeff(d)
  for e in edges(B,d):
   assert l[d]<=a+b*l[e];assert u[d]>=a+b*u[e];edgecount+=1
 span=max((u[d]-l[d])/2**jr(d)[0] for d in lo)
 certs[B]={'lower':l,'upper':u,'span':span}
expected={4:F(0),5:F(512,565),8:F(2952,565),16:F(20664,565),17:F(4952,113),18:F(5976,113),24:F(91512,565),32:F(374904,565)}
assert {B:c['span'] for B,c in certs.items()}==expected
l,u=certs[17]['lower'],certs[17]['upper'];assert l[2]==F(513,113) and u[2]==F(23729,565)
assert u[2]-l[2]==F(21164,565)
assert len([(d,e) for d in range(1,18) for e in edges(17,d)])==60

def interval(y,M,d,e):
 j0,r0=jr(d);j1,r1=jr(e);assert (9*M+r1-r0)%4==0
 beta=F(2**((9*M+r1-r0)//4),5**M);Y=2**j1*y
 return ((beta*(Y+u[e])-u[d])/2**j0,(beta*(Y+l[e])-l[d])/2**j0)
def vp2(n):return (n&-n).bit_length()-1
def replay(n,M,d,B,c=5):
 word=[]
 for _ in range(M):
  if n<=1:return None
  a=vp2(c*n+1);n=(c*n+1)//2**a;d+=4*a-9;word.append(a)
  if not 1<=d<=B:return None
 return n,d,tuple(word)
L,U=interval(621583,8,2,2)
assert (L,U)==(F(814694289887,1953125),F(162943670671,390625))
candidates=[n for n in range((L.numerator+L.denominator-1)//L.denominator,U.numerator//U.denominator+1) if n%2]
accepted=[n for n in candidates if (r:=replay(n,8,2,17)) is not None and r[:2]==(621583,2)]
assert candidates==list(range(417125,417136,2));assert accepted==[417131,417135]
for t in [1,2,3,17,100,1000,2**40]:
 L1,U1=interval(621583+781250*t,8,2,2)
 assert L1-L==U1-U==524288*t
 for n in candidates:
  r=replay(n+524288*t,8,2,17)
  assert (r is not None and r[:2]==(621583+781250*t,2))==(n in accepted)

# Exhaustive bridge wall comparison on moderate finite graphs; no finite test is used as proof.
wallpaths=wallprefixes=0
for B in range(4,11):
 for d in range(1,B+1):
  paths=[(d,)]
  for M in range(1,7):
   paths=[p+(e,) for p in paths for e in edges(B,p[-1])]
   for p in paths:
    e=p[-1];lo=[d];hi=[d]
    for i in range(1,M):
     r=(d-i-1)%4+1;bot=max(1,d-5*i);top=min(B,e+5*(M-i))
     lo.append(bot+(r-bot)%4);hi.append(top-(top-r)%4)
    lo.append(e);hi.append(e)
    assert all(y in edges(B,x) for x,y in zip(lo,lo[1:]));assert all(y in edges(B,x) for x,y in zip(hi,hi[1:]))
    assert all(x<=y<=z for x,y,z in zip(lo,p,hi));wallpaths+=1;wallprefixes+=M+1

# Complete finite C3 ancestry with exact division and positive pre-absorption guard.
def inverse_layer(layer,B):
 out=set()
 for y,e in layer:
  for d in range(1,B+1):
   k=e-d+9
   if k%4 or k<4:continue
   a=k//4;z=2**a*y-1
   if z%3==0 and z//3>1 and (z//3)%2:out.add((z//3,d))
 return out
ancestry={}
for B in [15,17]:
 layer={(91,2)}
 for depth in range(1,81):layer=inverse_layer(layer,B)
 ancestry[B]=sum(d==2 for _,d in layer)
assert ancestry=={15:33,17:1563}
exhaust={}
for B in [9,17]:
 layer={(9757,2)};depth=0
 while layer:
  depth+=1;layer=inverse_layer(layer,B);assert depth<100
 exhaust[B]=depth
assert exhaust=={9:16,17:17}
# Recompute the inherited matrix count here as well, keeping this verifier self-contained.
row=[int(i==7) for i in range(15)]
for _ in range(24):row=[sum(row[d-1] for d in range(1,16) if e in edges(15,d)) for e in range(1,16)]
N=row[7];assert N==292366481680;den=3**24
assert (N**100+den**100-1)//den**100==32
output={'status':'passed','scope':'Independent rational certificate and finite bridge/inverse checks; N14 archive and 64,001,096 record tests were not rerun.','certificate_edges_all_widths':edgecount,'width17_edges':60,'certificates':{str(B):{'span':str(v['span']),'lower':{str(d):str(z) for d,z in v['lower'].items()},'upper':{str(d):str(z) for d,z in v['upper'].items()}} for B,v in certs.items()},'base_candidates':candidates,'base_accepted':accepted,'wall_paths':wallpaths,'wall_prefixes':wallprefixes,'C3_80_round_ancestor_counts':ancestry,'C3_9757_inverse_exhaustion_depths':exhaust,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(BASE/'navigation14_audit_verification.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='certificates'},indent=2))
