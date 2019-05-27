#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
import matplotlib
dataoffset = pandas.read_excel('은지꾸.xlsx')### offset.excel 파일 이름을 입력하세요.


# In[2]:


print(dataoffset.head())


# In[99]:


def WL(s,w):
    result = dataoffset.iloc[s+2,w+2]
    return result
def FAP(s,w):
    
    total = 0
    a = w
    while w-2 <= a <= w:
        if a == w-1:
            total += WL(s,a)*4
        else:
            total += WL(s,a)
        a=a-1
        total = total
    return total
def FAm(s,w):
    a = s
    if a == -1:
        total = FAP(a,w)*4*3/8
    else :
        total = FAP(a,w)*3/8
    total = total
    return total
def SFAm(w):
    a = -2
    total = 0
    while a <= 0:
        total += FAm(a,w)
        a = a+1
    total = total
    return total
def VAP(w,t):
    result = SFAm(w)*t*2*3/8
    return result
def VVAP(w,t):
    if VAP(w-1,t) == 0:
        result = 0
    else :
        result = VAP(w,t)
    return result
def WAP(w,t):
    if VAP(w-1,t) == 0:
        result = 0
    else :
        result = VAP(w,t)*1.025
    return result
def FyAP(s,w):
    if s == -1:
        result = WL(s,w)*4
    else :
        result = WL(s,w)
    return result
def AwAP(w,t):
    s = 0
    result = 0
    while -2 <= s :
         
        result += FyAP(s,w)
        s= s-1
       
        result1 = result*t*2/3
    return result1
def AAwAP(w,t):
    if AwAP(w-2,t) == 0 or AwAP(w-1,t) == 0 or AwAP(w,t) == 0:
        result = 0
    else :
        result = AAwAP(w,t)
    return result
def OB(w,t):
    if AwAP(w,t) == 0:
        result = 0
    else :
        result = (2/2+VAP(w,t)/AwAP(w,t))/3
    return result
def KbAP(w,t):
    if OB(w,t) == 0:
        result = 0
    else :
        result = w-1 - OB(w,t)
    return result
def xfAm(s,w):
    if s == -2:
        result = (-2)*FAm(s,w)
    elif s == -1:
        result = (-1)*FAm(s,w)   
    else :
        result = 0
    return result
def SxfAm(w):
    s = 0
    total = 0
    while -2<=s:
        total += xfAm(s,w)
        s =s-1
    total = total
    return total
def APb(w,t):
    if SFAm(w) == 0:
        result = 0
    else :
        result = t*SxfAm(w)/SFAm(w)
    return result
def lcbAP(w,t,L):
    if APb(w,t) == 0 or APb(w-1,t) == 0 or APb(w-2,t)==0:
        result = 0
    else :
        result = -(L/2)+APb(w,t)
    return result
def IxAP(w,t):
    s = 0
    result = 0
    while -2<=s:
        if s == -1:
            result += pow(WL(s,w),3)*4
        else :
            result += pow(WL(s,w),3)
        s = s-1
        result = result
    return result*t*2/3*1/3
def SSIx(w,t,j,h):
    result =IxAP(w,t)+IxFP(w,j)+Ix(w,h)
    return result
def SfyAP(w):
    s = 0
    result = 0
    while -2<=s:
        if s == -1:
            result += WL(s,w)*4
        else :
            result += WL(s,w)
        s = s-1
        result = result
    return result
def SxfyAP(w):
    s = 0
    total = 0
    while -2<=s:
        if s == -1:
            total += WL(s,w)*(-1)*4
        elif s == 0:
            total += 0
        else :
            total += WL(s,w) *(-2)
        s =s-1
        total = total
    return total
def APf(w,t):
    if SfyAP(w) == 0:
        result =0
    else :
        result = t*SxfyAP(w)/SfyAP(w)
    return result
def MyAP(w,t,L):
        
    result =AwAP(w,t)*(-L/2+APf(w,t))
    return result
def APIAP(w,t):
    s = 0
    total = 0
    while -2<=s:
        if s == -1:
            total += WL(s,w)*(1)*4
        elif s == 0:
            total += 0
        else :
            total += WL(s,w) *(4)
        s =s-1
        total = total
    return total*t*t*t*2*1/3
def APIY(w,t,L):
    result = APIAP(w,t)+ AwAP(w,t)*L/2*L/2+AwAP(w,t)*(-L)*APf(w,t)
    return result
