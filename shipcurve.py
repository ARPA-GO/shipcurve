import sys
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
from pandas import DataFrame


def WL(s, w):  # s는 staion no, w는 W.L.no
    result = dataoffset.iloc[s + 2, w + 2]
    return result


def FAP(s, w):  # transom~AP까지 staion 별 ∑f(yH)입니다. -2는 transom, -1은 중간 0 은 AP

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


def FAm(s, w):  # 이것은 선미부 staion별 f(AM)입니다. -2는 transom, -1은 중간 0 은 AP
    a = s
    if a == -1:
        total = FAP(a, w) * 4 * 3 / 8
    else:
        total = FAP(a, w) * 3 / 8
    total = total
    return total


def SFAm(w):  # 이것은 WL w-1 ~ w-2 까지 선미부가부의 ∑f(AM)입니다.
    a = -2
    total = 0
    while a <= 0:
        total += FAm(a, w)
        a = a + 1
    total = total
    return total


def VAP(w, t):  # 이것은 WL w-1 ~ w-2 까지 선미부가부의 V입니다. t는 staion 간격
    result = SFAm(w) * t * 2 * 3 / 8
    return result


def VVAP(w, t):  # 이것은 WL w-1 ~ w-2 까지 선미부가부의 V입니다. t는 staion 간격
    if VAP(w - 1, t) == 0:
        result = 0
    else:
        result = VAP(w, t)
    return result


def WAP(w, t):  # 이것은 WL w-1 ~ w-2 까지 선미부가부의 w입니다. t는 staion 간격
    if VAP(w - 1, t) == 0:
        result = 0
    else:
        result = VAP(w, t) * 1.025
    return result


def FyAP(s, w):  # 이것은 WL w-1, staion no,s의 f(y)입니다. s=0,(AP),s=-1(중간), s=(-2)끝
    if s == -1:
        result = WL(s, w) * 4
    else:
        result = WL(s, w)
    return result


def AwAP(w, t):  # 이것은 WL w-1의 선미부가부 Aw입니다. h는 staion 간격
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


def OB(w, t):  # 이것은 WL w-1 ~ w-1까지의 선미부가부의 OB입니다. h는 staion 간격
    if AwAP(w, t) == 0:
        result = 0
    else:
        result = (2 / 2 + VAP(w, t) / AwAP(w, t)) / 3
    return result


def KbAP(w, t):  # 이것은 WL w-1 ~ w-2까지의 선미부가부의 Kb입니다. h는 staion 간격
    if OB(w, t) == 0:
        result = 0
    else:
        result = w - 1 - OB(w, t)
    return result


def xfAm(s, w):  # 이것은 WL w-1 의 선미부가부x' * f(AM)의 Kb입니다. s=0,(AP),s=-1(중간), s=(-2)끝
    if s == -2:
        result = (-2) * FAm(s, w)
    elif s == -1:
        result = (-1) * FAm(s, w)
    else:
        result = 0
    return result


def SxfAm(w):  # 이것은 WL w-1 ~ w-2까지의 선미부가부의 ∑x' * f(AM)입니다.
    s = 0
    total = 0
    while -2 <= s:
        total += xfAm(s, w)
        s = s - 1
    total = total
    return total


def APb(w, t):  # 이것은 WL w-1 ~ w-2까지의 선미부가부의 APb입니다. t는 선미부가부 간격
    if SFAm(w) == 0:
        result = 0
    else:
        result = t * SxfAm(w) / SFAm(w)
    return result


def lcbAP(w, t, L):  # 이것은 WL w-1 ~ w-2까지의 선미부가부의 lcb입니다. t는 선미부가부 간격, L은 LBP
    if APb(w, t) == 0 or APb(w - 1, t) == 0 or APb(w - 2, t) == 0:
        result = 0
    else:
        result = -(L / 2) + APb(w, t)
    return result


def IxAP(w, t):  # 이것은 WL w-1 의 선미부가부의 Ix입니다. t는 선미부가부 간격
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
    result = IxAP(w, t) + IxFP(w, j) + Ix(w, h)
    return result


def SfyAP(w):  # 이것은 WL w-1의 선미부가부의 ∑f(y)입니다.
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


def SxfyAP(w):  # 이것은 WL w-1의 선미부가부의 ∑x' * f(y)입니다.
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


def APf(w, t):  # 이것은 WL w-1의 선미부가부의 APf입니다. h는 선미부가부 간격
    if SfyAP(w) == 0:
        result = 0
    else:
        result = t * SxfyAP(w) / SfyAP(w)
    return result


