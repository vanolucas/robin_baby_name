"""
Devinette :
1. Il y a une lettre en commun avec le prénom Robin 
2. Il y a une lettre qu'on n'entend pas 
3. Il y a 3 lettres en commun avec le prénom Floriane
4. Il y a une lettre qui vaut 10 points au Scrabble: K,W,X,Y,Z
5. Il y a le son de "salut" dans une autre langue
BONUS. Ça ressemble à ETHAN.
"""

from unidecode import unidecode as remove_accents
import csv

def count_occurences(str, letters):
	"""Count occurences of provided letters in a string.
	Returns a dict of letters that have at least one occurence in `str`.
	"""
	return {letter: str.count(letter) for letter in letters if str.count(letter) > 0}

# condition 1
def has_strictly_one_letter_in_common_with_robin(name):
	return sum(count_occurences(name, 'ROBIN').values()) == 1

def has_one_letter_in_common_with_robin(name):
	letter_occurences = count_occurences(name, 'ROBIN')
	return sum(letter_occurences.values()) == 1 or len(letter_occurences.keys()) == 1

# condition 2
def has_mute_letter(name):
	excluded = [
		"LIAM", "EDEN", "ISAAC", "AYDEN", "NAËL", "MALO", "EVAN", "MAXIME", "ISMAËL", "CHARLY", "KAYDEN", "MYLAN", "AYMEN", "FÉLIX", "OCTAVE", "ILYAS", "JAYDEN", "MATTEO", 
		"KAMIL", "ELYO", "ANGE", "DYLAN", "ÉMILE", "ISMAÏL", "EZRA", "NAÏL", "ALOÏS", "MALIK", "LEO", "AÏDEN", "LEWIS", "SALIM", "ALIX", "EDGAR", "TYLER", "LENY", "SELIM", 
		"MAXENCE", "WILLIAM", "AYLAN", "MATEO", "CESAR", "MYLANN", "ISMAIL", "SOLAL", "PAOLO", "CAYDEN", "YASSER", "YLAN", "YOUCEF", "ALAN", "JADEN", "WALID", 
		"GAETAN", "KAYLAN", "MAYLAN", "ISLEM", "KARL", "ADIL", "PACOME", "WAIL", "AKSIL", "LOUKAS", "EWAN", "MELVYN", "JULYAN", "DARYL", "ILYAM", "MIKAIL", "YLIAM",
		"", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
	]
	return not name in excluded

# condition 3
def has_strictly_three_letters_in_common_with_floriane(name):
	occurences = count_occurences(name, 'FLORIANE')
	return sum(occurences.values()) == 3 and max(occurences.values()) == 1

def has_three_letters_in_common_with_floriane(name):
	occurences = count_occurences(name, 'FLORIANE')
	return (sum(occurences.values()) == 3 and max(occurences.values()) == 1) or len(occurences.keys()) == 3

# condition 4
def has_a_scrabble_10pts_letter(name):
	scrabble_10pts_letters = ['K', 'W', 'X', 'Y', 'Z']
	for letter in scrabble_10pts_letters:
		if letter in name:
			return True
	return False

# load names
with open('names.csv') as f:
	reader = csv.reader(f, delimiter=';')
	names = {remove_accents(row[0]): int(row[1]) for row in reader}

# count all possible boy names
possible = names.keys()
print("{} boy names in 2020".format(len(possible)))

# filter based on condition 1
# possible = list(filter(lambda name: has_strictly_one_letter_in_common_with_robin(name), possible))
possible = list(filter(lambda name: has_one_letter_in_common_with_robin(name), possible))
print("{} after condition 1".format(len(possible)))

# filter based on condition 2
possible = [name for name in possible if has_mute_letter(name)]
print("{} after condition 2".format(len(possible)))

# filter based on condition 3
# possible = list(filter(lambda name: has_strictly_three_letters_in_common_with_floriane(name), possible))
possible = list(filter(lambda name: has_three_letters_in_common_with_floriane(name), possible))
print("{} after condition 3".format(len(possible)))

# filter based on condition 4
possible = list(filter(lambda name: has_a_scrabble_10pts_letter(name), possible))
print("{} after condition 4".format(len(possible)))

