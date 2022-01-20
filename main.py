from datetime import date
import os

mysteries = {
	'joyful' : [
        'The Annunciation',
		'The Visitation',
		'The Nativity',
		'The Presentation',
		'The Finding in the Temple'
	],

	'sorrowful' : [
		'The Agony in the Garden',
		'The Scourging at Pillar',
		'The Crowning with Thorns',
		'The Carrying of the Cross',
		'The Crucifixion'
	],

	'glorious' : [
		'The Resurrection of Our Lord',
		'The Ascension of Our Lord',
		'The Descent of the Holy Ghost upon the Apostles',
		'The Assumption of the Blessed Virgin Mary into Heaven',
		'The Coronation of Our Lady as Queen of Heaven and Earth'
	],

	'luminous' : [
		'The Baptism of Jesus',
		'The Wedding of Cana',
		'The Proclamation of the Kingdom of God',
		'The Transfiguration',
		'The institution of the Eucharist'
	]
}

today = date.today().weekday()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def int_mystery():

    if (today == 0, 5) is True:
        return 'joyful'

    elif (today in (1, 4)) is True:
        return 'sorrowful'

    elif (today in (2, 6)) is True:
        return 'glorious'

    elif (today == 3) is True:
        return 'luminous'

MYSTERY = str(int_mystery())

def find_mystery():

    return mysteries.get(MYSTERY)


print(f'Today\'s mysteries are the {MYSTERY}')
print(find_mystery())
print('Version = Beta')

