import matplotlib
import pandas

"""
This command lines make Python import offset file from Excel.
"""
dataoffset = pandas.read_excel('offset.xlsx')  ### Enter offset file name.


def WL(s, w):
    """
    In WL(s,w), 's' is for station number and 'w' for the number of waterline.
    You can command any station and waterline you want.
    This will show how far it is located from baseline and centerline of ship.
    """
    result = dataoffset.iloc[s + 2, w + 2]
    return result


def FAP(s, w):
    """
    The command lines are to get the value of ∑f(yH) of stern attachments.
    ∑f(yH) is the value to find the area of midship section.
    You can command FAP(s,w) to get it.
    BUT, you have to be very careful about station number.
    Since, These are about stern attachments, station number starts from AP with number 0.
    And now you will know that if you type -1 in 's', you would get the value which is located middle of transom and AP and -2 is transom of stern.
    """
    total = 0
    a = w
    while w - 2 <= a <= w:
        if a == w - 1:
            total += WL(s, a) * 4
        else:
            total += WL(s, a)
        a = a - 1
        total = total
    return total


def FAm(s, w):
    """
    These are to know the area of midship section of the stern.
    Just same as above, AP starts with number 0.
    If you want to know about transom or middle of transom and AP, command -2 , -1 each in 's'.
    It is applicable in other value also, if you are to get the values of something in the place of stern attachments.
    Type the station number and waterline number you want to know.
    """
    a = s
    if a == -1:
        total = FAP(a, w) * 4 * 3 / 8
    else:
        total = FAP(a, w) * 3 / 8
    total = total
    return total


def SFAm(w):
    """
    These command lines are to get the value of ∑f(Am) of stern attachments.
    ∑f(Am) is the value, using to know the displacements of stern attachments part of ship.
    You can command SFAm(w) to get this value.
    And SFAm(w) configures the ∑f(Am) of stern attachments, which has waterline 'w-1' to 'w-2'.
    """
    a = -2
    total = 0
    while a <= 0:
        total += FAm(a, w)
        a = a + 1
    total = total
    return total


def VAP(w, t):
    """
    Now, you can get the displacements of stern attachments part of ship.
    Displacement is weight of water that a ship pushes aside when it is floating, which in turn is the weight of a ship
    To get this value, we divided ship by station and waterline.
    As you know, you can just type waterline in the place of 'w', and 't' means the space between two station.
    """
    result = SFAm(w) * t * 2 * 3 / 8
    return result


def VVAP(w, t):
    """
    Now, you can get the displacements of stern attachments part of ship.
    Displacement is weight of water that a ship pushes aside when it is floating.
    To get this value, we divided ship by station and waterline.
    As you know, you can just type waterline in the place of 'w', and 't' means the space between two stations.
    """
    if VAP(w - 1, t) == 0:
        result = 0
    else:
        result = VAP(w, t)
    return result


def WAP(w, t):
    """
    If you got the displacements of ship, you can definitely know the weight.
    These command lines help to get the weight.
    We got the displacements from just above command function VAP(w-1,t).
    What we have to do is just multiply density of water with its result.
    Since, ARPA-GO helps calculation of ship, the density is 1.025 which is sea water.
    You can change the density freely, if you are necessary to.
    Mentioned before, w is for waterline number, t is for the space between two stations.
    """
    if VAP(w - 1, t) == 0:
        result = 0
    else:
        result = VAP(w, t) * 1.025
    return result


def FyAP(s, w):
    """
      FyAP(s,w) is the necessary value to get the water plane area.
      's' is for station number and 'w' is for the number of waterline.
      Don't confuse : Transom of ship is located with station number '-2' and AP is '0'.
      """
    if s == -1:
        result = WL(s, w) * 4
    else:
        result = WL(s, w)
    return result


def AwAP(w, t):
    """
    AwAP(w,t) is the command function for water plane area.
    'w' for water line and 't' for the space between stations.
    """

    s = 0
    result = 0
    while -2 <= s:
        result += FyAP(s, w)
        s = s - 1

        result1 = result * t * 2 / 3
    return result1


def AAwAP(w, t):
    if AwAP(w - 2, t) == 0 or AwAP(w - 1, t) == 0 or AwAP(w, t) == 0:
        result = 0
    else:
        result = AAwAP(w, t)
    return result


def OB(w, t):
    """
    The command lines help to get the value of OB.
    To prove the stability of ship, you might heard of KB,GM ...
    We put the value of OB to get KB, the distance between keel and the center of buoyancy.
    OB means the distance from center of buoyancy to waterline.
    Thus, KB+OB is the distance between keel and waterline.
    Since it is about stern attachments, the waterline starts with w-1 to w-2.
    """

    if AwAP(w, t) == 0:
        result = 0
    else:
        result = (2 / 2 + VAP(w, t) / AwAP(w, t)) / 3
    return result


def KbAP(w, t):
    """
     KB is the centre of buoyancy which is the height above the keel.
     KbAP(w,t) is to get the value of it.
     """
    if OB(w, t) == 0:
        result = 0
    else:
        result = w - 1 - OB(w, t)
    return result


def xfAm(s, w):
    """
    x' * f(AM) is the value to get the longitudinal center of gravity (LCB) of ship.
    Here, 'w' indicates 'waterline - 1' which means :
    if you want to get the value about waterline number 10, you have to enter 11 in 'w' place.
    's' is same as before.
    Station number of AP is '0'.
    """
    if s == -2:
        result = (-2) * FAm(s, w)
    elif s == -1:
        result = (-1) * FAm(s, w)
    else:
        result = 0
    return result


def SxfAm(w):
    """
    The command function SxfAm(w) is the sum of x' * f(AM).
    If you enter waterline you want to know, you will get all station's sum of x' * f(AM).
    This function shows the value of w-1 to w-2's ∑x' * f(AM).
    """
    s = 0
    total = 0
    while -2 <= s:
        total += xfAm(s, w)
        s = s - 1
    total = total
    return total


