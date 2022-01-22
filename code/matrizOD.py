from gurobipy import *
import csv
import sys
sys.setrecursionlimit(3000000)

model = Model('sentidoD')


C4=model.addVar(vtype="I", name="C4")
model.addConstr(C4 <= 377, "c28")

D4=model.addVar(vtype="I", name="D4")
model.addConstr(D4 <= 377, "c29")

E4=model.addVar(vtype="I", name="E4")
model.addConstr(E4 <= 377, "c30")

F4=model.addVar(vtype="I", name="F4")
model.addConstr(F4 <= 377, "c31")

G4=model.addVar(vtype="I", name="G4")
model.addConstr(G4 <= 377, "c32")

H4=model.addVar(vtype="I", name="H4")
model.addConstr(H4 <= 377, "c33")

I4=model.addVar(vtype="I", name="I4")
model.addConstr(I4 <= 377, "c34")

J4=model.addVar(vtype="I", name="J4")
model.addConstr(J4 <= 377, "c35")

K4=model.addVar(vtype="I", name="K4")
model.addConstr(K4 <= 377, "c36")

L4=model.addVar(vtype="I", name="L4")
model.addConstr(L4 <= 377, "c37")

M4=model.addVar(vtype="I", name="M4")
model.addConstr(M4 <= 377, "c38")

N4=model.addVar(vtype="I", name="N4")
model.addConstr(N4 <= 377, "c39")

O4=model.addVar(vtype="I", name="O4")
model.addConstr(O4 <= 377, "c40")

P4=model.addVar(vtype="I", name="P4")
model.addConstr(P4 <= 377, "c")

Q4=model.addVar(vtype="I", name="Q4")
model.addConstr(Q4 <= 377, "c")

R4=model.addVar(vtype="I", name="R4")
model.addConstr(R4 <= 377, "c")

S4=model.addVar(vtype="I", name="S4")
model.addConstr(S4 <= 377, "c")

T4=model.addVar(vtype="I", name="T4")
model.addConstr(T4 <= 377, "c")

U4=model.addVar(vtype="I", name="U4")
model.addConstr(U4 <= 377, "c")

V4=model.addVar(vtype="I", name="V4")
model.addConstr(V4 <= 377, "c")

W4=model.addVar(vtype="I", name="W4")
model.addConstr(W4 <= 377, "c")

X4=model.addVar(vtype="I", name="X4")
model.addConstr(X4 <= 377, "c")

C5=model.addVar(vtype="I", name="C5")
model.addConstr(C5 <= 377, "c")

D5=model.addVar(vtype="I", name="D5")
model.addConstr(D5 <= 377, "c")

E5=model.addVar(vtype="I", name="E5")
model.addConstr(E5 <= 377, "c")

F5=model.addVar(vtype="I", name="F5")
model.addConstr(F5 <= 377, "c")

G5=model.addVar(vtype="I", name="G5")
model.addConstr(G5 <= 377, "c")

H5=model.addVar(vtype="I", name="H5")
model.addConstr(H5 <= 377, "c")

I5=model.addVar(vtype="I", name="I5")
model.addConstr(I5 <= 377, "c")

J5=model.addVar(vtype="I", name="J5")
model.addConstr(J5 <= 377, "c")

K5=model.addVar(vtype="I", name="K5")
model.addConstr(K5 <= 377, "c")

L5=model.addVar(vtype="I", name="L5")
model.addConstr(L5 <= 377, "c")

M5=model.addVar(vtype="I", name="M5")
model.addConstr(M5 <= 377, "c")

N5=model.addVar(vtype="I", name="N5")
model.addConstr(N5 <= 377, "c")

O5=model.addVar(vtype="I", name="O5")
model.addConstr(O5 <= 377, "c")

P5=model.addVar(vtype="I", name="P5")
model.addConstr(P5 <= 377, "c")

Q5=model.addVar(vtype="I", name="Q5")
model.addConstr(Q5 <= 377, "c")

R5=model.addVar(vtype="I", name="R5")
model.addConstr(R5 <= 377, "c")

S5=model.addVar(vtype="I", name="S5")
model.addConstr(S5 <= 377, "c")

T5=model.addVar(vtype="I", name="T5")
model.addConstr(T5 <= 377, "c")

U5=model.addVar(vtype="I", name="U5")
model.addConstr(U5 <= 377, "c")

V5=model.addVar(vtype="I", name="V5")
model.addConstr(V5 <= 377, "c")

W5=model.addVar(vtype="I", name="W5")
model.addConstr(W5 <= 377, "c")

X5=model.addVar(vtype="I", name="X5")
model.addConstr(X5 <= 377, "c")

C6=model.addVar(vtype="I", name="C6")
model.addConstr(C6 <= 377, "c")

D6=model.addVar(vtype="I", name="D6")
model.addConstr(D6 <= 377, "c")

E6=model.addVar(vtype="I", name="E6")
model.addConstr(E6 <= 377, "c")

F6=model.addVar(vtype="I", name="F6")
model.addConstr(F6 <= 377, "c")

G6=model.addVar(vtype="I", name="G6")
model.addConstr(G6 <= 377, "c")

H6=model.addVar(vtype="I", name="H6")
model.addConstr(H6 <= 377, "c")

I6=model.addVar(vtype="I", name="I6")
model.addConstr(I6 <= 377, "c")

J6=model.addVar(vtype="I", name="J6")
model.addConstr(J6 <= 377, "c")

K6=model.addVar(vtype="I", name="K6")
model.addConstr(K6 <= 377, "c")

L6=model.addVar(vtype="I", name="L6")
model.addConstr(L6 <= 377, "c")

M6=model.addVar(vtype="I", name="M6")
model.addConstr(M6 <= 377, "c")

N6=model.addVar(vtype="I", name="N6")
model.addConstr(N6 <= 377, "c")

O6=model.addVar(vtype="I", name="O6")
model.addConstr(O6 <= 377, "c")

P6=model.addVar(vtype="I", name="P6")
model.addConstr(P6 <= 377, "c")

Q6=model.addVar(vtype="I", name="Q6")
model.addConstr(Q6 <= 377, "c")

R6=model.addVar(vtype="I", name="R6")
model.addConstr(R6 <= 377, "c")

S6=model.addVar(vtype="I", name="S6")
model.addConstr(S6 <= 377, "c")

T6=model.addVar(vtype="I", name="T6")
model.addConstr(T6 <= 377, "c")

U6=model.addVar(vtype="I", name="U6")
model.addConstr(U6 <= 377, "c")

V6=model.addVar(vtype="I", name="V6")
model.addConstr(V6 <= 377, "c")

W6=model.addVar(vtype="I", name="W6")
model.addConstr(W6 <= 377, "c")

X6=model.addVar(vtype="I", name="X6")
model.addConstr(X6 <= 377, "c")

C7=model.addVar(vtype="I", name="C7")
model.addConstr(C7 <= 377, "c")

D7=model.addVar(vtype="I", name="D7")
model.addConstr(D7 <= 377, "c")

E7=model.addVar(vtype="I", name="E7")
model.addConstr(E7 <= 377, "c")

F7=model.addVar(vtype="I", name="F7")
model.addConstr(F7 <= 377, "c")

G7=model.addVar(vtype="I", name="G7")
model.addConstr(G7 <= 377, "c")

H7=model.addVar(vtype="I", name="H7")
model.addConstr(H7 <= 377, "c")

I7=model.addVar(vtype="I", name="I7")
model.addConstr(I7 <= 377, "c")

J7=model.addVar(vtype="I", name="J7")
model.addConstr(J7 <= 377, "c")

K7=model.addVar(vtype="I", name="K7")
model.addConstr(K7 <= 377, "c")

L7=model.addVar(vtype="I", name="L7")
model.addConstr(L7 <= 377, "c")

M7=model.addVar(vtype="I", name="M7")
model.addConstr(M7 <= 377, "c")

N7=model.addVar(vtype="I", name="N7")
model.addConstr(N7 <= 377, "c")

O7=model.addVar(vtype="I", name="O7")
model.addConstr(O7 <= 377, "c")

P7=model.addVar(vtype="I", name="P7")
model.addConstr(P7 <= 377, "c")

Q7=model.addVar(vtype="I", name="Q7")
model.addConstr(Q7 <= 377, "c")

R7=model.addVar(vtype="I", name="R7")
model.addConstr(R7 <= 377, "c")

S7=model.addVar(vtype="I", name="S7")
model.addConstr(S7 <= 377, "c")

T7=model.addVar(vtype="I", name="T7")
model.addConstr(T7 <= 377, "c")

U7=model.addVar(vtype="I", name="U7")
model.addConstr(U7 <= 377, "c")

V7=model.addVar(vtype="I", name="V7")
model.addConstr(V7 <= 377, "c")

W7=model.addVar(vtype="I", name="W7")
model.addConstr(W7 <= 377, "c")

X7=model.addVar(vtype="I", name="X7")
model.addConstr(X7 <= 377, "c")

C8=model.addVar(vtype="I", name="C8")
model.addConstr(C8 <= 377, "c")

D8=model.addVar(vtype="I", name="D8")
model.addConstr(D8 <= 377, "c")

E8=model.addVar(vtype="I", name="E8")
model.addConstr(E8 <= 377, "c")

F8=model.addVar(vtype="I", name="F8")
model.addConstr(F8 <= 377, "c")

G8=model.addVar(vtype="I", name="G8")
model.addConstr(G8 <= 377, "c")

H8=model.addVar(vtype="I", name="H8")
model.addConstr(H8 <= 377, "c")

I8=model.addVar(vtype="I", name="I8")
model.addConstr(I8 <= 377, "c")

J8=model.addVar(vtype="I", name="J8")
model.addConstr(J8 <= 377, "c")

K8=model.addVar(vtype="I", name="K8")
model.addConstr(K8 <= 377, "c")

L8=model.addVar(vtype="I", name="L8")
model.addConstr(L8 <= 377, "c")

M8=model.addVar(vtype="I", name="M8")
model.addConstr(M8 <= 377, "c")

N8=model.addVar(vtype="I", name="N8")
model.addConstr(N8 <= 377, "c")

O8=model.addVar(vtype="I", name="O8")
model.addConstr(O8 <= 377, "c")

P8=model.addVar(vtype="I", name="P8")
model.addConstr(P8 <= 377, "c")

Q8=model.addVar(vtype="I", name="Q8")
model.addConstr(Q8 <= 377, "c")

R8=model.addVar(vtype="I", name="R8")
model.addConstr(R8 <= 377, "c")

S8=model.addVar(vtype="I", name="S8")
model.addConstr(S8 <= 377, "c")

T8=model.addVar(vtype="I", name="T8")
model.addConstr(T8 <= 377, "c")

U8=model.addVar(vtype="I", name="U8")
model.addConstr(U8 <= 377, "c")

V8=model.addVar(vtype="I", name="V8")
model.addConstr(V8 <= 377, "c")

W8=model.addVar(vtype="I", name="W8")
model.addConstr(W8 <= 377, "c")

X8=model.addVar(vtype="I", name="X8")
model.addConstr(X8 <= 377, "c")

C9=model.addVar(vtype="I", name="C9")
model.addConstr(C9 <= 377, "c")

