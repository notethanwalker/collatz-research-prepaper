from fractions import Fraction
from math import isqrt
from itertools import product
import json
from pathlib import Path

def v2(n):
 assert n>0
 return (n&-n).bit_length()-1

def C(n):return (3*n+1)//2 if n%2 else n//2
def T(n):return 3*n+1 if n%2 else n//2
def S(n,c=3):
 a=v2(c*n+1);return (c*n+1)>>a,a

def it(f,n,k):
 for _ in range(k):n=f(n)
 return n

def core(n):
 if n<=1 or n%2==0:return False
 h=v2(n+1);u=(n+1)>>h;b=v2(3**h*u-1)
 return v2(3*n-1) in (2,4) and b==1 and (n+1)%3!=0

def profile(n):
 q=v2(3*n-1);w=(3*n-1)>>q
 if q==1:
  a=v2(3*n+1);return (3*n+1)>>a,1+a
 j=q//2
 if q%2==0:return 2*3**(j-1)*w+1,3*j-1
 g=v2(3**j*w+1);return (3**j*w+1)>>g,3*j+2+g

def D(n):
 if n%2==0:return n//2,'even'
 if (n+1)%3==0:return (2*n-1)//3,'inverse'
 h=v2(n+1);u=(n+1)>>h;b=v2(3**h*u-1)
 if b>=2:return (n-1)//2,'merger'
 assert not core(n)
 return profile(n)[0],'profile'

counts={}
n=27;M=H=0;first_dip=None
for t in range(1,112):
 assert n>1
 if n%2:M+=1
 else:H+=1
 n=T(n);q=H-M+1
 assert q>=0
 assert 3**M*27+2**q*(3**M-2**M)>2**H*27
 assert 10**M>3**M*2**H
 if n<27 and first_dip is None:first_dip=(t,n)
assert (n,M,H,first_dip)==(1,41,70,(96,23))
counts['R27_all_preterminal_integer_checks']=111

np=nd=nm=0
for n in range(2,10001):
 if n%2:
  z,t=profile(n);assert it(T,n,t)==z;np+=1
  h=v2(n+1);u=(n+1)>>h;b=v2(3**h*u-1)
  if b>=2:
   assert it(C,n,h+2)==it(C,(n-1)//2,h+1)==(3**h*u-1)//4;nm+=1
 if not core(n):
  d,kind=D(n);assert 7*(d+5)<=6*(n+5);nd+=1
counts.update(regional_clock_checks=np,merger_checks=nm,complement_contractions=nd)

Q=10**12
for n in range(1,1024,2):
 inputs=[n+2*j for j in range(4)]
 outputs=[S(x)[0] for x in inputs]
 lower=sum(isqrt((x-1)*Q*Q) for x in inputs)
 upper=sum(0 if y==1 else isqrt((y-1)*Q*Q)+1 for y in outputs)
 assert 10000*upper<=9999*lower
counts['complete_small_packet_radical_certificates']=512
for n in range(1,3073,2):
 x=n
 for t in range(10000):
  if x==1:break
  x=S(x)[0]
 else:raise AssertionError(n)
counts['certified_odd_base_inputs']=1536
nw=0
for c in (3,5,7):
 for m in range(1,6):
  for word in product(range(1,5),repeat=m):
   H=B=0
   for a in word:B=c*B+2**H;H+=a
   modulus=2**(H+1);r=((2**H-B)*pow(c**m,-1,modulus))%modulus
   assert r%2==1
   for x0 in (r,r+modulus):
    x=x0
    for a in word:
     x,aa=S(x,c);assert aa==a
    assert 2**H*x==c**m*x0+B
   nw+=1
counts['exact_cross_coefficient_depth_words']=nw
for k in range(1,33):
 x=2**(3*k+1)-5
 for a in [1,2]*k:
  x,aa=S(x);assert aa==a
 assert x==2*9**k-5
 y,a=S(x);assert a==3 and y==(3*9**k-7)//4
 assert v2(y+1)-1==v2(k)
counts['pair_burst_and_regeneration_checks']=32
result={'status':'PASS','counts':counts,'scope':'Finite independent exact-integer/regression checks; universal statements rest on displayed proofs, not sampling.'}
Path(__file__).with_name('gdr_verification_results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