def APb(w, t):
    """
    These are for APb of stern attachments of ship.
    The inputs are 'w' & 't'.
    Just same as before the waterline expresses w-1 to w-2.
    Enter the waterline what you want to know + 1 in the place of 'w'.
    't' is the distance between two stations.
    """
    if SFAm(w) == 0:
        result = 0
    else:
        result = t * SxfAm(w) / SFAm(w)
    return result


def lcbAP(w, t, L):
    """
    The centroid of the underwater volume of the ship expressed as a longitudinal location.
    We call that centroid point as LCB (longitudinal center of gravity) and it is connected with stability of ship.
    To get the value, enter the command function, lcbAP(w,t,L).
    'L' means LBP, in full form Length between perpendiculars.
    """
    if APb(w, t) == 0 or APb(w - 1, t) == 0 or APb(w - 2, t) == 0:
        result = 0
    else:
        result = -(L / 2) + APb(w, t)
    return result


def IxAP(w, t):
    """
    BM is the metacentric radius of ship.
    Transverse metacentric height (BM) = Transverse moment of inertia of waterplane / volume displacement of ship
    To get the parameter BM, transverse moment of inertia is necassary value.
    Enter IxAP(w,t).
    DO NOT FORGET : the water line to find should be added by 1.
    """
    s = 0
    result = 0
    while -2 <= s:
        if s == -1:
            result += pow(WL(s, w), 3) * 4
        else:
            result += pow(WL(s, w), 3)
        s = s - 1
        result = result
    return result * t * 2 / 3 * 1 / 3


def SSIx(w, t, j, h):
    """
    SSIx(w,t,j,h) is command function, which adds every parts of transverse moment of inertia.
    We devided ship as 3 parts, stern attachments, bow attachments and the rest part of ship.
    The result of these command lines shows the sum of transverse moment of inertia of three parts.
    'w' is for waterline and 't','j''h' are space between two stations for each part.
    't' for stern attachments, 'j' for bow attachments and 'h' is for station of ship.
    """
    result = IxAP(w, t) + IxFP(w, j) + Ix(w, h)
    return result


def SfyAP(w):
    """
     The command lines are to get the value of ∑f(y) of stern attachments.
     You can command SfyAP(w) to get it.
     ∑f(y) adds all the values of station and expresses with waterline form.
     Here, 'w' indicates 'waterline - 1' which means :
     if you want to get the value about waterline number 10, you have to enter 11 in 'w' place.
     """
    s = 0
    result = 0
    while -2 <= s:
        if s == -1:
            result += WL(s, w) * 4
        else:
            result += WL(s, w)
        s = s - 1
        result = result
    return result


def SxfyAP(w):
    """
    The command function SxfyAP(w) is the sum of x' * f(y).
    If you enter waterline you want to know, you will get all station's sum of x' * f(y).
    This function shows the value of w-1 to w-2's ∑x' * f(y).
    """
    s = 0
    total = 0
    while -2 <= s:
        if s == -1:
            total += WL(s, w) * (-1) * 4
        elif s == 0:
            total += 0
        else:
            total += WL(s, w) * (-2)
        s = s - 1
        total = total
    return total


def APf(w, t):
    """
    The result of command lines are APf of stern attachments of ship.
    This parameter is necessary to get the longitudinal moment of inertia of stern attachments part.
    'w' : waterline + 1
    't' : distance between two stations in stern attachments part
    """
    if SfyAP(w) == 0:
        result = 0
    else:
        result = t * SxfyAP(w) / SfyAP(w)
    return result


def MyAP(w, t, L):
    """
    These are command lines for longitudinal moment of stern attachments.
    'w' : waterline + 1
    't' : distance between two stations in stern attachments part
    'L' : Length between perpendiculars
    """

    result = AwAP(w, t) * (-L / 2 + APf(w, t))
    return result


def APIAP(w, t):
    """
    APIAP(w,t) is the command function to get the value of IA.P.
    This parameter helps to get the longitudinal moment of inertia of stern attachments part.
    'w' : waterline + 1
    't' : distance between two stations in stern attachments part
    """

    s = 0
    total = 0
    while -2 <= s:
        if s == -1:
            total += WL(s, w) * (1) * 4
        elif s == 0:
            total += 0
        else:
            total += WL(s, w) * (4)
        s = s - 1
        total = total
    return total * t * t * t * 2 * 1 / 3


def APIY(w, t, L):
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
    result = APIAP(w, t) + AwAP(w, t) * L / 2 * L / 2 + AwAP(w, t) * (-L) * APf(w, t)
    return result


def SfyFP(w):
    """
    The command lines are to get the value of ∑f(y) of bow attachments.
    You can command SfyFP(w) to get it.
    ∑f(y) adds all the values of station and expresses with waterline form.
    Here, 'w' indicates 'waterline - 1' which means :
    if you want to get the value about waterline number 10, you have to enter 11 in 'w' place.
    """
    s = 26
    result = 0
    while 24 <= s:
        if s == 25:
            result += WL(s, w) * 4
        else:
            result += WL(s, w)
        s = s - 1
        result = result
    return result


def SFyHFP(s, w):
    """
    The command lines are to get the value of ∑f(yH) of bow attachments.
    ∑f(yH) is the value to find the area of midship section.
    You can command SFyHFP(s,w) to get it.
    Since, These are about bow attachments, station number ends FP with number 24.
    And now you will know that if you want to get the value of bow attachments, enter 24 + j in the place of 's'.
    j: distance between two stations in bow attachments part
    """

    total = 0
    a = w
    while w - 2 <= a <= w:
        if a == w - 1:
            total += WL(s, a) * 4
        else:
            total += WL(s, a)
        a = a - 1
        total = total
    return total