D9=model.addVar(vtype="I", name="D9")
model.addConstr(D9 <= 377, "c")

E9=model.addVar(vtype="I", name="E9")
model.addConstr(E9 <= 377, "c")

F9=model.addVar(vtype="I", name="F9")
model.addConstr(F9 <= 377, "c")

G9=model.addVar(vtype="I", name="G9")
model.addConstr(G9 <= 377, "c")

H9=model.addVar(vtype="I", name="H9")
model.addConstr(H9 <= 377, "c")

I9=model.addVar(vtype="I", name="I9")
model.addConstr(I9 <= 377, "c")

J9=model.addVar(vtype="I", name="J9")
model.addConstr(J9 <= 377, "c")

K9=model.addVar(vtype="I", name="K9")
model.addConstr(K9 <= 377, "c")

L9=model.addVar(vtype="I", name="L9")
model.addConstr(L9 <= 377, "c")

M9=model.addVar(vtype="I", name="M9")
model.addConstr(M9 <= 377, "c")

N9=model.addVar(vtype="I", name="N9")
model.addConstr(N9 <= 377, "c")

O9=model.addVar(vtype="I", name="O9")
model.addConstr(O9 <= 377, "c")

P9=model.addVar(vtype="I", name="P9")
model.addConstr(P9 <= 377, "c")

Q9=model.addVar(vtype="I", name="Q9")
model.addConstr(Q9 <= 377, "c")

R9=model.addVar(vtype="I", name="R9")
model.addConstr(R9 <= 377, "c")

S9=model.addVar(vtype="I", name="S9")
model.addConstr(S9 <= 377, "c")

T9=model.addVar(vtype="I", name="T9")
model.addConstr(T9 <= 377, "c")

U9=model.addVar(vtype="I", name="U9")
model.addConstr(U9 <= 377, "c")

V9=model.addVar(vtype="I", name="V9")
model.addConstr(V9 <= 377, "c")

W9=model.addVar(vtype="I", name="W9")
model.addConstr(W9 <= 377, "c")

X9=model.addVar(vtype="I", name="X9")
model.addConstr(X9 <= 377, "c")

C10=model.addVar(vtype="I", name="C10")
model.addConstr(C10 <= 377, "c")

D10=model.addVar(vtype="I", name="D10")
model.addConstr(D10 <= 377, "c")

E10=model.addVar(vtype="I", name="E10")
model.addConstr(E10 <= 377, "c")

F10=model.addVar(vtype="I", name="F10")
model.addConstr(F10 <= 377, "c")

G10=model.addVar(vtype="I", name="G10")
model.addConstr(G10 <= 377, "c")

H10=model.addVar(vtype="I", name="H10")
model.addConstr(H10 <= 377, "c")

I10=model.addVar(vtype="I", name="I10")
model.addConstr(I10 <= 377, "c")

J10=model.addVar(vtype="I", name="J10")
model.addConstr(J10 <= 377, "c")

K10=model.addVar(vtype="I", name="K10")
model.addConstr(K10 <= 377, "c")

L10=model.addVar(vtype="I", name="L10")
model.addConstr(L10 <= 377, "c")

M10=model.addVar(vtype="I", name="M10")
model.addConstr(M10 <= 377, "c")

N10=model.addVar(vtype="I", name="N10")
model.addConstr(N10 <= 377, "c")

O10=model.addVar(vtype="I", name="O10")
model.addConstr(O10 <= 377, "c")

P10=model.addVar(vtype="I", name="P10")
model.addConstr(P10 <= 377, "c")

Q10=model.addVar(vtype="I", name="Q10")
model.addConstr(Q10 <= 377, "c")

R10=model.addVar(vtype="I", name="R10")
model.addConstr(R10 <= 377, "c")

S10=model.addVar(vtype="I", name="S10")
model.addConstr(S10 <= 377, "c")

T10=model.addVar(vtype="I", name="T10")
model.addConstr(T10 <= 377, "c")

U10=model.addVar(vtype="I", name="U10")
model.addConstr(U10 <= 377, "c")

V10=model.addVar(vtype="I", name="V10")
model.addConstr(V10 <= 377, "c")

W10=model.addVar(vtype="I", name="W10")
model.addConstr(W10 <= 377, "c")

X10=model.addVar(vtype="I", name="X10")
model.addConstr(X10 <= 377, "c")

C11=model.addVar(vtype="I", name="C11")
model.addConstr(C11 <= 377, "c")

D11=model.addVar(vtype="I", name="D11")
model.addConstr(D11 <= 377, "c")

E11=model.addVar(vtype="I", name="E11")
model.addConstr(E11 <= 377, "c")

F11=model.addVar(vtype="I", name="F11")
model.addConstr(F11 <= 377, "c")

G11=model.addVar(vtype="I", name="G11")
model.addConstr(G11 <= 377, "c")

H11=model.addVar(vtype="I", name="H11")
model.addConstr(H11 <= 377, "c")

I11=model.addVar(vtype="I", name="I11")
model.addConstr(I11 <= 377, "c")

J11=model.addVar(vtype="I", name="J11")
model.addConstr(J11 <= 377, "c")

K11=model.addVar(vtype="I", name="K11")
model.addConstr(K11 <= 377, "c")

L11=model.addVar(vtype="I", name="L11")
model.addConstr(L11 <= 377, "c")

M11=model.addVar(vtype="I", name="M11")
model.addConstr(M11 <= 377, "c")

N11=model.addVar(vtype="I", name="N11")
model.addConstr(N11 <= 377, "c")

O11=model.addVar(vtype="I", name="O11")
model.addConstr(O11 <= 377, "c")

P11=model.addVar(vtype="I", name="P11")
model.addConstr(P11 <= 377, "c")

Q11=model.addVar(vtype="I", name="Q11")
model.addConstr(Q11 <= 377, "c")

R11=model.addVar(vtype="I", name="R11")
model.addConstr(R11 <= 377, "c")

S11=model.addVar(vtype="I", name="S11")
model.addConstr(S11 <= 377, "c")

T11=model.addVar(vtype="I", name="T11")
model.addConstr(T11 <= 377, "c")

U11=model.addVar(vtype="I", name="U11")
model.addConstr(U11 <= 377, "c")

V11=model.addVar(vtype="I", name="V11")
model.addConstr(V11 <= 377, "c")

W11=model.addVar(vtype="I", name="W11")
model.addConstr(W11 <= 377, "c")

X11=model.addVar(vtype="I", name="X11")
model.addConstr(X11 <= 377, "c")

C12=model.addVar(vtype="I", name="C12")
model.addConstr(C12 <= 377, "c")

D12=model.addVar(vtype="I", name="D12")
model.addConstr(D12 <= 377, "c")

E12=model.addVar(vtype="I", name="E12")
model.addConstr(E12 <= 377, "c")

F12=model.addVar(vtype="I", name="F12")
model.addConstr(F12 <= 377, "c")

G12=model.addVar(vtype="I", name="G12")
model.addConstr(G12 <= 377, "c")

H12=model.addVar(vtype="I", name="H12")
model.addConstr(H12 <= 377, "c")

I12=model.addVar(vtype="I", name="I12")
model.addConstr(I12 <= 377, "c")

J12=model.addVar(vtype="I", name="J12")
model.addConstr(J12 <= 377, "c")

K12=model.addVar(vtype="I", name="K12")
model.addConstr(K12 <= 377, "c")

L12=model.addVar(vtype="I", name="L12")
model.addConstr(L12 <= 377, "c")

M12=model.addVar(vtype="I", name="M12")
model.addConstr(M12 <= 377, "c")

N12=model.addVar(vtype="I", name="N12")
model.addConstr(N12 <= 377, "c")

O12=model.addVar(vtype="I", name="O12")
model.addConstr(O12 <= 377, "c")

P12=model.addVar(vtype="I", name="P12")
model.addConstr(P12 <= 377, "c")

Q12=model.addVar(vtype="I", name="Q12")
model.addConstr(Q12 <= 377, "c")

R12=model.addVar(vtype="I", name="R12")
model.addConstr(R12 <= 377, "c")

S12=model.addVar(vtype="I", name="S12")
model.addConstr(S12 <= 377, "c")

T12=model.addVar(vtype="I", name="T12")
model.addConstr(T12 <= 377, "c")

U12=model.addVar(vtype="I", name="U12")
model.addConstr(U12 <= 377, "c")

V12=model.addVar(vtype="I", name="V12")
model.addConstr(V12 <= 377, "c")

W12=model.addVar(vtype="I", name="W12")
model.addConstr(W12 <= 377, "c")

X12=model.addVar(vtype="I", name="X12")
model.addConstr(X12 <= 377, "c")

C13=model.addVar(vtype="I", name="C13")
model.addConstr(C13 <= 377, "c")

D13=model.addVar(vtype="I", name="D13")
model.addConstr(D13 <= 377, "c")

E13=model.addVar(vtype="I", name="E13")
model.addConstr(E13 <= 377, "c")

F13=model.addVar(vtype="I", name="F13")
model.addConstr(F13 <= 377, "c")

G13=model.addVar(vtype="I", name="G13")
model.addConstr(G13 <= 377, "c")

H13=model.addVar(vtype="I", name="H13")
model.addConstr(H13 <= 377, "c")

I13=model.addVar(vtype="I", name="I13")
model.addConstr(I13 <= 377, "c")

J13=model.addVar(vtype="I", name="J13")
model.addConstr(J13 <= 377, "c")

K13=model.addVar(vtype="I", name="K13")
model.addConstr(K13 <= 377, "c")

L13=model.addVar(vtype="I", name="L13")
model.addConstr(L13 <= 377, "c")

M13=model.addVar(vtype="I", name="M13")
model.addConstr(M13 <= 377, "c")

N13=model.addVar(vtype="I", name="N13")
model.addConstr(N13 <= 377, "c")

O13=model.addVar(vtype="I", name="O13")
model.addConstr(O13 <= 377, "c")

P13=model.addVar(vtype="I", name="P13")
model.addConstr(P13 <= 377, "c")

Q13=model.addVar(vtype="I", name="Q13")
model.addConstr(Q13 <= 377, "c")

R13=model.addVar(vtype="I", name="R13")
model.addConstr(R13 <= 377, "c")

S13=model.addVar(vtype="I", name="S13")
model.addConstr(S13 <= 377, "c")

T13=model.addVar(vtype="I", name="T13")
model.addConstr(T13 <= 377, "c")

U13=model.addVar(vtype="I", name="U13")
model.addConstr(U13 <= 377, "c")

V13=model.addVar(vtype="I", name="V13")
model.addConstr(V13 <= 377, "c")

W13=model.addVar(vtype="I", name="W13")
model.addConstr(W13 <= 377, "c")

X13=model.addVar(vtype="I", name="X13")
model.addConstr(X13 <= 377, "c")


C14=model.addVar(vtype="I", name="C14")
model.addConstr(C14 <= 377, "c")

D14=model.addVar(vtype="I", name="D14")
model.addConstr(D14 <= 377, "c")

E14=model.addVar(vtype="I", name="E14")
model.addConstr(E14 <= 377, "c")

