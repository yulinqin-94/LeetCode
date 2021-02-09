class Solution:
    def longestPalindrome(self, s: str) -> str:
		max_list = []
		# 1 center
		for i in range(len(L)):
			r = 0
			while r <= min(abs(i-0),abs(len(L)-1-i)):
				temp_list = L[i-r:i+r+1]
				if L[i-r] == L[i+r]:
					if len(temp_list) > len(max_list):
						max_list = temp_list
					r += 1
				else:
					break
		# 2 centers
		for i in range(len(L)-1):
			if L[i] == L[i+1]:
				r = 0
				while r <= min(abs(i-0),abs(len(L)-1-(i+1))):
					temp_list = L[i-r:i+r+2]
					if L[i-r] == L[i+r+1]:
						if len(temp_list) > len(max_list):
							max_list = temp_list
						r += 1
					else:
						break
		return max_list