def FAmFP(s, w):
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
        total = SFyHFP(s, w) * 4 * 3 / 8
    else:
        total = SFyHFP(s, w) * 3 / 8
    total = total
    return total


def SFAmFP(w):
    """
    These command lines are to get the value of ∑f(Am) of bow attachments.
    ∑f(Am) is the value, using to know the displacements of bow attachments part of ship.
    You can command SFAmFP(w) to get this value.
    And SFAmFP(w) configures the ∑f(Am) of bow attachments, which has waterline 'w-1' to 'w-2'.
    """
    a = 24
    total = 0
    while a <= 26:
        total += FAmFP(a, w)
        a = a + 1
    total = total
    return total


def VFP(w, j):
    """
    Now, you can get the displacements of bow attachments part of ship.
    Displacement is weight of water that a ship pushes aside when it is floating, which in turn is the weight of a ship
    To get this value, we divided ship by station and waterline.
    'w': waterline + 1
    'j': distance between two stations in bow attachments part
    """
    result = SFAmFP(w) * j * 3 / 8 * 2
    return result


def AwFP(w, j):
    """
    AwFP(w,j) is the command function for water plane area.
    'w': waterline + 1
    'j': distance between two stations in bow attachments part
    """
    result = 0
    s = 24
    while s <= 26:
        if s == 25:
            result += WL(s, w) * 4
        else:
            result += WL(s, w)
        s = s + 1
        result = result
    return result * j * 2 / 3


def WFP(w, j):
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
    result = VFP(w, j) * 1.025
    return result


def FPb(w, j):
    """
     These are for FPb of bow attachments of ship.
     The inputs are 'w' & 'j'.
     Just same as before the waterline expresses w-1 to w-2.
     Enter the waterline what you want to know + 1 in the place of 'w'.
     'j' is the distance between two stations.
     """
    s = 24
    result = 0
    while s <= 26:
        if s == 24:
            result += FAmFP(s, w) * 0
        elif s == 25:
            result += FAmFP(s, w) * 1
        else:
            result += FAmFP(s, w) * 2
        s = s + 1
        result = result
    return result / SFAmFP(w) * j


def lcbFP(w, j, L):
    """
    The centroid of the underwater volume of the ship expressed as a longitudinal location.
    We call that centroid point as LCB (longitudinal center of gravity) and it is connected with stability of ship.
    To get the value, enter the command function, lcbFP(w,j,L).
    'L' means LBP, in full form Length between perpendiculars.
    'w': waterline + 1
    'j': distance between two stations in bow attachments part
    """
    result = FPb(w, j) + (L / 2)
    return result


def SfVFP(w):
    """
    Command function SfVFP(w) shows the sum of displacements divided by each stations.
    It is functioned by waterline wise.
    'w'= waterline + 1
    Thus, the result of this command lines is ∑f(V) of bow attachments of ship.
    """
    a = w
    result = 0
    while w - 2 <= a:
        if a == w - 1:
            result += SfyFP(a) * 4
        else:
            result += SfyFP(a)
        a = a - 1
        result = result
    return result


def kbFP(w, f):
    """
       KB is the centre of buoyancy which is the height above the keel.
       kbFP(w,f) is to get the value of it.
       'w' = waterline + 1
       'f' = the distance between waterline
       """
    a = w
    result = 0
    while w - 2 <= a:
        if a == 0:
            result += 0
        elif a == 1:
            result += 0
        elif a == w - 1:
            result += SfyFP(a) * 4 * (a - 1)
        else:
            result += SfyFP(a) * (a - 1)
        a = a - 1
        result = result
    return result / SfVFP(w) * f


def IxFP(w, j):
    """
     BM is the metacentric radius of ship.
     Transverse metacentric height (BM) = Transverse moment of inertia of waterplane / volume displacement of ship
     To get the parameter BM, transverse moment of inertia is necessary value.
     Enter IxFP(w,j).
     DO NOT FORGET : the water line to find should be added by 1.
     'w': waterline + 1
     'j': distance between two stations in bow attachments part
     """
    a = 26
    result = 0
    while a >= 24:
        if a == 25:
            result += pow(WL(a, w), 3) * 4
        else:
            result += pow(WL(a, w), 3)
        a = a - 1
        result = result
    return result * 2 / 3 * 1 / 3 * j


def FPf(w, j):
    """
    The result of command lines are FPf of bow attachments of ship.
    This parameter is necessary to get the longitudinal moment of inertia of bow attachments part.
    'w' : waterline + 1
    'j' : distance between two stations in bow attachments part
    """
    a = 26
    result = 0
    result1 = 0
    while a >= 24:
        if w == 2:
            result1 = 0
        else:
            if a == 24:
                result += 0
            elif a == 25:
                result += WL(a, w) * 4
            else:
                result += WL(a, w) * 2
            a = a - 1
            result1 = result / SfyFP(w) * j
    return result1


def SxfyFP(w):
    """
    The command function SxfyFP(w) is the sum of x' * f(y).
    If you enter waterline you want to know, you will get all station's sum of x' * f(y).
    This function shows the value of (w-1 to w-2)'s ∑x' * f(y).
    """
    a = 26
    result = 0
    while a >= 24:
        if a == 25:
            result += WL(a, w) * 4 * 1
        elif a == 26:
            result += WL(a, w) * 2
        else:
            result += 0
        a = a - 1
        result = result
    return result


def FPf(w, j):
    """
    The result of command lines are FPf of bow attachments of ship.
    This parameter is necessary to get the longitudinal moment of inertia of bow attachments part.
    'w' : waterline + 1
    'j' : distance between two stations in bow attachments part
    """
    if SxfyFP(w) == 0:
        result = 0
    else:
        result = SxfyFP(w) / SfyFP(w) * j
    return result


