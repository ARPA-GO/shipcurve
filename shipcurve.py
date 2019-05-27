
# coding: utf-8

# In[19]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import matplotlib as mpl
import math
import matplotlib.pyplot as plt

"""
This command lines make Python import offset file from Excel.

"""
dataoffset = pd.read_excel('your excel file name.xlsx')

class data:
    
        
    def WL(self,s,w):
        
        """
        In WL(s,w), 's' is for station number and 'w' for the number of waterline.
        You can command any station and waterline you want.
        This will show how far it is located from baseline and centerline of ship.
        
        """
        result= dataoffset.iloc[s+2,w+2]
        return result


# In[43]:


class ship_transom:
    def __init__(self,f,h,j,t,L):
        self.f=f
        self.h=h
        self.j=j
        self.t=t
        self.L=L
        
    def FAP(self,s,w):
        """
        The command lines are to get the value of ∑f(yH) of stern attachments.
        ∑f(yH) is the value to find the area of midship section.
        You can command FAP(s,w) to get it.
        BUT, you have to be very careful about station number.
        Since, These are about stern attachments, station number starts from AP with number 0.
        And now you will know that if you type -1 in 's', you would get the value which is located middle of transom and AP and -2 is transom of stern.
        
        """
        # self.s=s #__init__ 생성자 함수 없으면 , self 필요없음
        #self.w=w
        #self.a=self.w
        
        a=w
        total=0
        while w-2 <= a <= w:
            if a == w-1:
                total += dataoffset.iloc[s+2,a+2] *4
            else:
                total += dataoffset.iloc[s+2,a+2]
            a =a-1
        total=total    
        return total
    
    def FAm(self,s,w):
        """
        These are to know the area of midship section of the stern.
        Just same as above, AP starts with number 0.
        If you want to know about transom or middle of transom and AP, command -2 , -1 each in 's'.
        It is applicable in other value also, if you are to get the values of something in the place of stern attachments.
        Type the station number and waterline number you want to know.
        
        """
        a=s
        if a == -1:
            total = self.FAP(a,w)*4*3/8
        else:
            total = self.FAP(a,w)*3/8
        total=total
        return total
    
    def SFAm(self,w):
        """
        These command lines are to get the value of ∑f(Am) of stern attachments.
        ∑f(Am) is the value, using to know the displacements of stern attachments part of ship.
        You can command SFAm(w) to get this value.
        And SFAm(w) configures the ∑f(Am) of stern attachments, which has waterline 'w-1' to 'w-2'.
        
        """
        
        a = -2
        total = 0
        while a <=0:
            total += self.FAm(a,w)
            a = a +1
        return total
    
    def VAP(self,w,t):
        """
        Now, you can get the displacements of stern attachments part of ship.
        Displacement is weight of water that a ship pushes aside when it is floating, which in turn is the weight of a ship
        To get this value, we divided ship by station and waterline.
        As you know, you can just type waterline in the place of 'w', and 't' means the space between two station.
        
        """
        result = self.SFAm(w)*self.t*2*3/8
        return result
    
    def VVAP(self,w,t):
        """
        Now, you can get the displacements of stern attachments part of ship.
        Displacement is weight of water that a ship pushes aside when it is floating.
        To get this value, we divided ship by station and waterline.
        As you know, you can just type waterline in the place of 'w', and 't' means the space between two stations.
        
        """    
        
        if self.VAP(w-1,self.t) ==0:
            result = 0
        else:
            result = self.VAP(w,self.t)
        return result
    
    def WAP(self,w,t):
        """
        If you got the displacements of ship, you can definitely know the weight.
        These command lines help to get the weight.
        We got the displacements from just above command function VAP(w-1,t).
        What we have to do is just multiply density of water with its result.
        Since, ARPA-GO helps calculation of ship, the density is 1.025 which is sea water.
        You can change the density freely, if you are necessary to.
        Mentioned before, w is for waterline number, t is for the space between two stations.
        
        """  
        
        if self.VAP(w-1,self.t) ==0:
            result = 0
        else:
            result = self.VAP(w,self.t) * 1.025
        return result
    
    def FyAP(self,s,w):
        """
        FyAP(s,w) is the necessary value to get the water plane area.
        's' is for station number and 'w' is for the number of waterline.
        Don't confuse : Transom of ship is located with station number '-2' and AP is '0'.
        
        """
        if s == -1:
            result = dataoffset.iloc[s+2,w+2] *4
        else:
            result = dataoffset.iloc[s+2,w+2] 
        return result
        
    def AwAP(self,w,t):
        """
        AwAP(w,t) is the command function for water plane area.
        'w' for water line and 't' for the space between stations.
        """
        
        s=0
        result=0
        result1=0
        while -2<=s:
            result+= self.FyAP(s,w)
            s=s-1
            result1=result*self.t*2/3
        return result1
    
    def AAwAP(self,w,t):
        
        if self.AwAP(w-2,self.t) ==0 or self.AwAP(w-1,self.t)==0 or self.AwAP(w,self.t)==0:
            result = 0
        else:
            result = self.AAwAP(w,self.t)
        return result
    
    def OB(self,w,t):
        """
        The command lines help to get the value of OB.
        To prove the stability of ship, you might heard of KB,GM ...
        We put the value of OB to get KB, the distance between keel and the center of buoyancy.
        OB means the distance from center of buoyancy to waterline.
        Thus, KB+OB is the distance between keel and waterline.
        Since it is about stern attachments, the waterline starts with w-1 to w-2.
        
        
        """
        
        if self.AwAP(w,self.t) ==0:
            result = 0
        else:
            result = (2/2+self.VAP(w,self.t)/self.AwAP(w,self.t))/3
        return result
    
    def KbAP(self,w,t):
        """
        KB is the centre of buoyancy which is the height above the keel.
        KbAP(w,t) is to get the value of it.
        
        """
        
        if self.OB(w,self.t)==0:
            result=0
        else:
            result=(w-1)-self.OB(w,self.t)
        return result
    
    def xfAm(self,s,w):
        """
        x' * f(AM) is the value to get the longitudinal center of gravity (LCB) of ship.
        Here, 'w' indicates 'waterline - 1' which means :
        if you want to get the value about waterline number 10, you have to enter 11 in 'w' place.
        's' is same as before.
        Station number of AP is '0'.
        
        """        
        if s == -2:
            result = (-2)*self.FAm(s,w)
        elif s == -1:
            result = (-1)*self.FAm(s,w)   
        else :
            result = 0
        return result

    def SxfAm(self,w):
        """
        The command function SxfAm(w) is the sum of x' * f(AM).
        If you enter waterline you want to know, you will get all station's sum of x' * f(AM).
        This function shows the value of w-1 to w-2's ∑x' * f(AM).
        
        """
        
        s=0
        total=0
        while -2<=s:
            total += self.xfAm(s,w)
            s =s-1
        return total

    def APb(self,w,t):
        """
        These are for APb of stern attachments of ship.
        The inputs are 'w' & 't'.
        Just same as before the waterline expresses w-1 to w-2.
        Enter the waterline what you want to know + 1 in the place of 'w'.
        't' is the distance between two stations.
        
        """
        if self.SFAm(w) == 0:
            result = 0
        else :
            result = self.t*self.SxfAm(w)/self.SFAm(w)
        return result

    def lcbAP(self,w,t,L):
        """
        The centroid of the underwater volume of the ship expressed as a longitudinal location. 
        We call that centroid point as LCB (longitudinal center of gravity) and it is connected with stability of ship.
        To get the value, enter the command function, lcbAP(w,t,L).
        'L' means LBP, in full form Length between perpendiculars.
        
        """
        
        if self.APb(w,self.t) == 0 or self.APb(w-1,self.t) == 0 or self.APb(w-2,self.t)==0:
            result = 0
        else :
            result = -(self.L/2)+self.APb(w,self.t)
        return result

    def IxAP(self,w,t):
        """
        BM is the metacentric radius of ship.
        Transverse metacentric height (BM) = Transverse moment of inertia of waterplane / volume displacement of ship
        To get the parameter BM, transverse moment of inertia is necassary value.
        Enter IxAP(w,t).
        DO NOT FORGET : the water line to find should be added by 1.
        """
        
        s=0
        result=0
        result1=0
        while -2<=s:
            if s == -1:
                result += pow(dataoffset.iloc[s+2,w+2],3)*4
            else :
                result += pow(dataoffset.iloc[s+2,w+2],3)
            s = s-1
            result1=result*self.t*2/3*1/3
        return result1
    
    def SSIx(self,w,t,j,h):
        """
        SSIx(w,t,j,h) is command function, which adds every parts of transverse moment of inertia.
        We devided ship as 3 parts, stern attachments, bow attachments and the rest part of ship.
        The result of these command lines shows the sum of transverse moment of inertia of three parts.
        'w' is for waterline and 't','j''h' are space between two stations for each part.
        't' for stern attachments, 'j' for bow attachments and 'h' is for station of ship.
        
        """
        temp1=ship_bow(1,8.7,2,1.9245,174)
        temp3=ship_mid(1,8.7,2,1.9245,174)
        result=self.IxAP(w,self.t)+temp1.IxFP(w,self.j)+temp3.Ix(w,self.h)
        return result
    
    def SfyAP(self,w):
        """
        The command lines are to get the value of ∑f(y) of stern attachments.
        You can command SfyAP(w) to get it.
        ∑f(y) adds all the values of station and expresses with waterline form.
        Here, 'w' indicates 'waterline - 1' which means :
        if you want to get the value about waterline number 10, you have to enter 11 in 'w' place.
        
        """
        
        s=0
        result=0
        while -2<=s:
            if s == -1:
                result += (dataoffset.iloc[s+2,w+2])*4
            else:
                result += dataoffset.iloc[s+2,w+2]
            s= s - 1
        return result
        
    def SxfyAP(self,w):
        """
        The command function SxfyAP(w) is the sum of x' * f(y).
        If you enter waterline you want to know, you will get all station's sum of x' * f(y).
        This function shows the value of w-1 to w-2's ∑x' * f(y).
        """
        
        s=0
        total=0
        while -2<= s:
            if s ==-1:
                total += dataoffset.iloc[s+2,w+2]*(-1)*4
            elif s ==0:
                total += 0
            else:
                total += dataoffset.iloc[s+2,w+2]*(-2)
            s=s-1
        return total
    
    def APf(self,w,t):
        """
        The result of command lines are APf of stern attachments of ship.
        This parameter is necessary to get the longitudinal moment of inertia of stern attachments part.
        'w' : waterline + 1
        't' : distance between two stations in stern attachments part
        """
        
        if self.SfyAP(w)==0:
            result=0
        else:
            result = self.t*self.SxfyAP(w)/self.SfyAP(w)
        return result
    
    def MyAP(self,w,t,L):
        """
        These are command lines for longitudinal moment of stern attachments.
        'w' : waterline + 1
        't' : distance between two stations in stern attachments part
        'L' : Length between perpendiculars
        """
        
        result = self.AwAP(w,self.t)*((-self.L)/2+self.APf(w,self.t))
        return result
    
    def APIAP(self,w,t):
        """
        APIAP(w,t) is the command function to get the value of IA.P.
        This parameter helps to get the longitudinal moment of inertia of stern attachments part.
        'w' : waterline + 1
        't' : distance between two stations in stern attachments part
        
        """
        
        s=0
        total=0
        while -2<=s:
            if s == -1:
                total += dataoffset.iloc[s+2,w+2]*1*4
            elif s==0:
                total += 0
            else:
                total += dataoffset.iloc[s+2,w+2]*4
            s=s-1
        return total*t*t*t*2*1/3
    
    def APIY(self,w,t,L):
        """
        BM is the metacentric radius of ship.
        Longitudinal metacentric height (BMl) = Longitudinal moment of inertia of waterplane / volume displacement of ship
        To get the parameter BM, longitudinal moment of inertia is necessary value.
        Enter APIY(w,t,L).
        DO NOT FORGET : the water line to find should be added by 1.
        'w' : waterline + 1
        't' : distance between two stations in stern attachments part
        'L' : Length between perpendiculars
        
        """
        
        result = self.APIAP(w,self.t)+self.AwAP(w,self.t)*self.L/2*self.L/2+self.AwAP(w,self.t)*(-self.L)*self.APf(w,self.t)
        return result
    

