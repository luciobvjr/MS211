a11 = float(input('Digite o valor da posição A11 = '))
a12 = float(input('Digite o valor da posição A12 = '))
a21 = float(input('Digite o valor da posição A21 = '))
a22 = float(input('Digite o valor da posição A22 = '))

b11 = float(input('Digite o valor da posição B11 = '))
b12 = float(input('Digite o valor da posição B12 = '))
b21 = float(input('Digite o valor da posição B21 = '))
b22 = float(input('Digite o valor da posição B22 = '))

c11 = float(input('Digite o valor da posição C11 = '))
c12 = float(input('Digite o valor da posição C12 = '))
c21 = float(input('Digite o valor da posição C21 = '))
c22 = float(input('Digite o valor da posição C22 = '))

AxB_11 = a11*b11 + a12*b21
AxB_12 = a11*b12 + a12*b22
AxB_21 = a21*b11 + a22*b21
AxB_22 = a21*b12 + a22*b22

R11 = AxB_11 + c11
R12 = AxB_12 + c12
R21 = AxB_21 + c21
R22 = AxB_22 + c22

R=[[],[]]
R[0].append(R11)
R[0].append(R12)
R[1].append(R21)
R[1].append(R22)

print('\n','A matriz que resulta da expressão A * B + C é:','\n',R[0],'\n',R[1])

#Passando para FP(10,3,-9,-9)

a11_FP = f'{a11:.3e}'
a11_FP = float(a11_FP)
a12_FP = f'{a12:.3e}'
a12_FP = float(a12_FP)
a21_FP = f'{a21:.3e}'
a21_FP = float(a21_FP)
a22_FP = f'{a22:.3e}'
a22_FP = float(a22_FP)

b11_FP = f'{b11:.3e}'
b11_FP = float(b11_FP)
b12_FP = f'{b12:.3e}'
b12_FP = float(b12_FP)
b21_FP = f'{b21:.3e}'
b21_FP = float(b21_FP)
b22_FP = f'{b22:.3e}'
b22_FP = float(b22_FP)

c11_FP = f'{c11:.3e}'
c11_FP = float(c11_FP)
c12_FP = f'{c12:.3e}'
c12_FP = float(c12_FP)
c21_FP = f'{c21:.3e}'
c21_FP = float(c21_FP)
c22_FP = f'{c22:.3e}'
c22_FP = float(c22_FP)

AxB_11_FP = f'{a11_FP*b11_FP + a12_FP*b21_FP:.3e}'
AxB_11_FP = float(AxB_11_FP)
AxB_12_FP = f'{a11_FP*b12_FP + a12_FP*b22_FP:.3e}'
AxB_12_FP = float(AxB_12_FP)
AxB_21_FP = f'{a21_FP*b11_FP + a22_FP*b21_FP:.3e}'
AxB_21_FP = float(AxB_21_FP)
AxB_22_FP = f'{a21_FP*b12_FP + a22_FP*b22_FP:.3e}'
AxB_22_FP = float(AxB_22_FP)

R11_FP = f'{AxB_11_FP + c11_FP:.3e}'
R12_FP = f'{AxB_12_FP + c12_FP:.3e}'
R21_FP = f'{AxB_21_FP + c21_FP:.3e}'
R22_FP = f'{AxB_22_FP + c22_FP:.3e}'

RFP = [[],[]]
RFP[0].append(R11_FP)
RFP[0].append(R12_FP)
RFP[1].append(R21_FP)
RFP[1].append(R22_FP)

print('\n','A representação da matriz resultante em FP(10,3,-9,-9) é:','\n',RFP[0],'\n',RFP[1])