def SfyFP(w):
    s = 26
    result = 0
    while 24<=s:
        if s == 25:
            result += WL(s,w)*4
        else :
            result += WL(s,w)
        s = s-1
        result = result
    return result
def SFyHFP(s,w):
    
    total = 0
    a = w
    while w-2 <= a <= w:
        if a == w-1:
            total += WL(s,a)*4
        else:
            total += WL(s,a)
        a=a-1
        total = total
    return total
def FAmFP(s,w):
    
    if s == 25:
        total = SFyHFP(s,w)*4*3/8
    else :
        total = SFyHFP(s,w)*3/8
    total = total
    return total
def SFAmFP(w):
    a = 24
    total = 0
    while a <= 26:
        total += FAmFP(a,w)
        a = a+1
    total = total
    return total
def VFP(w,j):
    result = SFAmFP(w)*j*3/8*2
    return result
def AwFP(w,j):
    result = 0 
    s= 24
    while s <= 26:
        if s == 25:
            result+= WL(s,w)*4
        else :
            result += WL(s,w)
        s=s+1
        result = result
    return result*j*2/3
def WFP(w,j):
    result = VFP(w,j)*1.025
    return result
def FPb(w,j):
    s = 24
    result = 0
    while s <=26:
        if s == 24:
            result +=FAmFP(s,w)*0
        elif s == 25:
            result += FAmFP(s,w)*1
        else :
            result += FAmFP(s,w)*2
        s = s+1
        result = result
    return result/SFAmFP(w)*j
def lcbFP(w,j,L):
    result = FPb(w,j)+(L/2)
    return result
def SfVFP(w):
    a = w
    result = 0
    while  w-2<=a:
        if a == w-1:
            result+= SfyFP(a)*4
        else :
            result+= SfyFP(a)
        a= a-1
        result = result
    return result   
def kbFP(w,f):
    a = w
    result = 0
    while  w-2<=a:
        if a == 0:
            result +=0
        elif a == 1:
            result +=0
        elif a == w-1:
            result+= SfyFP(a)*4*(a-1)
        else :
            result+= SfyFP(a)*(a-1)
        a= a-1
        result = result
    return result/SfVFP(w)*f
def IxFP(w,j):
    a = 26
    result = 0
    while a >= 24:
        if a == 25:
            result += pow(WL(a,w),3)*4
        else :
            result += pow(WL(a,w),3)
        a = a-1
        result = result
    return result*2/3*1/3*j
def FPf(w,j):
    a = 26
    result = 0
    result1 = 0
    while a >=24:
        if w == 2:
            result1 = 0
        else :
            if a == 24 :
                result += 0
            elif a == 25:
                result += WL(a,w)*4
            else :
                result += WL(a,w)*2
            a = a-1
            result1 = result/SfyFP(w)*j
    return result1
def SxfyFP(w):
    a = 26
    result = 0
    while a >=24:
        if a == 25:
            result += WL(a,w)*4*1
        elif a == 26:
            result += WL(a,w)*2
        else :
            result +=0
        a =a-1
        result =result
    return result
def FPf(w,j):
    if SxfyFP(w) == 0:
        result = 0
    else :
        result = SxfyFP(w)/SfyFP(w)*j
    return result
def FPMy(w,j,L):
    result =AwFP(w,j)*(-L/2+FPf(w,j))
    return result
def FPIFP(w,j):
    result = 0
    s = 26
    while s >= 24:
        if s  == 24:
            result += 0
        elif s == 25:
            result += WL(s,w)*4
        else:
            result += WL(s,w)*4
        s =s-1
        result = result
    return result*2*1/3*j*j*j
def FPIy(w,j,L):
    result = FPIFP(w,j)+ AwFP(w,j)*(L/2)*(L/2)+AwFP(w,j)*(-L)*FPf(w,j)
    return result
def simy(w):

    total = 0
    s = 0

    while s <= 24 :
       
        if s == 0 or s == 24:
            total += 0.5*WL(s,w)
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += 2*WL(s,w)
        elif s == 2 or s == 22:
            total += WL(s,w)
        elif s == 4 or s == 20:
            total += 1.5*WL(s,w)
        elif s % 2 != 0:
            total += 4*WL(s,w)
        else :
            total += 2*WL(s,w)
        s = s+1    
        total = total

    return total