class ship_bow:
    def __init__(self,f,h,j,t,L):
        self.f=f
        self.h=h
        self.j=j
        self.t=t
        self.L=L
        
    def SfyFP(self,w):
        """
        The command lines are to get the value of ∑f(y) of bow attachments.
        You can command SfyFP(w) to get it.
        ∑f(y) adds all the values of station and expresses with waterline form.
        Here, 'w' indicates 'waterline - 1' which means :
        if you want to get the value about waterline number 10, you have to enter 11 in 'w' place.
        
        """
        
        s=26
        result=0
        while 24<=s:
            if s ==25:
                result += dataoffset.iloc[s+2,w+2] *4
            else:
                result += dataoffset.iloc[s+2,w+2]
            s += -1
        return result
    
    def SFyHFP(self,s,w):
        """
        The command lines are to get the value of ∑f(yH) of bow attachments.
        ∑f(yH) is the value to find the area of midship section.
        You can command SFyHFP(s,w) to get it.
        Since, These are about bow attachments, station number ends FP with number 24.
        And now you will know that if you want to get the value of bow attachments, enter 24 + j in the place of 's'.
        j: distance between two stations in bow attachments part
        
        """
        total=0
        a=w
        while w-2<=a<=w:
            if a == w-1:
                total += dataoffset.iloc[s+2,a+2]*4
            else:
                total += dataoffset.iloc[s+2,a+2]
            a=a-1
        return total
    
    def FAmFP(self,s,w):
        """
        Just same as above, station of FP ends with number 24.
        If you want to get the value of bow attachments, enter 24 + j in the place of 's'.
        It is applicable in other value of bow attachments also.
        Type the station number and waterline number you want to know.
        's': station number
        'w': waterline + 1
        'j': distance between two stations in bow attachments part
        
        """      
        if s == 25:
            total=self.SFyHFP(s,w)*4*3/8
        else:
            total=self.SFyHFP(s,w)*3/8
        return total
    
    def SFAmFP(self,w):
        """
        These command lines are to get the value of ∑f(Am) of bow attachments.
        ∑f(Am) is the value, using to know the displacements of bow attachments part of ship.
        You can command SFAmFP(w) to get this value.
        And SFAmFP(w) configures the ∑f(Am) of bow attachments, which has waterline 'w-1' to 'w-2'.
        
        """ 
        a=24
        total=0
        while a<=26:
            total += self.FAmFP(a,w)
            a=a+1
        return total
    
    def VFP(self,w,j):
        """
        Now, you can get the displacements of bow attachments part of ship.
        Displacement is weight of water that a ship pushes aside when it is floating, which in turn is the weight of a ship
        To get this value, we divided ship by station and waterline.
        'w': waterline + 1
        'j': distance between two stations in bow attachments part
        
        """        
        result = self.SFAmFP(w)*self.j*3/8*2
        return result
    
    def AwFP(self,w,j):
        """
        AwFP(w,j) is the command function for water plane area.
        'w': waterline + 1
        'j': distance between two stations in bow attachments part
        
        """
        
        result=0
        s=24
        while s<=26:
            if s ==25:
                result += dataoffset.iloc[s+2,w+2]*4
            else:
                result += dataoffset.iloc[s+2,w+2]
            s=s+1
        return result*self.j*2/3
    
    def WFP(self,w,j):
        """
        If you got the displacements of ship, you can definitely know the weight.
        These command lines help to get the weight.
        We got the displacements from above command function VFP(w,j).
        What we have to do is just multiply density of water with its result.
        Since, ARPA-GO helps calculation of ship, the density is 1.025 which is sea water.
        You can change the density freely, if you are necessary to.
        'w': waterline + 1
        'j': distance between two stations in bow attachments part
        
        """
        
        result = self.VFP(w,self.j)*1.025
        return result
    
    def FPb(self,w,j):
        """
        These are for FPb of bow attachments of ship.
        The inputs are 'w' & 'j'.
        Just same as before the waterline expresses w-1 to w-2.
        Enter the waterline what you want to know + 1 in the place of 'w'.
        'j' is the distance between two stations.
        
        """
        s=24
        result=0
        result1=0
        while s <=26:
            if s == 24:
                result += self.FAmFP(s,w)*0
            elif s ==25:
                result += self.FAmFP(s,w)*1
            else:
                result += self.FAmFP(s,w)*2
            s = s+1
            result1 = result/self.SFAmFP(w)*self.j
        return result1
    
    def lcbFP(self,w,j,L):
        """
        The centroid of the underwater volume of the ship expressed as a longitudinal location. 
        We call that centroid point as LCB (longitudinal center of gravity) and it is connected with stability of ship.
        To get the value, enter the command function, lcbFP(w,j,L).
        'L' means LBP, in full form Length between perpendiculars.
        'w': waterline + 1
        'j': distance between two stations in bow attachments part
        
        """
        
        result = self.FPb(w,self.j)+(self.L/2)
        return result
    
    def SfVFP(self,w):
        """
        Command function SfVFP(w) shows the sum of displacements divided by each stations.
        It is functioned by waterline wise.
        'w'= waterline + 1
        Thus, the result of this command lines is ∑f(V) of bow attachments of ship.
        
        """
        
        a=w
        result=0
        while w-2 <= a:
            if a == w-1:
                result += self.SfyFP(a)*4
            else:
                result += self.SfyFP(a)
            a= a-1
        return result
    
    def kbFP(self,w,f):
        """
        KB is the centre of buoyancy which is the height above the keel.
        kbFP(w,f) is to get the value of it.
        'w' = waterline + 1
        'f' = the distance between waterline
        
        """
        a=w
        result=0
        result1=0
        while w-2<=a:
            if a ==0:
                result += 0
            elif a==1:
                result += 0
            elif a == w-1:
                result += self.SfyFP(a) * 4 * (a-1)
            else:
                result += self.SfyFP(a) * (a-1)
            a= a-1
            result1=result/self.SfVFP(w)*self.f
        return result1
    
    def IxFP(self,w,j):
        """
        BM is the metacentric radius of ship.
        Transverse metacentric height (BM) = Transverse moment of inertia of waterplane / volume displacement of ship
        To get the parameter BM, transverse moment of inertia is necessary value.
        Enter IxFP(w,j).
        DO NOT FORGET : the water line to find should be added by 1.
        'w': waterline + 1
        'j': distance between two stations in bow attachments part
        
        """
        a=26
        result=0
        result1=0
        while a>=24:
            if a == 25:
                result += pow(dataoffset.iloc[a+2,w+2],3)*4
            else :
                result += pow(dataoffset.iloc[a+2,w+2],3)
            a = a-1
            result1=result*self.j*2/3*1/3
        return result1
    
   
    
    def SxfyFP(self,w):
        """
        The command function SxfyFP(w) is the sum of x' * f(y).
        If you enter waterline you want to know, you will get all station's sum of x' * f(y).
        This function shows the value of (w-1 to w-2)'s ∑x' * f(y).
        """
        
        a=26
        result=0
        while a >=24:
            if a ==25:
                result += dataoffset.iloc[a+2,w+2]*4*1
            elif a ==26:
                result += dataoffset.iloc[a+2,w+2]*2
            else:
                result += 0
            a=a-1
        return result
    
    def FPf(self,w,j):
        """
        The result of command lines are FPf of bow attachments of ship.
        This parameter is necessary to get the longitudinal moment of inertia of bow attachments part.
        'w' : waterline + 1
        'j' : distance between two stations in bow attachments part
        """
        if self.SxfyFP(w)==0:
            result = 0
        else:
            result = self.SxfyFP(w)/self.SfyFP(w)*self.j
        return result
    
    def FPMy(self,w,j,L):
        """
        These are command lines for longitudinal moment of bow attachments.
        'w' : waterline + 1
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars
        """
        
        result= self.AwFP(w,self.j)*(-self.L/2+self.FPf(w,self.j))
        return result
        
    def FPIFP(self,w,j):
        """
        FPIFP(w,j) is the command function to get the value of IF.P.
        This parameter helps to get the longitudinal moment of inertia of bow attachments part.
        'w' : waterline + 1
        'j' : distance between two stations in bow attachments part
        
        """
        
        result=0
        s=26
        while s>=24:
            if s == 24:
                result +=0 
            elif s ==25:
                result += dataoffset.iloc[s+2,w+2]*4
            else:
                result += dataoffset.iloc[s+2,w+2]*4
            s=s-1
        return result*2*1/3*self.j*self.j*self.j
    
    def FPIY(self,w,j,L):
        """
        BM is the metacentric radius of ship.
        Longitudinal metacentric height (BMl) = Longitudinal moment of inertia of waterplane / volume displacement of ship
        To get the parameter BM, longitudinal moment of inertia is necessary value.
        Enter FPIy(w,j,L).
        DO NOT FORGET : the water line to find should be added by 1.
        'w' : waterline + 1
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars
        
        """
        
        result = self.FPIFP(w,self.j)+self.AwFP(w,self.j)*self.L/2*self.L/2+self.AwFP(w,self.j)*(-self.L)*self.FPf(w,self.j)
        return result
    
    
