"""Fresh adversarial checks of selected chapter formulas, not universal proofs."""
from itertools import product
from fractions import Fraction
from math import isqrt
import json

def v2(n):
    assert n>0
    return (n&-n).bit_length()-1

def C(n): return n//2 if n%2==0 else (3*n+1)//2

def S(n): return (3*n+1)>>v2(3*n+1)

def iterate(n,k):
    for _ in range(k): n=C(n)
    return n

def core(n):
    if n<=2 or not n%2:return False
    h=v2(n+1); u=(n+1)>>h; b=v2(3**h*u-1)
    return v2(3*n-1) in (2,4) and b==1 and (n+1)%3!=0

def schema(n):
    if n<=2 or not n%2:return False
    h=v2(n+1);u=(n+1)>>h
    if h==2:return n%96 in (27,91)
    if h>=3 and h%2:return u%12 in (1,5)
    if h>=4:return u%12 in (7,11)
    return False

def D(n):
    if not n%2:return n//2,'even'
    if (n+1)%3==0:return (2*n-1)//3,'inverse'
    h=v2(n+1);u=(n+1)>>h;b=v2(3**h*u-1)
    if b>=2:return (n-1)//2,'merger'
    q=v2(3*n-1);w=(3*n-1)>>q
    if q==1:return S(n),'q1'
    if q%2==0:return 2*3**(q//2-1)*w+1,'evenq'
    z=3**(q//2)*w+1
    return z>>v2(z),'oddq'

out={}
branches={}
for n in range(2,200001):
    assert core(n)==schema(n),(n,'schema')
    if core(n):
        h=v2(n+1);u=(n+1)>>h;un=(3**h*u-1)//2
        assert (un+5)*2**(h+1)<=3**h*(n+5),(n,'core shift')
        assert iterate(n,h+1)==un,(n,'core time')
    else:
        dn,branch=D(n); branches[branch]=branches.get(branch,0)+1
        assert 7*(dn+5)<=6*(n+5),(n,dn,branch)
        if branch=='merger':
            h=v2(n+1);u=(n+1)>>h
            assert iterate(n,h+2)==iterate(dn,h+1)==(3**h*u-1)//4,(n,'merger')
        if branch=='inverse':assert C(dn)==n
out['residual_normalizer']={'sources':199999,'branches':branches}

# Integral exact lower/upper square-root enclosures.
def sqrt_enclosure(n,den=10**12):
    lo=isqrt(n*den*den)
    return Fraction(lo,den),Fraction(lo if lo*lo==n*den*den else lo+1,den)
packet_checks=0
for d in [1,3,5,7,9,31,101]:
    starts=range(1024*d+1,1024*d+10002,2)
    if d==1:starts=list(range(1,1025,2))+list(starts)
    for n in starts:
        rho=Fraction(9999,10000) if n<1025 else Fraction(99,100)
        lhs=sum(sqrt_enclosure(S(x)-1)[1] for x in range(n,n+8*d,2*d))
        rhs=rho*sum(sqrt_enclosure(x-1)[0] for x in range(n,n+8*d,2*d))
        assert lhs<rhs,(n,d,lhs,rhs)
        packet_checks+=1
out['packet_contraction']={'exact_rational_enclosures':packet_checks}

# Direct action representation over Z[q]/(q^2-q-1)^2.
seen={}
for n in range(65536):
    A=B=Cc=Dd=0
    for digit in bin(n)[2:]:
        A,B,Cc,Dd=B+int(digit),A+B,B+Dd,Cc+Dd
    jet=(A,B,B-Cc+2*Dd,2*Cc+Dd)
    assert jet not in seen,(n,seen.get(jet),'jet collision')
    seen[jet]=n
out['first_jets']={'distinct_sources':len(seen)}

# Every canonical reachable state has a terminating repunit representative.
automata=0
for q in range(1,5):
    maps=list(product(range(q),repeat=q))
    for kind in ['involution','idempotent']:
        eligible=[a for a in maps if all(a[a[x]]==(x if kind=='involution' else a[x]) for x in range(q))]
        for a in eligible:
            for b in eligible:
                reached={0}; queue=[0]
                while queue:
                    x=queue.pop()
                    for t in [a[x],b[x]]:
                        if t not in reached:reached.add(t);queue.append(t)
                canonical={b[x] for x in reached}
                reps=set()
                for j in range(1,2*q+2):
                    z=(4**j-1)//3
                    for n in [z,2*z]:
                        x=0
                        for t in bin(n)[:1:-1]:x=(b if t=='1' else a)[x]
                        reps.add(x)
                assert canonical<=reps,(q,kind,a,b,canonical,reps)
                automata+=1
out['involution_idempotent_automata']={'transition_pairs':automata,'states_up_to':4}

# Source-budget bootstrap thresholds, including just after binary jumps.
for m in range(32,100001):
    ell=m.bit_length() # ceil(log2(m+1))
    assert 3*m>=16*ell
for m in range(64,100001):assert m>=8*m.bit_length()
assert 5**16>2**37
out['navigation_thresholds']={'drawdown_threshold_range':[32,100000],'multiscale_bootstrap_range':[64,100000],'integer_growth_inequality':True}

# Every finite positive depth word's exact source cylinder, including small reps.
wordchecks=0
for m in range(1,6):
    for word in product(range(1,5),repeat=m):
        B=0;H=0
        for a in word:B=3*B+2**H;H+=a
        mod=2**(H+1);r=((2**H-B)*pow(3**m,-1,mod))%mod
        assert r>0 and r%2
        for x in [r,r+mod]:
            n=x
            for a in word:
                assert v2(3*n+1)==a,(word,x,n,a)
                n=(3*n+1)>>a
            assert mod//2*n==3**m*x+B
            wordchecks+=1
out['exact_depth_guards']={'source_word_pairs':wordchecks}
print(json.dumps(out,indent=2))
open('audits/adversarial_checks.json','w').write(json.dumps(out,indent=2)+'\n')