def FPMy(w, j, L):
    """
    These are command lines for longitudinal moment of bow attachments.
    'w' : waterline + 1
    'j' : distance between two stations in bow attachments part
    'L' : Length between perpendiculars
    """
    result = AwFP(w, j) * (-L / 2 + FPf(w, j))
    return result


def FPIFP(w, j):
    """
    FPIFP(w,j) is the command function to get the value of IF.P.
    This parameter helps to get the longitudinal moment of inertia of bow attachments part.
    'w' : waterline + 1
    'j' : distance between two stations in bow attachments part
    """
    result = 0
    s = 26
    while s >= 24:
        if s == 24:
            result += 0
        elif s == 25:
            result += WL(s, w) * 4
        else:
            result += WL(s, w) * 4
        s = s - 1
        result = result
    return result * 2 * 1 / 3 * j * j * j


def FPIy(w, j, L):
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
    result = FPIFP(w, j) + AwFP(w, j) * (L / 2) * (L / 2) + AwFP(w, j) * (-L) * FPf(w, j)
    return result


def simy(w):
    """
    The command lines are to get the value of ∑f(y) of main part of ship.
    You can command simy(w) to get it.
    ∑f(y) adds all the values of station and expresses with waterline form.
    Here, 'w' indicates 'waterline - 1' which means :
    if you want to get the value about waterline number 10, you have to enter 11 in 'w' place.
    """
    total = 0
    s = 0

    while s <= 24:

        if s == 0 or s == 24:
            total += 0.5 * WL(s, w)
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += 2 * WL(s, w)
        elif s == 2 or s == 22:
            total += WL(s, w)
        elif s == 4 or s == 20:
            total += 1.5 * WL(s, w)
        elif s % 2 != 0:
            total += 4 * WL(s, w)
        else:
            total += 2 * WL(s, w)
        s = s + 1
        total = total

    return total


def simx(n):
    """
    Command function simx(n) shows the sum of displacements divided by each stations.
    It is functioned by waterline wise.
    'n'= waterline + 1
    Thus, the result of this command lines is ∑f(V) of main part of ship.
    Reference : This command lines show the displacements of ship with three waterlines combined.
    """
    total1 = 0
    w = n - 2
    while w <= n:
        if w == n or w == n - 2:
            total1 += simy(w)
        else:
            total1 += 4 * simy(w)
        w = w + 1
        total1 = total1
    return total1


def W(n, h, f):
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
    if n == 2:
        result = simx(n) * h / 3 * f / 3 * 1.025
    else:
        result = simx(n) * h / 3 * f / 3 * 1.025 * 2
    return result


def DIS(s, h, f, t, j):
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

    total2 = 0
    n = s
    while n > 1:
        total2 += W(n, h, f) + WAP(n, t) + WFP(n, j)
        n = n - 2
        total2 = total2
    return total2


def W(n, h, f):
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
    if n == 2:
        result = simx(n) * h / 3 * f / 3 * 1.025
    else:
        result = simx(n) * h / 3 * f / 3 * 1.025 * 2
    return result


def SSW(w, j, t):
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
    result = (VFP(w, j) + VAP(w, t)) * 1.025
    return result


def Kb(t):
    """
    KB is the centre of buoyancy which is the height above the keel.
    Kb(t) is to get the value of it.
    The product of this command lines shows kb with three waterlines combined.
    """

    total3 = 0
    w = t
    while t - 2 <= w <= t:
        if w == 0:
            total3 += 0
        elif w == 1:
            total3 += simy(1) * 2
        elif w == 2:
            total3 += simy(2)
        elif w == t - 1:
            total3 += simy(w) * 4 * (w - 1)
        else:
            total3 += simy(w) * (w - 1)
        w = w - 1
        total3 = total3
    return total3 / simx(t)


def SSM(n, h, f, t, j):
    """
    To get the KB of ship, the parameter ∑z' * f(V)is necessary.
    SSM(n,h,f,t,j) is command function to get its value.
    'n' : waterline + 1
    'h' : distance between two stations in main part of ship
    'f' : distance between waterlines
    't' : distance between two stations in stern attachments part
    'j' : distance between two stations in bow attachments part
    """
    result = 0
    a = n
    while a >= 2:
        result += (KbAP(a, t) * VVAP(a, j) * 1.025) + (kbFP(a, f) * VFP(a, j) * 1.025) + Kb(a) * W(a, h, f)
        a = a - 2
        result = result
    return result


def KB(n, h, f, t, j):
    """
    KB is the centre of buoyancy which is the height above the keel.
    KB(n,h,f,t,j) is to get the value of it.
    'n' : waterline + 1
    'h' : distance between two stations in main part of ship
    'f' : distance between waterlines
    't' : distance between two stations in stern attachments part
    'j' : distance between two stations in bow attachments part
    """
    result = SSM(n, h, f, t, j) / DIS(n, h, f, t, j)
    return result


def X(s, g):
    """
     The command lines are to get the value of ∑f(yH) of main part of ship.
     ∑f(yH) is the value to find the area of midship section.
     You can command X(s,g) to get it.
     's' : station number
     'g' : waterline number + 1
     """
    total4 = 0
    w = g
    while g - 2 <= w <= g:
        if w == g - 1:
            total4 += WL(s, w) * 4
        else:
            total4 += WL(s, w)
        w = w - 1
        total4 = total4
    return total4


fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]


def lcb(f, h):
    """
    x' * f(V) is the value to get the longitudinal center of gravity (LCB) of ship.
    """
    total = 0
    s = 0
    while s <= 24:
        if s == 0 or s == 24:
            total += X(s, f) * fx[s] * 0.5
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += X(s, f) * fx[s] * 2
        elif s == 2 or s == 22:
            total += X(s, f) * fx[s]
        elif s == 4 or s == 20:
            total += X(s, f) * fx[s] * 1.5
        elif s % 2 != 0:
            total += X(s, f) * fx[s] * 4
        else:
            total += X(s, f) * fx[s] * 2
        s = s + 1
        total = total
    return total * h / simx(f)


