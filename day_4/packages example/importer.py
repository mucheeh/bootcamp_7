from A.classes import Animal, Poacher, Tourist
from A.functions import word_counts, sum_of_digits

#another way to import
import A.functions as func
# A.functions.sum_of_digits([10, 5])

import A.classes as clas

# import A.functions as f
# f.sum_of_digits([10, 5])

print Animal, word_counts
print clas.Animal,func.word_counts

# {
# 	'Animal': <class>,
# 	'Poacher': <class>,
# 	'Tourist': <class>,
# 	'word_counts': <func>,
# 	'sum_of_digits': <func>,
# 	'func':{
# 		'word_counts': <func>
# 		'sum_of_digits': <func>
# 	},
# 	'clas': {
# 		'Animal': <class>
# 		'Poacher': <class>
# 	},
# 	'x': 20
# }