# -*- coding: utf-8 -*-
import time
from functools import wraps
def timing(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		time1 = time.time()
		ret = f(*args, **kwargs)
		time2 = time.time()
		print('************************************************<fun: {0}>;[cost: {1} ms]'.format(f.__name__, (time2 - time1) * 1000.0))
		return ret
	return wrap

import pydawg

# words = [u'foo', u'bar', u'baz', u'qux', u'quux', u'corge', u'grault', u'garply', u'waldo', u'fred', u'plugh', u'xyzzy',
# 		 u'thud',
#          ]
# words.sort()
words = [x.strip().lower() for x in open('file_one_word_in_one_line')]
words.sort()

d = pydawg.PyDawg()
for word in words:
	d.insert(word)
d.finish()

@timing
def run(test_word):
	results = d.fuzzy_search(test_word, 3)
	return results

for test_word in ["周解伦", "周杰轮"]:
	results = run(test_word)
	for result in results:
		print(result.word.decode("utf-8"))


