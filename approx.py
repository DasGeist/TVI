#Aproximador de raizes com precisao arbitraria
#Implementado por Sergio Freitas da Silva Junior em 05/04/2019

import math
#import ipdb

def pol(a,v):
	va=0
	i=len(a)-1
	for coef in a:
		va=va+(coef*pow(v,i))
		i=i-1
	return va
def approx(a,prec,p,r):
	r1=p-r
	r2=p+r
	r3=p
	v1=pol(a,r1)
	v2=pol(a,r2)
	#ipdb.set_trace(context=10)
	prev1=v1
	prev2=v2
	state=0 #0-afasta 1-1 para direita 2-2 para esquerda
	while (v1*v2)>=0:
		print("Procurando pontos em setores diferentes. (Estado "+("<-|##|->" if state!=1 else "|->#|#")+"), pontos ["+str(round(r1,2))+","+str(round(r2,2))+"], valores ["+str(round(v1,2))+","+str(round(v2,2))+"]",end="\r")
		if v1==0:
			return r1
		if v2==0:
			return r2
		
		step=0.001
		if(state==0):
			if(((v1-prev1)*(v2-prev2))>0):
				state=1
		elif(state==1):
			if(r1>=r2):
				state=2
		r1=(r1-step) if state==0 else ((r1+step) if state==1 else r1-step)
		r2=(r2+step) if state==0 else ((r2+step) if state==2 else r2)
		prev1=v1
		prev2=v2
		v1=pol(a,r1)
		v2=pol(a,r2)
	print("Procurando pontos em setores diferentes. (Estado "+("<-|##|->" if state!=1 else "|->#|#")+"), pontos ["+str(round(r1,2))+","+str(round(r2,2))+"], valores ["+str(round(v1,2))+","+str(round(v2,2))+"] <--Encontrado")
	#O codigo abaixo e- a aproximacao em si
	while math.copysign(r1-r2,1)>prec:
		print("Aproximando pontos. Pontos ["+str(r1)+","+str(r2)+"], com valores ["+str(v1)+","+str(v2)+"]",end="\r")
		#ipdb.set_trace(context=10)
		r3=(r1+r2)/2
		v3=pol(a,r3)
		v1=pol(a,r1)
		v2=pol(a,r2)
		if(v3==0):
			return r3
		r1=r1 if ((v3*v1)<0) else r3
		r2=r2 if ((v3*v2)<0) else r3
	return r3

#Nessa linha, definimos os coeficientes (essa funcao e x^3-3x+3)
a=[1,0,-3,3]
#Nessa linha, procuramos uma raiz do polinomio a com precisao 10^-35 que esteja proxima ao intervalo [-2;1] (pode estar fora, mas comecamos a busca nele)
x=approx(a,1e-35,-2,1)
print("\nF("+str(x)+")="+str(pol(a,x))+".\r")