def SSSM(s, h, f, t, j, L):
    """
    The command function SSSM(s,h,f,t,j,L) is the sum of x' * f(V).
    We've got the parameter x' * f(V) from above command lines.
    's' : waterline + 1
    'h' : distance between two stations in main part of ship
    'f' : distance between waterlines
    't' : distance between two stations in stern attachments part
    'j' : distance between two stations in bow attachments part
    """
    result = 0
    n = s
    while n >= 2:
        result += (lcb(n, h) * W(n, h, f) / 1.025) + (lcbFP(n, j, L) * VFP(n, j)) + (lcbAP(n, t, L) * VAP(n, t))
        n = n - 2
    return result


def LCB(s, h, f, t, j, L):
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
    result = SSSM(s, h, f, t, j, L) / DIS(s, h, f, t, j)
    return result


def Am(a):
    """
    Am(a) is the command function for midsection area of ship.
    'a' : waterline +1
    The product of this command lines shows midsection area with three waterlines combined.
    """
    if a == 2:
        result = X(12, a) / 3
    else:
        result = X(12, a) * 2 / 3
    return result


def SAm(q):
    """
    SAm(q) is the command function for midsection area of ship.
    'q' : waterline +1
    """
    total6 = 0
    a = q
    while a >= 2:
        total6 += Am(a)
        a = a - 2
        total6 = total6
    return total6


def Cb(m, h, f, L, B, t, j):
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
    result = DIS(m, h, f, t, j) / 1.025 / (m - 1) / L / B
    return result


def Cm(m, B):
    """
    The midship section coefficient (Cm) is the ratio of the area of the immersed midship section (Am) at a particular draft to that of a rectangle of the same draft and breadth as the ship
    Cm= Am / B x d
    We've got parameter Am with command function SAm(m).
    'B' : Breadth of ship
    'm' : waterline + 1
    """
    result = SAm(m) / (m - 1) / B
    return result


def Cp(m, h, f, L, B, t, j):
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
    result = Cb(m, h, f, L, B, t, j) / Cm(m, B)
    return result


def Aw(r, h):
    """
    Aw(r,h) is the command function for water plane area.
    'r' for water line and 'h' for the space between stations.
    """
    result = simy(r) * 2 / 3 * h
    return result


def Cw(r, h, L, B):
    """
    These command lines show the waterplane coefficient of ship.
    It is the ratio of the actual area of the waterplane to the product of the length and breadth of the ship.
    'r' : waterline + 1
    'h' : distance between two stations
    'L' : Length between perpendiculars
    'B' : Breadth of ship
    """
    result = Aw(r, h) / B / L
    return result


def Cvp(r, h, f, L, B, t, j):
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
    result = Cb(r, h, f, L, B, t, j) / Cw(r, h, L, B)
    return result


def simy3(w):
    """
    These command lines represents ∑f(y^3) by each waterline.
    This parameter is necessary value to get inertia moment of ship.
    'w' = waterline + 1
    """
    total = 0
    s = 0
    while s <= 24:
        if s == 0 or s == 24:
            total += 0.5 * pow(WL(s, w), 3)
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += 2 * pow(WL(s, w), 3)
        elif s == 2 or s == 22:
            total += pow(WL(s, w), 3)
        elif s == 4 or s == 20:
            total += 1.5 * pow(WL(s, w), 3)
        elif s % 2 != 0:
            total += 4 * pow(WL(s, w), 3)
        else:
            total += 2 * pow(WL(s, w), 3)
        s = s + 1
        total = total
    return total


def Ix(w, h):
    """
    BM is the metacentric radius of ship.
    Transverse metacentric height (BM) = Transverse moment of inertia of waterplane / volume displacement of ship
    To get the parameter BM, transverse moment of inertia is necessary value.
    Enter Ix(w,h).
    DO NOT FORGET : the water line to find should be added by 1.
    'w' : waterline + 1
    'h' : distance between two stations
    """
    result = 2 / 3 * h / 3 * simy3(w)
    return result


def BM(w, h, f, t, j):
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
    result = (IxAP(w, t) + IxFP(w, j) + Ix(w, h)) / DIS(w, h, f, t, j) * 1.025
    return result


def KM(w, h, f, t, j):
    """
    KM is the distance from the keel to the metacentre.
    Enter KM(w,h,f,t,j) to calculate its value.
    'w' : waterline + 1
    'h' : distance between two stations in main part of ship
    'f' : distance between waterlines
    't' : distance between two stations in stern attachments part
    'j' : distance between two stations in bow attachments part
    """
    result = BM(w, h, f, t, j) + KB(w, h, f, t, j)
    return result


fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]


def xfy(f):
    """
    The command function xfy(w) is the sum of x' * f(y).
    If you enter waterline you want to know, you will get all station's sum of x' * f(y).
    'w' : waterline + 1
    """
    total = 0
    s = 0
    while s <= 24:
        if s == 0 or s == 24:
            total += WL(s, f) * fx[s] * 0.5
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += WL(s, f) * fx[s] * 2
        elif s == 2 or s == 22:
            total += WL(s, f) * fx[s]
        elif s == 4 or s == 20:
            total += WL(s, f) * fx[s] * 1.5
        elif s % 2 != 0:
            total += WL(s, f) * fx[s] * 4
        else:
            total += WL(s, f) * fx[s] * 2
        s = s + 1
        total = total
    return total


