#Given two strings, write a method to decide if one is a permutation of the other.

#go through first string and create hashmap with counter for each character
	#"aba" - {a:2, b:1}
#go through second string and decrement the hashmap chracter accordingly
	#if character is not found in the hashmap or negative value detected, return false
#go through the updated hashmap, if any not zero detected return false
#return true

#Time complexity - O(N) - N is first string length
#Space complexity - O(N) - N is first string length

#Another idea is to sort both strings and then check if they are the same. TC is O(NlogN) but SC is O(1)

def Check_Permitation(str1, str2):
	print(str1, ";", str2)
	HM = {}
	for i in str1:
		curr = 0
		if(i in HM): 
			curr = HM[i]
		HM[i] = curr + 1
	print(HM)

	for i in str2:
		if i in HM:
			HM[i] -= 1
			if(HM[i]<0):
				return False
		else:
			return False
	print(HM)
	for i in HM:
		if(HM[i]>0):
			return False

	return True

print(Check_Permitation("abc", "abc"))	#True
print(Check_Permitation("abc", "ab"))	#False
print(Check_Permitation("ab", "abc"))	#False
print(Check_Permitation("abd", "abc"))	#False
print(Check_Permitation("aaa", "aaaa"))	#False
print(Check_Permitation("", ""))		#True

#if(i in HashMap): -> check if i key exists in the hashmap