def MyAP(w, t, L):  # 이것은 WL w-1의 선미부가부의 A.P.MY입니다. t는 선미부가부 간격,L는 LBP양

    result = AwAP(w, t) * (-L / 2 + APf(w, t))
    return result


def APIAP(w, t):  # 이것은 WL w-1의 선미부가부의 A.P.IA.P.입니다. t는 선미부가부
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


def APIY(w, t, L):  # 이것은 WL w-1의 선미부가부의 A.P.IY입니다. t는 선미부가부
    result = APIAP(w, t) + AwAP(w, t) * L / 2 * L / 2 + AwAP(w, t) * (-L) * APf(w, t)
    return result


def SfyFP(w):  # 이것은 WL w-1의 선수부가부의 ∑f(y)입니다.
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


def SFyHFP(s, w):  # staion 별, WL w-1 ~ w-2선수부가부∑f(yH)입니다. S=24(FP), S=25(FP+J), S=26(FP+2J),J는 선수부 간격

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


def FAmFP(s, w):  # 이것은 선수부 staion별 f(AM)입니다. S=24(FP), S=25(FP+J), S=26(FP+2J),J는 선수부 간격

    if s == 25:
        total = SFyHFP(s, w) * 4 * 3 / 8
    else:
        total = SFyHFP(s, w) * 3 / 8
    total = total
    return total


def SFAmFP(w):  # 이것은 WL w-1 ~ w-2 까지 선수부가부의 ∑f(AM)입니다.
    a = 24
    total = 0
    while a <= 26:
        total += FAmFP(a, w)
        a = a + 1
    total = total
    return total


def VFP(w, j):  # 이것은 WL w-1 ~ w-2 까지 선수부가부의 V입니다. j는 선수부가부 간격
    result = SFAmFP(w) * j * 3 / 8 * 2
    return result


def AwFP(w, j):  # 이것은 WL w-1의 선수부가부의 Aw입니다. j는 선수부가부 간
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


def WFP(w, j):  # 이것은 WL w-1~w-2의 선수부가부의 W입니다. t는 선수부가부 간
    result = VFP(w, j) * 1.025
    return result


def FPb(w, j):  # 이것은 WL w-1~w-2의 선수부가부의 FPb입니다. t는 선수부가부 간
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


def lcbFP(w, j, L):  # 이것은 WL w-1~w-2의 선수부가부의 lcb입니다. t는 선수부가부 간격 L은 LBP
    result = FPb(w, j) + (L / 2)
    return result


def SfVFP(w):  # 이것은 WL w-1~w-2의 선수부가부의∑f(V)
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


def kbFP(w, f):  # 이것은 WL w-1~w-2의 선수부가부의kb값니다. f는 WL간격
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


def IxFP(w, j):  # 이것은 WL w-1의 선수부가부의 lx입니다. j는 선수부가부 간격
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


def FPf(w, j):  # 이것은 WL w-1의 선수부가부의 FPf입니다. j는 선수부가부 간격
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
    if SxfyFP(w) == 0:
        result = 0
    else:
        result = SxfyFP(w) / SfyFP(w) * j
    return result


def FPMy(w, j, L):  # 이것은 WL w-1의 선수부가부의 F.P.MY입니다. t는 선수부가부 간격
    result = AwFP(w, j) * (-L / 2 + FPf(w, j))
    return result


def FPIFP(w, j):  # 이것은 WL w-1의 선수부가부의 F.P.IF.P. 입니다. j는 선수부가부 간격
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
    result = FPIFP(w, j) + AwFP(w, j) * (L / 2) * (L / 2) + AwFP(w, j) * (-L) * FPf(w, j)
    return result


def simy(w):  # 이것은 각 waterline 별 ∑f(y)입니다. w-1이 waterline 숫자이다.

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


def simx(n):  # 이것은 W.L n-1~n-3까지의 ∑f(V)의 값이다.

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


def W(n, h, f):  # 이것은 W.L n-1 ~ n-3 까지의 W이다.
    if n == 2:
        result = simx(n) * h / 3 * f / 3 * 1.025
    else:
        result = simx(n) * h / 3 * f / 3 * 1.025 * 2
    return result


def DIS(s, h, f, t, j):  # bottom ~ W.L s-1의 총 배수량 h = staion 간격, f = WL간격, t = 선미부 간격, j = 선수부간격
    total2 = 0
    n = s
    while n > 1:
        total2 += W(n, h, f) + WAP(n, t) + WFP(n, j)
        n = n - 2
        total2 = total2
    return total2