F14=model.addVar(vtype="I", name="F14")
model.addConstr(F14 <= 377, "c")

G14=model.addVar(vtype="I", name="G14")
model.addConstr(G14 <= 377, "c")

H14=model.addVar(vtype="I", name="H14")
model.addConstr(H14 <= 377, "c")

I14=model.addVar(vtype="I", name="I14")
model.addConstr(I14 <= 377, "c")

J14=model.addVar(vtype="I", name="J14")
model.addConstr(J14 <= 377, "c")

K14=model.addVar(vtype="I", name="K14")
model.addConstr(K14 <= 377, "c")

L14=model.addVar(vtype="I", name="L14")
model.addConstr(L14 <= 377, "c")

M14=model.addVar(vtype="I", name="M14")
model.addConstr(M14 <= 377, "c")

N14=model.addVar(vtype="I", name="N14")
model.addConstr(N14 <= 377, "c")

O14=model.addVar(vtype="I", name="O14")
model.addConstr(O14 <= 377, "c")

P14=model.addVar(vtype="I", name="P14")
model.addConstr(P14 <= 377, "c")

Q14=model.addVar(vtype="I", name="Q14")
model.addConstr(Q14 <= 377, "c")

R14=model.addVar(vtype="I", name="R14")
model.addConstr(R14 <= 377, "c")

S14=model.addVar(vtype="I", name="S14")
model.addConstr(S14 <= 377, "c")

T14=model.addVar(vtype="I", name="T14")
model.addConstr(T14 <= 377, "c")

U14=model.addVar(vtype="I", name="U14")
model.addConstr(U14 <= 377, "c")

V14=model.addVar(vtype="I", name="V14")
model.addConstr(V14 <= 377, "c")

W14=model.addVar(vtype="I", name="W14")
model.addConstr(W14 <= 377, "c")

X14=model.addVar(vtype="I", name="X14")
model.addConstr(X14 <= 377, "c")


C15=model.addVar(vtype="I", name="C15")
model.addConstr(C15 <= 377, "c")

D15=model.addVar(vtype="I", name="D15")
model.addConstr(D15 <= 377, "c")

E15=model.addVar(vtype="I", name="E15")
model.addConstr(E15 <= 377, "c")

F15=model.addVar(vtype="I", name="F15")
model.addConstr(F15 <= 377, "c")

G15=model.addVar(vtype="I", name="G15")
model.addConstr(G15 <= 377, "c")

H15=model.addVar(vtype="I", name="H15")
model.addConstr(H15 <= 377, "c")

I15=model.addVar(vtype="I", name="I15")
model.addConstr(I15 <= 377, "c")

J15=model.addVar(vtype="I", name="J15")
model.addConstr(J15 <= 377, "c")

K15=model.addVar(vtype="I", name="K15")
model.addConstr(K15 <= 377, "c")

L15=model.addVar(vtype="I", name="L15")
model.addConstr(L15 <= 377, "c")

M15=model.addVar(vtype="I", name="M15")
model.addConstr(M15 <= 377, "c")

N15=model.addVar(vtype="I", name="N15")
model.addConstr(N15 <= 377, "c")

O15=model.addVar(vtype="I", name="O15")
model.addConstr(O15 <= 377, "c")

P15=model.addVar(vtype="I", name="P15")
model.addConstr(P15 <= 377, "c")

Q15=model.addVar(vtype="I", name="Q15")
model.addConstr(Q15 <= 377, "c")

R15=model.addVar(vtype="I", name="R15")
model.addConstr(R15 <= 377, "c")

S15=model.addVar(vtype="I", name="S15")
model.addConstr(S15 <= 377, "c")

T15=model.addVar(vtype="I", name="T15")
model.addConstr(T15 <= 377, "c")

U15=model.addVar(vtype="I", name="U15")
model.addConstr(U15 <= 377, "c")

V15=model.addVar(vtype="I", name="V15")
model.addConstr(V15 <= 377, "c")

W15=model.addVar(vtype="I", name="W15")
model.addConstr(W15 <= 377, "c")

X15=model.addVar(vtype="I", name="X15")
model.addConstr(X15 <= 377, "c")


C16=model.addVar(vtype="I", name="C16")
model.addConstr(C16 <= 377, "c")

D16=model.addVar(vtype="I", name="D16")
model.addConstr(D16 <= 377, "c")

E16=model.addVar(vtype="I", name="E16")
model.addConstr(E16 <= 377, "c")

F16=model.addVar(vtype="I", name="F16")
model.addConstr(F16 <= 377, "c")

G16=model.addVar(vtype="I", name="G16")
model.addConstr(G16 <= 377, "c")

H16=model.addVar(vtype="I", name="H16")
model.addConstr(H16 <= 377, "c")

I16=model.addVar(vtype="I", name="I16")
model.addConstr(I16 <= 377, "c")

J16=model.addVar(vtype="I", name="J16")
model.addConstr(J16 <= 377, "c")

K16=model.addVar(vtype="I", name="K16")
model.addConstr(K16 <= 377, "c")

L16=model.addVar(vtype="I", name="L16")
model.addConstr(L16 <= 377, "c")

M16=model.addVar(vtype="I", name="M16")
model.addConstr(M16 <= 377, "c")

N16=model.addVar(vtype="I", name="N16")
model.addConstr(N16 <= 377, "c")

O16=model.addVar(vtype="I", name="O16")
model.addConstr(O16 <= 377, "c")

P16=model.addVar(vtype="I", name="P16")
model.addConstr(P16 <= 377, "c")

Q16=model.addVar(vtype="I", name="Q16")
model.addConstr(Q16 <= 377, "c")

R16=model.addVar(vtype="I", name="R16")
model.addConstr(R16 <= 377, "c")

S16=model.addVar(vtype="I", name="S16")
model.addConstr(S16 <= 377, "c")

T16=model.addVar(vtype="I", name="T16")
model.addConstr(T16 <= 377, "c")

U16=model.addVar(vtype="I", name="U16")
model.addConstr(U16 <= 377, "c")

V16=model.addVar(vtype="I", name="V16")
model.addConstr(V16 <= 377, "c")

W16=model.addVar(vtype="I", name="W16")
model.addConstr(W16 <= 377, "c")

X16=model.addVar(vtype="I", name="X16")
model.addConstr(X16 <= 377, "c")


C17=model.addVar(vtype="I", name="C17")
model.addConstr(C17 <= 377, "c")

D17=model.addVar(vtype="I", name="D17")
model.addConstr(D17 <= 377, "c")

E17=model.addVar(vtype="I", name="E17")
model.addConstr(E17 <= 377, "c")

F17=model.addVar(vtype="I", name="F17")
model.addConstr(F17 <= 377, "c")

G17=model.addVar(vtype="I", name="G17")
model.addConstr(G17 <= 377, "c")

H17=model.addVar(vtype="I", name="H17")
model.addConstr(H17 <= 377, "c")

I17=model.addVar(vtype="I", name="I17")
model.addConstr(I17 <= 377, "c")

J17=model.addVar(vtype="I", name="J17")
model.addConstr(J17 <= 377, "c")

K17=model.addVar(vtype="I", name="K17")
model.addConstr(K17 <= 377, "c")

L17=model.addVar(vtype="I", name="L17")
model.addConstr(L17 <= 377, "c")

M17=model.addVar(vtype="I", name="M17")
model.addConstr(M17 <= 377, "c")

N17=model.addVar(vtype="I", name="N17")
model.addConstr(N17 <= 377, "c")

O17=model.addVar(vtype="I", name="O17")
model.addConstr(O17 <= 377, "c")

P17=model.addVar(vtype="I", name="P17")
model.addConstr(P17 <= 377, "c")

Q17=model.addVar(vtype="I", name="Q17")
model.addConstr(Q17 <= 377, "c")

R17=model.addVar(vtype="I", name="R17")
model.addConstr(R17 <= 377, "c")

S17=model.addVar(vtype="I", name="S17")
model.addConstr(S17 <= 377, "c")

T17=model.addVar(vtype="I", name="T17")
model.addConstr(T17 <= 377, "c")

U17=model.addVar(vtype="I", name="U17")
model.addConstr(U17 <= 377, "c")

V17=model.addVar(vtype="I", name="V17")
model.addConstr(V17 <= 377, "c")

W17=model.addVar(vtype="I", name="W17")
model.addConstr(W17 <= 377, "c")

X17=model.addVar(vtype="I", name="X17")
model.addConstr(X17 <= 377, "c")


C18=model.addVar(vtype="I", name="C18")
model.addConstr(C18 <= 377, "c")

D18=model.addVar(vtype="I", name="D18")
model.addConstr(D18 <= 377, "c")

E18=model.addVar(vtype="I", name="E18")
model.addConstr(E18 <= 377, "c")

F18=model.addVar(vtype="I", name="F18")
model.addConstr(F18 <= 377, "c")

G18=model.addVar(vtype="I", name="G18")
model.addConstr(G18 <= 377, "c")

H18=model.addVar(vtype="I", name="H18")
model.addConstr(H18 <= 377, "c")

I18=model.addVar(vtype="I", name="I18")
model.addConstr(I18 <= 377, "c")

J18=model.addVar(vtype="I", name="J18")
model.addConstr(J18 <= 377, "c")

K18=model.addVar(vtype="I", name="K18")
model.addConstr(K18 <= 377, "c")

L18=model.addVar(vtype="I", name="L18")
model.addConstr(L18 <= 377, "c")

M18=model.addVar(vtype="I", name="M18")
model.addConstr(M18 <= 377, "c")

N18=model.addVar(vtype="I", name="N18")
model.addConstr(N18 <= 377, "c")

O18=model.addVar(vtype="I", name="O18")
model.addConstr(O18 <= 377, "c")

P18=model.addVar(vtype="I", name="P18")
model.addConstr(P18 <= 377, "c")

Q18=model.addVar(vtype="I", name="Q18")
model.addConstr(Q18 <= 377, "c")

R18=model.addVar(vtype="I", name="R18")
model.addConstr(R18 <= 377, "c")

S18=model.addVar(vtype="I", name="S18")
model.addConstr(S18 <= 377, "c")

T18=model.addVar(vtype="I", name="T18")
model.addConstr(T18 <= 377, "c")

U18=model.addVar(vtype="I", name="U18")
model.addConstr(U18 <= 377, "c")

V18=model.addVar(vtype="I", name="V18")
model.addConstr(V18 <= 377, "c")

W18=model.addVar(vtype="I", name="W18")
model.addConstr(W18 <= 377, "c")

X18=model.addVar(vtype="I", name="X18")
model.addConstr(X18 <= 377, "c")


C19=model.addVar(vtype="I", name="C19")
model.addConstr(C19 <= 377, "c")

D19=model.addVar(vtype="I", name="D19")
model.addConstr(D19 <= 377, "c")

E19=model.addVar(vtype="I", name="E19")
model.addConstr(E19 <= 377, "c")

F19=model.addVar(vtype="I", name="F19")
model.addConstr(F19 <= 377, "c")

G19=model.addVar(vtype="I", name="G19")
model.addConstr(G19 <= 377, "c")

H19=model.addVar(vtype="I", name="H19")
model.addConstr(H19 <= 377, "c")