def simy1(w):
    """
    The command lines are to get the value of ∑f(y) of main part of ship.
    You can command simy1(w) to get it.
    ∑f(y) adds all the values of station and expresses with waterline form.
    Here, 'w' indicates 'waterline - 1' which means :
    if you want to get the value about waterline number 10, you have to enter 11 in 'w' place.
    """
    total = 0
    s = 0
    while s <= 24:
        if s == 0 or s == 24:
            total += 0.5 * WL(s, w)
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += 2 * WL(s, w)
        elif s == 2 or s == 22:
            total += WL(s, w)
        elif s == 4 or s == 20:
            total += 1.5 * WL(s, w)
        elif s % 2 != 0:
            total += 4 * WL(s, w)
        else:
            total += 2 * WL(s, w)
        s = s + 1
        total = total
    return total


def LCF(w, h):
    """
    Longitudinal Center of Flotation(LCF) is the center of the waterplane.
    When you are considering the addition of new weight(cargo) and you want to calculate its effect without having to recalculate the LCG of the whole vessel, use the distance from the LCF to the CG of the added cargo.
    'w' : waterline + 1
    'h' : distance between two stations
    """
    result = xfy(w) / simy1(w) * h
    return result


def TPC(r, h):
    """
     Tons per centimetre(TPC), i.e. the number of tons required to sink the vessel one centimetre.
     For instance, if the vessel has a TPC of 60 tons and uses 30 tons of fuel and water a day, then it will reduce its draft by half a centimetre a day.
     'r' : waterline + 1
     'h' : distance between two stations
     """
    result = Aw(r, h) / 100 * 1.025
    return result


def My(w, h):
    """
    These are command lines for longitudinal moment of main part of ship.
    'w' : waterline + 1
    'h' : distance between two stations
    """

    result = Aw(w, h) * LCF(w, h)
    return result


fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]


def x2fy(f):
    """
    The command function x2fy(w) is the twice of sum of x' * f(y).
    If you enter waterline you want to know, you will get all station's sum of x' * f(y) multiplied by 2.
    This function shows the value of f-1's ∑x'* 2 * f(y).
    'w' = waterline + 1
    """
    total = 0
    s = 0
    while s <= 24:
        if s == 0 or s == 24:
            total += WL(s, f) * pow(fx[s], 2) * 0.5
        elif s == 1 or s == 23 or s == 3 or s == 21:
            total += WL(s, f) * pow(fx[s], 2) * 2
        elif s == 2 or s == 22:
            total += WL(s, f) * pow(fx[s], 2)
        elif s == 4 or s == 20:
            total += WL(s, f) * pow(fx[s], 2) * 1.5
        elif s % 2 != 0:
            total += WL(s, f) * pow(fx[s], 2) * 4
        else:
            total += WL(s, f) * pow(fx[s], 2) * 2
        s = s + 1
        total = total
    return total


def Iy(w, h):
    """
    BM is the metacentric radius of ship.
    Longitudinal metacentric height (BMl) = Longitudinal moment of inertia of waterplane / volume displacement of ship
    To get the parameter BM, longitudinal moment of inertia is necessary value.
    Enter Iy(w,h).
    DO NOT FORGET : the water line to find should be added by 1.
    'w' : waterline + 1
    'h' : distance between two stations
    """
    result = 2 / 3 * h * h * h * x2fy(w)
    return result


def SSAw(w, h, t, j):
    """
    You've got the waterplane area (Aw) of stern/bow attachments part and main part of ship.
    These command lines help to get the sum of these three Aw.
    'w' : waterline + 1
    'h' : distance between two stations in main part of ship
    't' : distance between two stations in stern attachments part
    'j' : distance between two stations in bow attachments part
    """

    result = Aw(w, h) + AwAP(w, t) + AwFP(w, j)
    return result


def SSMy(w, h, t, j, L):
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
    result = My(w, h) + FPMy(w, j, L) + MyAP(w, t, L)
    return result


def SSLCF(w, h, t, j, L):
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
    result = SSMy(w, h, t, j, L) / SSAw(w, h, t, j)
    return result


def SSIy(w, h, t, j, L):
    """
    You've got the Iy of stern/bow attachments part and main part of ship.
    These command lines help to get the sum of these three Iy.
    'w' : waterline + 1
    'h' : distance between two stations in main part of ship
    't' : distance between two stations in stern attachments part
    'j' : distance between two stations in bow attachments part
    'L' : Length between perpendiculars
    """
    result = Iy(w, h) + APIY(w, t, L) + FPIy(w, j, L)
    return result


def Il(w, h, t, j, L):
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
    result = SSIy(w, h, t, j, L) - SSLCF(w, h, t, j, L) * SSAw(w, h, t, j)
    return result


def BML(w, h, f, t, j, L):
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
    result = Il(w, h, t, j, L)
    return result / (DIS(w, h, f, t, j) / 1.025)


def MTC(w, h, f, t, j, L):
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
    result = DIS(w, h, f, t, j) * BML(w, h, f, t, j, L) / (100 * L)
    return result


def Wcm(w, h, t, j, L):
    """
    Weight tonnage change trim one Centimeter is full form of Wcm.
    Enter Wcm(w,h,t,j,L) to get the value of it.
    'w' : waterline + 1
    'h' : distance between two stations in main part of ship
    't' : distance between two stations in stern attachments part
    'j' : distance between two stations in bow attachments part
    'L' : length between perpendiculars
    """
    result = -1 * (TPC(w, h) * SSLCF(w, h, t, j, L) / L)
    return result


def KML(w, h, f, t, j, L):
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
    result = BML(w, h, f, t, j, L) + KB(w, h, f, t, j)
    return result


def DISLIST(w, h, f, t, j):
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
    a = w
    result = []
    while a >= 2:
        result.append(DIS(a, h, f, t, j))
        a = a - 2
    result.reverse()
    return result