def W(n, h, f):  # 이것은 W.L n-1 ~ n-3 까지의 W이다.
    if n == 2:
        result = simx(n) * h / 3 * f / 3 * 1.025
    else:
        result = simx(n) * h / 3 * f / 3 * 1.025 * 2
    return result


def SSW(w, j, t):  # 부가부의 w-1~w-3
    result = (VFP(w, j) + VAP(w, t)) * 1.025
    return result


def Kb(t):  # 이것은 W.L t-1 ~ t-3의 KB이다.
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
    result = 0
    a = n
    while a >= 2:
        result += (KbAP(a, t) * VVAP(a, j) * 1.025) + (kbFP(a, f) * VFP(a, j) * 1.025) + Kb(a) * W(a, h, f)
        a = a - 2
        result = result
    return result


def KB(n, h, f, t, j):
    result = SSM(n, h, f, t, j) / DIS(n, h, f, t, j)
    return result


def X(s, g):  # 이것은 staion별, W.L g-1 ~ g-3 별 ∑f(yH)입니다.

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


def SSSM(s, h, f, t, j, L):  # 이것은 WL s-1까지의 LCB를 구하는 것이다. h는 Sation 간격 f는 WL 간격
    result = 0
    n = s
    while n >= 2:
        result += (lcb(n, h) * W(n, h, f) / 1.025) + (lcbFP(n, j, L) * VFP(n, j)) + (lcbAP(n, t, L) * VAP(n, t))
        n = n - 2
    return result


def LCB(s, h, f, t, j, L):
    result = SSSM(s, h, f, t, j, L) / DIS(s, h, f, t, j)
    return result


def Am(a):  # 이것은 WL a-1 ~ a-3 까지의 Am입니다.
    if a == 2:
        result = X(12, a) / 3
    else:
        result = X(12, a) * 2 / 3
    return result


def SAm(q):  # 이것은 W.Lq-1 까지의 Am 입니다.
    total6 = 0
    a = q
    while a >= 2:
        total6 += Am(a)
        a = a - 2
        total6 = total6
    return total6


def Cb(m, h, f, L, B, t, j):  # 이것은 W.L m-1 까지의 Cb입니다. h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
    result = DIS(m, h, f, t, j) / 1.025 / (m - 1) / L / B
    return result


def Cm(m, B):  # 이것은 W.L m-1까지의 Cm을 구하는 것이다.B는 breadth
    result = SAm(m) / (m - 1) / B
    return result


def Cp(m, h, f, L, B, t, j):  # 이것은 WL m-1까지의 Cp이다.
    result = Cb(m, h, f, L, B, t, j) / Cm(m, B)
    return result


def Aw(r, h):  # 이것은 WL r-1별 Aw입니다. h는 staion 간격
    result = simy(r) * 2 / 3 * h
    return result


def Cw(r, h, L, B):  # 이것은 W.L r-1 별 Cw이다.  h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
    result = Aw(r, h) / B / L
    return result


def Cvp(r, h, f, L, B, t, j):  # 이것은 W.L r-1 별 Cvp이다.  h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
    result = Cb(r, h, f, L, B, t, j) / Cw(r, h, L, B)
    return result


def simy3(w):  # 이것은 각 waterline 별 ∑f(y3)입니다. w-1이 waterline 숫자이다.
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


def Ix(w, h):  # 이것은 W.L w-1별 Ix 입니다.
    result = 2 / 3 * h / 3 * simy3(w)
    return result


def BM(w, h, f, t, j):  # 이것은 WL w-1까지의 BM입니다.
    result = (IxAP(w, t) + IxFP(w, j) + Ix(w, h)) / DIS(w, h, f, t, j) * 1.025
    return result


def KM(w, h, f, t, j):  # 이것은 WL w-1까지의 KM의 값이다. h는 staion 간격 f는 WL 간격
    result = BM(w, h, f, t, j) + KB(w, h, f, t, j)
    return result


fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]


def xfy(f):  # 이것은 WL f-1의 ∑x' * f(y)값입니다.
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


def simy1(w):  # 이것은 각 waterline 별 ∑f(y)입니다. w-1이 waterline 숫자이다.
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


def LCF(w, h):  # 이것은 WL w-1별 LCF 값니다. h는 staion 간격
    result = xfy(w) / simy1(w) * h
    return result