I19=model.addVar(vtype="I", name="I19")
model.addConstr(I19 <= 377, "c")

J19=model.addVar(vtype="I", name="J19")
model.addConstr(J19 <= 377, "c")

K19=model.addVar(vtype="I", name="K19")
model.addConstr(K19 <= 377, "c")

L19=model.addVar(vtype="I", name="L19")
model.addConstr(L19 <= 377, "c")

M19=model.addVar(vtype="I", name="M19")
model.addConstr(M19 <= 377, "c")

N19=model.addVar(vtype="I", name="N19")
model.addConstr(N19 <= 377, "c")

O19=model.addVar(vtype="I", name="O19")
model.addConstr(O19 <= 377, "c")

P19=model.addVar(vtype="I", name="P19")
model.addConstr(P19 <= 377, "c")

Q19=model.addVar(vtype="I", name="Q19")
model.addConstr(Q19 <= 377, "c")

R19=model.addVar(vtype="I", name="R19")
model.addConstr(R19 <= 377, "c")

S19=model.addVar(vtype="I", name="S19")
model.addConstr(S19 <= 377, "c")

T19=model.addVar(vtype="I", name="T19")
model.addConstr(T19 <= 377, "c")

U19=model.addVar(vtype="I", name="U19")
model.addConstr(U19 <= 377, "c")

V19=model.addVar(vtype="I", name="V19")
model.addConstr(V19 <= 377, "c")

W19=model.addVar(vtype="I", name="W19")
model.addConstr(W19 <= 377, "c")

X19=model.addVar(vtype="I", name="X19")
model.addConstr(X19 <= 377, "c")


C20=model.addVar(vtype="I", name="C20")
model.addConstr(C20 <= 377, "c")

D20=model.addVar(vtype="I", name="D20")
model.addConstr(D20 <= 377, "c")

E20=model.addVar(vtype="I", name="E20")
model.addConstr(E20 <= 377, "c")

F20=model.addVar(vtype="I", name="F20")
model.addConstr(F20 <= 377, "c")

G20=model.addVar(vtype="I", name="G20")
model.addConstr(G20 <= 377, "c")

H20=model.addVar(vtype="I", name="H20")
model.addConstr(H20 <= 377, "c")

I20=model.addVar(vtype="I", name="I20")
model.addConstr(I20 <= 377, "c")

J20=model.addVar(vtype="I", name="J20")
model.addConstr(J20 <= 377, "c")

K20=model.addVar(vtype="I", name="K20")
model.addConstr(K20 <= 377, "c")

L20=model.addVar(vtype="I", name="L20")
model.addConstr(L20 <= 377, "c")

M20=model.addVar(vtype="I", name="M20")
model.addConstr(M20 <= 377, "c")

N20=model.addVar(vtype="I", name="N20")
model.addConstr(N20 <= 377, "c")

O20=model.addVar(vtype="I", name="O20")
model.addConstr(O20 <= 377, "c")

P20=model.addVar(vtype="I", name="P20")
model.addConstr(P20 <= 377, "c")

Q20=model.addVar(vtype="I", name="Q20")
model.addConstr(Q20 <= 377, "c")

R20=model.addVar(vtype="I", name="R20")
model.addConstr(R20 <= 377, "c")

S20=model.addVar(vtype="I", name="S20")
model.addConstr(S20 <= 377, "c")

T20=model.addVar(vtype="I", name="T20")
model.addConstr(T20 <= 377, "c")

U20=model.addVar(vtype="I", name="U20")
model.addConstr(U20 <= 377, "c")

V20=model.addVar(vtype="I", name="V20")
model.addConstr(V20 <= 377, "c")

W20=model.addVar(vtype="I", name="W20")
model.addConstr(W20 <= 377, "c")

X20=model.addVar(vtype="I", name="X20")
model.addConstr(X20 <= 377, "c")


C21=model.addVar(vtype="I", name="C21")
model.addConstr(C21 <= 377, "c")

D21=model.addVar(vtype="I", name="D21")
model.addConstr(D21 <= 377, "c")

E21=model.addVar(vtype="I", name="E21")
model.addConstr(E21 <= 377, "c")

F21=model.addVar(vtype="I", name="F21")
model.addConstr(F21 <= 377, "c")

G21=model.addVar(vtype="I", name="G21")
model.addConstr(G21 <= 377, "c")

H21=model.addVar(vtype="I", name="H21")
model.addConstr(H21 <= 377, "c")

I21=model.addVar(vtype="I", name="I21")
model.addConstr(I21 <= 377, "c")

J21=model.addVar(vtype="I", name="J21")
model.addConstr(J21 <= 377, "c")

K21=model.addVar(vtype="I", name="K21")
model.addConstr(K21 <= 377, "c")

L21=model.addVar(vtype="I", name="L21")
model.addConstr(L21 <= 377, "c")

M21=model.addVar(vtype="I", name="M21")
model.addConstr(M21 <= 377, "c")

N21=model.addVar(vtype="I", name="N21")
model.addConstr(N21 <= 377, "c")

O21=model.addVar(vtype="I", name="O21")
model.addConstr(O21 <= 377, "c")

P21=model.addVar(vtype="I", name="P21")
model.addConstr(P21 <= 377, "c")

Q21=model.addVar(vtype="I", name="Q21")
model.addConstr(Q21 <= 377, "c")

R21=model.addVar(vtype="I", name="R21")
model.addConstr(R21 <= 377, "c")

S21=model.addVar(vtype="I", name="S21")
model.addConstr(S21 <= 377, "c")

T21=model.addVar(vtype="I", name="T21")
model.addConstr(T21 <= 377, "c")

U21=model.addVar(vtype="I", name="U21")
model.addConstr(U21 <= 377, "c")

V21=model.addVar(vtype="I", name="V21")
model.addConstr(V21 <= 377, "c")

W21=model.addVar(vtype="I", name="W21")
model.addConstr(W21 <= 377, "c")

X21=model.addVar(vtype="I", name="X21")
model.addConstr(X21 <= 377, "c")


C22=model.addVar(vtype="I", name="C22")
model.addConstr(C22 <= 377, "c")

D22=model.addVar(vtype="I", name="D22")
model.addConstr(D22 <= 377, "c")

E22=model.addVar(vtype="I", name="E22")
model.addConstr(E22 <= 377, "c")

F22=model.addVar(vtype="I", name="F22")
model.addConstr(F22 <= 377, "c")

G22=model.addVar(vtype="I", name="G22")
model.addConstr(G22 <= 377, "c")

H22=model.addVar(vtype="I", name="H22")
model.addConstr(H22 <= 377, "c")

I22=model.addVar(vtype="I", name="I22")
model.addConstr(I22 <= 377, "c")

J22=model.addVar(vtype="I", name="J22")
model.addConstr(J22 <= 377, "c")

K22=model.addVar(vtype="I", name="K22")
model.addConstr(K22 <= 377, "c")

L22=model.addVar(vtype="I", name="L22")
model.addConstr(L22 <= 377, "c")

M22=model.addVar(vtype="I", name="M22")
model.addConstr(M22 <= 377, "c")

N22=model.addVar(vtype="I", name="N22")
model.addConstr(N22 <= 377, "c")

O22=model.addVar(vtype="I", name="O22")
model.addConstr(O22 <= 377, "c")

P22=model.addVar(vtype="I", name="P22")
model.addConstr(P22 <= 377, "c")

Q22=model.addVar(vtype="I", name="Q22")
model.addConstr(Q22 <= 377, "c")

R22=model.addVar(vtype="I", name="R22")
model.addConstr(R22 <= 377, "c")

S22=model.addVar(vtype="I", name="S22")
model.addConstr(S22 <= 377, "c")

T22=model.addVar(vtype="I", name="T22")
model.addConstr(T22 <= 377, "c")

U22=model.addVar(vtype="I", name="U22")
model.addConstr(U22 <= 377, "c")

V22=model.addVar(vtype="I", name="V22")
model.addConstr(V22 <= 377, "c")

W22=model.addVar(vtype="I", name="W22")
model.addConstr(W22 <= 377, "c")

X22=model.addVar(vtype="I", name="X22")
model.addConstr(X22 <= 377, "c")


C23=model.addVar(vtype="I", name="C23")
model.addConstr(C23 <= 377, "c")

D23=model.addVar(vtype="I", name="D23")
model.addConstr(D23 <= 377, "c")

E23=model.addVar(vtype="I", name="E23")
model.addConstr(E23 <= 377, "c")

F23=model.addVar(vtype="I", name="F23")
model.addConstr(F23 <= 377, "c")

G23=model.addVar(vtype="I", name="G23")
model.addConstr(G23 <= 377, "c")

H23=model.addVar(vtype="I", name="H23")
model.addConstr(H23 <= 377, "c")

I23=model.addVar(vtype="I", name="I23")
model.addConstr(I23 <= 377, "c")

J23=model.addVar(vtype="I", name="J23")
model.addConstr(J23 <= 377, "c")

K23=model.addVar(vtype="I", name="K23")
model.addConstr(K23 <= 377, "c")

L23=model.addVar(vtype="I", name="L23")
model.addConstr(L23 <= 377, "c")

M23=model.addVar(vtype="I", name="M23")
model.addConstr(M23 <= 377, "c")

N23=model.addVar(vtype="I", name="N23")
model.addConstr(N23 <= 377, "c")

O23=model.addVar(vtype="I", name="O23")
model.addConstr(O23 <= 377, "c")

P23=model.addVar(vtype="I", name="P23")
model.addConstr(P23 <= 377, "c")

Q23=model.addVar(vtype="I", name="Q23")
model.addConstr(Q23 <= 377, "c")

R23=model.addVar(vtype="I", name="R23")
model.addConstr(R23 <= 377, "c")

S23=model.addVar(vtype="I", name="S23")
model.addConstr(S23 <= 377, "c")

T23=model.addVar(vtype="I", name="T23")
model.addConstr(T23 <= 377, "c")

U23=model.addVar(vtype="I", name="U23")
model.addConstr(U23 <= 377, "c")

V23=model.addVar(vtype="I", name="V23")
model.addConstr(V23 <= 377, "c")

W23=model.addVar(vtype="I", name="W23")
model.addConstr(W23 <= 377, "c")

X23=model.addVar(vtype="I", name="X23")
model.addConstr(X23 <= 377, "c")


C24=model.addVar(vtype="I", name="C24")
model.addConstr(C24 <= 377, "c")

D24=model.addVar(vtype="I", name="D24")
model.addConstr(D24 <= 377, "c")

E24=model.addVar(vtype="I", name="E24")
model.addConstr(E24 <= 377, "c")

F24=model.addVar(vtype="I", name="F24")
model.addConstr(F24 <= 377, "c")

G24=model.addVar(vtype="I", name="G24")
model.addConstr(G24 <= 377, "c")

H24=model.addVar(vtype="I", name="H24")
model.addConstr(H24 <= 377, "c")

I24=model.addVar(vtype="I", name="I24")
model.addConstr(I24 <= 377, "c")

J24=model.addVar(vtype="I", name="J24")
model.addConstr(J24 <= 377, "c")

