from person import Person

# creating class Kenyan
class Kenyan(Person):
	corrupt = False
	# initialise brope to find out if kenyan is corrupt
	def probe(self, corrupt):
		self.corrupt = corrupt

	# initialise is_corrupt, if corrupt is yes print yes otherwise print no
	def is_corrupt(self):
		if self.corrupt:
			return "Yes"
		return "No" 

