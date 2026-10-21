"""Exact independent enumeration of the analytically bounded 40 jet states."""
import json

def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def scale(x,n):return(n*x[0],n*x[1])
def timesphi(x):return(x[1],x[0]+x[1])
def dividephi(x):return(x[1]-x[0],x[0])
def conjugate(x):return(x[0]+x[1],-x[1])
def sgn(z):return (z>0)-(z<0)
def algebraic_sign(x):
    # 2(a+b phi) = 2a+b+b sqrt(5).
    A=2*x[0]+x[1]; B=x[1]
    if not B:return sgn(A)
    if not A:return sgn(B)
    if sgn(A)==sgn(B):return sgn(A)
    return sgn(A)*sgn(A*A-5*B*B)

def step(state):
    p,d=state
    epsilon=int(algebraic_sign(sub(conjugate(sub(scale(p,3),timesphi(d))),(1,0)))>0)
    pp=dividephi(sub(p,(epsilon,0)))
    dd=dividephi(sub(d,pp))
    return (pp,dd),epsilon

# Derive candidate list directly from all four exact embedding bounds.
ps=[];ds=[]
for a in range(-20,21):
 for b in range(-20,21):
    x=(a,b);xc=conjugate(x)
    if algebraic_sign(sub(x,(0,-1)))>=0 and algebraic_sign(neg(x))>=0 and algebraic_sign(add(xc,(1,0)))>=0 and algebraic_sign(sub((0,1),xc))>=0:ps.append(x)
    if algebraic_sign(x)>=0 and algebraic_sign(sub((1,1),x))>=0 and algebraic_sign(add(xc,(0,2)))>=0 and algebraic_sign(sub((2,1),xc))>=0:ds.append(x)
assert len(ps)==4 and len(ds)==10
states={(p,d) for p in ps for d in ds}
cycles=set()
for initial in states:
    visited={};s=initial;route=[]
    while s in states and s not in visited:
        visited[s]=len(route);route.append(s);s,_=step(s)
    if s in visited:
        cycle=route[visited[s]:]
        cycles.add(min(tuple(cycle[i:]+cycle[:i]) for i in range(len(cycle))))
assert len(cycles)==3
expected={(((0,0),(0,0)),),(((0,-1),(1,1)),), (((-1,0),(3,-1)),((1,-1),(-2,2)))}
assert cycles==expected,cycles
out={'candidate_p':ps,'candidate_derivative':ds,'candidate_count':len(states),'cycles':[{'states':list(c),'bits':[step(s)[1] for s in c]} for c in sorted(cycles)]}
open('audits/adversarial_jet_cycles.json','w').write(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