K24=model.addVar(vtype="I", name="K24")
model.addConstr(K24 <= 377, "c")

L24=model.addVar(vtype="I", name="L24")
model.addConstr(L24 <= 377, "c")

M24=model.addVar(vtype="I", name="M24")
model.addConstr(M24 <= 377, "c")

N24=model.addVar(vtype="I", name="N24")
model.addConstr(N24 <= 377, "c")

O24=model.addVar(vtype="I", name="O24")
model.addConstr(O24 <= 377, "c")

P24=model.addVar(vtype="I", name="P24")
model.addConstr(P24 <= 377, "c")

Q24=model.addVar(vtype="I", name="Q24")
model.addConstr(Q24 <= 377, "c")

R24=model.addVar(vtype="I", name="R24")
model.addConstr(R24 <= 377, "c")

S24=model.addVar(vtype="I", name="S24")
model.addConstr(S24 <= 377, "c")

T24=model.addVar(vtype="I", name="T24")
model.addConstr(T24 <= 377, "c")

U24=model.addVar(vtype="I", name="U24")
model.addConstr(U24 <= 377, "c")

V24=model.addVar(vtype="I", name="V24")
model.addConstr(V24 <= 377, "c")

W24=model.addVar(vtype="I", name="W24")
model.addConstr(W24 <= 377, "c")

X24=model.addVar(vtype="I", name="X24")
model.addConstr(X24 <= 377, "c")


C25=model.addVar(vtype="I", name="C25")
model.addConstr(C25 <= 377, "c")

D25=model.addVar(vtype="I", name="D25")
model.addConstr(D25 <= 377, "c")

E25=model.addVar(vtype="I", name="E25")
model.addConstr(E25 <= 377, "c")

F25=model.addVar(vtype="I", name="F25")
model.addConstr(F25 <= 377, "c")

G25=model.addVar(vtype="I", name="G25")
model.addConstr(G25 <= 377, "c")

H25=model.addVar(vtype="I", name="H25")
model.addConstr(H25 <= 377, "c")

I25=model.addVar(vtype="I", name="I25")
model.addConstr(I25 <= 377, "c")

J25=model.addVar(vtype="I", name="J25")
model.addConstr(J25 <= 377, "c")

K25=model.addVar(vtype="I", name="K25")
model.addConstr(K25 <= 377, "c")

L25=model.addVar(vtype="I", name="L25")
model.addConstr(L25 <= 377, "c")

M25=model.addVar(vtype="I", name="M25")
model.addConstr(M25 <= 377, "c")

N25=model.addVar(vtype="I", name="N25")
model.addConstr(N25 <= 377, "c")

O25=model.addVar(vtype="I", name="O25")
model.addConstr(O25 <= 377, "c")

P25=model.addVar(vtype="I", name="P25")
model.addConstr(P25 <= 377, "c")

Q25=model.addVar(vtype="I", name="Q25")
model.addConstr(Q25 <= 377, "c")

R25=model.addVar(vtype="I", name="R25")
model.addConstr(R25 <= 377, "c")

S25=model.addVar(vtype="I", name="S25")
model.addConstr(S25 <= 377, "c")

T25=model.addVar(vtype="I", name="T25")
model.addConstr(T25 <= 377, "c")

U25=model.addVar(vtype="I", name="U25")
model.addConstr(U25 <= 377, "c")

V25=model.addVar(vtype="I", name="V25")
model.addConstr(V25 <= 377, "c")

W25=model.addVar(vtype="I", name="W25")
model.addConstr(W25 <= 377, "c")

X25=model.addVar(vtype="I", name="X25")
model.addConstr(X25 <= 377, "c")

# C26=model.addVar(vtype="I", name="C26")
# D26=model.addVar(vtype="I", name="D26")
# E26=model.addVar(vtype="I", name="E26")
# F26=model.addVar(vtype="I", name="F26")
# G26=model.addVar(vtype="I", name="G26")
# H26=model.addVar(vtype="I", name="H26")
# I26=model.addVar(vtype="I", name="I26")
# J26=model.addVar(vtype="I", name="J26")
# K26=model.addVar(vtype="I", name="K26")
# L26=model.addVar(vtype="I", name="L26")
# M26=model.addVar(vtype="I", name="M26")
# N26=model.addVar(vtype="I", name="N26")
# O26=model.addVar(vtype="I", name="O26")
# P26=model.addVar(vtype="I", name="P26")
# Q26=model.addVar(vtype="I", name="Q26")
# R26=model.addVar(vtype="I", name="R26")
# S26=model.addVar(vtype="I", name="S26")
# T26=model.addVar(vtype="I", name="T26")
# U26=model.addVar(vtype="I", name="U26")
# V26=model.addVar(vtype="I", name="V26")
# W26=model.addVar(vtype="I", name="W26")
# X26=model.addVar(vtype="I", name="X26")

C27=model.addVar(vtype="I", name="C27")
model.addConstr(C27 <= 377, "c")

D27=model.addVar(vtype="I", name="D27")
model.addConstr(D27 <= 377, "c")

E27=model.addVar(vtype="I", name="E27")
model.addConstr(E27 <= 377, "c")

F27=model.addVar(vtype="I", name="F27")
model.addConstr(F27 <= 377, "c")

G27=model.addVar(vtype="I", name="G27")
model.addConstr(G27 <= 377, "c")

H27=model.addVar(vtype="I", name="H27")
model.addConstr(H27 <= 377, "c")

I27=model.addVar(vtype="I", name="I27")
model.addConstr(I27 <= 377, "c")

J27=model.addVar(vtype="I", name="J27")
model.addConstr(J27 <= 377, "c")

K27=model.addVar(vtype="I", name="K27")
model.addConstr(K27 <= 377, "c")

L27=model.addVar(vtype="I", name="L27")
model.addConstr(L27 <= 377, "c")

M27=model.addVar(vtype="I", name="M27")
model.addConstr(M27 <= 377, "c")

N27=model.addVar(vtype="I", name="N27")
model.addConstr(N27 <= 377, "c")

O27=model.addVar(vtype="I", name="O27")
model.addConstr(O27 <= 377, "c")

P27=model.addVar(vtype="I", name="P27")
model.addConstr(P27 <= 377, "c")

Q27=model.addVar(vtype="I", name="Q27")
model.addConstr(Q27 <= 377, "c")

R27=model.addVar(vtype="I", name="R27")
model.addConstr(R27 <= 377, "c")

S27=model.addVar(vtype="I", name="S27")
model.addConstr(S27 <= 377, "c")

T27=model.addVar(vtype="I", name="T27")
model.addConstr(T27 <= 377, "c")

U27=model.addVar(vtype="I", name="U27")
model.addConstr(U27 <= 377, "c")

V27=model.addVar(vtype="I", name="V27")
model.addConstr(V27 <= 377, "c")

W27=model.addVar(vtype="I", name="W27")
model.addConstr(W27 <= 377, "c")

X27=model.addVar(vtype="I", name="X27")
model.addConstr(X27 <= 377, "c")

Sensor12=model.addVar(vtype="I", name="Sensor12")
Sensor10=model.addVar(vtype="I", name="Sensor10")
Sensor9=model.addVar(vtype="I", name="Sensor9")
Sensor8=model.addVar(vtype="I", name="Sensor8")
Sensor7=model.addVar(vtype="I", name="Sensor7")
Sensor6=model.addVar(vtype="I", name="Sensor6")
Sensor5=model.addVar(vtype="I", name="Sensor5")
Sensor21=model.addVar(vtype="I", name="Sensor21")
Sensor20=model.addVar(vtype="I", name="Sensor20")
Sensor19=model.addVar(vtype="I", name="Sensor19")
Sensor25=model.addVar(vtype="I", name="Sensor25")
Sensor24=model.addVar(vtype="I", name="Sensor24")
Sensor11=model.addVar(vtype="I", name="Sensor11")
										

model.addConstr(C4+D4+E4+F4+G4+H4+I4+J4+K4+L4+M4+N4+O4+P4+Q4+R4+S4+T4+U4+V4+W4+X4+C5+C6+D6+C7+D7+E7+C8+D8+E8+F8+C9+D9+E9+F9+G9+C10+D10
+E10+F10+G10+H10+I10+C11+D11+E11+F11+G11+H11+I11+J11+C12+D12+E12+F12+G12+H12+I12+J12+K12+C13+D13+E13+F13+G13+H13+I13+J13+K13+L13+M13+
C14+D14+E14+F14+G14+H14+I14+J14+K14+L14+M14+C15+D15+E15+F15+G15+H15+I15+J15+K15+L15+M15+C16+D16+E16+F16+G16+H16+I16+J16+K16+L16+M16+N16+
C17+D17+E17+F17+G17+H17+I17+J17+K17+L17+M17+N17+O17+C18+D18+E18+F18+G18+H18+I18+J18+K18+L18+M18+N18+O18+P18+Q18+C19+D19+E19+F19+G19+H19+
I19+J19+K19+L19+M19+N19+O19+P19+Q19+R19+C20+D20+E20+F20+G20+H20+I20+J20+K20+L20+M20+N20+O20+P20+Q20+R20+C21+D21+E21+F21+G21+H21+I21+J21+
K21+L21+M21+N21+O21+P21+Q21+R21+S21+C22+D22+E22+F22+G22+H22+I22+J22+K22+L22+M22+N22+O22+P22+Q22+R22+S22+T22+C23+D23+E23+F23+G23+H23+I23+
J23+K23+L23+M23+N23+O23+P23+Q23+R23+S23+T23+C24+D24+E24+F24+G24+H24+I24+J24+K24+L24+M24+N24+O24+P24+Q24+R24+S24+T24+U24+C25+D25+E25+F25+
G25+H25+I25+J25+K25+L25+M25+N25+O25+P25+Q25+R25+S25+T25+U25+V25+C27+D27+E27+F27+G27+H27+I27+J27+K27+L27+M27+N27+O27+P27+Q27+R27+S27+T27+
U27+V27+W27 == Sensor12, "c1")
# C26+D26+E26+F26+G26+H26+I26+J26+K26+L26+M26+N26+O26+P26+Q26+R26+S26+T26+U26+V26+W26+

model.addConstr(Sensor12 <= 5265, "c15")


