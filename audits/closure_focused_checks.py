"""Independent exact checks of representative audited identities, not universal orbit evidence."""
import json,re
from pathlib import Path
from fractions import Fraction
BASE=Path(__file__).resolve().parent.parent

def add(x,y):return(x[0]+y[0],x[1]+y[1])
def mul(x,y):return(x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def neg(x):return(-x[0],-x[1])
def sign_sqrt(A,B):
 if B==0:return (A>0)-(A<0)
 if A==0:return (B>0)-(B<0)
 if A>0 and B>0:return 1
 if A<0 and B<0:return -1
 d=A*A-5*B*B
 return ((d>0)-(d<0))*(1 if A>0 else -1)
def sign_conj(x):return sign_sqrt(2*x[0]+x[1],-x[1])
def step(p,d):
 h=add(add((3*p[0],3*p[1]),neg(mul((0,1),d))),(-1,0))
 bit=int(sign_conj(h)>0)
 pn=mul(add(p,(-bit,0)),(-1,1)); dn=mul(add(d,neg(pn)),(-1,1))
 return bit,pn,dn
rows=[]
for line in (BASE/'sources/closure/decoder_table.md').read_text().splitlines():
 m=re.fullmatch(r'\| (\d+) \| \[(-?\d+), (-?\d+)\] \| \[(-?\d+), (-?\d+)\] \| ([01]) \| (outside|\d+) \|',line)
 if m:
  a=m.groups();rows.append((int(a[0]),(int(a[1]),int(a[2])),(int(a[3]),int(a[4])),int(a[5]),None if a[6]=='outside' else int(a[6])))
assert len(rows)==40
lookup={(p,d):i for i,p,d,b,n in rows}; nxt={}
for i,p,d,b,n in rows:
 b2,p2,d2=step(p,d); assert b2==b and lookup.get((p2,d2))==n,(i,b2,p2,d2)
 nxt[i]=n
cycles=set()
for start in nxt:
 seen={};cur=start;path=[]
 while cur is not None and cur not in seen:
  seen[cur]=len(path);path.append(cur);cur=nxt[cur]
 if cur is not None:
  cyc=path[seen[cur]:];mi=cyc.index(min(cyc));cycles.add(tuple(cyc[mi:]+cyc[:mi]))
assert cycles=={(9,30),(16,),(23,)}
# Check binary finite decoder without floating point.
for n in range(4096):
 p=(0,0);d=(0,0);q=(1,0);qm=(0,0)
 for i in range(n.bit_length()):
  if n>>i&1:
   p=add(p,q)
   if i:d=add(d,(i*qm[0],i*qm[1]))
  qm=q;q=mul(q,(0,1))
 x=n
 while x:
  b,p,d=step(p,d);assert b==x%2;x//=2
 assert p==d==(0,0)
# Exact benchmark proof words.
def run(n,w):
 for ch in w:
  if ch=='H':assert n%2==0;n//=2
  else:assert n>1 and n%2;n=(3*n+1)//2
 return n
bench=[]
for ell,tw,sw,A,B,D in [(109,'OOOOOHOOHHHHHO','HOOHOOOHOOHH',6561,4489,4096),(201,'OOOOOHOHHHHHO','HOOHOHOOOHH',2187,1187,2048),(157,'OOOOOHOOHOHHHHHO','HOOHOOOOHHOOHH',19683,11035,16384)]:
 N=4*8**ell-5;a=3*8**ell-5;z=(A*9**ell-B)//D
 assert run(N,'OOH'*ell+tw)==run(a,'OOH'*ell+sw)==z
 bench.append({'ell':ell,'source_below_original':a<N,'target_length':3*ell+len(tw),'source_length':3*ell+len(sw)})
# Collision capacity and source grammar exact rational controls.
lam=Fraction(3136,6561)+Fraction(8,27)+Fraction(1,8)+Fraction(1,64)
assert lam==Fraction(384169,419904) and lam<Fraction(11,12)
assert Fraction(9,16)**19<Fraction(29,50)**20
assert Fraction(3,8)**19<Fraction(197,500)**20
assert 4**171>100000**20
# Golden scalar false quotient.
def P(n):
 out=(0,0);v=(1,0)
 while n:
  if n&1:out=add(out,v)
  n//=2;v=mul(v,(0,1))
 return out
assert P(15)==P(19) and P(23)==P(25)
assert (3*15+1)//2==23 and (3*25+1)//4==19
out={'status':'passed','scope':'Exact representative checks; analytic proofs control unbounded parameters. No downloaded scripts run and no Lean build claimed.','decoder_table_rows':40,'decoder_cycles':[list(c) for c in sorted(cycles)],'finite_decoder_inputs':4096,'benchmark_certificates':bench,'capacity_lambda':str(lam),'grammar_exponent':'19/20, exact twentieth-power inequalities','scalar_false_quotient_cycle':'15->23;25->19, with equal P15=P19 and P23=P25','draft_correction':'Sibling obstruction requires k>=1,1<=m<=L; m=0 separately E_k(X)>3X.'}
(BASE/'audits/closure_focused_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