def TPC(r, h):  # 이것은 WL r-1까지의 TPC값입니당. h는 station 간격 t는 선미부 간격 j는 선수부간격
    result = Aw(r, h) / 100 * 1.025
    return result


def My(w, h):
    result = Aw(w, h) * LCF(w, h)
    return result


fx = [-10, -9.5, -9, -8.5, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8.5, 9, 9.5, 10]


def x2fy(f):  # 이것은 WL f-1의 ∑x' 2* f(y)값입니다.
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


def Iy(w, h):  # 이것은 WL w-1의 Iy값입니다. h는 station 간격입니다.
    result = 2 / 3 * h * h * h * x2fy(w)
    return result


def SSAw(w, h, t, j):  # 부가부를 포함한 Aw
    result = Aw(w, h) + AwAP(w, t) + AwFP(w, j)
    return result


def SSMy(w, h, t, j, L):  # 부가물 포함 My
    result = My(w, h) + FPMy(w, j, L) + MyAP(w, t, L)
    return result


def SSLCF(w, h, t, j, L):  # 부가물 포함 LCF
    result = SSMy(w, h, t, j, L) / SSAw(w, h, t, j)
    return result


def SSIy(w, h, t, j, L):  # 부가물 포함 Iy
    result = Iy(w, h) + APIY(w, t, L) + FPIy(w, j, L)
    return result


def Il(w, h, t, j, L):
    result = SSIy(w, h, t, j, L) - SSLCF(w, h, t, j, L) * SSAw(w, h, t, j)
    return result


def BML(w, h, f, t, j, L):
    result = Il(w, h, t, j, L)
    return result / (DIS(w, h, f, t, j) / 1.025)


def MTC(w, h, f, t, j, L):
    result = DIS(w, h, f, t, j) * BML(w, h, f, t, j, L) / (100 * L)
    return result


def Wcm(w, h, t, j, L):  # 이것은 WL w-1까지의 "매 Cm 트리밍 정톤수 (Wcm)" 입니다. h는 staion간격  L은 LBP
    result = -1 * (TPC(w, h) * SSLCF(w, h, t, j, L) / L)
    return result


def KML(w, h, f, t, j, L):
    result = BML(w, h, f, t, j, L) + KB(w, h, f, t, j)
    return result


def DISLIST(w, h, f, t, j):  # 이것은 W.L w-1. w-3, w-5, w-7 .......1 까지의 배수량입니다. h는 staion 간격 f는 waterlin 간격.
    a = w
    result = []
    while a >= 2:
        result.append(DIS(a, h, f, t, j))
        a = a - 2
    result.reverse()
    return result


def DISLIST2(w, h, f, t, j):  # 이것은 W.Lw-1. w-3, w-5, w-7 .......1 까지의 배수용적입니다. h는 staion 간격 f는 waterlin 간격.
    a = w
    result = []
    while a >= 2:
        result.append(DIS(a, h, f, t, j) / 1.025)
        a = a - 2
    result.reverse()
    return result


def AwLIST(w, h):  # 이것은 W.Lw-1. w-3, w-5, w-7 .......1 각각의 Aw입니다. h는 staion 간격
    a = w
    result = []
    while a >= 2:
        result.append(Aw(a, h))
        a = a - 2
    result.reverse()
    return result


def AmLIST(w):  # 이것은 W.Lw-1. w-3, w-5, w-7 .......1 까지의 Aw입니다.
    a = w
    result = []
    while a >= 2:
        result.append(SAm(a))
        a = a - 2
    result.reverse()
    return result


def TPCLIST(w, h):  # 이것은 W.Lw-1. w-3, w-5, w-7 .......1 까지의 TPC입니다. h는 staion 간격
    a = w
    result = []
    while a >= 2:
        result.append(TPC(a, h))
        a = a - 2
    result.reverse()
    return result


def MTCLIST(w, h, f, t, j, L):  # 이것은 W.Lw-1. w-3, w-5, w-7 .......1 까지의 MTC입니다. h는 staion 간격
    a = w
    result = []
    while a >= 2:
        result.append(MTC(a, h, f, t, j, L))
        a = a - 2
    result.reverse()
    return result


def WcmLIST(w, h, t, j, L):  ##이것은 WL w-1까지의 "각각의 매 Cm 트리밍 정톤수 (Wcm)" 입니다. h는 staion간격  L은 LBP
    a = w
    result = []
    while a >= 2:
        result.append(Wcm(a, h, t, j, L))
        a = a - 2
    result.reverse()
    return result