model.addConstr(D4+E4+F4+G4+H4+I4+J4+K4+L4+M4+N4+O4+P4+Q4+R4+S4+T4+U4+V4+W4+X4+C5+D5+E5+F5+G5+H5+I5+J5+K5+L5+M5+N5+O5+P5+Q5+R5+S5+T5+U5+
V5+W5+X5+D6+D7+E7+D8+E8+F8+D9+E9+F9+G9+D10+E10+F10+G10+H10+I10+D11+E11+F11+G11+H11+I11+J11+D12+E12+F12+G12+H12+I12+J12+K12+D13+E13+F13+
G13+H13+I13+J13+K13+L13+M13+D14+E14+F14+G14+H14+I14+J14+K14+L14+M14+D15+E15+F15+G15+H15+I15+J15+K15+L15+M15+D16+E16+F16+G16+H16+I16+J16+
K16+L16+M16+N16+D17+E17+F17+G17+H17+I17+J17+K17+L17+M17+N17+O17+D18+E18+F18+G18+H18+I18+J18+K18+L18+M18+N18+O18+P18+Q18+D19+E19+F19+G19+
H19+I19+J19+K19+L19+M19+N19+O19+P19+Q19+R19+D20+E20+F20+G20+H20+I20+J20+K20+L20+M20+N20+O20+P20+Q20+R20+D21+E21+F21+G21+H21+I21+J21+K21+
L21+M21+N21+O21+P21+Q21+R21+S21+D22+E22+F22+G22+H22+I22+J22+K22+L22+M22+N22+O22+P22+Q22+R22+S22+T22+D23+E23+F23+G23+H23+I23+J23+K23+L23+
M23+N23+O23+P23+Q23+R23+S23+T23+D24+E24+F24+G24+H24+I24+J24+K24+L24+M24+N24+O24+P24+Q24+R24+S24+T24+U24+D25+E25+F25+G25+H25+I25+J25+K25+
L25+M25+N25+O25+P25+Q25+R25+S25+T25+U25+V25+D27+E27+F27+
G27+H27+I27+J27+K27+L27+M27+N27+O27+P27+Q27+R27+S27+T27+U27+V27+W27 == Sensor10,"c2")
# D26+E26+F26+G26+H26+I26+J26+K26+L26+M26+N26+O26+P26+Q26+R26+S26+T26+U26+V26+W26+

model.addConstr(Sensor10 <= 1287, "c16")

												
model.addConstr(G4+H4+I4+J4+K4+L4+M4+N4+O4+P4+Q4+R4+S4+T4+U4+V4+W4+X4+G5+H5+I5+J5+K5+L5+M5+N5+O5+P5+Q5+R5+S5+T5+U5+V5+W5+X5+C5+
G6+H6+I6+J6+K6+L6+M6+N6+O6+P6+Q6+R6+S6+T6+U6+V6+W6+X6+C6+D6+G7+H7+I7+J7+K7+L7+M7+N7+O7+P7+Q7+R7+S7+T7+U7+V7+W7+X7+C7+D7+E7+G9+
G10+H10+I10+G11+H11+I11+J11+G12+H12+I12+J12+K12+G13+H13+I13+J13+K13+L13+M13+G14+H14+I14+J14+K14+L14+M14+G15+H15+I15+J15+K15+L15+M15+
G16+H16+I16+J16+K16+L16+M16+N16+G17+H17+I17+J17+K17+L17+M17+N17+O17+G18+H18+I18+J18+K18+L18+M18+N18+O18+P18+Q18+G19+H19+I19+J19+K19+
L19+M19+N19+O19+P19+Q19+R19+G20+H20+I20+J20+K20+L20+M20+N20+O20+P20+Q20+R20+G21+H21+I21+J21+K21+L21+M21+N21+O21+P21+Q21+R21+S21+G22+
H22+I22+J22+K22+L22+M22+N22+O22+P22+Q22+R22+S22+T22+G23+H23+I23+J23+K23+L23+M23+N23+O23+P23+Q23+R23+S23+T23+G24+H24+I24+J24+K24+L24+
M24+N24+O24+P24+Q24+R24+S24+T24+U24+G25+H25+I25+J25+K25+L25+M25+N25+O25+P25+Q25+R25+S25+T25+U25+V25+G27+H27+I27+J27+K27+L27+M27+N27+
O27+P27+Q27+R27+S27+T27+U27+V27+W27 == Sensor9 ,"c4")
# + G26+H26+I26+J26+K26+L26+M26+N26+ O26+P26+Q26+R26+S26+T26+U26+V26+W26

model.addConstr(Sensor9 <= 4666, "c17")

model.addConstr(G4+H4+I4+J4+K4+L4+M4+N4+O4+P4+Q4+R4+S4+T4+U4+V4+W4+X4+G5+H5+I5+J5+K5+L5+M5+N5+O5+P5+Q5+R5+S5+T5+U5+V5+W5+X5+C5+G6+H6+
I6+J6+K6+L6+M6+N6+O6+P6+Q6+R6+S6+T6+U6+V6+W6+X6+C6+D6+G7+H7+I7+J7+K7+L7+M7+N7+O7+P7+Q7+R7+S7+T7+U7+V7+W7+X7+C7+D7+E7+C8+D8+E8+F8+G8+H8+
I8+J8+K8+L8+M8+N8+O8+P8+Q8+R8+S8+T8+U8+V8+W8+X8+G9+G10+H10+I10+G11+H11+I11+J11+G12+H12+I12+J12+K12+G13+H13+I13+J13+K13+L13+M13+G14+H14+
I14+J14+K14+L14+M14+G15+H15+I15+J15+K15+L15+M15+G16+H16+I16+J16+K16+L16+M16+N16+G17+H17+I17+J17+K17+L17+M17+N17+O17+G18+H18+I18+J18+K18+
L18+M18+N18+O18+P18+Q18+G19+H19+I19+J19+K19+L19+M19+N19+O19+P19+Q19+R19+G20+H20+I20+J20+K20+L20+M20+N20+O20+P20+Q20+R20+G21+H21+I21+J21+
K21+L21+M21+N21+O21+P21+Q21+R21+S21+G22+H22+I22+J22+K22+L22+M22+N22+O22+P22+Q22+R22+S22+T22+G23+H23+I23+J23+K23+L23+M23+N23+O23+P23+Q23+
R23+S23+T23+G24+H24+I24+J24+K24+L24+M24+N24+O24+P24+Q24+R24+S24+T24+U24+G25+H25+I25+J25+K25+L25+M25+N25+O25+P25+Q25+R25+S25+T25+U25+V25+
G27+H27+I27+J27+K27+L27+M27+N27+O27+P27+Q27+R27+S27+T27+U27+V27+W27 == Sensor8,"c5")
# G26+H26+I26+J26+K26+L26+M26+N26+O26+P26+Q26+R26+S26+T26+U26+V26+W26+

model.addConstr(Sensor8 <= 4798, "c18")

model.addConstr(H4+I4+J4+K4+L4+M4+N4+O4+P4+Q4+R4+S4+T4+U4+V4+W4+X4+H5+I5+J5+K5+L5+M5+N5+O5+P5+Q5+R5+S5+T5+U5+V5+W5+X5+H6+I6+J6+K6+L6+M6+
N6+O6+P6+Q6+R6+S6+T6+U6+V6+W6+X6+H7+I7+J7+K7+L7+M7+N7+O7+P7+Q7+R7+S7+T7+U7+V7+W7+X7+H8+I8+J8+K8+L8+M8+N8+O8+P8+Q8+R8+S8+T8+U8+V8+W8+X8+
C5+C6+D6+C7+D7+E7+C8+D8+E8+F8+C9+D9+E9+F9+G9+H9+I9+J9+K9+L9+M9+N9+O9+P9+Q9+R9+S9+T9+U9+V9+W9+X9+H10+I10+H11+I11+J11+H12+I12+J12+K12+H13+
I13+J13+K13+L13+M13+H14+I14+J14+K14+L14+M14+H15+I15+J15+K15+L15+M15+H16+I16+J16+K16+L16+M16+N16+H17+I17+J17+K17+L17+M17+N17+O17+H18+I18+
J18+K18+L18+M18+N18+O18+P18+Q18+H19+I19+J19+K19+L19+M19+N19+O19+P19+Q19+R19+H20+I20+J20+K20+L20+M20+N20+O20+P20+Q20+R20+H21+I21+J21+K21+
L21+M21+N21+O21+P21+Q21+R21+S21+H22+I22+J22+K22+L22+M22+N22+O22+P22+Q22+R22+S22+T22+H23+I23+J23+K23+L23+M23+N23+O23+P23+Q23+R23+S23+T23+
H24+I24+J24+K24+L24+M24+N24+O24+P24+Q24+R24+S24+T24+U24+H25+I25+J25+K25+L25+M25+N25+O25+P25+Q25+R25+S25+T25+U25+V25+
H27+I27+J27+K27+L27+M27+N27+O27+P27+Q27+R27+S27+T27+U27+V27+W27 == Sensor7 ,"c6")
# H26+I26+J26+K26+L26+M26+N26+O26+P26+Q26+R26+S26+T26+U26+V26+W26+

model.addConstr(Sensor7 <= 4847, "c19")

model.addConstr(J4+K4+L4+M4+N4+O4+P4+Q4+R4+S4+T4+U4+V4+W4+X4+J5+K5+L5+M5+N5+O5+P5+Q5+R5+S5+T5+U5+V5+W5+X5+J6+K6+L6+M6+N6+O6+P6+Q6+R6+S6+T6+U6+V6+
W6+X6+J7+K7+L7+M7+N7+O7+P7+Q7+R7+S7+T7+U7+V7+W7+X7+J8+K8+L8+M8+N8+O8+P8+Q8+R8+S8+T8+U8+V8+W8+X8+J9+K9+L9+M9+N9+O9+P9+Q9+R9+S9+T9+U9+V9+W9+X9+C5+
C6+D6+C7+D7+E7+C8+D8+E8+F8+C9+D9+E9+F9+G9+C10+D10+E10+F10+G10+H10+I10+J10+K10+L10+M10+N10+O10+P10+Q10+R10+S10+T10+U10+V10+W10+X10+J11+J12+K12+
J13+K13+L13+M13+J14+K14+L14+M14+J15+K15+L15+M15+J16+K16+L16+M16+N16+J17+K17+L17+M17+N17+O17+J18+K18+L18+M18+N18+O18+P18+Q18+J19+K19+L19+M19+N19+
O19+P19+Q19+R19+J20+K20+L20+M20+N20+O20+P20+Q20+R20+J21+K21+L21+M21+N21+O21+P21+Q21+R21+S21+J22+K22+L22+M22+N22+O22+P22+Q22+R22+S22+T22+J23+K23+
L23+M23+N23+O23+P23+Q23+R23+S23+T23+J24+K24+L24+M24+N24+O24+P24+Q24+R24+S24+T24+U24+J25+K25+L25+M25+N25+O25+P25+Q25+R25+S25+T25+U25+V25+
J27+K27+L27+M27+N27+O27+P27+Q27+R27+S27+T27+U27+V27+W27 == Sensor6 ,"c7")
# J26+K26+L26+M26+N26+O26+P26+Q26+R26+S26+T26+U26+V26+W26+

model.addConstr(Sensor6 <= 4026, "c20")