class ship_mid:
    def __init__(self,f,h,j,t,L):
        self.f=f
        self.h=h
        self.j=j
        self.t=t
        self.L=L
    
    
    def simy(self,w):
        """
        The command lines are to get the value of ∑f(y) of main part of ship.
        You can command simy(w) to get it.
        ∑f(y) adds all the values of station and expresses with waterline form.
        Here, 'w' indicates 'waterline - 1' which means :
        if you want to get the value about waterline number 10, you have to enter 11 in 'w' place.
        
        """
       
        total = 0
        s = 0
        while s <= 24 :
            if s == 0 or s == 24:
                total += 0.5*dataoffset.iloc[s+2,w+2]
            elif s == 1 or s == 23 or s == 3 or s == 21:
                total += 2*dataoffset.iloc[s+2,w+2]
            elif s == 2 or s == 22:
                total += dataoffset.iloc[s+2,w+2]
            elif s == 4 or s == 20:
                total += 1.5*dataoffset.iloc[s+2,w+2]
            elif s % 2 != 0:
                total += 4*dataoffset.iloc[s+2,w+2]
            else :
                total += 2*dataoffset.iloc[s+2,w+2]
            s = s+1    
        return total
        
    def simx(self,n):
        """
        Command function simx(n) shows the sum of displacements divided by each stations.
        It is functioned by waterline wise.
        'n'= waterline + 1
        Thus, the result of this command lines is ∑f(V) of main part of ship.
        Reference : This command lines show the displacements of ship with three waterlines combined.
        
        """

        total=0
        w=n-2
        while w <= n:
            if w == n or w ==n-2:
                total += self.simy(w)
            else:
                total += self.simy(w)*4
            w=w+1
        return total
    
    def W(self,n,h,f):
        """
        If you got the displacements of ship, you can definitely know the weight.
        These command lines help to get the weight.
        We got the displacements from above command function simx(n).
        What we have to do is just multiply density of water with its result.
        Since, ARPA-GO helps calculation of ship, the density is 1.025 which is sea water.
        You can change the density freely, if you are necessary to.
        'n' = waterline + 1
        'h' = distance between two stations
        'f' = distance between waterlines
        The product of this command lines also shows weight with three waterlines combined.
        
        """
        if n ==2:
            result = self.simx(n)*self.h/3*self.f/3*1.025
        else:
            result = self.simx(n)*self.h/3*self.f/3*1.025*2
        return result
    
    #선수부가부,선미부가부에 필요한 값이 있기때문에 클래스에 객체 할당해줘야한다.
    def DIS(self,s,h,f,t,j):
        """
        Now, you can get the displacements of ship.
        Displacement is weight of water that a ship pushes aside when it is floating.
        To get this value, we divided ship by station and waterline.
        's' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        total=0
        n=s
        temp1 = ship_transom(1,8.7,2,1.9245,174)
        temp2 = ship_bow(1,8.7,2,1.9245,174)
        while n>1:
            total += self.W(n,self.h,self.f)+temp1.WAP(n,self.t)+temp2.WFP(n,self.j)
            n = n-2
        return total
        
    def SSW(self,w,j,t):
        """
        You've got the displacements and weight of stern/bow attachments of ship.
        These command lines help to get the sum of these two weight.
        What we have to do is just multiply density of water with sum of both displacements.
        Since, ARPA-GO helps calculation of ship, the density is 1.025 which is sea water.
        You can change the density freely, if you are necessary to.
        The product of this command lines shows weight with three waterlines combined.
        'w' : waterline + 1
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """ 
        
        temp1 = ship_transom(1,8.7,2,1.9245,174)
        temp2 = ship_bow(1,8.7,2,1.9245,174)
        result = (temp2.VFP(w,self.j)+temp1.VAP(w,self.t))*1.025
        return result
    
    def Kb(self,n):
        """
        KB is the centre of buoyancy which is the height above the keel.
        Kb(t) is to get the value of it.
        The product of this command lines shows kb with three waterlines combined.
        """
        
        total3=0
        w=n
        while n-2 <= w <= n:
            if w == 0:
                total3 +=0
            elif w == 1:
                total3 += self.simy(1)*2
            elif w == 2:
                total3 += self.simy(2)
            elif w == n-1:
                total3 += self.simy(w)*4*(w-1)
            else :
                total3 += self.simy(w)*(w-1)
            w= w-1
            total=total3/self.simx(n)
        return total
    
    def SSM(self,s,h,f,t,j):
        """
        To get the KB of ship, the parameter ∑z' * f(V)is necessary.
        SSM(n,h,f,t,j) is command function to get its value.
        'n' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        result=0
        n=s
        temp1 = ship_transom(1,8.7,2,1.9245,174)
        temp2 = ship_bow(1,8.7,2,1.9245,174)
        while n>=2:
            result += (self.Kb(n)*self.W(n,self.h,self.f))+(temp2.VFP(n,self.j)*temp2.kbFP(n,self.j)*1.025)+(temp1.KbAP(n,self.t)* temp1.VVAP(n,self.j)*1.025)
            n= n-2
        return result
    
    def KB(self,n,h,f,t,j):
        """
        KB is the centre of buoyancy which is the height above the keel.
        KB(n,h,f,t,j) is to get the value of it.
        'n' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        result = self.SSM(n,self.h,self.f,self.t,self.j)/self.DIS(n,self.h,self.f,self.t,self.j)
        return result
    
    def X(self,s,g):
        """
        The command lines are to get the value of ∑f(yH) of main part of ship.
        ∑f(yH) is the value to find the area of midship section.
        You can command X(s,g) to get it.
        's' : station number
        'g' : waterline number + 1
        
        """
        
        total=0
        w=g
        while g-2<=w<=g:
            if w == g-1:
                total += dataoffset.iloc[s+2,w+2]*4
            else:
                total += dataoffset.iloc[s+2,w+2]
            w=w-1
        return total
    
    fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]
    def lcb(self,g,h):
        """
        x' * f(V) is the value to get the longitudinal center of gravity (LCB) of ship.
        
        """
        
        total=0
        s=0
        while s<=24:
            if s ==0 or s==24:
                total += self.X(s,g)*self.fx[s]*0.5
            elif s ==1 or s ==23 or s==3 or s==21:
                total += self.X(s,g)*self.fx[s]*2
            elif s ==2 or s==22:
                total += self.X(s,g)*self.fx[s]
            elif s==4 or s==20:
                total += self.X(s,g)*self.fx[s]*1.5
            elif s%2!=0:
                total += self.X(s,g)*self.fx[s]*4
            else:
                total += self.X(s,g)*self.fx[s]*2
            s=s+1
            total=total
        return total*self.h/self.simx(g)
    
    def SSSM(self,s,h,f,t,j,L):
        """
        The command function SSSM(s,h,f,t,j,L) is the sum of x' * f(V).
        We've got the parameter x' * f(V) from above command lines.
        's' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        result=0
        n=s
        temp1 = ship_transom(1,8.7,2,1.9245,174)
        temp2 = ship_bow(1,8.7,2,1.9245,174)
        while n>=2:
            result += (self.lcb(n,self.h)*self.W(n,self.h,self.f)/1.025)+(temp2.lcbFP(n,self.j,self.L)*temp2.VFP(n,self.j))+(temp1.lcbAP(n,self.t,self.L)* temp1.VAP(n,self.t))
            n=n-2
        return result
    
    def LCB(self,s,h,f,t,j,L):
        """
        The centroid of the underwater volume of the ship expressed as a longitudinal location. 
        We call that centroid point as LCB (longitudinal center of gravity) and it is connected with stability of ship.
        To get the value, enter the command function, LCB(s,h,f,t,j,L).
        's' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' means LBP, in full form Length between perpendiculars.
        
        """
        
        result=self.SSSM(s,self.h,self.f,self.t,self.j,self.L)/self.DIS(s,self.h,self.f,self.t,self.j)
        return result
    
    def Am(self,a):
        """
        Am(a) is the command function for midsection area of ship.
        'a' : waterline +1
        The product of this command lines shows midsection area with three waterlines combined.
        
        """
        if a ==2:
            result =self.X(12,a)/3
        else:
            result = self.X(12,a)*2/3
        return result
    
    def SAm(self,q):
        """
        SAm(q) is the command function for midsection area of ship.
        'q' : waterline +1
        
        """
        
        total=0
        a=q
        while a>=2:
            total += self.Am(a)
            a=a-2
        return total
    
    def Cb(self,m,h,f,L,B,t,j):
        """
        Coefficients of form are dimensionless numbers that describe hull fineness and overall shape characteristics.
        The coefficients are ratios of areas or volumes for the actual hull form compared to prisms or rectangles defined by the ship’s length, breadth, and draft
        The block coefficient of a ship is the ratio of the underwater volume of ship to the volume of a rectangular block having the same overall length, breadth and depth.
        We call block coefficient of a ship as Cb
        This coefficients of form represents how fat ship is.
        To know this value, command with Cb(m,h,f,L,B,t,j).
        'm' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars.
        'B' : Breadth of ship
        
        """
        
        result= self.DIS(m,self.h,self.f,self.t,self.j)/1.025/(m-1)/self.L/B
        return result
    
    def Cm(self,m,B):
        """
        The midship section coefficient (Cm) is the ratio of the area of the immersed midship section (Am) at a particular draft to that of a rectangle of the same draft and breadth as the ship
        Cm= Am / B x d 
        We've got parameter Am with command function SAm(m).
        'B' : Breadth of ship
        'm' : waterline + 1
        
        """
        
        result= self.SAm(m)/(m-1)/B
        return result
    
    def Cp(self,m,h,f,L,B,t,j):
        """
        The prismatic coefficient(Cp) is the underwater area divided by the area of a midship section.
        Thus, The prismatic coefficient of a ship at any draft is the ratio of the volume of displacement at that draft to the volume of a prism having the same length as the ship and the same cross-sectional area as the ship’s midships area.
        The prismatic coefficient is used mostly by ship-model researchers.
        Command Cp(m,h,f,L,B,t,j) to get its value.
        'm' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars.
        'B' : Breadth of ship
        
        """
        
        result = self.Cb(m,self.h,self.f,self.L,B,self.t,self.j)/self.Cm(m,B)
        return result
    
    def Aw(self,r,h):
        """
        Aw(r,h) is the command function for water plane area.
        'r' for water line and 'h' for the space between stations.
        
        """
        
        result=self.simy(r)*2/3*self.h
        return result
    
    def Cw(self,r,h,L,B):
        """
        These command lines show the waterplane coefficient of ship.
        It is the ratio of the actual area of the waterplane to the product of the length and breadth of the ship.
        'r' : waterline + 1
        'h' : distance between two stations
        'L' : Length between perpendiculars
        'B' : Breadth of ship
        """
        
        result=self.Aw(r,self.h)/B/self.L
        return result
    
    def Cvp(self,r,h,f,L,B,t,j):
        """
        Cvp(r,h,f,L,B,t,j) is the command function for vertical prismatic coefficient.
        A large value of vertical prismatic coefficient indicates will indicate body sections of U-form and a low will indicate V-sections.
        'r' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars.
        'B' : Breadth of ship
        
        """
        
        result=self.Cb(r,self.h,self.f,self.L,B,self.t,self.j)/self.Cw(r,self.h,self.L,B)
        return result
    
    def simy3(self,w):
        """
        These command lines represents ∑f(y^3) by each waterline.
        This parameter is necessary value to get inertia moment of ship.
        'w' = waterline + 1
        
        """
        
        total=0
        s=0
        while s<=24:
            if s ==0 or s==24:
                total += 0.5*pow(dataoffset.iloc[s+2,w+2],3)
            elif s==1 or s ==23 or s==3 or s==21:
                total += 2*pow(dataoffset.iloc[s+2,w+2],3)
            elif s==2 or s==22:
                total += pow(dataoffset.iloc[s+2,w+2],3)
            elif s==4 or s==20:
                total += 1.5*pow(dataoffset.iloc[s+2,w+2],3)
            elif s%2!=0:
                total += 4*pow(dataoffset.iloc[s+2,w+2],3)
            else:
                total += 2*pow(dataoffset.iloc[s+2,w+2],3)
            s=s+1
        return total
    
    def Ix(self,w,h):
        """
        BM is the metacentric radius of ship.
        Transverse metacentric height (BM) = Transverse moment of inertia of waterplane / volume displacement of ship
        To get the parameter BM, transverse moment of inertia is necessary value.
        Enter Ix(w,h).
        DO NOT FORGET : the water line to find should be added by 1.
        'w' : waterline + 1
        'h' : distance between two stations
        """
        
        
        result=2/3*h/3*self.simy3(w)
        return result
    
    def BM(self,w,h,f,t,j):
        """
        The metacentric radius of a ship is the vertical distance between its center of buoyancy and metacenter.
        This parameter can be visualized as the length of the string of a swinging pendulum of the center of gravity of the pendulum coincides the center of buoyancy of the ship.
        In other words, the ship behaves as a pendulum swinging about its metacenter.
        That is reason BM is directly connected with stability of ship.
        BM(w,h,f,t,j) is the command function calculating BM.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        temp1=ship_bow(1,8.7,2,1.9245,174)
        temp2=ship_transom(1,8.7,2,1.9245,174)
        result=(temp2.IxAP(w,self.t)+temp1.IxFP(w,self.j)+self.Ix(w,self.h))/self.DIS(w,self.h,self.f,self.t,self.j)*1.025
        return result
    
    def KM(self,w,h,f,t,j):
        """
        KM is the distance from the keel to the metacentre.
        Enter KM(w,h,f,t,j) to calculate its value.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        result=self.BM(w,self.h,self.f,self.t,self.j)+self.KB(w,self.h,self.f,self.t,self.j)
        return result
    
    fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]
    def xfy(self,w):
        """
        The command function xfy(w) is the sum of x' * f(y).
        If you enter waterline you want to know, you will get all station's sum of x' * f(y).
        'w' : waterline + 1
        
        """
        
        total=0
        s=0
        while s<=24:
            if s ==0 or s==24:
                total += dataoffset.iloc[s+2,w+2]*self.fx[s]*0.5
            elif s ==1 or s ==23 or s==3 or s==21:
                total += dataoffset.iloc[s+2,w+2]*self.fx[s]*2
            elif s ==2 or s==22:
                total += dataoffset.iloc[s+2,w+2]*self.fx[s]
            elif s==4 or s==20:
                total += dataoffset.iloc[s+2,w+2]*self.fx[s]*1.5
            elif s%2!=0:
                total += dataoffset.iloc[s+2,w+2]*self.fx[s]*4
            else:
                total += dataoffset.iloc[s+2,w+2]*self.fx[s]*2
            s=s+1
        return total

    def simy1(self,w):
        """
        The command lines are to get the value of ∑f(y) of main part of ship.
        You can command simy1(w) to get it.
        ∑f(y) adds all the values of station and expresses with waterline form.
        Here, 'w' indicates 'waterline - 1' which means :
        if you want to get the value about waterline number 10, you have to enter 11 in 'w' place.
        
        """
        
        total=0
        s=0
        while s<=24:
            if s ==0 or s==24:
                total += dataoffset.iloc[s+2,w+2]*0.5
            elif s ==1 or s ==23 or s==3 or s==21:
                total += dataoffset.iloc[s+2,w+2]*2
            elif s ==2 or s==22:
                total += dataoffset.iloc[s+2,w+2]
            elif s==4 or s==20:
                total += dataoffset.iloc[s+2,w+2]*1.5
            elif s%2!=0:
                total += dataoffset.iloc[s+2,w+2]*4
            else:
                total += dataoffset.iloc[s+2,w+2]*2
            s=s+1
        return total

    def LCF(self,w,h):
        """
        Longitudinal Center of Flotation(LCF) is the center of the waterplane.
        When you are considering the addition of new weight(cargo) and you want to calculate its effect without having to recalculate the LCG of the whole vessel, use the distance from the LCF to the CG of the added cargo.
        'w' : waterline + 1
        'h' : distance between two stations
        
        """
        
        result=self.xfy(w)/self.simy1(w)*self.h
        return result

    def TPC(self,r,h):
        """
        Tons per centimetre(TPC), i.e. the number of tons required to sink the vessel one centimetre.
        For instance, if the vessel has a TPC of 60 tons and uses 30 tons of fuel and water a day, then it will reduce its draft by half a centimetre a day.
        'r' : waterline + 1
        'h' : distance between two stations
        
        """
        
        result=self.Aw(r,self.h)/100*1.025
        return result

    def My(self,w,h):
        """
        These are command lines for longitudinal moment of main part of ship.
        'w' : waterline + 1
        'h' : distance between two stations
        
        """
        
        result=self.Aw(w,self.h)*self.LCF(w,self.h)
        return result

    fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]
    def x2fy(self,w):
        """
        The command function x2fy(w) is the twice of sum of x' * f(y).
        If you enter waterline you want to know, you will get all station's sum of x' * f(y) multiplied by 2.
        This function shows the value of f-1's ∑x'* 2 * f(y).
        'w' = waterline + 1
        """
        
        total=0
        s=0
        while s<=24:
            if s ==0 or s==24:
                total += dataoffset.iloc[s+2,w+2]*pow(self.fx[s],2)*0.5
            elif s ==1 or s ==23 or s==3 or s==21:
                total += dataoffset.iloc[s+2,w+2]*pow(self.fx[s],2)*2
            elif s ==2 or s==22:
                total += dataoffset.iloc[s+2,w+2]*pow(self.fx[s],2)
            elif s==4 or s==20:
                total += dataoffset.iloc[s+2,w+2]*pow(self.fx[s],2)*1.5
            elif s%2!=0:
                total += dataoffset.iloc[s+2,w+2]*pow(self.fx[s],2)*4
            else:
                total += dataoffset.iloc[s+2,w+2]*pow(self.fx[s],2)*2
            s=s+1
        return total

    def Iy(self,w,h):
        """
        BM is the metacentric radius of ship.
        Longitudinal metacentric height (BMl) = Longitudinal moment of inertia of waterplane / volume displacement of ship
        To get the parameter BM, longitudinal moment of inertia is necessary value.
        Enter Iy(w,h).
        DO NOT FORGET : the water line to find should be added by 1.
        'w' : waterline + 1
        'h' : distance between two stations
        
        """
        
        result=2/3*self.h*self.h*self.h*self.x2fy(w)
        return result

    def SSAw(self,w,h,t,j):
        """
        You've got the waterplane area (Aw) of stern/bow attachments part and main part of ship.
        These command lines help to get the sum of these three Aw.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        temp1=ship_bow(1,8.7,2,1.9245,174)
        temp2=ship_transom(1,8.7,2,1.9245,174)
        result=self.Aw(w,self.h)+temp2.AwAP(w,self.t)+temp1.AwFP(w,self.j)
        return result

    def SSMy(self,w,h,t,j,L):
        """
        These are command lines for longitudinal moment.
        You've got the longitudinal moment (My) of stern/bow attachments part and main part of ship.
        These command lines help to get the sum of these three My.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars
        
        """
        
        temp1=ship_bow(1,8.7,2,1.9245,174)
        temp2=ship_transom(1,8.7,2,1.9245,174)
        result=self.My(w,self.h)+temp1.FPMy(w,self.j,self.L)+temp2.MyAP(w,self.t,self.L)
        return result

    def SSLCF(self,w,h,t,j,L):
        """
        Longitudinal Center of Flotation(LCF) is the center of the waterplane.
        You've got the waterplane area (Aw) and longitudinal moment (My) of ship.
        LCF is longitudinal divided by waterplane area.
        These command lines help to calculate it.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars
        
        """
        
        result=self.SSMy(w,self.h,self.t,self.j,self.L)/self.SSAw(w,self.h,self.t,self.j)
        return result

    def SSIy(self,w,h,t,j,L):
        """
        You've got the Iy of stern/bow attachments part and main part of ship.
        These command lines help to get the sum of these three Iy.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars
        
        """
        
        temp1=ship_bow(1,8.7,2,1.9245,174)
        temp2=ship_transom(1,8.7,2,1.9245,174)
        result=self.Iy(w,self.h)+temp2.APIY(w,self.t,self.L)+temp1.FPIY(w,self.j,self.L)
        return result

    def I1(self,w,h,t,j,L):
        """
        BM is the metacentric radius of ship.
        Longitudinal metacentric height (BMl) = Longitudinal moment of inertia of waterplane / volume displacement of ship
        To get the parameter BM, longitudinal moment of inertia is necessary value.
        These command lines help to get the longitudinal moment of inertia (Il).
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars
        
        """
        
        result=self.SSIy(w,self.h,self.t,self.j,self.L)-self.SSLCF(w,self.h,self.t,self.j,self.L)*self.SSAw(w,self.h,self.t,self.j)
        return result

    def BML(self,w,h,f,t,j,L):
        """
        BML is the longitudinal metacentric radius.
        It is directly connected with stability of ship.
        BML(w,h,f,t,j,L) is the command function calculating BML.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : length between perpendiculars
        
        """
        
        result=self.I1(w,self.h,self.t,self.j,self.L)
        return result/(self.DIS(w,self.h,self.f,self.t,self.j)/1.025)

    def MTC(self,w,h,f,t,j,L):
        """
        Moment to change Trim one Centimeter is full form of MTC.
        Enter MTC(w,h,f,t,j,L) to get the value of it.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : length between perpendiculars
        
        """
        
        result=self.DIS(w,self.h,self.f,self.t,self.j)*self.BML(w,self.h,self.f,self.t,self.j,self.L)/(100*self.L)
        return result

    def Wcm(self,w,h,t,j,L):
        """
        Weight tonnage change trim one Centimeter is full form of Wcm.
        Enter Wcm(w,h,t,j,L) to get the value of it.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : length between perpendiculars
        """
        
        result=-1*(self.TPC(w,self.h)*self.SSLCF(w,self.h,self.t,self.j,self.L)/self.L)
        return result

    def KML(self,w,h,f,t,j,L):
        """
        KM is the distance from the keel to the metacentre.
        KML = BML + KB
        Enter KML(w,h,f,t,j,L) to calculate its value.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : length between perpendiculars
        
        """
        
        result=self.BML(w,self.h,self.f,self.t,self.j,self.L)+self.KB(w,self.h,self.f,self.t,self.j)
        return result
    
    def DISLIST(self,w,h,f,t,j):
        """
        Now, you can get the displacements of ship.
        Displacement is weight of water that a ship pushes aside when it is floating.
        To get this value, we divided ship by station and waterline.
        These command lines will show bi-waterline wise.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.DIS(a,self.h,self.f,self.t,self.j))
            a=a-2
        return result

    def DISLIST2(self,w,h,f,t,j):
        """
        If you got the displacements of ship, you can definitely know the volume of displacements.
        These command lines help to get it.
        What we have to do is just divide density of water with displacements of ship.
        Since, ARPA-GO helps calculation of ship, the density is 1.025 which is sea water.
        You can change the density freely, if you are necessary to.
        'w' = waterline + 1
        'h' = distance between two stations
        'f' = distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.DIS(a,self.h,self.f,self.t,self.j)/1.025)
            a=a-2
        return result

    def AwLIST(self,w,h):
        """
        AwLIST(w,h) is the command function for water plane area.
        'w' for water line and 'h' for the space between stations.
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.Aw(a,self.h))
            a=a-2
        return result

    def AmLIST(self,w):
        """
        AmLIST(w) is the command function for midsection area of ship.
        'w' : waterline +1
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.SAm(a))
            a=a-2
        return result

    def TPCLIST(self,w,h):
        """
        Tons per centimetre(TPC), i.e. the number of tons required to sink the vessel one centimetre.
        For instance, if the vessel has a TPC of 60 tons and uses 30 tons of fuel and water a day, then it will reduce its draft by half a centimetre a day.
        'w' : waterline + 1
        'h' : distance between two stations
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.TPC(a,self.h))
            a=a-2
        return result

    def MTCLIST(self,w,h,f,t,j,L):
        """
        Moment to change Trim one Centimeter is full form of MTC.
        Enter MTCLIST(w,h,f,t,j,L) to get the value of it.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : length between perpendiculars
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.MTC(a,self.h,self.f,self.t,self.j,self.L))
            a=a-2
        return result

    def WcmLIST(self,w,h,t,j,L):
        """
        Weight tonnage change trim one Centimeter is full form of Wcm.
        Enter WcmLIST(w,h,t,j,L) to get the value of it.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : length between perpendiculars
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.Wcm(a,self.h,self.t,self.j,self.L))
            a=a-2
        return result

    def KBLIST(self,w,h,f,t,j):
        """
        KB is the centre of buoyancy which is the height above the keel.
        KBLIST(w,h,f,t,j) is to get the value of it.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.KB(a,self.h,self.f,self.t,self.j))
            a=a-2
        return result

    def BMLIST(self,w,h,f,t,j):
        """
        The metacentric radius of a ship is the vertical distance between its center of buoyancy and metacenter.
        This parameter can be visualized as the length of the string of a swinging pendulum of the center of gravity of the pendulum coincides the center of buoyancy of the ship.
        In other words, the ship behaves as a pendulum swinging about its metacenter.
        That is reason BM is directly connected with stability of ship.
        BMLIST(w,h,f,t,j) is the command function calculating BM.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.BM(a,self.h,self.f,self.t,self.j))
            a=a-2
        return result

    def KMLIST(self,w,h,f,t,j):
        """
        KM is the distance from the keel to the metacentre.
        Enter KMLIST(w,h,f,t,j) to calculate its value.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.KM(a,self.h,self.f,self.t,self.j))
            a=a-2
        return result

    def LCBLIST(self,w,h,f,t,j,L):
        """
        The centroid of the underwater volume of the ship expressed as a longitudinal location. 
        We call that centroid point as LCB (longitudinal center of gravity) and it is connected with stability of ship.
        To get the value, enter the command function, LCBLIST(w,h,f,t,j,L).
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' means LBP, in full form Length between perpendiculars.
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.LCB(a,self.h,self.f,self.t,self.j,self.L))
            a=a-2
        return result

    def LCFLIST(self,w,h,t,j,L):
        """
        Longitudinal Center of Flotation(LCF) is the center of the waterplane.
        When you are considering the addition of new weight(cargo) and you want to calculate its effect without having to recalculate the LCG of the whole vessel, use the distance from the LCF to the CG of the added cargo.
        'w' : waterline + 1
        'h' : distance between two stations
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : length between perpendiculars
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.SSLCF(a,self.h,self.t,self.j,self.L))
            a=a-2
        return result

    def BMLLIST(self,w,h,f,t,j,L):
        """
        The metacentric radius of a ship is the vertical distance between its center of buoyancy and metacenter.
        This parameter can be visualized as the length of the string of a swinging pendulum of the center of gravity of the pendulum coincides the center of buoyancy of the ship.
        In other words, the ship behaves as a pendulum swinging about its metacenter.
        That is reason BM is directly connected with stability of ship.
        BMLLIST(w,h,f,t,j,L) is the command function calculating BM.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : length between perpendiculars
        
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.BML(a,self.h,self.f,self.t,self.j,self.L))
            a=a-2
        return result

    def KMLLIST(self,w,h,f,t,j,L):
        """
        KM is the distance from the keel to the metacentre.
        Enter KMLLIST(w,h,f,t,j,L) to calculate its value.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : length between perpendiculars
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.KML(a,self.h,self.f,self.t,self.j,self.L))
            a=a-2
        return result

    def CbLIST(self,w,h,f,L,B,t,j):
        """
        Coefficients of form are dimensionless numbers that describe hull fineness and overall shape characteristics.
        The coefficients are ratios of areas or volumes for the actual hull form compared to prisms or rectangles defined by the ship’s length, breadth, and draft
        The block coefficient of a ship is the ratio of the underwater volume of ship to the volume of a rectangular block having the same overall length, breadth and depth.
        We call block coefficient of a ship as Cb
        This coefficients of form represents how fat ship is.
        To know this value, command with CbLIST(w,h,f,L,B,t,j).
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars.
        'B' : Breadth of ship

        """
        
        
        a=w
        result=[]
        while a>=2:
            result.append(self.Cb(a,self.h,self.f,self.L,B,self.t,self.j))
            a=a-2
        return result

    def CpLIST(self,w,h,f,L,B,t,j):
        """
        The prismatic coefficient(Cp) is the underwater area divided by the area of a midship section.
        Thus, The prismatic coefficient of a ship at any draft is the ratio of the volume of displacement at that draft to the volume of a prism having the same length as the ship and the same cross-sectional area as the ship’s midships area.
        The prismatic coefficient is used mostly by ship-model researchers.
        Command CpLIST(w,h,f,L,B,t,j) to get its value.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars.
        'B' : Breadth of ship
        
        """
        
        
        a=w
        result=[]
        while a>=2:
            result.append(self.Cp(a,self.h,self.f,self.L,B,self.t,self.j))
            a=a-2
        return result

    def CwLIST(self,w,h,L,B):
        """
        These command lines show the waterplane coefficient of ship.
        It is the ratio of the actual area of the waterplane to the product of the length and breadth of the ship.
        'w' : waterline + 1
        'h' : distance between two stations
        'L' : Length between perpendiculars
        'B' : Breadth of ship
        """
        
        a=w
        result=[]
        while a>=2:
            result.append(self.Cw(a,self.h,self.L,B))
            a=a-2
        return result

    def CmLIST(self,w,B):
        
        """
        The midship section coefficient (Cm) is the ratio of the area of the immersed midship section (Am) at a particular draft to that of a rectangle of the same draft and breadth as the ship
        'w' : waterline+ 1
        'B' : Breadth
        
        """    
        
        a=w
        result=[]
        while a>=2:
            result.append(self.Cm(a,B))
            a=a-2
        return result

    def CvpLIST(self,w,h,f,L,B,t,j):
        """
        CvpLIST(w,h,f,L,B,t,j) is the command function for vertical prismatic coefficient.
        A large value of vertical prismatic coefficient indicates will indicate body sections of U-form and a low will indicate V-sections.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        'f' : distance between waterlines
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : Length between perpendiculars.
        'B' : Breadth of ship
        
        """
        a=w
        result=[]
        while a>=2:
            result.append(self.Cvp(a,self.h,self.f,self.L,B,self.t,self.j))
            a=a-2
        return result

    def SSIxLIST(self,w,t,j,h):
        """
        BM is the metacentric radius of ship.
        Transverse metacentric height (BM) = Transverse moment of inertia of waterplane / volume displacement of ship
        To get the parameter BM, transverse moment of inertia is necessary value.
        Enter SSIxLIST(w,t,j,h).
        DO NOT FORGET : the water line to find should be added by 1.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        
        """
        temp2=ship_transom(1,8.7,2,1.9245,174)
        a=w
        result=[]
        while a>=2:
            result.append(temp2.SSIx(a,self.t,self.j,self.h))
            a=a-2
        return result

    def I1LIST(self,w,h,t,j,L):
        """
        BM is the metacentric radius of ship.
        Longitudinal metacentric height (BM) = Longitudinal moment of inertia of waterplane / volume displacement of ship
        To get the parameter BML, longitudinal moment of inertia is necessary value.
        Enter IlLIST(w,h,t,j,L).
        DO NOT FORGET : the water line to find should be added by 1.
        'w' : waterline + 1
        'h' : distance between two stations in main part of ship
        't' : distance between two stations in stern attachments part
        'j' : distance between two stations in bow attachments part
        'L' : length between perpendiculars
        
        """
        a = w
        result=[]
        while a>=2:
            result.append(self.I1(a,self.h,self.t,self.j,self.L))
            a=a-2
        return result


    def WLlist(self,w,h,f,L,B):
        
        a=1
        result=[]
        for a in range(1,w+1,2):
            result.append("%d" %a)
            a=a+2
        return result
    

    
class offss:
    def __init__(self,f,h,j,t,L):
        self.f=f
        self.h=h
        self.j=j
        self.t=t
        self.L=L
        
    def offset(self,w,h,f,L,B,t,j):
        """
        BM is the metacentric radius of ship.
        Longitudinal metacentric height (BM) = Longitudinal moment of inertia of waterplane / volume displacement of ship
        To get the parameter BML, longitudinal moment of inertia is necessary value.
        Enter IlLIST(w,h,t,j,L).
        DO NOT FORGET : the water line to find should be added by 1.

        
        """
        temp3 = ship_mid(1,8.7,2,1.9245,174)
        data = temp3.WLlist(w,h,f,L,B)
        result=pd.DataFrame(data)
        
        result['배수용적 (▽mld.)'] = temp3.DISLIST2(w,self.h,self.f,self.t,self.j)
        result['배수량 (△mld.)'] = temp3.DISLIST(w,self.h,self.f,self.t,self.j)
        result['수선면적(Aw)'] = temp3.AwLIST(w,self.h)
        result['중앙횡단면적(Am)'] = temp3.AmLIST(w)    
        result['매 Cm 배수톤수(TPC)'] = temp3.TPCLIST(w,self.h)
        result['매 Cm 트리밍 정톤수(Wcm)'] = temp3.WcmLIST(w,self.h,self.t,self.j,self.L)
        result['부심위치(KB)'] = temp3.KBLIST(w,self.h,self.f,self.t,self.j)
        result['횡메타센터 반지름(BM)'] = temp3.BMLIST(w,self.h,self.f,self.t,self.j)
        result['횡메타센터 높이(KM)'] = temp3.KMLIST(w,self.h,self.f,self.t,self.j)
        result['종메타센터 반지름(BML)'] = temp3.BMLLIST(w,self.h,self.f,self.t,self.j,self.L)
        result['종메타센터 높이(KML)'] = temp3.KMLLIST(w,self.h,self.f,self.t,self.j,self.L)
        result['부심위치(LCB)'] = temp3.LCBLIST(w,self.h,self.f,self.t,self.j,self.L)
        result['부면심 위치(LCF)'] = temp3.LCFLIST(w,self.h,self.t,self.j,self.L)
        result['방형 계수(Cb)'] = temp3.CbLIST(w,self.h,self.f,self.L,B,self.t,self.j)
        result['주형 계수(Cp)'] = temp3.CpLIST(w,self.h,self.f,self.L,B,self.t,self.j)
        result['수선면 계수(Cw)'] = temp3.CwLIST(w,self.h,self.L,B)
        result['중앙 횡단면 계수(Cm)'] = temp3.CmLIST(w,B)
        result['연직 주형 계수(Cvp)'] = temp3.CvpLIST(w,self.h,self.f,self.L,B,self.t,self.j)
        result['It'] = temp3.SSIxLIST(w,self.t,self.j,self.h)
        result['Il'] = temp3.I1LIST(w,self.h,self.t,self.j,self.L)
        
        
        return result
    

class hydrostaticCurve:
    def __init__(self,f,h,j,t,L):
        self.f=f
        self.h=h
        self.j=j
        self.t=t
        self.L=L
        
    def curve(self,w,h,f,L,B,t,j):
        temp1=ship_mid(1,8.7,2,1.9245,174)
        
        a=w
        y = range(2,w)
        plt.yticks(range(2,w,2))
        x = [temp1.DIS(a+1,self.h,self.f,self.t,self.j)/2000 for a in y]#축척 1 = 2000t
        z = [temp1.DIS(a+1,self.h,self.f,self.t,self.j)/2000/1.025 for a in y]#축척 1 = 2000t
        e = [temp1.KB(a+1,self.h,self.f,self.t,self.j) for a in y] #축척 1 = 1m
        g = [temp1.Aw(a+1,self.h)/200 for a in y]#축척 1 = 200
        p = [temp1.TPC(a+1,self.h)/2 for a in y]#축척 1 = 2t
        u = [temp1.Cm(a+1,B)/0.05 for a in y]#축척 1 = 0.05
        c = [temp1.Cw(a+1,self.h,self.L,B)/0.05 for a in y]#축척 1 = 0.05
        q = [temp1.KM(a+1,self.h,self.f,self.t,self.j) for a in y]
        m = [temp1.MTC(a+1,self.h,self.f,self.t,self.j,self.L)/20 for a in y]
        v = [temp1.KML(a+1,self.h,self.f,self.t,self.j,self.L)/40 for a in y]
        ww = [temp1.Cb(a+1,self.h,self.f,self.L,B,self.t,self.j)/0.05 for a in y]
        ii = [temp1.Cp(a+1,self.h,self.f,self.L,B,self.t,self.j)/0.05 for a in y]
        kk = [temp1.SSLCF(a+1,self.h,self.t,self.j,self.L) for a in y]
        hh = [temp1.LCB(a+1,self.h,self.f,self.t,self.j,self.L) for a in y]
        ll = [temp1.Cvp(a+1,self.h,self.f,self.L,B,self.t,self.j)/0.05 for a in y]
        
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
        
        return plt.show()
        


# In[44]:


A=ship_transom(1,8.7,2,1.9245,174)


# In[45]:


B=ship_bow(1,8.7,2,1.9245,174)


# In[46]:


C=ship_mid(1,8.7,2,1.9245,174)


# In[47]:


o=offss(1,8.7,2,1.9245,174)
o.offset(20,8.7,1,174,32.1,1.9245,2)


# In[41]:


curve=hydrostaticCurve(1,8.7,2,1.9245,174)
curve.curve(20,8.7,1,174,32.1,1.9245,2)