def DISLIST2(w, h, f, t, j):
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
    a = w
    result = []
    while a >= 2:
        result.append(DIS(a, h, f, t, j) / 1.025)
        a = a - 2
    result.reverse()
    return result


def AwLIST(w, h):
    """
    AwLIST(w,h) is the command function for water plane area.
    'w' for water line and 'h' for the space between stations.
    """
    a = w
    result = []
    while a >= 2:
        result.append(Aw(a, h))
        a = a - 2
    result.reverse()
    return result


def AmLIST(w):
    """
    AmLIST(w) is the command function for midsection area of ship.
    'w' : waterline +1
    """
    a = w
    result = []
    while a >= 2:
        result.append(SAm(a))
        a = a - 2
    result.reverse()
    return result


def TPCLIST(w, h):
    """
    Tons per centimetre(TPC), i.e. the number of tons required to sink the vessel one centimetre.
    For instance, if the vessel has a TPC of 60 tons and uses 30 tons of fuel and water a day, then it will reduce its draft by half a centimetre a day.
    'w' : waterline + 1
    'h' : distance between two stations
    """
    a = w
    result = []
    while a >= 2:
        result.append(TPC(a, h))
        a = a - 2
    result.reverse()
    return result


def MTCLIST(w, h, f, t, j, L):
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
    a = w
    result = []
    while a >= 2:
        result.append(MTC(a, h, f, t, j, L))
        a = a - 2
    result.reverse()
    return result


def WcmLIST(w, h, t, j, L):
    """
     Weight tonnage change trim one Centimeter is full form of Wcm.
     Enter WcmLIST(w,h,t,j,L) to get the value of it.
     'w' : waterline + 1
     'h' : distance between two stations in main part of ship
     't' : distance between two stations in stern attachments part
     'j' : distance between two stations in bow attachments part
     'L' : length between perpendiculars
     """
    a = w
    result = []
    while a >= 2:
        result.append(Wcm(a, h, t, j, L))
        a = a - 2
    result.reverse()
    return result


def KBLIST(w, h, f, t, j):
    """
    KB is the centre of buoyancy which is the height above the keel.
    KBLIST(w,h,f,t,j) is to get the value of it.
    'w' : waterline + 1
    'h' : distance between two stations in main part of ship
    'f' : distance between waterlines
    't' : distance between two stations in stern attachments part
    'j' : distance between two stations in bow attachments part
    """
    a = w
    result = []
    while a >= 2:
        result.append(KB(a, h, f, t, j))
        a = a - 2
    result.reverse()
    return result


def BMLIST(w, h, f, t, j):
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
    a = w
    result = []
    while a >= 2:
        result.append(BM(a, h, f, t, j))
        a = a - 2
    result.reverse()
    return result


def KMLIST(w, h, f, t, j):
    """
    KM is the distance from the keel to the metacentre.
    Enter KMLIST(w,h,f,t,j) to calculate its value.
    'w' : waterline + 1
    'h' : distance between two stations in main part of ship
    'f' : distance between waterlines
    't' : distance between two stations in stern attachments part
    'j' : distance between two stations in bow attachments part
    """
    a = w
    result = []
    while a >= 2:
        result.append(KM(a, h, f, t, j))
        a = a - 2
    result.reverse()
    return result


def LCBLIST(w, h, f, t, j, L):
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
    a = w
    result = []
    while a >= 2:
        result.append(LCB(a, h, f, t, j, L))
        a = a - 2
    result.reverse()

    return result


def LCFLIST(w, h, t, j, L):
    """
    Longitudinal Center of Flotation(LCF) is the center of the waterplane.
    When you are considering the addition of new weight(cargo) and you want to calculate its effect without having to recalculate the LCG of the whole vessel, use the distance from the LCF to the CG of the added cargo.
    'w' : waterline + 1
    'h' : distance between two stations
    't' : distance between two stations in stern attachments part
    'j' : distance between two stations in bow attachments part
    'L' : length between perpendiculars
    """
    a = w
    result = []
    while a >= 2:
        result.append(SSLCF(a, h, t, j, L))
        a = a - 2
    result.reverse()
    return result


def BMLLIST(w, h, f, t, j, L):
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
    a = w
    result = []
    while a >= 2:
        result.append(BML(a, h, f, t, j, L))
        a = a - 2
    result.reverse()

    return result


def KMLLIST(w, h, f, t, j, L):
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
    a = w
    result = []
    while a >= 2:
        result.append(KML(a, h, f, t, j, L))
        a = a - 2
    result.reverse()
    return result


def CbLIST(w, h, f, L, B, t, j):
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
    a = w
    result = []
    while a >= 2:
        result.append(Cb(a, h, f, L, B, t, j))
        a = a - 2
    result.reverse()

    return result


def CpLIST(w, h, f, L, B, t, j):
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
    a = w
    result = []
    while a >= 2:
        result.append(Cp(a, h, f, L, B, t, j))
        a = a - 2
    result.reverse()
    return result


def CwLIST(w, h, L, B):
    """
    These command lines show the waterplane coefficient of ship.
    It is the ratio of the actual area of the waterplane to the product of the length and breadth of the ship.
    'w' : waterline + 1
    'h' : distance between two stations
    'L' : Length between perpendiculars
    'B' : Breadth of ship
    """
    a = w
    result = []
    while a >= 2:
        result.append(Cw(a, h, B, L))
        a = a - 2
    result.reverse()
    return result


def CmLIST(w, B):
    """
    The midship section coefficient (Cm) is the ratio of the area of the immersed midship section (Am) at a particular draft to that of a rectangle of the same draft and breadth as the ship
    'w' : waterline+ 1
    'B' : Breadth
    """
    a = w
    result = []
    while a >= 2:
        result.append(Cm(a, B))
        a = a - 2
    result.reverse()
    return result