model.addConstr(L4+M4+N4+O4+P4+Q4+R4+S4+T4+U4+V4+W4+X4+L5+M5+N5+O5+P5+Q5+R5+S5+T5+U5+V5+W5+X5+L6+M6+N6+O6+P6+Q6+R6+S6+T6+U6+V6+W6+X6+L7+M7+N7+
O7+P7+Q7+R7+S7+T7+U7+V7+W7+X7+L8+M8+N8+O8+P8+Q8+R8+S8+T8+U8+V8+W8+X8+L9+M9+N9+O9+P9+Q9+R9+S9+T9+U9+V9+W9+X9+L10+M10+N10+O10+P10+Q10+R10+S10+
T10+U10+V10+W10+X10+L11+M11+N11+O11+P11+Q11+R11+S11+T11+U11+V11+W11+X11+C5+C6+D6+C7+D7+E7+C8+D8+E8+F8+C9+D9+E9+F9+G9+C10+D10+E10+F10+G10+H10+
I10+C11+D11+E11+F11+G11+H11+I11+J11+L13+M13+L14+M14+L15+M15+L16+M16+N16+L17+M17+N17+O17+L18+M18+N18+O18+P18+Q18+L19+M19+N19+O19+P19+Q19+R19+
L20+M20+N20+O20+P20+Q20+R20+L21+M21+N21+O21+P21+Q21+R21+S21+L22+M22+N22+O22+P22+Q22+R22+S22+T22+L23+M23+N23+O23+P23+Q23+R23+S23+T23+L24+M24+
N24+O24+P24+Q24+R24+S24+T24+U24+L25+M25+N25+O25+P25+Q25+R25+S25+T25+U25+V25+L27+M27+N27+O27+
P27+Q27+R27+S27+T27+U27+V27+W27+X27 == Sensor5,"c8")
# L26+M26+N26+O26+P26+Q26+R26+S26+T26+U26+V26+W26+

model.addConstr(Sensor5 <= 4017, "c21")

model.addConstr(N4+O4+P4+Q4+R4+S4+T4+U4+V4+W4+X4+N5+O5+P5+Q5+R5+S5+T5+U5+V5+W5+X5+N6+O6+P6+Q6+R6+S6+T6+U6+V6+W6+X6+N7+O7+P7+Q7+R7+S7+T7+U7+V7+W7+X7+
N8+O8+P8+Q8+R8+S8+T8+U8+V8+W8+X8+N9+O9+P9+Q9+R9+S9+T9+U9+V9+W9+X9+N10+O10+P10+Q10+R10+S10+T10+U10+V10+W10+X10+N11+O11+P11+Q11+R11+S11+T11+U11+V11+
W11+X11+N12+O12+P12+Q12+R12+S12+T12+U12+V12+W12+X12+C5+C6+D6+C7+D7+E7+C8+D8+E8+F8+C9+D9+E9+F9+G9+C10+D10+E10+F10+G10+H10+I10+C11+D11+E11+F11+G11+
H11+I11+J11+C12+D12+E12+F12+G12+H12+I12+J12+K12+C13+D13+E13+F13+G13+H13+I13+J13+K13+L13+M13+N13+O13+P13+Q13+R13+S13+T13+U13+V13+W13+X13+C14+D14+
E14+F14+G14+H14+I14+J14+K14+L14+M14+N14+O14+P14+Q14+R14+S14+T14+U14+V14+W14+X14+C15+D15+E15+F15+G15+H15+I15+J15+K15+L15+M15+N15+O15+P15+Q15+R15+
S15+T15+U15+V15+W15+X15+N16+N17+O17+N18+O18+P18+Q18+N19+O19+P19+Q19+R19+N20+O20+P20+Q20+R20+N21+O21+P21+Q21+R21+S21+N22+O22+P22+Q22+R22+S22+T22+
N23+O23+P23+Q23+R23+S23+T23+N24+O24+P24+Q24+R24+S24+T24+U24+N25+O25+P25+Q25+R25+S25+T25+U25+V25+N27+O27+
P27+Q27+R27+S27+T27+U27+V27+W27 == Sensor21,"c9")
# +N26+O26+P26+Q26+R26+S26+T26+U26+V26+W26

model.addConstr(Sensor21 <= 2415, "c22")

model.addConstr(R4+S4+T4+U4+V4+W4+X4+R5+S5+T5+U5+V5+W5+X5+R6+S6+T6+U6+V6+W6+X6+R7+S7+T7+U7+V7+W7+X7+R8+S8+T8+U8+V8+W8+X8+R9+S9+T9+U9+V9+W9+X9+R10+
S10+T10+U10+V10+W10+X10+R11+S11+T11+U11+V11+W11+X11+R12+S12+T12+U12+V12+W12+X12+R13+S13+T13+U13+V13+W13+X13+R14+S14+T14+U14+V14+W14+X14+R15+S15+T15+
U15+V15+W15+X15+R16+S16+T16+U16+V16+W16+X16+R17+S17+T17+U17+V17+W17+X17+C5+C6+D6+C7+D7+E7+C8+D8+E8+F8+C9+D9+E9+F9+G9+C10+D10+E10+F10+G10+H10+I10+C11+
D11+E11+F11+G11+H11+I11+J11+C12+D12+E12+F12+G12+H12+I12+J12+K12+C13+D13+E13+F13+G13+H13+I13+J13+K13+L13+M13+C14+D14+E14+F14+G14+H14+I14+J14+K14+L14+
M14+C15+D15+E15+F15+G15+H15+I15+J15+K15+L15+M15+C16+D16+E16+F16+G16+H16+I16+J16+K16+L16+M16+N16+C17+D17+E17+F17+G17+H17+I17+J17+K17+L17+M17+N17+O17+
R19+R20+R21+S21+R22+S22+T22+R23+S23+T23+R24+S24+T24+U24+R25+S25+T25+U25+V25+R27+S27+T27+U27+V27+W27 == Sensor20,"c10")
# +R26+S26+T26+U26+V26+W26

model.addConstr(Sensor20 <= 2363, "c23")

model.addConstr(S4+T4+U4+V4+W4+X4+S5+T5+U5+V5+W5+X5+S6+T6+U6+V6+W6+X6+S7+T7+U7+V7+W7+X7+S8+T8+U8+V8+W8+X8+S9+T9+U9+V9+W9+X9+S10+T10+U10+V10+W10+X10+
S11+T11+U11+V11+W11+X11+S12+T12+U12+V12+W12+X12+S13+T13+U13+V13+W13+X13+S14+T14+U14+V14+W14+X14+S15+T15+U15+V15+W15+X15+S16+T16+U16+V16+W16+X16+S17+
T17+U17+V17+W17+X17+S18+T18+U18+V18+W18+X18+C5+C6+D6+C7+D7+E7+C8+D8+E8+F8+C9+D9+E9+F9+G9+C10+D10+E10+F10+G10+H10+I10+C11+D11+E11+F11+G11+H11+I11+J11+
C12+D12+E12+F12+G12+H12+I12+J12+K12+C13+D13+E13+F13+G13+H13+I13+J13+K13+L13+M13+C14+D14+E14+F14+G14+H14+I14+J14+K14+L14+M14+C15+D15+E15+F15+G15+H15+
I15+J15+K15+L15+M15+C16+D16+E16+F16+G16+H16+I16+J16+K16+L16+M16+N16+C17+D17+E17+F17+G17+H17+I17+J17+K17+L17+M17+N17+O17+C18+D18+E18+F18+G18+H18+I18+
J18+K18+L18+M18+N18+O18+P18+Q18+S21+S22+T22+S23+T23+S24+T24+U24+S25+T25+U25+V25+S27+T27+U27+V27+W27 == Sensor19,"c11")
# +S26+T26+U26+V26+W26

model.addConstr(Sensor19 <= 2641, "c24")

model.addConstr(U4+V4+W4+X4+U5+V5+W5+X5+U6+V6+W6+X6+U7+V7+W7+X7+U8+V8+W8+X8+U9+V9+W9+X9+U10+V10+W10+X10+U11+V11+W11+X11+U12+V12+W12+X12+U13+V13+W13+X13
+U14+V14+W14+X14+U15+V15+W15+X15+U16+V16+W16+X16+U17+V17+W17+X17+U18+V18+W18+X18+U19+V19+W19+X19+U20+V20+W20+X20+U21+V21+W21+X21+C5+C6+D6+C7+D7+E7+C8+D8
+E8+F8+C9+D9+E9+F9+G9+C10+D10+E10+F10+G10+H10+I10+C11+D11+E11+F11+G11+H11+I11+J11+C12+D12+E12+F12+G12+H12+I12+J12+K12+C13+D13+E13+F13+G13+H13+I13+J13+K13
+L13+M13+C14+D14+E14+F14+G14+H14+I14+J14+K14+L14+M14+C15+D15+E15+F15+G15+H15+I15+J15+K15+L15+M15+C16+D16+E16+F16+G16+H16+I16+J16+K16+L16+M16+N16+C17+D17
+E17+F17+G17+H17+I17+J17+K17+L17+M17+N17+O17+C18+D18+E18+F18+G18+H18+I18+J18+K18+L18+M18+N18+O18+P18+Q18+C19+D19+E19+F19+G19+H19+I19+J19+K19+L19+M19+N19
+O19+P19+Q19+R19+C20+D20+E20+F20+G20+H20+I20+J20+K20+L20+M20+N20+O20+P20+Q20+R20+C21+D21+E21+F21+G21+H21+I21+J21+K21+L21+M21+N21+O21+P21+Q21+R21+S21+C22
+D22+E22+F22+G22+H22+I22+J22+K22+L22+M22+N22+O22+P22+Q22+R22+S22+T22+U22+V22+W22+X22+C23+D23+E23+F23+G23+H23+I23+J23+K23+L23+M23+N23+O23+P23+Q23+R23+S23
+T23+U23+V23+W23+X23+U24+U25+V25+U27+V27+W27  == Sensor25,"c12")
# +U26+V26+W26

model.addConstr(Sensor25 <= 3805, "c25")

model.addConstr(V4+W4+X4+V5+W5+X5+V6+W6+X6+V7+W7+X7+V8+W8+X8+V9+W9+X9+V10+W10+X10+V11+W11+X11+V12+W12+X12+V13+W13+X13+V14+W14+X14+V15+W15+X15+V16+W16+X16+
V17+W17+X17+V18+W18+X18+V19+W19+X19+V20+W20+X20+V21+W21+X21+V22+W22+X22+V23+W23+X23+C5+C6+D6+C7+D7+E7+C8+D8+E8+F8+C9+D9+E9+F9+G9+C10+D10+E10+F10+G10+H10+
I10+C11+D11+E11+F11+G11+H11+I11+J11+C12+D12+E12+F12+G12+H12+I12+J12+K12+C13+D13+E13+F13+G13+H13+I13+J13+K13+L13+M13+C14+D14+E14+F14+G14+H14+I14+J14+K14+
L14+M14+C15+D15+E15+F15+G15+H15+I15+J15+K15+L15+M15+C16+D16+E16+F16+G16+H16+I16+J16+K16+L16+M16+N16+C17+D17+E17+F17+G17+H17+I17+J17+K17+L17+M17+N17+O17+
C18+D18+E18+F18+G18+H18+I18+J18+K18+L18+M18+N18+O18+P18+Q18+C19+D19+E19+F19+G19+H19+I19+J19+K19+L19+M19+N19+O19+P19+Q19+R19+C20+D20+E20+F20+G20+H20+I20+
J20+K20+L20+M20+N20+O20+P20+Q20+R20+C21+D21+E21+F21+G21+H21+I21+J21+K21+L21+M21+N21+O21+P21+Q21+R21+S21+C22+D22+E22+F22+G22+H22+I22+J22+K22+L22+M22+N22+
O22+P22+Q22+R22+S22+T22+C23+D23+E23+F23+G23+H23+I23+J23+K23+L23+M23+N23+O23+P23+Q23+R23+S23+T23+C24+D24+E24+F24+G24+H24+I24+J24+K24+L24+M24+N24+O24+P24+
Q24+R24+S24+T24+U24+V24+W24+X24+V25+V27+W27 == Sensor24,"c13")
# +V26+W26