def KBLIST(w, h, f, t, j):  ##이것은 WL w-1까지의 각각 KB 입니다. h는 staion간격  f은 WL간격
    a = w
    result = []
    while a >= 2:
        result.append(KB(a, h, f, t, j))
        a = a - 2
    result.reverse()
    return result


def BMLIST(w, h, f, t, j):  ##이것은 WL w-1까지의 각각 BM입니다. h는 staion간격  f은 WL간격
    a = w
    result = []
    while a >= 2:
        result.append(BM(a, h, f, t, j))
        a = a - 2
    result.reverse()
    return result  # 근데 부가물 안더해서 값이 일단은 달라


def KMLIST(w, h, f, t, j):  ##이것은 WL w-1까지의 "각각의  KM입니다. h는 staion간격 f는 WL 간격
    a = w
    result = []
    while a >= 2:
        result.append(KM(a, h, f, t, j))
        a = a - 2
    result.reverse()
    return result


def LCBLIST(w, h, f, t, j, L):  ##이것은 WL w-1까지의 "각각의  LCB입니다. h는 staion간격 f는 WL 간격
    a = w
    result = []
    while a >= 2:
        result.append(LCB(a, h, f, t, j, L))
        a = a - 2
    result.reverse()

    return result  # 부가물 안더해서 값이 일단은 달라!


def LCFLIST(w, h, t, j, L):  ##이것은 WL w-1까지의 "각각의  LCF입니다. h는 staion간격
    a = w
    result = []
    while a >= 2:
        result.append(SSLCF(a, h, t, j, L))
        a = a - 2
    result.reverse()
    return result


def BMLLIST(w, h, f, t, j, L):  # 이것은 W.L m-1 까지의 Cb입니다. h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
    a = w
    result = []
    while a >= 2:
        result.append(BML(a, h, f, t, j, L))
        a = a - 2
    result.reverse()

    return result


def KMLLIST(w, h, f, t, j, L):  # 이것은 W.L m-1 까지의 Cb입니다. h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
    a = w
    result = []
    while a >= 2:
        result.append(KML(a, h, f, t, j, L))
        a = a - 2
    result.reverse()
    return result  # 부가물 안더해서 값이 일단은 달라!


def CbLIST(w, h, f, L, B, t, j):  # 이것은 W.L m-1 까지의 Cb입니다. h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
    a = w
    result = []
    while a >= 2:
        result.append(Cb(a, h, f, L, B, t, j))
        a = a - 2
    result.reverse()

    return result  # 부가물 안더해서 값이 일단은 달라!


def CpLIST(w, h, f, L, B, t, j):  # 이것은 W.L m-1 까지의 Cp입니다. h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
    a = w
    result = []
    while a >= 2:
        result.append(Cp(a, h, f, L, B, t, j))
        a = a - 2
    result.reverse()
    return result


def CwLIST(w, h, L, B):  # 이것은 W.L m-1 까지의 Cw입니다. h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
    a = w
    result = []
    while a >= 2:
        result.append(Cw(a, h, B, L))
        a = a - 2
    result.reverse()
    return result


def CmLIST(w, B):  # 이것은 W.L m-1 까지의 Cm입니다.B는 breadth
    a = w
    result = []
    while a >= 2:
        result.append(Cm(a, B))
        a = a - 2
    result.reverse()
    return result


def CvpLIST(w, h, f, L, B, t, j):  # 이것은 W.L m-1 까지의 Cvp입니다. h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
    a = w
    result = []
    while a >= 2:
        result.append(Cvp(a, h, f, L, B, t, j))
        a = a - 2
    result.reverse()
    return result


def SSIxLIST(w, t, j, h):  # 이것은 W.L m-1 까지의 Cvp입니다. h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
    a = w
    result = []
    while a >= 2:
        result.append(SSIx(a, t, j, h))
        a = a - 2
    result.reverse()
    return result


def IlLIST(w, h, t, j, L):  # 이것은 W.L m-1 까지의 Cvp입니다. h = station 간격 f는 W.L간격 L은 LBP ,B는 breadth
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


def Calculation_sheet(a, L, B):
    w = a + 1
    h = WL(7, -1) - WL(6, -1)
    f = 1
    t = -WL(-1, -1)
    j = WL(25, -1) - WL(24, -1)
    data = WLlist(w, h, f, L, B)

    result = DataFrame(data)

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