def CvpLIST(w, h, f, L, B, t, j):
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
    a = w
    result = []
    while a >= 2:
        result.append(Cvp(a, h, f, L, B, t, j))
        a = a - 2
    result.reverse()
    return result


def SSIxLIST(w, t, j, h):
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
    a = w
    result = []
    while a >= 2:
        result.append(SSIx(a, t, j, h))
        a = a - 2
    result.reverse()
    return result


def IlLIST(w, h, t, j, L):
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
    result = []
    while a >= 2:
        result.append(Il(a, h, t, j, L))
        a = a - 2
    result.reverse()
    return result


def WLlist(w, h, f, L, B):
    a = 1
    result = []
    for a in range(1, w + 1, 2):
        result.append("%d " % a)
        a = a + 2
    return result


import pandas as pd


def Calculation_sheet():
    w = dataoffset.shape[1] - 3
    h = WL(7, -1) - WL(6, -1)
    f = 1
    t = -WL(-1, -1)
    j = WL(25, -1) - WL(24, -1)
    L = WL(24, -1)
    B = WL(12, w)
    data = WLlist(w, h, f, L, B)

    result = pd.DataFrame(data)

    result['배수용적 (▽mld.)'] = DISLIST2(w, h, f, t, j)
    result['배수량 (△mld.)'] = DISLIST(w, h, f, t, j)
    result['수선면적(Aw)'] = AwLIST(w, h)
    result['중앙횡단면적(Am)'] = AmLIST(w)
    result['매 Cm 배수톤수(TPC)'] = TPCLIST(w, h)
    result['매 Cm 트리밍 정톤수(Wcm)'] = WcmLIST(w, h, t, j, L)
    result['부심위치(KB)'] = KBLIST(w, h, f, t, j)
    result['횡메타센터 반지름(BM)'] = BMLIST(w, h, f, t, j)
    result['횡메타센터 높이(KM)'] = KMLIST(w, h, f, t, j)
    result['종메타센터 반지름(BML)'] = BMLLIST(w, h, f, t, j, L)
    result['종메타센터 높이(KML)'] = KMLLIST(w, h, f, t, j, L)
    result['부심위치(LCB)'] = LCBLIST(w, h, f, t, j, L)
    result['부면심 위치(LCF)'] = LCFLIST(w, h, t, j, L)
    result['방형 계수(Cb)'] = CbLIST(w, h, f, L, B, t, j)
    result['주형 계수(Cp)'] = CpLIST(w, h, f, L, B, t, j)
    result['수선면 계수(Cw)'] = CwLIST(w, h, L, B)
    result['중앙 횡단면 계수(Cm)'] = CmLIST(w, B)
    result['연직 주형 계수(Cvp)'] = CvpLIST(w, h, f, L, B, t, j)
    result['It'] = SSIxLIST(w, t, j, h)
    result['Il'] = IlLIST(w, h, t, j, L)

    return result


print(Calculation_sheet())

import matplotlib.pyplot as plt


def Hydrostatic_curve():
    w = dataoffset.shape[1] - 3
    h = WL(7, -1) - WL(6, -1)
    f = 1
    t = -WL(-1, -1)
    j = WL(25, -1) - WL(24, -1)
    L = WL(24, -1)
    B = WL(12, w)
    data = WLlist(w, h, f, L, B)
    y = range(2, w)
    plt.yticks(range(2, w, 2))
    plt.xticks(range(-5, 150, 5))
    x = [DIS(a + 1, h, f, t, j) / 8000 for a in y]
    z = [DIS(a + 1, h, f, t, j) / 8000 / 1.025 for a in y]
    e = [KB(a + 1, h, f, t, j) for a in y]
    g = [Aw(a + 1, h) / 600 for a in y]
    p = [TPC(a + 1, h) / 20 for a in y]
    u = [Cm(a + 1, B) / 0.05 for a in y]
    c = [Cw(a + 1, h, L, B) / 0.05 for a in y]
    q = [KM(a + 1, h, f, t, j) / 2 for a in y]
    m = [MTC(a + 1, h, f, t, j, L) / 200 for a in y]
    v = [KML(a + 1, h, f, t, j, L) / 50 for a in y]
    ww = [Cb(a + 1, h, f, L, B, t, j) / 0.05 for a in y]
    ii = [Cp(a + 1, h, f, L, B, t, j) / 0.05 for a in y]
    kk = [SSLCF(a + 1, h, t, j, L) for a in y]
    hh = [LCB(a + 1, h, f, t, j, L) for a in y]
    ll = [Cvp(a + 1, h, f, L, B, t, j) / 0.05 for a in y]

    plt.plot(x, y, 'r')
    plt.plot(z, y, 'b')
    plt.plot(e, y, 'g')
    plt.plot(g, y, 'c')
    plt.plot(p, y, 'm')
    plt.plot(u, y, 'k')
    plt.plot(c, y, 'y')
    plt.plot(q, y, color='brown')
    plt.plot(m, y, color='grey')
    plt.plot(v, y, color='violet')
    plt.plot(ww, y, color='orange')
    plt.plot(ii, y, '--')
    plt.plot(kk, y, color='tan')
    plt.plot(hh, y, color='maroon')
    plt.plot(ll, y, color='navy')
    plt.grid()
    plt.legend(
        ['△ 1= 8000t', '▽ 1= 8000t', 'KB 1= 1m', 'Aw 1= 600m^2', 'TPC 1= 20t', 'Cm 1= 0.05', 'Cw 1= 0.05', 'KM 1= 2m',
         'MTC 1= 200t-m', 'KML 1= 50m', 'Cb 1= 0.05', 'Cp 1= 0.05', 'LCF 1= 1m', 'LCB 1= 1m', 'Cvp 1= 0.05'])

    return plt.show()


Hydrostatic_curve()
