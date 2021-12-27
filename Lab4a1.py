import random as rand
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson
import numpy as np



class Dado:
    
    Faces=(1,2,3,4,5,6)

    def __init__(self,name):
        self.name=name



    def FairRoll(self,Faces):
        return rand.choice(Faces)



    
    
class Kniffel(Dado):


    

    param_labels=['l']
    N=1000
    Faces=(1,2,3,4,5,6)
    counter=1
    dado1=Dado("dado1")
    dado2=Dado("dado2")
    dado3=Dado("dado3")
    dado4=Dado("dado4")
    dado5=Dado("dado5")
    list=[]
    histo=[]
    flag=False
    check=[0,0,0,0,0,0]

    for i in range(N):
       
        while not flag:
            list.append(dado1.FairRoll(Faces))
            list.append(dado2.FairRoll(Faces))
            list.append(dado3.FairRoll(Faces))
            list.append(dado4.FairRoll(Faces))
            list.append(dado5.FairRoll(Faces))
            list.sort()
            
            if (check[0]==False and list.count(1)==list.count(2)==list.count(3)==list.count(4)==list.count(5)):
                check[0]=counter
                
            elif (check[1]==False and list.count(2)==list.count(3)==list.count(4)==list.count(5)==list.count(6)):
                check[1]=counter
                
            elif (check[2]==0 and list[0]==list[1]==list[2]==list[3]==list[4]):
                check[2]=counter
                
            elif (not check[3] and (list.count(1)==4 or list.count(2)==4 or list.count(3)==4 or list.count(4)==4 or list.count(5)==4 or list.count(6)==4)):
                check[3]=counter
                
            elif (check[4]==0 and list[0]==list[1]==list[2]):
                if(list[3]!=list[4] and list[3]!=list[2]):
                    check[4]=counter
                    
            elif(check[4]==0 and list[2]==list[3]==list[4]):
                if(list[0]!=list[1] and list[1]!=list[2]):
                    check[4]=counter
                        
            elif(check[4]==0 and list[1]==list[2]==list[3]):
                check[4]=counter
                        
            elif (check[5]==0 and list[0]==list[1]==list[2]):
                if(list[3]==list[4] and list[3]!=list[2]):
                    check[5]=counter
                    
            elif (check[5]==0 and list[2]==list[3]==list[4]):
                if(list[0]==list[1] and list[1]!=list[2]):
                    check[5]=counter
                

        
                
            if (all(check)!=False):
                flag=True

            list.clear()
            counter+=1

           

        print("Numero di lanci necessari per il tutto: {0}".format(counter-1))
        check=[0]*6
        histo.append(counter)
        counter=1
        flag=False
    
    d=np.array(histo)
    n,bins,patches=plt.hist(d,bins=len(set(histo)))
    plt.savefig("prova")
    plt.close()


    d=np.array(histo)
    bins=np.arange(10)-0.5
    n,bins,patches=plt.hist(d,bins=bins,density=True,label='data')
    for j in range(len(bins)-1):
        bin_middles=(0.5*(bins[j+1]+bins[j]))

    #bin_middles=0.5*(bins[1:]+bins[:-1])


    def fitfunc(k,lambd):
        #return poisson.pmf(k,lambd)
        #return (lambd**k/factorial(k))*np.exp(-lambd)
        return lambd*np.exp(-k*lambd)
    parameters,cov_matrix=curve_fit(fitfunc,bin_middles,n,maxfev=8000,p0=[0.001])

    x_plot=np.arange(0,600)
    plt.plot(x_plot,fitfunc(x_plot,*parameters),marker='o',linestyle='',label='Fit')
    plt.legend()
    plt.xlim(0,8000)
    plt.savefig("IstogrammaKNIFFEL2_0")  
    











                 
                            
        
       
        
        










   

    
    