def simx(n):
    
    total1 = 0
    w = n-2
    while w <= n :
        if w == n or w == n-2 :
            total1 += simy(w)
        else :
            total1 += 4*simy(w)
        w = w+1
        total1 = total1
    return total1 
def W(n,h,f):
    if n == 2:
        result = simx(n)*h/3*f/3*1.025
    else :
        result = simx(n)*h/3*f/3*1.025*2
    return result
def DIS(s,h,f,t,j):
    total2 = 0
    n = s
    while n > 1:
        total2 += W(n,h,f)+ WAP(n,t)+ WFP(n,j)
        n = n-2
        total2 = total2
    return total2
def W(n,h,f):
    if n == 2:
        result = simx(n)*h/3*f/3*1.025
    else :
        result = simx(n)*h/3*f/3*1.025*2
    return result
def SSW(w,j,t):
    result = (VFP(w,j)+VAP(w,t))*1.025
    return result
def Kb(t):
    total3 = 0
    w = t
    while t-2 <= w <= t:
        if w == 0:
            total3 +=0
        elif w == 1:
            total3 += simy(1)*2
        elif w == 2:
            total3 += simy(2)
        elif w == t-1:
            total3 += simy(w)*4*(w-1)
        else :
            total3 += simy(w)*(w-1)
        w= w-1
        total3 = total3
    return total3/simx(t)
def SSM(n,h,f,t,j):
    result = 0
    a = n
    while a >=2:
        result += (KbAP(a,t)*VVAP(a,j)*1.025)+(kbFP(a,f)*VFP(a,j)*1.025)+Kb(a)*W(a,h,f)
        a = a-2
        result = result
    return result
def KB(n,h,f,t,j):
    result = SSM(n,h,f,t,j)/DIS(n,h,f,t,j)
    return result
def X(s,g):
    
    total4 = 0
    w = g
    while g-2 <= w <= g:
        if w == g-1:
            total4 += WL(s,w)*4
        else:
            total4 += WL(s,w)
        w=w-1
        total4 = total4
    return total4
fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]
def lcb(f,h):
    total= 0
    s = 0
    while s <=24:
        if s == 0 or s == 24:
            total += X(s,f) * fx[s]*0.5
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += X(s,f) * fx[s]*2
        elif s == 2 or s == 22:
            total += X(s,f) * fx[s]
        elif s == 4 or s == 20:
            total += X(s,f) * fx[s]*1.5
        elif s % 2 != 0:
            total += X(s,f) * fx[s]*4
        else :
            total += X(s,f) * fx[s]*2
        s=s+1
        total = total
    return total*h/simx(f)
def SSSM(s,h,f,t,j,L):
    result = 0
    n = s
    while n >= 2:
        result += (lcb(n,h)*W(n,h,f)/1.025)+(lcbFP(n,j,L)*VFP(n,j))+(lcbAP(n,t,L)* VAP(n,t))
        n = n-2
    return result
def LCB(s,h,f,t,j,L):
    result = SSSM(s,h,f,t,j,L)/DIS(s,h,f,t,j)
    return result
def Am(a):
    if a == 2:
        result = X(12,a)/3
    else :
        result =X(12,a)*2/3
    return result
def SAm(q):
    total6 = 0
    a = q
    while a >=2:
        total6 += Am(a)
        a = a-2
        total6 = total6
    return total6 
def Cb(m,h,f,L,B,t,j):
    result = DIS(m,h,f,t,j)/1.025/(m-1)/L/B
    return result
def Cm(m,B):
    result = SAm(m)/(m-1)/B
    return result
def Cp(m,h,f,L,B,t,j):
    result = Cb(m,h,f,L,B,t,j)/Cm(m,B)
    return result
def Aw(r,h):
    result = simy(r)*2/3*h
    return result
def Cw(r,h,L,B):
    result = Aw(r,h)/B/L
    return result
def Cvp(r,h,f,L,B,t,j):
    result = Cb(r,h,f,L,B,t,j)/Cw(r,h,L,B)
    return result
def simy3(w):
    total = 0
    s = 0
    while s <= 24 :
        if s == 0 or s == 24:
            total += 0.5*pow(WL(s,w),3)
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += 2*pow(WL(s,w),3)
        elif s == 2 or s == 22:
            total += pow(WL(s,w),3)
        elif s == 4 or s == 20:
            total += 1.5*pow(WL(s,w),3)
        elif s % 2 != 0:
            total += 4*pow(WL(s,w),3)
        else :
            total += 2*pow(WL(s,w),3)
        s = s+1    
        total = total
    return total
