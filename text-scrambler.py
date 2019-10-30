# To scramble words into human-readable but non machine-searchable texts.
# By Lily Ren

import sys
import os
import random
import optparse

parser = optparse.OptionParser()
parser.add_option('-s', '--step', dest="step",
	help="Size of substrings for randomization, default is 5", default="5")
options, args = parser.parse_args()

def main():
	if len(sys.argv) < 2:
		print('You have not entered enough arguments. Please specify path of the file you want scrambled.')
		sys.exit()
	filename = sys.argv[1]
	outname = '{0}-scrambled.txt'.format(os.path.splitext(filename)[0])
	if len(sys.argv) > 2:
		outname = '{0}'.format(sys.argv[2])

	print ('Scrambling words for {0}, output to file {1}\n'.format(filename, outname))
	scrambled = scramble(filename)

	# Write out to file
	f_out = open(outname, 'w+')
	f_out.write(scrambled)
	f_out.close()

def scramble(filename):
	scrambled = ''
	currentword = ''
	with open(filename, "r") as f:
		while True:
			c = f.read(1)
			if not c:
				break
			if c.isalpha():
				currentword += c
			else:
				if len(currentword) > 0:
					randomized = get_randomized_word(currentword)
					scrambled += randomized
				scrambled += c
				currentword = ''
	return scrambled

def get_randomized_word(word):
	step = int(options.step)
	wordlen = len(word)
	word_front = word[0]
	word_end = word[-1]
	final_rand_word = ''
	if wordlen == 1 or wordlen == 2: # special cases
		final_rand_word = word
	elif wordlen == 3: # special cases
		partialword = word[1:]
		rand_partialword = randomize_order(partialword)
		final_rand_word = word_front + rand_partialword
	else:
		rand_word = ''
		for idx in range(1, wordlen, step):
			partialword = ''
			if (idx + step) >= wordlen:
				partialword = word[idx:-1]
			else:
				partialword = word[idx:(idx + step)]
			rand_partialword = randomize_order(partialword)
			rand_word += rand_partialword
		final_rand_word = word_front + rand_word + word_end

	return final_rand_word

def randomize_order(midword):
	return ''.join(random.sample(midword,len(midword)))

if __name__== "__main__":
	main()