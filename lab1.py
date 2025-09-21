import re

def conversionToDecimalSystem(a,c):
	numberInDecimalSystem = 0
	if c == '10':
		numberInDecimalSystem = int(a)

	elif c == "Фиб":
		fibs = [1, 2]
		for i in range(2, len(a) + 1):
			fibs.append(fibs[i-1] + fibs[i-2])
		for i, ch in enumerate(reversed(a)):
			if ch == '1':
				numberInDecimalSystem += fibs[i]
			elif ch == '0':
				pass
			else:
				raise ValueError(f"Invalid Symbol: '{ch}'")

	elif re.fullmatch(r"[0-9]+С", c):
		s = a[::-1]
		base = int(c.replace("С", ''))
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
				raise ValueError(f"Invalid Symbol '{s[i]}'")

	elif re.fullmatch(r"-[0-9]+", c):
		base = int(c)
		for i, ch in enumerate(reversed(a)):
			if not ch.isdigit():
				raise ValueError(f"Invalid Symbol: '{ch}'")
			numberInDecimalSystem += int(ch) * (base ** i)

	elif re.fullmatch(r"[0-9]+", c):
		numberInDecimalSystem = int(a, int(c))

	else:
		raise ValueError(f"Произошла какая-то ошибка")

	return numberInDecimalSystem


def conversionFromDecimalToDifferentSystem(a, b):
	answer = ''

	if b == '10':
		return str(a)
	
	elif b == "Фиб":
		fibAr=[1, 2]
		x = 2
		while x <= a:
			fibAr.append(x)
			x = fibAr[-2] + fibAr[-1]
		
		for i in range(len(fibAr) - 1, -1, -1):
			if a >= fibAr[i] :
				answer += '1'
				a -= fibAr
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
			if r == -1:
				answer = "{^1}" + answer
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
		while x != 0:
			x, r = divmod(x, base)
			answer += str(r)
		return reversed(answer) or "0"

def convert(a, b, c):
	dec = conversionToDecimalSystem(a, c)
	return conversionFromDecimalToDifferentSystem(dec, b)

if __name__ == "__main__":
	print("Program works correct only with systems with base less than 11")
	a, b, c = input("Enter the numbers A B C that correspond to the problem statement:").split()
	print(convert(a, b, c))