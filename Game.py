class Monster:
	defaultMaxHealth = 30
	defaultLevel = 3
	defaultPowerPoints = 13

	def __init__(self, species, maxHealth = defaultMaxHealth, level = defaultLevel, powerPoints = defaultPowerPoints):
		self.species = species
		self.maxHealth = maxHealth
		self.currentHealth = maxHealth
		self.level = level
		self.powerPoints = powerPoints
		self.attacks = {
			"Scratch" : ("obj", -5),
		    "Tackle"  : ("obj", -2),
		    "Heal"    : ("subj", 8)
		}

	def changeHealth(self, amount):
		self.currentHealth += amount
		if self.currentHealth > self.maxHealth:
			self.currentHealth = self.maxHealth
		elif self.currentHealth < 0:
			self.currentHealth = 0
		else:
			pass

	def changePowerPoints(self, amount):
		self.powerPoints += amount

	def levelUp(self):
		self.level += 1

	def attack(self, enemy, attackName):
		if self.attacks[attackName][0] == "subj":
			self.changeHealth(self.attacks[attackName][1])
		else:
			enemy.changeHealth(self.attacks[attackName][1])






monster = Monster("Phantoptera")
enemy = Monster("Potguana")

game = True

while (game == True):

	selectedAttack = input("Enter your attack: ")
	monster.attack(enemy, selectedAttack)
	print(f"{monster.species} used {selectedAttack}!")
	print(f"{enemy.species}'s health fell to {enemy.currentHealth}.\n")

	if monster.currentHealth == 0 or enemy.currentHealth == 0:
		break

	selectedAttack = input("Enter your attack: ")
	enemy.attack(monster, selectedAttack)
	print(f"{enemy.species} used {selectedAttack}!")
	print(f"{monster.species}'s health fell to {monster.currentHealth}.\n")

	if monster.currentHealth == 0 or enemy.currentHealth == 0:
		break

print("Game has ended.")