def Hydrostatic_curve(a, L, B):
    w = a + 1
    h = WL(7, -1) - WL(6, -1)
    f = 1
    t = -WL(-1, -1)
    j = WL(25, -1) - WL(24, -1)
    data = WLlist(w, h, f, L, B)
    y = range(2, w)
    plt.yticks(range(2, w, 2))
    plt.xticks(range(-5, 150, 5))
    x = [DIS(a + 1, h, f, t, j) / 8000 for a in y]  # 축척 1 = 2000t
    z = [DIS(a + 1, h, f, t, j) / 8000 / 1.025 for a in y]  # 축척 1 = 2000t
    e = [KB(a + 1, h, f, t, j) for a in y]  # 축척 1 = 1m
    g = [Aw(a + 1, h) / 600 for a in y]  # 축척 1 = 200
    p = [TPC(a + 1, h) / 20 for a in y]  # 축척 1 = 2t
    u = [Cm(a + 1, B) / 0.05 for a in y]  # 축척 1 = 0.05
    c = [Cw(a + 1, h, L, B) / 0.05 for a in y]  # 축척 1 = 0.05
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


class CreateToolTip(object):

    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background='yellow', relief='solid', borderwidth=1)
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()


class ARPAGO(object):

    def __init__(self):
        root = tk.Tk()
        root.title("ARPA-GO")
        root.geometry("500x150")

        # row 0
        label1 = tk.Label(root, text="Waterline No. ")
        label1.grid(column=0, row=1)

        self.entry1 = tk.Entry(root, text="")
        self.entry1.grid(column=1, row=1)

        # row 1
        label2 = tk.Label(root, text="Length Between Perpendiculars ")
        label2.grid(column=0, row=2)

        self.entry2 = tk.Entry(root, text="")
        self.entry2.grid(column=1, row=2)

        label3 = tk.Label(root, text="Breadth ")
        label3.grid(column=0, row=3)

        self.entry3 = tk.Entry(root, text="")
        self.entry3.grid(column=1, row=3)

        # row 2

        button2 = tk.Button(root, text="Hydrostatic Curve", command=self.get_new_window2)
        button2.grid(column=1, row=5)
        frm = ttk.Frame(root)
        frm.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        frm.columnconfigure(0, weight=1)
        frm.rowconfigure(0, weight=1)

        self.filename_var = tkinter.StringVar()

        open_button = ttk.Button(frm, text="Input File", command=self.select_file)
        open_button.grid(column=1, row=1, sticky=tkinter.W)
        open_button['command'] = self.select_file

        display_box = ttk.Label(frm, textvariable=self.filename_var, width=30)
        display_box.grid(column=2, row=1, sticky=((tkinter.W, tkinter.E)))
        button4 = tk.Button(root, text="Calculation Sheet", command=self.get_new_window4)
        button4.grid(column=0, row=5)
        root.mainloop()

    def get_new_window2(self):
        a = int(self.entry1.get())
        L = float(self.entry2.get())
        B = float(self.entry3.get())
        fig = Figure()
        Hydrostatic_curve(a, L, B)

    def select_file(self):
        global dataoffset
        filename = filedialog.askopenfilename(
            filetypes=[('Excel Spreadsheet', '*.xlsx'), ('Excel Spreadsheet', '*.xls'), ('All files', '*.*')])
        self.filename_var.set(filename)
        dataoffset = pd.read_excel(filename)
        print(dataoffset)

    def get_new_window4(self):
        root = tk.Tk()
        root.title('Export Calculation Sheet')

        frm = ttk.Frame(root)
        frm.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        frm.columnconfigure(0, weight=1)
        frm.rowconfigure(0, weight=1)

        self.filename_var = tkinter.StringVar()
        self.filename_var.set("<select an export file>")

        open_button = ttk.Button(frm, text="Export Sheet", command=self.load_file)
        open_button_ttp = CreateToolTip(open_button, "Click this button to save calculation sheet in Excel form")
        open_button.grid(column=1, row=1, sticky=tkinter.W)
        open_button['command'] = self.load_file

        display_box = ttk.Label(frm, textvariable=self.filename_var, width=30)
        display_box.grid(column=1, row=2, sticky=((tkinter.W, tkinter.E)))

        root.mainloop()

    def load_file(self):
        a = int(self.entry1.get())
        L = float(self.entry2.get())
        B = float(self.entry3.get())
        file = Calculation_sheet(a, L, B)

        savefile = filedialog.asksaveasfilename(filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
        file.to_excel(savefile + ".xlsx", index=False, sheet_name="Results")


if __name__ == "__main__":
    ARPAGO()