def Ix(w,h):
    result = 2/3*h/3*simy3(w)
    return result
def BM(w,h,f,t,j):
    result =(IxAP(w,t) +IxFP(w,j)+Ix(w,h))/DIS(w,h,f,t,j)*1.025
    return result
def KM(w,h,f,t,j):
    result = BM(w,h,f,t,j)+KB(w,h,f,t,j)
    return result
fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]
def xfy(f):
    total= 0
    s = 0
    while s <=24:
        if s == 0 or s == 24:
            total += WL(s,f) * fx[s]*0.5
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += WL(s,f) * fx[s]*2
        elif s == 2 or s == 22:
            total += WL(s,f) * fx[s]
        elif s == 4 or s == 20:
            total += WL(s,f) * fx[s]*1.5
        elif s % 2 != 0:
            total += WL(s,f) * fx[s]*4
        else :
            total += WL(s,f) * fx[s]*2
        s=s+1
        total = total
    return total
def simy1(w):
    total = 0
    s = 0
    while s <= 24 :
        if s == 0 or s == 24:
            total += 0.5*WL(s,w)
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += 2*WL(s,w)
        elif s == 2 or s == 22:
            total += WL(s,w)
        elif s == 4 or s == 20:
            total += 1.5*WL(s,w)
        elif s % 2 != 0:
            total += 4*WL(s,w)
        else :
            total += 2*WL(s,w)
        s = s+1    
        total = total
    return total
def LCF(w,h):
    result = xfy(w)/simy1(w)*h
    return  result
def TPC(r,h):
    result = Aw(r,h)/100*1.025
    return result
def My(w,h):
    result = Aw(w,h)*LCF(w,h)
    return  result
fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]
def x2fy(f):
    total= 0
    s = 0
    while s <=24:
        if s == 0 or s == 24:
            total += WL(s,f) * pow(fx[s],2)*0.5
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += WL(s,f) * pow(fx[s],2)*2
        elif s == 2 or s == 22:
            total += WL(s,f) * pow(fx[s],2)
        elif s == 4 or s == 20:
            total += WL(s,f) * pow(fx[s],2)*1.5
        elif s % 2 != 0:
            total += WL(s,f) * pow(fx[s],2)*4
        else :
            total += WL(s,f) * pow(fx[s],2)*2
        s=s+1
        total = total
    return total
def Iy(w,h):
    result = 2/3*h*h*h*x2fy(w)
    return result
def SSAw(w,h,t,j):
    result = Aw(w,h)+AwAP(w,t)+AwFP(w,j)
    return result
def SSMy(w,h,t,j,L):
    result = My(w,h)+FPMy(w,j,L)+MyAP(w,t,L)
    return result
def SSLCF(w,h,t,j,L):
    result =SSMy(w,h,t,j,L)/ SSAw(w,h,t,j)
    return result
def SSIy(w,h,t,j,L):
    result = Iy(w,h)+APIY(w,t,L)+FPIy(w,j,L)
    return result
def Il(w,h,t,j,L):
    result = SSIy(w,h,t,j,L)-SSLCF(w,h,t,j,L)*SSAw(w,h,t,j)
    return result
def BML(w,h,f,t,j,L):
    result = Il(w,h,t,j,L)
    return  result/(DIS(w,h,f,t,j)/1.025)
def MTC(w,h,f,t,j,L):
    result = DIS(w,h,f,t,j)*BML(w,h,f,t,j,L)/(100*L)
    return result
def Wcm(w,h,t,j,L):
    result = -1*(TPC(w,h)*SSLCF(w,h,t,j,L)/L)
    return result
def KML(w,h,f,t,j,L):
    result = BML(w,h,f,t,j,L)+KB(w,h,f,t,j)
    return result

def DISLIST(w,h,f,t,j):
    a = w
    result=[]
    while a>=2:
        result.append( DIS(a,h,f,t,j))
        a = a-2
    result.reverse()   
    return result
def DISLIST2(w,h,f,t,j):
    a = w
    result=[]
    while a>=2:
        result.append(DIS(a,h,f,t,j)/1.025)
        a = a-2
    result.reverse()
    return result
