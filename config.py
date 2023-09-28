import pygame

PLAYERNAME = "Tesla"
PLAYERLEVEL = 10
WIDTH = 600
HEIGHT = 400

minSwipe = 50
maxClick = 15
longPressTime = 200
touchScale = 1
invertPosition = False
GPIO_AVAILABLE = True
RADIO_PLAYING = True
QUICKLOAD = True
LOAD_CACHED_MAP = False
# Main

TINTCOLOUR = pygame.Color(26, 255, 128) # Green
# TINTCOLOUR = pygame.Color (46, 207, 255) # Blue
# TINTCOLOUR = pygame.Color (255, 182, 66) # Amber
# TINTCOLOUR = pygame.Color (192, 255, 255) # White


#MAP_FOCUS = (-5.9347681, 54.5889076)
#MAP_FOCUS = (-102.3016145, 21.8841274) #Old Default?
#MAP_FOCUS = (-118.5723894,34.3917171)#CodeNinjasValencia
#MAP_FOCUS = (32.7157, 117.1611)
MAP_FOCUS = (-87.9063582, 43.1462029)

WORLD_MAP_FOCUS = 0.07 #Needed to handle the 50k node limit from OSM

LOAD_CACHED_MAP = False
SOUND_ENABLED = True

EVENTS = {
    'SONG_END': pygame.USEREVENT + 1
}

MODULES = {
    0: "stats",
    1: "items",
    2: "data"
}

ACTIONS = {
    pygame.K_F1: "module_stats",
    pygame.K_F2: "module_items",
    pygame.K_F3: "module_data",
    pygame.K_1:	"knob_1",
    pygame.K_2: "knob_2",
    pygame.K_3: "knob_3",
    pygame.K_4: "knob_4",
    pygame.K_5: "knob_5",
    pygame.K_UP: "dial_up",
    pygame.K_DOWN: "dial_down",
    pygame.K_PLUS: "zoom_in",
    pygame.K_MINUS: "zoom_out",
    pygame.K_KP_PLUS: "zoom_in",
    pygame.K_KP_MINUS: "zoom_out"
}

# Using GPIO.BCM as mode
#GPIO 23 pin16 reboot
#GPIO 25 pin 22 blank screen do not use
GPIO_ACTIONS = {
	15: "dial_down", #GPIO 23
	14: "dial_up", #GPIO 24
	20: "knob_down", #GPIO 4
	16: "knob_up", #GPIO 17
}

# LEDs
# pin 18, 23, 24,

MAP_ICONS = {
    "camp": 		pygame.image.load('images/map_icons/camp.png'),
    "factory": 		pygame.image.load('images/map_icons/factory.png'),
    "metro": 		pygame.image.load('images/map_icons/metro.png'),
    "misc": 		pygame.image.load('images/map_icons/misc.png'),
    "monument": 	pygame.image.load('images/map_icons/monument.png'),
    "vault": 		pygame.image.load('images/map_icons/vault.png'),
    "settlement": 	pygame.image.load('images/map_icons/settlement.png'),
    "ruin": 		pygame.image.load('images/map_icons/ruin.png'),
    "cave": 		pygame.image.load('images/map_icons/cave.png'),
    "landmark": 	pygame.image.load('images/map_icons/landmark.png'),
    "city": 		pygame.image.load('images/map_icons/city.png'),
    "office": 		pygame.image.load('images/map_icons/office.png'),
    "sewer": 		pygame.image.load('images/map_icons/sewer.png'),
}

AMENITIES = {
    'pub': 				MAP_ICONS['vault'],
    'nightclub': 		MAP_ICONS['vault'],
    'bar': 				MAP_ICONS['vault'],
    'fast_food': 		MAP_ICONS['settlement'],
	'cafe': 			MAP_ICONS['settlement'],
#	'drinking_water': 	MAP_ICONS['sewer'],
    'restaurant': 		MAP_ICONS['settlement'],
    'cinema': 			MAP_ICONS['office'],
    'pharmacy': 		MAP_ICONS['office'],
    'school': 			MAP_ICONS['office'],
    'bank': 			MAP_ICONS['monument'],
    'townhall': 		MAP_ICONS['monument'],
#	'bicycle_parking': 	MAP_ICONS['misc'],
#	'place_of_worship': MAP_ICONS['misc'],
	'theatre': 			MAP_ICONS['office'],
#	'bus_station': 		MAP_ICONS['misc'],
#	'parking': 			MAP_ICONS['misc'],
#	'fountain': 		MAP_ICONS['misc'],
#	'marketplace': 		MAP_ICONS['misc'],
#	'atm': 				MAP_ICONS['misc'],
    'misc':             MAP_ICONS['misc']
}

INVENTORY_OLD = [
"Ranger Sequoia",
"Anti-Materiel Rifle ",
"Deathclaw Gauntlet",
"Flamer",
"NCR dogtag",
".45-70 Gov't(20)",
".44 Magnum(20)",
"Pulse Grenade (2)"
]

WEAPONS = [
    "Water Pistol",
    "Lighter"
    ]

ARMOR = [
    "$ \blacksquare Vault 913 Jumpsuit $",
    " $ \blacksquare Nice Leather Boots"
    ]

AID = [
    "Purified Water (3)",
    "Rad Away (2)",
    "Stim Pack (2)"
]

MISC = [
    "Nuka Cola",
    "Pre-War Money (25)"
    ]

AMMO = [
    "Water Pistol Magazine"
    ]

QUESTS = [
    "Party!",
    "Drink Nuka Cola",
    "Open Gifts",
    "Thank Everyone For Coming"
]

SKILLS = [
    "Water Guns      (20)",
    "Athletics       (05)",
    "Hacking         (10)",
    "Lockpick        (10)"
    "Repair          (05)",
    "Science         (15)",
    "Survival        (10)",
    "Speach          (10)"   
]

PERKS = [
    "Action Boy",
    "Animal Friend",
    "Awareness",
    "Gunslinger"
    "Hacker",
    "Mysterious Stranger",
    "Rifleman",
    "Science"   
]


pygame.font.init()
FONTS = {}
for x in range(10, 28):
    FONTS[x] = pygame.font.Font('monofonto.ttf', x)


kernedFontName = 'fonts/monofonto-kerned.ttf'
monoFontName = 'fonts/monofonto.ttf'

# Scale font-sizes to chosen resolution:
FONT_SML = pygame.font.Font(kernedFontName, int (HEIGHT * (12.0 / 360)))
FONT_MED = pygame.font.Font(kernedFontName, int (HEIGHT * (16.0 / 360.0)))
FONT_LRG = pygame.font.Font(kernedFontName, int (HEIGHT * (18.0 / 360.0)))
MONOFONT = pygame.font.Font(monoFontName, int (HEIGHT * (16.0 / 360.0)))
# Find monofont's character-size:
tempImg = MONOFONT.render("X", True, TINTCOLOUR, (0, 0, 0))
charHeight = tempImg.get_height()
charWidth = tempImg.get_width()
del tempImg
