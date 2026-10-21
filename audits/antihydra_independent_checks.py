"""Independent, bounded algebra/native checks for the pre-paper review.
No imports from research archives. These checks supplement, not replace, proofs.
"""
import json
from pathlib import Path
from fractions import Fraction
from itertools import product

def v2(n):
    assert n > 0
    return (n & -n).bit_length()-1

def f(x): return 3*x//2
def phase(y):
    k=v2(3*y+1)
    return 3**(k-1)*((3*y+1)//2**k), k

counts={}
for y in range(1,20000,2):
    z,k=phase(y);x=y+1;bb=0;mm=0
    for j in range(k):
        assert (x%2)==(j>0)
        bb+=2-3*(x%2);mm=min(mm,bb);x=f(x)
    assert x==z+1 and x%2==0 and bb==3-k and mm==min(0,3-k)
    D=3**k-2**k;w=D*y+3**(k-1);mu=v2(w);ell=(mu-1)//k
    assert ell>=1
    z=y
    for j in range(ell):
        z,cost=phase(z);assert cost==k
    nextcost=v2(3*z+1);e=mu-k*ell;V=3**(k*ell)*(w//2**mu)
    assert D*z+3**(k-1)==2**e*V
    assert nextcost==(e if e<k else k+v2(3*V-1)) and nextcost!=k
counts['phase_and_maximal_run_states']=10000

words=0
for n in range(1,10):
    for w in product([0,1],repeat=n):
        A=sum(3**(n-1-j)*2**j*p for j,p in enumerate(w))
        rho=(A*pow(3**n,-1,2**n))%(2**n)
        for lift in [1,2]:
            x=rho+lift*2**n;src=x
            for p in w:assert x%2==p;x=f(x)
            assert 2**n*x==3**n*src-A
        words+=1
counts['parity_word_guards_two_lifts']=words

unsafe=0
for k in range(1,6):
  for ell in range(1,6):
    for h in range(7):
      M=2**(h+3*ell+1);u=((2**ell-3**ell)*pow(3**(k+ell),-1,M))%M
      assert u%2==1 and v2(1+3**k*u)==ell
      nxt=3**ell*((1+3**k*u)//2**ell)
      assert v2(nxt-1)>h+2*ell
      unsafe+=1
counts['unsafe_cofactor_families']=unsafe

families=0
for j in range(1,5):
  for t in range(1,16,2):
    R=(3**(2**j*t)-1)//2**(j+2)
    for kind in ['odd','even']:
      a=2**j*t-(kind=='odd');x=2**a;b=0
      w=[0]*a+([1]+[0]*j if kind=='odd' else [1]*(j+2))
      for p in w:assert x%2==p;b+=2-3*p;assert b>=0;x=f(x)
      target=2*3**j*R if kind=='odd' else 3**(j+2)*R+1
      budget=2**(j+1)*t+2*j-3 if kind=='odd' else 2**(j+1)*t-j-2
      assert (x,b)==(target,budget)
      families+=1
counts['honest_source_prefixes']=families

table='1RB1LC_1RC1RB_1RD0LE_1LA1LD_1RH0LF_1LD1LA'
rules={(s,b):(int(row[3*b]),1 if row[3*b+1]=='R' else -1,row[3*b+2]) for s,row in zip('ABCDEF',table.split('_')) for b in [0,1]}
def native(n,stopreturn=True):
    ones=set(range(1,n+1));head=0;state='A';t=0
    while t<200000:
        bit=int(head in ones);write,d,state=rules[state,bit]
        if write:ones.add(head)
        else:ones.discard(head)
        head+=d;t+=1
        if state=='H':return ('H',t)
        if stopreturn and state=='A' and head not in ones and ones==set(range(head+1,head+len(ones)+1)):
            return (len(ones),t)
    raise AssertionError('native cap')
for n in range(128):
    k,r=divmod(n,4)
    expected=[(6*k+8,6*k*k+26*k+21),(6*k+7,6*k*k+24*k+19),(6*k+10,6*k*k+30*k+31),('H',8*k+14)][r]
    assert native(n)==expected,(n,native(n),expected)
assert native(5,False)==('H',667)
counts['id7546_native_all_residue_returns']=128
counts['id7546_native_same_seed_control_steps']=667

ah='1RB1RA_0LC1LE_1LD1LC_1LA0LB_1LF1RE_---0RA'
arules={}
for s,row in zip('ABCDEF',ah.split('_')):
    for bit in [0,1]:
        r=row[3*bit:3*bit+3]
        if r!='---':arules[s,bit]=(int(r[0]),1 if r[1]=='R' else -1,r[2])
def encoding(x,b):
    a=x-4
    return set(range(-a,0))|set(range(-a-1-b,-a-1))
def ahstep(ones,head,state):
    bit=int(head in ones);write,d,nstate=arules[state,bit]
    if write:ones.add(head)
    else:ones.discard(head)
    return head+d,nstate
ones=set();head=0;state='A'
for _ in range(11):head,state=ahstep(ones,head,state)
assert state=='E' and {p-head for p in ones}==encoding(8,0)
for x in range(6,65):
    for b in range(9):
        n=(x-4)//2;ones=encoding(x,b);head=0;state='E'
        halt=x%2==1 and b==0
        clock=(3*n*n+9*n-1 if halt else 3*n*n+12*n+5) if x%2 else 2*b+3*n*n+12*n+11
        for _ in range(clock):head,state=ahstep(ones,head,state)
        if halt:assert state=='F' and head not in ones
        else:assert state=='E' and {p-head for p in ones}==encoding(f(x),b+2-3*(x%2))
counts['antihydra_native_endpoint_and_clock_checks']=531
counts['antihydra_native_initialization_steps']=11

x=8;b=0;cap=0;peak=0;popfail=None;intervalfail=None;capfail=None
for step in range(1,1154):
    p=x%2;b+=2-3*p;cap=min(11,cap+2-3*p);x=f(x);peak=max(peak,b)
    if popfail is None and b+1<x.bit_count():popfail=step
    if step>=1 and x%2==0:
        margin=2**(b+4+(b%2))-(3*x-2)
        if intervalfail is None and margin<=0:intervalfail=step
    if capfail is None and cap<0:capfail=(step,b,peak,peak-b)
    assert b>=0
assert popfail==45 and intervalfail==40 and capfail==(1153,572,584,12)
counts['actual_source_controls']={'popcount_first_loss':popfail,'interval_first_loss':intervalfail,'cap11_first_failure':capfail}
x=16;b=0;t=0
while b>=0:p=x%2;x=f(x);b+=2-3*p;t+=1
assert (t,x,b)==(22,118342,-1)
counts['source16_first_failure']=[t,x,b]

S=30;m=10;y=17134933;a,b,q,d,t=9,17,8,4,1
E=a*3**(S+d*t)-q*2**S*y
lo=(b-q)*3**S+q*3**(S-m)*2**m
hi=b*3**S-q*(3**(S-1)+3**(m-1)*2**(S-m+1)-2**S)
assert E==2906681588696785 and lo==1881583926664833 and hi==2950784590682033 and lo<=E<=hi
assert v2(3*y+1)==13 and 9+3*m-S==9
counts['coefficient_envelope_counterexample']='verified, off-source relaxation only'

# The shadow extension uses 2-adic parity on odd-denominator rationals,
# not the real-floor function on arbitrary rationals.
from fractions import Fraction
def rational_driver(z):
    assert z.denominator % 2 == 1
    return (3*z - z.numerator%2)/2
for t in range(1,40,2):
    R=(3**(4*t)-1)//16;K=v2(243*R+1);x=18*R;b=8*t+1
    z=Fraction(-2,27)
    for step in range(K+1):
        assert x%2==z.numerator%2
        b+=2-3*(x%2);x=f(x);z=rational_driver(z)
        assert b>=0
    assert x%2!=z.numerator%2 and b>=11
    assert rational_driver(1-z)==1-rational_driver(z)
    if t==1:assert (K,x,b)==(6,1531,11)
counts['honest_rational_shadow_and_departure_checks']=20

out=Path(__file__).with_name('antihydra_independent_checks.json')
out.write_text(json.dumps({'status':'passed','counts':counts,'scope':'bounded independent review checks; not an infinite safety proof'},indent=2))
print(out.read_text())