# filter out unlikely options
excluded = [
	"MOHAMED", "YOUSSEF", "ABEL", "ILYES", "ALI", "CALEB", "HAYDEN", "LOUKA", "MOHAMMED", "JEAN", "KHALIL", "MOUHAMED", "PHILIPPE", "SOUHAYL"
]
possible = [name for name in possible if name not in excluded and names[name] > 10]

# sort based on popularity
possible = {name: names[name] for name in possible}
possible = dict(sorted(possible.items(), key=lambda item: item[1], reverse=True))

print(possible)

"""
Output:
364 after condition 4
{'LOUAY': 91, 'YLANN': 89, 'NAHYL': 82, 'AYMANE': 63, 'EDWARD': 62, 'MALICK': 61, 'MAYLANN': 59, 'KHALID': 54, 'SOUHEYL': 51, 'LIYAM': 50, 'WASSIL': 49, 'AUXENCE': 48, 'DWAYNE': 46, 'LAYAN': 46, 'EZECHIEL': 44, 'YLLAN': 44, 'KHALIS': 43, 'ILYASS': 42, 'LAYANN': 42, 'WAYNE': 42, 'JULYANN': 41, 'ILYESS': 39, 'KELYO': 39, 'MYLHAN': 39, 'AWEN': 37, 'DJAYDEN': 36, 'AYANE': 34, 'THELYO': 34, 'AYDENN': 31, 'ZAVEN': 31, 'LYWEN': 30, 'TAYLAN': 30, 'EYTHAN': 29, 'MAYDEN': 28, 'AYLANN': 26, 'EZEKIEL': 26, 'ELYOTT': 25, 'KAIL': 25, 'KENAN': 25, 'LYAN': 25, 'TYLAN': 25, 'KEZIAH': 24, 'LYVANN': 24, 'JAYLAN': 23, 'MAZEN': 23, 'SULLYVAN': 23, 'KALVYN': 22, 'NYLAN': 21, 'ZAYDEN': 21, 'AKIL': 20, 'LOUCKA': 20, 'TAREK': 20, 'TELYO': 20, 'AZER': 19, 'MAYLO': 19, 'WYLAN': 19, 'YOUSEF': 19, 'NAYDEN': 18, 'YOSSEF': 18, 'CLARK': 17, 'LOUEY': 17, 'EYTAN': 16, 'KENSLEY': 16, 'LENNY': 16, 'MAKSEN': 16, 'MIKEL': 16, 'YAZEN': 16, 'AKIF': 15, 'DJULYAN': 15, 'ELYOT': 15, 'HYLAN': 15, 'KALIL': 15, 'KAYDENN': 15, 'KELVYN': 15, 'KEYAN': 15, 'LAZAR': 15, 'LOAY': 15, 'MAXANCE': 15, 'SHAYNE': 15, 'AYWEN': 14, 'DJULYANN': 14, 'KYLIAM': 14, 'MAXENS': 14, 'MELIK': 14, 'SAWYER': 14, 'ZAYANE': 14, 'DANYL': 13, 'EYDAN': 13, 'HAYDER': 13, 'KEENAN': 13, 'LYVAN': 13, 'MAYWEN': 13, 'WILLEM': 13, 'YLIAS': 13, 'BELKACEM': 12, 'CEZAR': 12, 'DAYEN': 12, 'ELWEN': 12, 'EWANN': 12, 'JAYLANN': 12, 'JEFFREY': 12, 'KAYLANN': 12, 'MAREK': 12, 'MIKHAIL': 12, 'NAYL': 12, 'PRESLEY': 12, 'WAKIL': 12, 'WILLIAMS': 12, 'ALVYN': 11, 'DAYVEN': 11, 'DENZEL': 11, 'KADER': 11, 'KEYVAN': 11, 'LASZLO': 11, 'LUKEN': 11, 'MAHREZ': 11, 'MOULAY': 11, 'SOHEYL': 11, 'THYLAN': 11, 'TYLIAM': 11, 'WILLYAM': 11}

Possible :
LIYAM
LAYAN
AYLANN
EYTAN
WILLYAM
"""