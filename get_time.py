import re

def main(num):
	fh = open('source.txt')
	for line in fh:
		match = re.search(r't-\d+', line)
		if match:
			r = match.group()
			r = r[2:-3]
			print(r)
			r = int(r) + num
			r = str(r)
			#print(line.replace(match.group(), 'id="###'), end="")
			out = line.replace(match.group(), r)
			f.write(out)
f = open('text.txt', 'w')			
main(12)
f.close()