def AwLIST(w,h):
    a = w
    result=[]
    while a >=2:
        result.append(Aw(a,h))
        a = a-2
    result.reverse()
    return result
def AmLIST(w):
    a = w
    result=[]
    while a >=2:
        result.append(SAm(a))
        a = a-2
    result.reverse()
    return result
def TPCLIST(w,h):
    a = w
    result=[]
    while a >=2:
        result.append(TPC(a,h))
        a = a-2
    result.reverse()
    return result
def MTCLIST(w,h,f,t,j,L):
    a = w
    result=[]
    while a >=2:
        result.append(MTC(a,h,f,t,j,L))
        a = a-2
    result.reverse()
    return result
def WcmLIST(w,h,t,j,L):
    a = w
    result=[]
    while a >=2:
        result.append(Wcm(a,h,t,j,L))
        a = a-2
    result.reverse()
    return result 
def KBLIST(w,h,f,t,j):
    a = w
    result=[]
    while a >=2:
        result.append(KB(a,h,f,t,j))
        a = a-2
    result.reverse()
    return result 
def BMLIST(w,h,f,t,j):
    a = w
    result=[]
    while a >=2:
        result.append (BM(a,h,f,t,j))
        a = a-2
    result.reverse()
    return result
def KMLIST(w,h,f,t,j):
    a = w
    result=[]
    while a >=2:
        result.append(KM(a,h,f,t,j))
        a = a-2
    result.reverse()
    return result 
def LCBLIST(w,h,f,t,j,L):
    a = w
    result=[]
    while a >=2:
        result.append(LCB(a,h,f,t,j,L))
        a = a-2
    result.reverse()
        
    return result
def LCFLIST(w,h,t,j,L):
    a = w
    result=[]
    while a >=2:
        result.append(SSLCF(a,h,t,j,L))
        a = a-2
    result.reverse()
    return result
def BMLLIST(w,h,f,t,j,L):
    a = w
    result=[]
    while a >=2:
        result.append(BML(a,h,f,t,j,L))
        a = a-2
    result.reverse()

    return result
def KMLLIST(w,h,f,t,j,L):
    a = w
    result=[]
    while a >=2:
        result.append(KML(a,h,f,t,j,L))
        a = a-2
    result.reverse()
    return result
def CbLIST(w,h,f,L,B,t,j):
    a = w
    result=[]
    while a >=2:
        result.append(Cb(a,h,f,L,B,t,j))
        a = a-2
    result.reverse()

    return result
def CpLIST(w,h,f,L,B,t,j):
    a = w
    result=[]
    while a >=2:
        result.append(Cp(a,h,f,L,B,t,j))
        a = a-2
    result.reverse()
    return result
def CwLIST(w,h,L,B):
    a = w
    result=[]
    while a >=2:
        result.append(Cw(a,h,B,L))
        a = a-2
    result.reverse()
    return result
def CmLIST(w,B):
    a = w
    result=[]
    while a >=2:
        result.append(Cm(a,B))
        a = a-2
    result.reverse()
    return result
def CvpLIST(w,h,f,L,B,t,j):
    a = w
    result=[]
    while a >=2:
        result.append(Cvp(a,h,f,L,B,t,j))
        a = a-2
    result.reverse()
    return result 
def SSIxLIST(w,t,j,h):
    a = w
    result=[]
    while a >=2:
        result.append(SSIx(a,t,j,h))
        a = a-2
    result.reverse()
    return result 
def IlLIST(w,h,t,j,L):
    a = w
    result=[]
    while a >=2:
        result.append(Il(a,h,t,j,L))
        a = a-2
    result.reverse()
    return result 
def WLlist(w,h,f,L,B):
    a=1
    result=[]
    for a in range(1,w+1,2):
        result.append("%d " %a)
        a=a+2
    return result

import pandas as pd



