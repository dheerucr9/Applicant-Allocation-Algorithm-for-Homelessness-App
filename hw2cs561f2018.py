class ApplicationID:
	def __init__(self,x):
		self.id = x[:5]
		self.gender = x[5]
		self.age = x[6:9]
		self.pets = x[9]
		self.medCond = x[10]
		self.car = x[11]
		self.license = x[12]
		self.availability = []
		d = {13:0,14:1,15:2,16:3,17:4,18:5,19:6}
		self.value = 0
		for i in range(13,20):
			if x[i] == "1":
				self.availability.append(d[i])
				self.value+=1
	def printAll(self):
		print("id" + self.id)
		print("gender" + self.gender)
		print("age" + self.age)
		print("pets" + self.pets)
		print("medical condition" + self.medCond)
		print("car" + self.car)
		print("license" + self.license)
		print(self.availability)

#def compatible(avail_list,applicant):
#print(sdlfk)
ip = open("/Users/dheeraj/Documents/2 SEM/AI/2nd Assignment/input2.txt","r")
numOfBeds = int(ip.readline())
numOfSpaces = int(ip.readline())
beds_avail_list = [numOfBeds] * 7
spaces_avail_list = [numOfSpaces] * 7
L = int(ip.readline())
LAppIDs = []
for i in range(L):
	LAppIDs.append(ip.readline().split()[0])
S = int(ip.readline())
SAppIDs = []
for i in range(S):
	SAppIDs.append(ip.readline().split()[0])
A = int(ip.readline())
AppIDs = []
for i in range(A):																	# AppIDs for list of application ids objects
	AppIDs.append(ApplicationID(ip.readline().split()[0]))
#for i in range(A):
#	AppIDs[i].printAll()
SPLA_list = []
LAHSA_list = []
for i in range(A):
	if AppIDs[i].gender == "F" and int(AppIDs[i].age) > 17 and AppIDs[i].pets == "N" and AppIDs[i].id not in LAppIDs and AppIDs[i].id not in SAppIDs:
		LAHSA_list.append(i)
	if AppIDs[i].car == "Y" and AppIDs[i].license == "Y" and AppIDs[i].medCond == "N" and AppIDs[i].id not in SAppIDs and AppIDs[i].id not in LAppIDs:
		SPLA_list.append(i)
	if AppIDs[i].id in LAppIDs:
		for j in range(7):
			if j in AppIDs[i].availability:
				beds_avail_list[j]-=1
	elif AppIDs[i].id in SAppIDs:
		for j in range(7):
			if j in AppIDs[i].availability:
				spaces_avail_list[j]-=1
#	AppIDs[i].printAll()
#print(beds_avail_list)
#print(spaces_avail_list)

diction1 = {}
diction2 = {}
def minimax(S_list, L_list, S_avail_list, L_avail_list, flag):
	print("YO")
	print(S_list)
	print(L_list)
	finalOp = []
	if flag:
		print("max")
		if str(S_list)+str(L_list) in diction1:
			return diction1[str(S_list)+str(L_list)]
		else:
			if len(S_list) == 0:
				print("return0: 0")

				return 0
			if len(L_list)!= 0:
				for s in S_list:
					print("----------------")
					s_index = S_list.index(s)
					print(S_list)
					print(str(s_index) + "th time")
					print("s: " + str(s))
					count = 0
					for i in range(7):
						if (i in AppIDs[s].availability) and (S_avail_list[i]-1)>=0:
							count+=1
					if count == AppIDs[s].value:
						print("gotin1")
						if s in L_list:
							l_index = L_list.index(s)
							for h in AppIDs[s].availability:
								S_avail_list[h]-=1
							S_list.remove(s)
							L_list.remove(s)
							finalOp.append(AppIDs[s].value + minimax(S_list,L_list,S_avail_list,L_avail_list,False))
							S_list.insert(s_index,s)
							L_list.insert(l_index,s)
							for h in AppIDs[s].availability:
								S_avail_list[h]+=1
						else:
							for h in AppIDs[s].availability:
								S_avail_list[h]-=1
							S_list.remove(s)
							finalOp.append(AppIDs[s].value + minimax(S_list,L_list,S_avail_list,L_avail_list,False))
							S_list.insert(s_index,s)
							for h in AppIDs[s].availability:
								S_avail_list[h]+=1
					else:
						print("no available spaces")
						return 0
				print("final op: " + str(finalOp))
				if (s_num == len(S_list)) and (l_num == len(L_list)):
					print("google")
					print(finalOp)
					print(S_list[finalOp.index(max(finalOp))])
					return S_list[finalOp.index(max(finalOp))]
				else:
					print("return1: " + str(max(finalOp)))
					max_finalOp = max(finalOp)
					diction1[str(S_list)+str(L_list)]=max_finalOp
					return max_finalOp
			else:																															# check if all q can be fit, if not add best ones that can fit
				sum = 0
				print(S_list)
				for q in S_list:
					sum+=AppIDs[q].value
					print("sum"+str(sum))
				print("return2: " + str(sum))
				diction1[str(S_list)+str(L_list)]=sum
				return sum


	else:
		print("min")
		if str(S_list)+str(L_list) in diction2:
			return diction2[str(S_list)+str(L_list)]
		else:
			if len(L_list) == 0:
				sum = 0
				for q in S_list:
					sum+=AppIDs[q].value
					print("sum"+str(sum))
				print("return3: " + str(sum))
				diction2[str(S_list)+str(L_list)]=sum
				return sum
			if len(S_list)!= 0:
				for l in L_list:
					l_index = L_list.index(l)
					count = 0
					print("l: " + str(l))
					for i in range(7):
						if (i in AppIDs[l].availability) and (L_avail_list[i]-1)>=0:
							count+=1
					#print(AppIDs[l].availability)
					#print(L_avail_list)
					print(str(count) + " "+ str(AppIDs[l].value))
					if count == AppIDs[l].value:
						print("gotin2")
						if l in S_list:
							s_index = S_list.index(l)
							for h in AppIDs[l].availability:
								L_avail_list[h]-=1
							S_list.remove(l)
							L_list.remove(l)
							finalOp.append(minimax(S_list,L_list,S_avail_list,L_avail_list,True))
							S_list.insert(s_index,l)
							L_list.insert(l_index,l)
							for h in AppIDs[l].availability:
								L_avail_list[h]+=1
						else:
							for h in AppIDs[l].availability:
								L_avail_list[h]-=1
							L_list.remove(l)
							finalOp.append(minimax(S_list,L_list,S_avail_list,L_avail_list,True))
							L_list.insert(l_index,l)
							for h in AppIDs[l].availability:
								L_avail_list[h]+=1
					else:
						print("no available spaces")
						return 0
				print("return4: " + str(min(finalOp)))
				diction2[str(S_list)+str(L_list)]=min(finalOp)
				return(min(finalOp))
			else:
				print("return5: 0")
				diction2[str(S_list)+str(L_list)]=0
				return 0


s_num = len(SPLA_list)
l_num = len(LAHSA_list)
'''print(numOfBeds)
print(numOfBeds)
print(L)
print(LAppIDs)
print(S)
print(SAppIDs)
print(A)
print(SPLA_list)
print(LAHSA_list)
print(beds_avail_list)
print(spaces_avail_list)'''
print(AppIDs[minimax(SPLA_list,LAHSA_list,spaces_avail_list,beds_avail_list,True)].id)
#op = open("output.txt","w")
#op.write(AppIDs[minimax(SPLA_list,LAHSA_list,spaces_avail_list,beds_avail_list,True)].id)
#print(diction)
