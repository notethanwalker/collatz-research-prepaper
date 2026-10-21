"""Independent, standard-library transcription checks for the pre-paper audit.
Not a replay of the research archives and not a proof of any infinite-orbit claim.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import json, hashlib, pathlib

BASE=pathlib.Path(__file__).resolve().parent
counts={}
def tick(k,n=1): counts[k]=counts.get(k,0)+n
def vp(n,p=2):
    assert n
    n=abs(n); k=0
    while n%p==0:n//=p;k+=1
    return k
def compile(w,c=3,rho=1):
    P,B,H=1,0,0
    for a in w:
        p=c*rho**(a-1); q=rho**(a-1)
        P,B,H=p*P,p*B+q*2**H,H+a
    return P,B,H
def run(n,w,c=3,rho=1):
    path=[n]
    for a in w:
        assert vp(c*n+1)==a,(c,rho,n,a,vp(c*n+1))
        n=rho**(a-1)*(c*n+1)//2**a
        path.append(n)
    return path
def cylinder(w,c=3,rho=1):
    P,B,H=compile(w,c,rho)
    M=2**(H+1)
    return ((2**H-B)*pow(P,-1,M))%M,M
def scores(w):
    H=0;ds=[0];ws=[0];bs=[0]
    for i,a in enumerate(w,1):
        H+=a;ds.append(H-2*i);ws.append(9*i-4*H);bs.append(3*i-H)
    return ds,ws,bs
def compositions(s,m):
    if m==1:
        if s>=1:yield (s,)
    else:
        for a in range(1,s-m+2):
            for tail in compositions(s-a,m-1):yield (a,)+tail
def trees(m):
    for w in compositions(2*m-1,m):
        ds,_,_=scores(w)
        if min(ds[:-1])>=0:yield w
def cap(n,R,c,rho):
    q=1
    for i in range(1,R):
        a=vp(c*n+1); n=rho**(a-1)*(c*n+1)//2**a
        q+=a-2
        if q==0:return i
    return R
def recovery_cap(n,R,c,rho,strict=False):
    W=0
    for i in range(1,R):
        a=vp(c*n+1);n=rho**(a-1)*(c*n+1)//2**a;W+=9-4*a
        if W>0 or (W==0 and not strict):return i
    return R

# N05 event/neutral algebra and N09 E cofactor turnover from actual odd states.
for c,rho in [(3,1),(5,1),(3,3)]:
    d=c*rho-4
    for n in range(3,4000,2):
        a=vp(c*n+1); y=rho**(a-1)*(c*n+1)//2**a
        Z=d*n+rho;Zy=d*y+rho
        assert F(Zy)==F(c*rho,4)*F(rho,2)**(a-2)*Z+rho*(1-F(rho,2)**(a-2))
        tick('normal_form')
        Q=c*d*n+d+2*rho;q=vp(Q)
        if q%2==0:
            j=q//2;w=(1,)+(2,)*(j-1);out=run(n,w,c,rho)[-1]
            u=abs(Q)//2**q
            Q2=c*d*out+d+2*rho;u2=abs(Q2)//2**vp(Q2)
            import math
            assert math.gcd(u,u2)==1 and u>1 and u!=u2
            tick('cofactor_turnover')

# N06/N07 exact Catalan tree coding and envelope checks through size seven.
for m in range(1,8):
    tw=list(trees(m));assert len(tw)==comb(2*m-2,m-1)//m
    for c,rho in [(3,1),(5,1),(3,3)]:
        bU=((c*rho)**m-4**m)//(c*rho-4)
        bS=(c*rho)**(m-1)+2**m*(c**(m-1)-2**(m-1))//(c-2)
        assert compile((2,)*(m-1)+(1,),c,rho)[1]==bU
        assert compile((m,)+(1,)*(m-1),c,rho)[1]==bS
        for w in tw:
            P,B,H=compile(w,c,rho);assert min(bU,bS)<=B<=max(bU,bS)
            r,M=cylinder(w,c,rho); n=r+M
            end=run(n,w,c,rho)[-1];assert end==(P*n+B)//2**H
            ds,ws,bs=scores(w)
            assert -min(bs)<=max(0,m-3)
            assert -min(ws)<=max(0,4*m-9)
            if c==3 and rho==1:assert (end>n)==(m<=2)
            tick('tree_coding_and_bounds')

# N07 arbitrary-frontier formulas and tilted workload identification.
for L in range(1,7):
    for w in product(range(1,5),repeat=L):
        ds,ws,bs=scores(w);mu=min(ds);nu=max(ds)
        R=max(ds[t]-min(ds[:t+1]) for t in range(L+1))
        for q0 in [1,2,5]:
            q=q0;k=0;mx=q
            for a in w:
                q+=a-2
                if q==0:q=1;k+=1
                mx=max(mx,q)
            assert k==max(0,1-q0-mu) and q==q0+ds[-1]+k
            assert mx==max(q0+nu,1+R)
            if q0==1:
                assert q-1==ds[-1]-min(ds)
                assert 4*(q-1)>=max(ws)-ws[-1]
            tick('frontier_and_tilt')

# Exact cap-five masks and all odd-affine interval discrepancy constants.
mask_results=[]
for c,rho in [(3,1),(5,1),(3,3)]:
    vals=[cap(2*z+1,5,c,rho) for z in range(128)]
    assert [vals.count(k) for k in range(1,6)]==[64,16,8,5,35]
    spans=[]
    for A in range(1,128,2):
        pref=[0]
        for t in range(128):pref.append(pref[-1]+128*vals[(A*t)%128]-315)
        assert pref[-1]==0;spans.append(max(pref)-min(pref))
    assert max(spans)==(1001 if rho==3 else 1097)
    weak=[recovery_cap(n,5,c,rho) for n in range(1,1024,2)]
    strict=[recovery_cap(n,5,c,rho,True) for n in range(1,512,2)]
    assert [weak.count(k) for k in range(1,6)]==[384,32,16,24,56]
    assert [strict.count(k) for k in range(1,6)]==[192,16,8,5,35]
    mask_results.append({'map':[c,rho],'tree_cap5':[64,16,8,5,35],'affine_span_numerator':max(spans),'recovery_weak_cap5':[384,32,16,24,56],'recovery_strict_cap5':[192,16,8,5,35]})
    tick('mask_source_evaluations',128+512+256)

# N10 exact seven-feature impossibility certificate.
def features(x):
    return [1,x.bit_length(),x.bit_count(),bin(x)[2:].count('01')+1,vp(x),vp(x-1),vp(x+1)]
rows=[]
for kind,x,weight in [('nonnegative',256,F(13,420)),('step',279,F(2,7)),('step',281,F(5,21)),('step',285,F(43,84)),('step',301,F(5,21)),('step',342,F(1,7)),('step',439,F(1,84)),('initial',8,F(13,420))]:
    if kind=='nonnegative':row=[-v for v in features(x)];rhs=0
    elif kind=='initial':row=features(x);rhs=0
    else:row=[b-a for a,b in zip(features(x),features(3*x//2))];rhs=2-3*(x%2)
    rows.append((row,rhs,weight))
assert [sum(w*r[j] for r,_,w in rows) for j in range(7)]==[0]*7
assert sum(w*b for _,b,w in rows)==-1
tick('potential_certificate_rows',8)

# N11 credit envelope and shape extrema for all weak/strict packets through length six.
for L in range(1,7):
    for g in range(6):
        if (9*L-g)%4:continue
        H=(9*L-g)//4
        for w in compositions(H,L):
            ds,ws,bs=scores(w)
            if min(ws[:-1])>0:continue
            strict=g>0 and max(ws[1:-1],default=0)<=0
            weak=g>=0 and max(ws[1:-1],default=-1)<0
            if not (strict or weak):continue
            assert -min(ws)<=max(0,5*(L-1)-g)
            assert -min(bs)<=max(0,F(5*L-g-8,4))
            tick('recovery_packet_bounds')

# N12/N13 exact region workload including the concealed maximum.
for j in range(1,20):
    for h in range(1,12):
        w=(1,)+(2,)*(j-1)+(2+h,)
        for theta in [F(2),F(9,4),F(5,2),F(3)]:
            g=(theta-2)*(j+1)+1-h;q=h-(theta-2)
            for incoming in [F(0),F(2),F(20)]:
                U=incoming
                for a in w:U=max(0,U+a-theta)
                assert U==max(incoming-g,q)
                tick('region_tilt_transfer')

# N13 narrow-band inverse spacing, finite neutral-loop census, exact witness paths.
def adjacency(B):
    return [[int((e-d+9)%4==0 and (e-d+9)//4>=1) for e in range(1,B+1)] for d in range(1,B+1)]
v14=[9003,10863,11484,10278,9003,10863,11484,10278,9003,7862,7863,6450,5577,4861]
v15=[1713,2004,2043,1998,1713,2004,2043,1998,1713,1433,1375,1317,1047,862,707]
for B,v,target in [(14,v14,3),(15,v15,-174)]:
    A=adjacency(B)
    assert [3*v[i]-sum(A[i][j]*v[j] for j in range(B)) for i in range(B)]==[target]*B
A=adjacency(15);row=[int(i==7) for i in range(15)]
for _ in range(24):row=[sum(row[i]*A[i][j] for i in range(15)) for j in range(15)]
assert row[7]==292366481680>3**24
census={}
allwords=list(compositions(18,8));assert len(allwords)==19448
expected={4:[1,1,1,1],5:[4,4,4,4],6:[8,8,8,8],7:[32,32,32,32],8:[128,128,128,128],9:[288,284,288,288],16:[1926,1192,1926,1926],17:[2264,1312,2263,2264]}
for B,exp in expected.items():
    words=[w for w in allwords if all(1<=2-v<=B for v in scores(w)[1])]
    got=[len(words)]
    for c,rho in [(3,1),(5,1),(3,3)]:
        got.append(len({compile(w,c,rho)[1]%compile(w,c,rho)[0] for w in words}))
    assert got==exp,(B,got,exp);census[B]=got
    tick('loop_census_words',len(words))
for c,n,w,v,B in [(3,389809,(2,4,2,2,1,3,2,2),(3,2,2,2,4,1,2,2),9),(5,417135,(2,3,2,2,2,5,1,1),(3,4,2,2,4,1,1,1),17)]:
    pw=run(n,w,c);pv=run(n-4,v,c);assert pw[-1]==pv[-1]
    ds,ws,bs=scores(w);dt,wt,bt=scores(v)
    assert all(1<=2-x<=B for x in ws+wt)
    assert min(ds[:-1])>=0 and min(dt[:-1])>=0
    P,Bw,H=compile(w,c);_,Bv,_=compile(v,c)
    assert Bv-Bw==4*P
    if c==5:assert (-min(bs),-min(bt),-min(ws),-min(wt))==(0,1,10,15)
    tick('sharp_neutral_merger_pairs')

# Full-width-five last-choice decoding / prime separation.
Pword=(2,3,2,2);Qword=(3,2,2,2)
for c,rho,r,h in [(3,1,4,2),(5,1,4,2),(3,3,9,5)]:
    for k in range(1,9):
        codes=[]
        for bits in product([0,1],repeat=k):
            w=sum((Pword if b==0 else Qword for b in bits),())
            P,B,H=compile(w,c,rho);codes.append(B%P)
        assert len(set(codes))==2**k
        tick('width5_codes',len(codes))

out={'status':'passed','scope':'Independent small finite checks and full 19,448-word eight-update census; not archive reproduction or infinite-orbit validation.','counts':counts,'mask_results':mask_results,'neutral_loop_census':census,'band15_closed_paths_24_debt8':row[7],'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
(BASE/'navigation_audit_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
