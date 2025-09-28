import re

def conversionToDecimalSystem(a,c):
	numberInDecimalSystem = 0
	if c == '10':
		numberInDecimalSystem = int(a)
	
	elif c.lower() == "фиб":
		fibs = [1, 2]
		for i in range(2, len(a) + 1):
			fibs.append(fibs[i-1] + fibs[i-2])
		for i, ch in enumerate(a[::-1]):
			if ch == '1':
				numberInDecimalSystem += fibs[i]
			elif ch == '0':
				pass
			else:
				print(f"Error: Invalid Symbol: '{ch}'")
				exit()

	elif re.fullmatch(r"[0-9]+С", c):
		s = a[::-1]
		base = int(c.replace("С", ''))
		if abs(int(max(a.replace('{', '').replace('}', '').replace('^', ''), key = lambda x: int(x)))) <= base//2:
			st = 0
			i = 0
			while i < len(s):
				if s[i] == '}':
					i += 1
					numberInDecimalSystem -= (int(s[i]) * base ** st)
					st += 1
					i += 3
				elif s[i].isdigit():
					numberInDecimalSystem += (int(s[i]) * base ** st)
					i += 1
					st += 1
				else:
					print(f"Error: Invalid Symbol '{s[i]}'")
					exit()
		else:
			print("Error: Incorrect comp system")
			exit()

	elif re.fullmatch(r"-[0-9]+", c):
		base = int(c)
		if int(max(a, key = lambda x: int(x))) <= base // 2:
			for i, ch in enumerate(a[::-1]):
				if not ch.isdigit():
					print(f"Invalid Symbol: '{ch}'")
					exit()
				numberInDecimalSystem += int(ch) * (base ** i)
		else:
			print("Error: Incorrect comp system")
			exit()

	elif re.fullmatch(r"[0-9]+", c):
		if int(max(a, key = lambda x: int(x))) <= int(c) // 2:
			numberInDecimalSystem = int(a, int(c))
		else:
			print("Error: Incorrect comp system")
			exit()

	else:
		print(f"Error: Something went wrong")
		exit()

	return numberInDecimalSystem


def conversionFromDecimalToDifferentSystem(a, b):
	answer = ''
	if b == '10':
		return str(a)
	
	elif b.lower() == "фиб":
		fibAr=[1, 2]
		x = 2
		while x <= a:
			fibAr.append(x)
			x = fibAr[-2] + fibAr[-1]
		
		for i in range(len(fibAr) - 1, -1, -1):
			if a >= fibAr[i] :
				answer += '1'
				a -= fibAr[i]
			else:
				answer += '0'
		return answer.lstrip("0") or "0"
		
	
	elif re.fullmatch(r"[0-9]+С", b):
		base = int(b.replace('С', ''))
		x = a
		while x != 0:
			r = x % base
			x //= base
			if r > base // 2:
				r -= base
				x += 1
			if r < 0:
				answer = "{^" + str(abs(r)) + '}' + answer
			else:
				answer = str(r) + answer
		return answer or "0"
	
	elif re.fullmatch(r"-[0-9]+", b):
		base = int(b)
		x = a
		while x != 0:
			x, r = divmod(x, base)
			if r < 0:
				r += abs(base)
				x += 1
			answer = str(r) + answer
		return answer or "0"
	
	elif re.fullmatch(r"[0-9]+", b):
		base = int(b)
		x = int(a)
		fl = False
		if x < 0:
			x = -x
			fl = True
		while x != 0:
			x, r = divmod(x, base)
			answer += str(r)
		if fl:
			return '-' + answer[::-1] or "0"
		else:
			return answer[::-1] or "0"

def convert(a, b, c):
	dec = conversionToDecimalSystem(a, c)
	return conversionFromDecimalToDifferentSystem(dec, b)

if __name__ == "__main__":
	print("Program works correct only with systems with base less than 11")
	a, b, c = input("Enter the numbers A B C that correspond to the problem statement:").split()
	print(convert(a, b, c))