def Calculation_sheet():
    w = dataoffset.shape[1]-3
    h = WL(7,-1)-WL(6,-1)
    f = 1
    t = -WL(-1,-1)
    j = WL(25,-1)-WL(24,-1)
    L = WL(24, -1)
    B = WL(12,w)
    data = WLlist(w,h,f,L,B)
    
    result= pd.DataFrame(data)
    
    result['배수용적 (▽mld.)'] = DISLIST2(w,h,f,t,j)
    result['배수량 (△mld.)'] = DISLIST(w,h,f,t,j)
    result['수선면적(Aw)'] = AwLIST(w,h)
    result['중앙횡단면적(Am)'] = AmLIST(w)    
    result['매 Cm 배수톤수(TPC)'] = TPCLIST(w,h)
    result['매 Cm 트리밍 정톤수(Wcm)'] = WcmLIST(w,h,t,j,L)
    result['부심위치(KB)'] = KBLIST(w,h,f,t,j)
    result['횡메타센터 반지름(BM)'] = BMLIST(w,h,f,t,j)
    result['횡메타센터 높이(KM)'] = KMLIST(w,h,f,t,j)
    result['종메타센터 반지름(BML)'] = BMLLIST(w,h,f,t,j,L)
    result['종메타센터 높이(KML)'] = KMLLIST(w,h,f,t,j,L)
    result['부심위치(LCB)'] = LCBLIST(w,h,f,t,j,L)
    result['부면심 위치(LCF)'] = LCFLIST(w,h,t,j,L)
    result['방형 계수(Cb)'] = CbLIST(w,h,f,L,B,t,j)
    result['주형 계수(Cp)'] = CpLIST(w,h,f,L,B,t,j)
    result['수선면 계수(Cw)'] = CwLIST(w,h,L,B)
    result['중앙 횡단면 계수(Cm)'] = CmLIST(w,B)
    result['연직 주형 계수(Cvp)'] = CvpLIST(w,h,f,L,B,t,j)
    result['It'] = SSIxLIST(w,t,j,h)
    result['Il'] = IlLIST(w,h,t,j,L)
    
    
    return result




import matplotlib.pyplot as plt

def Hydrostatic_curve():
    w = dataoffset.shape[1]-3
    h = WL(7,-1)-WL(6,-1)
    f = 1
    t = -WL(-1,-1)
    j = WL(25,-1)-WL(24,-1)
    L = WL(24, -1)
    B = WL(12,w)
    data = WLlist(w,h,f,L,B)
    y = range(2,w)
    plt.yticks(range(2,w,2))
    plt.xticks(range(-5,150,5))
    x = [DIS(a+1,h,f,t,j)/8000for a in y]
    z = [DIS(a+1,h,f,t,j)/8000/1.025 for a in y]
    e = [KB(a+1,h,f,t,j) for a in y]
    g = [Aw(a+1,h)/600 for a in y]
    p = [TPC(a+1,h)/20 for a in y]
    u = [Cm(a+1,B)/0.05 for a in y]
    c = [Cw(a+1,h,L,B)/0.05 for a in y]
    q = [KM(a+1,h,f,t,j)/2 for a in y]
    m = [MTC(a+1,h,f,t,j,L)/200 for a in y]
    v = [KML(a+1,h,f,t,j,L)/50 for a in y]
    ww = [Cb(a+1,h,f,L,B,t,j)/0.05 for a in y]
    ii = [Cp(a+1,h,f,L,B,t,j)/0.05 for a in y]
    kk = [SSLCF(a+1,h,t,j,L) for a in y]
    hh = [LCB(a+1,h,f,t,j,L) for a in y]
    ll = [Cvp(a+1,h,f,L,B,t,j)/0.05 for a in y]
    
    plt.plot(x,y,'r')
    plt.plot(z,y,'b')
    plt.plot(e,y,'g')
    plt.plot(g,y,'c')
    plt.plot(p,y,'m')     
    plt.plot(u,y,'k')      
    plt.plot(c,y,'y')    
    plt.plot(q,y,color = 'brown')
    plt.plot(m,y,color = 'grey')  
    plt.plot(v,y,color = 'violet') 
    plt.plot(ww,y,color = 'orange') 
    plt.plot(ii,y,'--') 
    plt.plot(kk,y,color = 'tan') 
    plt.plot(hh,y,color = 'maroon') 
    plt.plot(ll,y,color = 'navy') 
    plt.grid()
    plt.legend(['△ 1= 8000t','▽ 1= 8000t','KB 1= 1m','Aw 1= 600m^2','TPC 1= 20t','Cm 1= 0.05','Cw 1= 0.05','KM 1= 2m','MTC 1= 200t-m','KML 1= 50m','Cb 1= 0.05','Cp 1= 0.05','LCF 1= 1m','LCB 1= 1m','Cvp 1= 0.05'])
    
    return plt.show()








