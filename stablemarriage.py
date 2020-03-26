#-----------------------------------------------------------------------------------------------------------------------
#STABLE MARRIAGE PROBLEM	
#-----------------------------------------------------------------------------------------------------------------------
"""
n men and women given. each man and woman has preferences. Must match each man with exactly 1 woman such that there is no 
blocking pair(there exists a pair of man and woman who both prefer each other more than the matching already present)
each man is matched with exactly 1 woman, and each woman with exactly 1 man, thus forming a bipartite graph. 

ALGORITHM:
1. Initialy all men and women are free
2. While there is still a free man
	2.1 choose a woman who is next on the man's prference list
	2.2 if the woman is not matched yet, then she accepts the proposal
	2.3 else if the woman already is matched
		2.3.1 if the woman likes the guy who has just proposed better than the guy she is already matched with, she accepts
		2.3.4 else she rejects
3. return the matched pairs

"""

#returns the index of the first freeman found, returns -1 if no freemen
def freeman(n,fmatch):
	men=[-1 for x in range(n)]
	for x in range(n):
		if fmatch[x]!=-1:
			men[fmatch[x]]=1
	for x in range(n):
		if men[x]==-1:
			return x
	return -1

def stablematching(n):
	mnames={}	#stores the names of the men with the index as key and name as value
	fnames={}	#stores the names of the women with the index as key and name as value

	ranking=[[[0,0] for i in range(n)] for j in range(n)]	#ranking matrix which contains mens as the rows, women as the columns, and each cell contains male preference,female preference

	names=input("Enter the names of the men: ").split()
	for i in range(n):
	    keys = i 
	    values = names[i] 
	    mnames[keys] = values

	names=input("Enter the names of the women: ").split()
	for i in range(n):
	    keys = i 
	    values = names[i] 
	    fnames[keys] = values
	print(mnames,fnames)

	#to find out the men rankings in the ranking matrix
	key_list = list(fnames.keys()) 
	val_list = list(fnames.values()) 
	for i in range(n):
		names=input("Enter the names of the women in order of preference for "+mnames[i]+": ").split()
		for j in range(n):
			ranking[i][key_list[val_list.index(names[j])]][0]=j+1

	#to find out the women rankings in the ranking matrix
	key_list = list(mnames.keys()) 
	val_list = list(mnames.values()) 
	for i in range(n):
		names=input("Enter the names of the men in order of preference for "+fnames[i]+": ").split()
		for j in range(n):
			ranking[key_list[val_list.index(names[j])]][i][1]=j+1

	#displays the ranking matrix
	print("\n")
	print("    ",list(fnames.values()))
	for i in range(n):
		print(list(mnames.values())[i],ranking[i])

	#fmatch[i]=j denotes woman i is matched with man j
	fmatch=[-1 for i in range(n)]

	while freeman(n,fmatch)!=-1:	#while there is still a free man
		i=freeman(n,fmatch)	#index of the free man
		found=0	
		pref=1	#stores the man's preference
		while found==0:	#while woman still not found for the man
			for j in range(n):	#find the index of the woman who is the pref preference of man i
				if ranking[i][j][0]==pref:	
					fpref=ranking[i][j][1]	#finds the preference of the woman for that man
					break
			if fmatch[j]==-1:	#woman has no match
				fmatch[j]=i
				found=1
			else:	#woman has match
				#check if main i is of greater preference to woman j than the existing man
				if fpref<ranking[fmatch[j]][j][1]:
					found=1
					fmatch[j]=i
			pref+=1

	print("\nStable match is: \n")
	for i in range(n):
		print(fnames[i],mnames[fmatch[i]])


def main():
	n=int(input("Enter the value of n: "))
	stablematching(n)

main()