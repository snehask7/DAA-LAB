#STABLE MATCHING PROBLEM
#SNEHA SRIRAM KANNAN - 185001157
men={}
women={}

#TO GET THE INPUT IN THE SPECIFIED FORMAT FROM A FILE
def get_input():
  inputfile=open("input.txt")
  n=0
  for x in inputfile:
    if x.split()!=[]:
      men[x[0]]=[x.split()[1:],'',0]
      n+=1
    else:
      break
  n=0
  
  for x in inputfile:
    women[x[0]]=[x.split()[1:],'']
    n+=1
  
#TO DISPLAY THE MATCHING
def display():
  for x in men:
    print(x,":",men[x][1])
  print('\n')

def unstable(m,w):
  currentWomanPref=women[w][0].index(women[w][1])
  newWomanPref=women[w][0].index(m)
  if newWomanPref<currentWomanPref:
    return 1
  else:
    return 0
    
def propose(m):
  men[m][1]=men[m][0][men[m][2]]
  men[m][2]+=1

def undo_proposal(m):
  men[m][1]=''
  
def accept_proposal(m,w):
  women[w][1]=m

def reject_proposal(w):
  rejectedman=women[w][1]
  men[rejectedman][1]=''
  women[w][1]=''
  
def unmatched_man():
  for x in men:
    if men[x][1]=='':
      return x
  return 0
  

#GAYLE SHAPELEY ALGORITHM
def GAYLE_SHAPELEY():
  i=1
  while unmatched_man():
    m=unmatched_man()
    w=men[m][0][men[m][2]]  #PREFERRED WOMAN
    propose(m)
    if women[w][1]=='': #UNMATCHED WOMAN
      accept_proposal(m,w)
    else: #MATCHED WOMAN
      if unstable(m,w):
        reject_proposal(w)
        accept_proposal(m,w)
      else:
        undo_proposal(m)
    print('AFTER ITERATION ',i)
    i+=1
    display()
      

def main():
  get_input()
  GAYLE_SHAPELEY()
  print('FINAL MATCHING')
  display()
    
main()