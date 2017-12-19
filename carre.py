 
indice = 10
#a = [[0]*indice]*indice
count_carre = 0
count_losange = 0
carre= []
losange= []

#def exist(pi,pj,pk,pl):
# for ic in carre.size:

indice = int(raw_input('entrez le nombre de points du quadriallage: '))
   

for i in range(0,indice):
 for j in range(0,indice):
   for k in range(0,indice):
     for l in range(0,indice):    
        cote1 = abs(i-j)
        cote2 = abs(k-l)
        if (j>i) and (l> k) and (cote1 == cote2) and (cote1 >0) and (cote2 > 0):
           #count of square
           count_carre=count_carre+1
           carre.append((i,j,k,l))
        else:
           if (j>i) and (k > l) and (cote1 >0) and (k+1 > cote1) and (k+1+cote1 <= indice) and (i+1-cote1 > 0): # removed (k == l)
            # count of losange
            count_losange=count_losange+1      
            losange.append((i,j,k,l))            

            
print "carre ", count_carre
print "losange ", count_losange
print "total ", count_carre+count_losange