model.addConstr(Sensor24 <= 2850, "c26")

model.addConstr(C5+C6+D6+C7+D7+E7+C8+D8+E8+F8+C9+D9+E9+F9+G9+C10+D10+E10+F10+G10+H10+I10+C11+D11+E11+F11+G11+H11+I11+J11+C12+D12+E12+F12+G12+H12+I12+J12
+K12+C13+D13+E13+F13+G13+H13+I13+J13+K13+L13+M13+C14+D14+E14+F14+G14+H14+I14+J14+K14+L14+M14+C15+D15+E15+F15+G15+H15+I15+J15+K15+L15+M15+C16+D16+E16+F16
+G16+H16+I16+J16+K16+L16+M16+N16+C17+D17+E17+F17+G17+H17+I17+J17+K17+L17+M17+N17+O17+C18+D18+E18+F18+G18+H18+I18+J18+K18+L18+M18+N18+O18+P18+Q18+C19+D19
+E19+F19+G19+H19+I19+J19+K19+L19+M19+N19+O19+P19+Q19+R19+C20+D20+E20+F20+G20+H20+I20+J20+K20+L20+M20+N20+O20+P20+Q20+R20+C21+D21+E21+F21+G21+H21+I21+J21
+K21+L21+M21+N21+O21+P21+Q21+R21+S21+C22+D22+E22+F22+G22+H22+I22+J22+K22+L22+M22+N22+O22+P22+Q22+R22+S22+T22+C23+D23+E23+F23+G23+H23+I23+J23+K23+L23+M23
+N23+O23+P23+Q23+R23+S23+T23+C24+D24+E24+F24+G24+H24+I24+J24+K24+L24+M24+N24+O24+P24+Q24+R24+S24+T24+U24+C25+D25+E25+F25+G25+H25+I25+J25+K25+L25+M25+N25
+O25+P25+Q25+R25+S25+T25+U25+V25+C27+D27+E27+F27+G27+H27+I27+J27+K27
+L27+M27+N27+O27+P27+Q27+R27+S27+T27+U27+V27+W27 == Sensor11,"c14")
#C26+D26+E26+F26+G26+H26+I26+J26+K26+L26+M26+N26+O26+P26+Q26+R26+S26+T26+U26+V26+W26+

model.addConstr(Sensor11 <= 4060, "c27")										


#model.setObjective((5265 - Sensor12) + (1287 - Sensor10) + (4666 - Sensor9) + (4798 - Sensor8) + (4847 - Sensor7) + (4026 - Sensor6) 
#    + (4017 - Sensor5 ) + (2415 - Sensor21 ) + (2363 - Sensor20 ) + (2641 - Sensor19 ) + (3805 - Sensor25 ) + (2850 - Sensor24 ) + (4060 - Sensor11 ), GRB.MINIMIZE)

model.setObjective(Sensor12 + Sensor10 + Sensor9 + Sensor8 + Sensor7 + Sensor6 + Sensor5 + Sensor21 + Sensor20 + Sensor19+ Sensor25 + Sensor24 + Sensor11, GRB.MAXIMIZE)

model.update() 										
model.optimize()								

print(model.ObjVal)

with open('matrizOD_d.csv', mode='a') as solution_file:
    constraints_writer = csv.writer(solution_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    constraints_writer.writerow([C4.X,D4.X,E4.X,F4.X,G4.X,H4.X,I4.X,J4.X,K4.X,L4.X,M4.X,N4.X,O4.X,P4.X,Q4.X,R4.X,S4.X,T4.X,U4.X,V4.X,W4.X,X4.X])
    constraints_writer.writerow([C5.X,D5.X,E5.X,F5.X,G5.X,H5.X,I5.X,J5.X,K5.X,L5.X,M5.X,N5.X,O5.X,P5.X,Q5.X,R5.X,S5.X,T5.X,U5.X,V5.X,W5.X,X5.X])
    constraints_writer.writerow([C6.X,D6.X,E6.X,F6.X,G6.X,H6.X,I6.X,J6.X,K6.X,L6.X,M6.X,N6.X,O6.X,P6.X,Q6.X,R6.X,S6.X,T6.X,U6.X,V6.X,W6.X,X6.X])
    constraints_writer.writerow([C7.X,D7.X,E7.X,F7.X,G7.X,H7.X,I7.X,J7.X,K7.X,L7.X,M7.X,N7.X,O7.X,P7.X,Q7.X,R7.X,S7.X,T7.X,U7.X,V7.X,W7.X,X7.X])
    constraints_writer.writerow([C8.X,D8.X,E8.X,F8.X,G8.X,H8.X,I8.X,J8.X,K8.X,L8.X,M8.X,N8.X,O8.X,P8.X,Q8.X,R8.X,S8.X,T8.X,U8.X,V8.X,W8.X,X8.X])
    constraints_writer.writerow([C9.X,D9.X,E9.X,F9.X,G9.X,H9.X,I9.X,J9.X,K9.X,L9.X,M9.X,N9.X,O9.X,P9.X,Q9.X,R9.X,S9.X,T9.X,U9.X,V9.X,W9.X,X9.X])
    constraints_writer.writerow([C10.X,D10.X,E10.X,F10.X,G10.X,H10.X,I10.X,J10.X,K10.X,L10.X,M10.X,N10.X,O10.X,P10.X,Q10.X,R10.X,S10.X,T10.X,U10.X,V10.X,W10.X,X10.X])
    constraints_writer.writerow([C11.X,D11.X,E11.X,F11.X,G11.X,H11.X,I11.X,J11.X,K11.X,L11.X,M11.X,N11.X,O11.X,P11.X,Q11.X,R11.X,S11.X,T11.X,U11.X,V11.X,W11.X,X11.X])
    constraints_writer.writerow([C12.X,D12.X,E12.X,F12.X,G12.X,H12.X,I12.X,J12.X,K12.X,L12.X,M12.X,N12.X,O12.X,P12.X,Q12.X,R12.X,S12.X,T12.X,U12.X,V12.X,W12.X,X12.X])
    constraints_writer.writerow([C13.X,D13.X,E13.X,F13.X,G13.X,H13.X,I13.X,J13.X,K13.X,L13.X,M13.X,N13.X,O13.X,P13.X,Q13.X,R13.X,S13.X,T13.X,U13.X,V13.X,W13.X,X13.X])
    constraints_writer.writerow([C14.X,D14.X,E14.X,F14.X,G14.X,H14.X,I14.X,J14.X,K14.X,L14.X,M14.X,N14.X,O14.X,P14.X,Q14.X,R14.X,S14.X,T14.X,U14.X,V14.X,W14.X,X14.X])
    constraints_writer.writerow([C15.X,D15.X,E15.X,F15.X,G15.X,H15.X,I15.X,J15.X,K15.X,L15.X,M15.X,N15.X,O15.X,P15.X,Q15.X,R15.X,S15.X,T15.X,U15.X,V15.X,W15.X,X15.X])
    constraints_writer.writerow([C16.X,D16.X,E16.X,F16.X,G16.X,H16.X,I16.X,J16.X,K16.X,L16.X,M16.X,N16.X,O16.X,P16.X,Q16.X,R16.X,S16.X,T16.X,U16.X,V16.X,W16.X,X16.X])
    constraints_writer.writerow([C17.X,D17.X,E17.X,F17.X,G17.X,H17.X,I17.X,J17.X,K17.X,L17.X,M17.X,N17.X,O17.X,P17.X,Q17.X,R17.X,S17.X,T17.X,U17.X,V17.X,W17.X,X17.X])
    constraints_writer.writerow([C18.X,D18.X,E18.X,F18.X,G18.X,H18.X,I18.X,J18.X,K18.X,L18.X,M18.X,N18.X,O18.X,P18.X,Q18.X,R18.X,S18.X,T18.X,U18.X,V18.X,W18.X,X18.X])
    constraints_writer.writerow([C19.X,D19.X,E19.X,F19.X,G19.X,H19.X,I19.X,J19.X,K19.X,L19.X,M19.X,N19.X,O19.X,P19.X,Q19.X,R19.X,S19.X,T19.X,U19.X,V19.X,W19.X,X19.X])
    constraints_writer.writerow([C20.X,D20.X,E20.X,F20.X,G20.X,H20.X,I20.X,J20.X,K20.X,L20.X,M20.X,N20.X,O20.X,P20.X,Q20.X,R20.X,S20.X,T20.X,U20.X,V20.X,W20.X,X20.X])
    constraints_writer.writerow([C21.X,D21.X,E21.X,F21.X,G21.X,H21.X,I21.X,J21.X,K21.X,L21.X,M21.X,N21.X,O21.X,P21.X,Q21.X,R21.X,S21.X,T21.X,U21.X,V21.X,W21.X,X21.X])
    constraints_writer.writerow([C22.X,D22.X,E22.X,F22.X,G22.X,H22.X,I22.X,J22.X,K22.X,L22.X,M22.X,N22.X,O22.X,P22.X,Q22.X,R22.X,S22.X,T22.X,U22.X,V22.X,W22.X,X22.X])
    constraints_writer.writerow([C23.X,D23.X,E23.X,F23.X,G23.X,H23.X,I23.X,J23.X,K23.X,L23.X,M23.X,N23.X,O23.X,P23.X,Q23.X,R23.X,S23.X,T23.X,U23.X,V23.X,W23.X,X23.X])
    constraints_writer.writerow([C24.X,D24.X,E24.X,F24.X,G24.X,H24.X,I24.X,J24.X,K24.X,L24.X,M24.X,N24.X,O24.X,P24.X,Q24.X,R24.X,S24.X,T24.X,U24.X,V24.X,W24.X,X24.X])
    constraints_writer.writerow([C25.X,D25.X,E25.X,F25.X,G25.X,H25.X,I25.X,J25.X,K25.X,L25.X,M25.X,N25.X,O25.X,P25.X,Q25.X,R25.X,S25.X,T25.X,U25.X,V25.X,W25.X,X25.X])
    # constraints_writer.writerow([C26.X,D26.X,E26.X,F26.X,G26.X,H26.X,I26.X,J26.X,K26.X,L26.X,M26.X,N26.X,O26.X,P26.X,Q26.X,R26.X,S26.X,T26.X,U26.X,V26.X,W26.X,X26.X])
    constraints_writer.writerow([C27.X,D27.X,E27.X,F27.X,G27.X,H27.X,I27.X,J27.X,K27.X,L27.X,M27.X,N27.X,O27.X,P27.X,Q27.X,R27.X,S27.X,T27.X,U27.X,V27.X,W27.X,X27.X])
    constraints_writer.writerow([])
    constraints_writer.writerow([Sensor12.X,Sensor10.X,Sensor9.X,Sensor8.X,Sensor7.X,Sensor6.X,Sensor5.X,Sensor21.X,Sensor20.X,Sensor19.X,Sensor25.X,Sensor24.X,Sensor11.X])
