#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import random


# Common 5-letter words for analysis
WORD_LIST = [
    "ABOUT", "ABOVE", "ABUSE", "ACTOR", "ACUTE", "ADMIT", "ADOPT", "ADULT", "AFTER", "AGAIN",
    "AGENT", "AGREE", "AHEAD", "ALARM", "ALBUM", "ALERT", "ALIEN", "ALIGN", "ALIKE", "ALIVE",
    "ALLOW", "ALONE", "ALONG", "ALTER", "ANGEL", "ANGER", "ANGLE", "ANGRY", "APART", "APPLY",
    "ARENA", "ARGUE", "ARISE", "ARRAY", "ARROW", "ASIDE", "ASSET", "AUDIO", "AUDIT", "AVOID",
    "AWAKE", "AWARD", "AWARE", "BADLY", "BAKER", "BALLS", "BANDS", "BASIC", "BEACH", "BEANS",
    "BEARD", "BEARS", "BEAST", "BEATS", "BEGAN", "BEGIN", "BEING", "BELOW", "BENCH", "BIKES",
    "BILLS", "BIRDS", "BIRTH", "BLACK", "BLADE", "BLAME", "BLANK", "BLAST", "BLIND", "BLOCK",
    "BLOOD", "BLOWN", "BLUES", "BOARD", "BOATS", "BONES", "BOOKS", "BOOST", "BOOTH", "BOOTS",
    "BOUND", "BOXES", "BRAIN", "BRAND", "BRASS", "BRAVE", "BREAD", "BREAK", "BREED", "BRICK",
    "BRIDE", "BRIEF", "BRING", "BROAD", "BROKE", "BROWN", "BRUSH", "BUILD", "BUILT", "BUNCH",
    "BUSES", "BUYER", "CABLE", "CAKES", "CALLS", "CAMEL", "CAMPS", "CARDS", "CARED", "CARGO",
    "CARRY", "CASES", "CATCH", "CAUSE", "CAVES", "CHAIN", "CHAIR", "CHAOS", "CHARM", "CHART",
    "CHASE", "CHEAP", "CHECK", "CHESS", "CHEST", "CHIEF", "CHILD", "CHIPS", "CHOSE", "CIVIL",
    "CLAIM", "CLAMS", "CLASS", "CLEAN", "CLEAR", "CLICK", "CLIMB", "CLOCK", "CLOSE", "CLOTH",
    "CLOUD", "CLUBS", "COACH", "COALS", "COAST", "COATS", "CODES", "COINS", "COLOR", "COMES",
    "COUCH", "COULD", "COUNT", "COURT", "COVER", "CRAFT", "CRANE", "CRASH", "CRAZY", "CREAM",
    "CREEK", "CRIME", "CROPS", "CROSS", "CROWD", "CROWN", "CRUDE", "CRUSH", "CURVE", "CYCLE",
    "DAILY", "DANCE", "DATED", "DEALS", "DEALT", "DEATH", "DEBUT", "DECKS", "DELAY", "DEPTH",
    "DESKS", "DIARY", "DICED", "DIETS", "DIRTY", "DISKS", "DOCKS", "DOING", "DOORS", "DOUBT",
    "DOUGH", "DOZEN", "DRAFT", "DRAMA", "DRANK", "DRAWN", "DREAM", "DRESS", "DRIED", "DRILL",
    "DRINK", "DRIVE", "DROVE", "DRUGS", "DRUMS", "DRUNK", "DUCKS", "DYING", "EAGER", "EARLY",
    "EARTH", "EATEN", "EDGES", "EIGHT", "ELBOW", "ELITE", "EMPTY", "ENEMY", "ENJOY", "ENTER",
    "ENTRY", "EQUAL", "ERROR", "EVENT", "EVERY", "EXACT", "EXAMS", "EXIST", "EXTRA", "FACED",
    "FACTS", "FAITH", "FALSE", "FANCY", "FARMS", "FATAL", "FAULT", "FEARS", "FENCE", "FERRY",
    "FIBER", "FIELD", "FIFTH", "FIFTY", "FIGHT", "FILES", "FINAL", "FINDS", "FINES", "FIRED",
    "FIRST", "FIXED", "FLAGS", "FLAME", "FLASH", "FLEET", "FLESH", "FLIES", "FLOOR", "FLOUR",
    "FLOWS", "FLUID", "FOCUS", "FOLKS", "FOODS", "FORCE", "FORMS", "FORTH", "FORTY", "FORUM",
    "FOUND", "FRAME", "FRAUD", "FRESH", "FRIED", "FRONT", "FROST", "FRUIT", "FULLY", "FUNNY",
    "GAMES", "GATES", "GHOST", "GIANT", "GIFTS", "GIRLS", "GIVEN", "GIVES", "GLASS", "GLOBE",
    "GLOVE", "GOALS", "GOATS", "GOING", "GOODS", "GRACE", "GRADE", "GRAIN", "GRAND", "GRANT",
    "GRAPE", "GRAPH", "GRASS", "GRAVE", "GREAT", "GREEN", "GRIND", "GROSS", "GROUP", "GROWN",
    "GUARD", "GUESS", "GUEST", "GUIDE", "GUILD", "HAPPY", "HARSH", "HATED", "HEART", "HEAVY",
    "HENCE", "HERBS", "HILLS", "HINTS", "HIRED", "HORSE", "HOTEL", "HOURS", "HOUSE", "HUMAN",
    "IDEAL", "IDEAS", "IMAGE", "INDEX", "INNER", "INPUT", "ISSUE", "ITEMS", "JEANS", "JEWEL",
    "JOKES", "JUICE", "JUMPS", "KEEPS", "KICKS", "KILLS", "KINDS", "KINGS", "KNEES", "KNIFE",
    "KNOTS", "KNOWN", "KNOWS", "LABEL", "LAKES", "LAMPS", "LANDS", "LARGE", "LASER", "LATER",
    "LAUGH", "LAYER", "LEADS", "LEARN", "LEASE", "LEAST", "LEAVE", "LEGAL", "LEVEL", "LIGHT",
    "LIKED", "LIKES", "LIMIT", "LINES", "LINKS", "LISTS", "LIVED", "LIVER", "LIVES", "LOANS",
    "LOCAL", "LOCKS", "LOOKS", "LOOSE", "LORDS", "LOSES", "LOVED", "LOVER", "LOVES", "LOWER",
    "LUCKY", "LUNCH", "LYING", "MAGIC", "MAJOR", "MAKER", "MAKES", "MARCH", "MARKS", "MATCH",
    "MAYBE", "MAYOR", "MEALS", "MEANS", "MEANT", "MEATS", "MEDAL", "MEDIA", "MEETS", "MELON",
    "MENUS", "MERCY", "METAL", "METER", "MIGHT", "MILES", "MINDS", "MINES", "MINOR", "MINUS",
    "MIXED", "MODEL", "MODES", "MONEY", "MONTH", "MORAL", "MOTOR", "MOUNT", "MOUSE", "MOUTH",
    "MOVED", "MOVES", "MOVIE", "MUSIC", "NAMES", "NASTY", "NEEDS", "NERVE", "NEVER", "NEWLY",
    "NIGHT", "NOISE", "NORTH", "NOTED", "NOTES", "NOVEL", "NURSE", "OCCUR", "OCEAN", "OFFER",
    "OFTEN", "OLDER", "OLIVE", "ONION", "ORDER", "OTHER", "OUGHT", "OWNED", "OWNER", "PAGES",
    "PAINS", "PAINT", "PAIRS", "PANEL", "PANIC", "PAPER", "PARKS", "PARTS", "PARTY", "PASTA",
    "PASTE", "PATCH", "PATHS", "PEACE", "PEAKS", "PEARL", "PENNY", "PHASE", "PHONE", "PHOTO",
    "PIANO", "PICKS", "PIECE", "PILES", "PILLS", "PILOT", "PIPES", "PITCH", "PIZZA", "PLACE",
    "PLAIN", "PLANE", "PLANT", "PLATE", "PLAYS", "PLOTS", "POEMS", "POINT", "POLES", "POOLS",
    "PORCH", "POUND", "POWER", "PRESS", "PRICE", "PRIDE", "PRIME", "PRINT", "PRIOR", "PRIZE",
    "PROOF", "PROUD", "PROVE", "PULLS", "PUMPS", "PUNCH", "PUPIL", "QUEEN", "QUEST", "QUICK",
    "QUIET", "QUITE", "QUOTE", "RADIO", "RAILS", "RAISE", "RANGE", "RAPID", "RATES", "RATIO",
    "REACH", "READS", "READY", "REALM", "REBEL", "REFER", "RELAX", "REMIX", "REPAY", "REPLY",
    "RIDER", "RIDES", "RIGHT", "RIGID", "RINGS", "RISKY", "RIVAL", "RIVER", "ROADS", "ROAST",
    "ROBOT", "ROCKS", "ROLES", "ROLLS", "ROOTS", "ROSES", "ROUGH", "ROUND", "ROUTE", "ROYAL",
    "RUGBY", "RULES", "RUINS", "RURAL", "SADLY", "SAFER", "SAILS", "SAINT", "SALAD", "SALES",
    "SANDY", "SAUCE", "SCALE", "SCARE", "SCENE", "SCOPE", "SCORE", "SCOTS", "SCRUB", "SEALS",
    "SEATS", "SEEDS", "SEEMS", "SELLS", "SENSE", "SERVE", "SETUP", "SEVEN", "SHADE", "SHAKE",
    "SHALL", "SHAME", "SHAPE", "SHARE", "SHARP", "SHEEP", "SHEET", "SHELF", "SHELL", "SHIFT",
    "SHINE", "SHIPS", "SHIRT", "SHOCK", "SHOES", "SHOOT", "SHOPS", "SHORT", "SHOTS", "SHOWN",
    "SHOWS", "SIDES", "SIGHT", "SIGNS", "SILLY", "SINCE", "SITES", "SIXTH", "SIXTY", "SIZED",
    "SIZES", "SKILL", "SLEEP", "SLICE", "SLIDE", "SLOPE", "SMALL", "SMART", "SMELL", "SMILE",
    "SMOKE", "SNAKE", "SNOWS", "SOAPS", "SOCKS", "SOLID", "SOLVE", "SONGS", "SORRY", "SORTS",
    "SOULS", "SOUND", "SOUTH", "SPACE", "SPARE", "SPEAK", "SPEED", "SPELL", "SPEND", "SPENT",
    "SPINE", "SPLIT", "SPOKE", "SPORT", "SPOTS", "SPRAY", "SQUAD", "STAFF", "STAGE", "STAKE",
    "STAMP", "STAND", "START", "STATE", "STAYS", "STEAM", "STEEL", "STEEP", "STEER", "STEPS",
    "STICK", "STILL", "STOCK", "STONE", "STOOD", "STORE", "STORM", "STORY", "STRIP", "STUCK",
    "STUDY", "STUFF", "STYLE", "SUGAR", "SUITE", "SUPER", "SWEET", "SWIFT", "SWING", "SWORN",
    "TABLE", "TAKEN", "TAKES", "TALKS", "TANKS", "TASTE", "TAXES", "TEACH", "TEAMS", "TEARS",
    "TEETH", "TELLS", "TERMS", "TESTS", "THANK", "THEFT", "THEIR", "THEME", "THERE", "THESE",
    "THICK", "THING", "THINK", "THIRD", "THOSE", "THREE", "THREW", "THROW", "THUMB", "TIDES",
    "TIGHT", "TILES", "TIMER", "TIMES", "TIRED", "TITLE", "TODAY", "TOAST", "TOKEN", "TOOLS",
    "TOOTH", "TOPIC", "TOTAL", "TOUCH", "TOUGH", "TOWER", "TOWNS", "TRACK", "TRADE", "TRAIL",
    "TRAIN", "TRASH", "TREAT", "TREES", "TREND", "TRIAL", "TRIBE", "TRICK", "TRIED", "TRIES",
    "TRIPS", "TRUCK", "TRULY", "TRUST", "TRUTH", "TUBES", "TURNS", "TWICE", "TWINS", "TYPED",
    "ULTRA", "UNCLE", "UNCUT", "UNDER", "UNION", "UNITE", "UNITY", "UNTIL", "UPPER", "UPSET",
    "URBAN", "URGED", "USAGE", "USERS", "USUAL", "VALID", "VALUE", "VAULT", "VIDEO", "VIEWS",
    "VIRUS", "VISIT", "VITAL", "VOCAL", "VOICE", "VOTES", "WAGES", "WALKS", "WALLS", "WANTS",
    "WASTE", "WATCH", "WATER", "WAVES", "WEEKS", "WEIRD", "WELLS", "WHALE", "WHEAT", "WHEEL",
    "WHERE", "WHICH", "WHILE", "WHITE", "WHOLE", "WHOSE", "WIDOW", "WIDTH", "WINDS", "WINES",
    "WINGS", "WIPED", "WIRED", "WIRES", "WOMAN", "WOMEN", "WOODS", "WORDS", "WORKS", "WORLD",
    "WORRY", "WORSE", "WORST", "WORTH", "WOULD", "WRITE", "WRONG", "WROTE", "YARDS", "YEARS",
    "YIELD", "YOUNG", "YOURS", "YOUTH", "ZONES", "ABBEY", "ABODE", "ACIDS", "ACORN", "ADDED",
    "AGING", "AIDED", "AIMED", "AIRED", "AISLE", "ALGAE", "ALIEN", "ALIVE", "ALPHA", "ALTAR",
    "AMBER", "AMINO", "AMPLE", "ANGEL", "ANKLE", "ANNOY", "ANTIC", "APHID", "APPLE", "APPLY",
    "ARBOR", "ARGON", "ARMED", "ARMOR", "ARROW", "ARSON", "ABYSS", "ATLAS", "ATTIC", "AUDIO",
    "AUGHT", "AUNTY", "AUTOS", "AVOID", "AWOKE", "AXIOM", "BADGE", "BADLY", "BAGEL", "BAKED",
    "BALES", "BALLS", "BALMY", "BANDS", "BANJO", "BANKS", "BARGE", "BARNS", "BASIC", "BASIN",
    "BASIS", "BATCH", "BATHS", "BEACH", "BEADS", "BEAMS", "BEANS", "BEARD", "BEARS", "BEAST",
    "BEATS", "BEGAN", "BEING", "BELLS", "BELLY", "BELOW", "BELTS", "BENCH", "BENDS", "BERTH",
    "BIKES", "BILLS", "BIRDS", "BIRTH", "BITES", "BLADE", "BLAME", "BLAND", "BLANK", "BLAST",
    "BLAZE", "BLEAK", "BLEED", "BLEND", "BLESS", "BLIND", "BLINK", "BLISS", "BLOCK", "BLOOD",
    "BLOOM", "BLOWN", "BLOWS", "BLUES", "BLUNT", "BLURS", "BLUSH", "BOARD", "BOAST", "BOATS",
    "BOBBY", "BOGEY", "BOILS", "BOMBS", "BONDS", "BONES", "BONUS", "BOOKS", "BOOMS", "BOOST",
    "BOOTH", "BOOTS", "BORED", "BOUND", "BOWEL", "BOWER", "BOWLS", "BOXED", "BOXER", "BOXES",
    "BRAGS", "BRAID", "BRAIN", "BRAKE", "BRAND", "BRASS", "BRAVE", "BRAVO", "BREAD", "BREAK",
    "BREED", "BRICK", "BRIDE", "BRIEF", "BRING", "BRINK", "BROAD", "BROKE", "BROOK", "BROOM",
    "BROWN", "BRUSH", "BUILD", "BUILT", "BULBS", "BULGE", "BULKS", "BULLS", "BUMPS", "BUNCH",
    "BUNNY", "BURNT", "BURST", "BUSES", "BUTTS", "BUYER", "BUZZY", "CABLE", "CACHE", "CAGES",
    "CAKES", "CALLS", "CALMS", "CAMEL", "CAMPS", "CANDY", "CANES", "CANOE", "CARDS", "CARED",
    "CARGO", "CARRY", "CARVE", "CASES", "CASTS", "CATCH", "CAUSE", "CAVES", "CEASE", "CELLS",
    "CHAIN", "CHAIR", "CHALK", "CHAMP", "CHAOS", "CHAPS", "CHARM", "CHART", "CHASE", "CHATS",
    "CHEAP", "CHEAT", "CHECK", "CHEEK", "CHESS", "CHEST", "CHEWS", "CHICK", "CHIEF", "CHILD",
    "CHILL", "CHIMP", "CHIPS", "CHOIR", "CHORE", "CHOSE", "CHUNK", "CHURN", "CIDER", "CIGAR",
    "CIRCA", "CITED", "CIVIC", "CIVIL", "CLADS", "CLAIM", "CLAMP", "CLAMS", "CLANG", "CLAPS",
    "CLASH", "CLASS", "CLAWS", "CLAYS", "CLEAN", "CLEAR", "CLERK", "CLICK", "CLIFF", "CLIMB",
    "CLING", "CLIPS", "CLOAK", "CLOCK", "CLOSE", "CLOTH", "CLOUD", "CLOWN", "CLUBS", "CLUES",
    "CLUMP", "CLUNG", "COACH", "COALS", "COAST", "COATS", "COBRA", "CODES", "COINS", "COLDS",
    "COLON", "COLOR", "COMAS", "COMBO", "COMES", "COMET", "COMIC", "CORAL", "CORDS", "CORES",
    "CORGI", "CORNS", "CORPS", "COSTS", "COUCH", "COUGH", "COULD", "COUNT", "COUPE", "COURT",
    "COVES", "COVER", "CRACK", "CRAFT", "CRAMP", "CRANE", "CRASH", "CRAVE", "CRAWL", "CRAZY",
    "CREAK", "CREAM", "CREEK", "CREEP", "CREME", "CREWS", "CRIBS", "CRIED", "CRIES", "CRIME",
    "CRISP", "CROPS", "CROSS", "CROWD", "CROWN", "CRUDE", "CRUEL", "CRUMB", "CRUSH", "CRUST",
    "CUBBY", "CUBES", "CUFFS", "CURBS", "CURED", "CURES", "CURLS", "CURRY", "CURSE", "CURVE",
    "CURVY", "CUSHY", "CYCLE", "DAILY", "DAIRY", "DAISY", "DANCE", "DANDY", "DARED", "DARES",
    "DATED", "DATES", "DEALT", "DEANS", "DEATH", "DEBIT", "DEBUT", "DECAL", "DECAY", "DECKS",
    "DECOR", "DECOY", "DEEDS", "DEEMS", "DELAY", "DELTA", "DEMUR", "DENSE", "DEPOT", "DEPTH",
    "DERBY", "DESKS", "DETER", "DIARY", "DICED", "DIETS", "DIGIT", "DIKED", "DIMLY", "DINER",
    "DINGO", "DINGY", "DIRTY", "DISCO", "DISKS", "DITCH", "DITTO", "DIVAN", "DIVER", "DIZZY",
    "DOCKS", "DODGE", "DOING", "DOLLY", "DONOR", "DONUT", "DOORS", "DOPED", "DOSED", "DOTED",
    "DOUBT", "DOUGH", "DOVES", "DOWNS", "DOZEN", "DRAFT", "DRAGS", "DRAIN", "DRAKE", "DRAMA",
    "DRANK", "DRAPE", "DRAWN", "DRAWS", "DREAD", "DREAM", "DRESS", "DRIED", "DRIER", "DRIFT",
    "DRILL", "DRINK", "DRIVE", "DROID", "DRONE", "DROOL", "DROOP", "DROVE", "DROWN", "DRUGS",
    "DRUMS", "DRUNK", "DUCKS", "DUDES", "DUETS", "DULLS", "DUMMY", "DUMPS", "DUNKS", "DUSKY",
    "DUSTY", "DUTCH", "DWARF", "DYING", "EAGER", "EAGLE", "EARLY", "EARTH", "EATEN", "EATER",
    "EBONY", "EDGES", "EDITS", "EIGHT", "ELBOW", "ELDER", "ELECT", "ELITE", "ELVES", "EMBER",
    "EMPTY", "ENDED", "ENEMY", "ENJOY", "ENTER", "ENTRY", "ENVOY", "EQUAL", "EQUIP", "ERASE",
    "ERROR", "ESSAY", "ETHER", "ETHIC", "EVENT", "EVERY", "EVILS", "EXACT", "EXAMS", "EXCEL",
    "EXIST", "EXITS", "EXTRA", "EYING", "FABLE", "FACED", "FACER", "FACES", "FACTS", "FADED",
    "FAILS", "FAINT", "FAIRY", "FAITH", "FAKES", "FALLS", "FALSE", "FAMED", "FANCY", "FARMS",
    "FATAL", "FAULT", "FAVOR", "FEARS", "FEAST", "FEATS", "FEELS", "FENCE", "FERRY", "FETCH",
    "FEVER", "FEWER", "FIBER", "FIELD", "FIEND", "FIFTH", "FIFTY", "FIGHT", "FILED", "FILES",
    "FILLS", "FILMS", "FILTH", "FINAL", "FINDS", "FINED", "FINES", "FINER", "FIRED", "FIRES",
    "FIRMS", "FIRST", "FISTS", "FIVES", "FIXED", "FIXER", "FIXES", "FLAGS", "FLAKE", "FLAKY",
    "FLAME", "FLAPS", "FLARE", "FLASH", "FLASK", "FLATS", "FLAWS", "FLEAS", "FLEET", "FLESH",
    "FLIES", "FLING", "FLIPS", "FLOAT", "FLOCK", "FLOOD", "FLOOR", "FLOUR", "FLOWS", "FLUID",
    "FLUKE", "FLUSH", "FLUTE", "FOAMS", "FOCUS", "FOGGY", "FOLDS", "FOLKS", "FONTS", "FOODS",
    "FOOLS", "FOOTS", "FORCE", "FORDS", "FORKS", "FORMS", "FORTH", "FORTY", "FORUM", "FOUND",
    "FOXES", "FRAME", "FRANK", "FRAUD", "FREAK", "FRESH", "FRIED", "FRISK", "FRIZZ", "FROCK",
    "FROGS", "FRONT", "FROST", "FROWN", "FROZE", "FRUIT", "FRUMP", "FUDGE", "FUELS", "FULLY",
    "FUMES", "FUNDS", "FUNNY", "FURRY", "FUSED", "FUSSY", "FUZZY", "GAINS", "GAMES", "GANGS",
    "GASES", "GATES", "GATED", "GAVEL", "GAZES", "GEARS", "GEESE", "GENES", "GENRE", "GHOST",
    "GIANT", "GIFTS", "GILLS", "GIRLS", "GIVEN", "GIVER", "GIVES", "GIZMO", "GLADE", "GLAND",
    "GLARE", "GLASS", "GLAZE", "GLEAM", "GLIDE", "GLOBE", "GLOOM", "GLORY", "GLOSS", "GLOVE",
    "GLOWS", "GLUED", "GLUES", "GOALS", "GOATS", "GODLY", "GOING", "GOODS", "GOOSE", "GRACE",
    "GRADE", "GRAIN", "GRAND", "GRANT", "GRAPE", "GRAPH", "GRASP", "GRASS", "GRAVE", "GRAVY",
    "GRAYS", "GREAT", "GREED", "GREEN", "GREET", "GRIDS", "GRIEF", "GRILL", "GRIME", "GRIMY",
    "GRIND", "GRINS", "GRIPS", "GROAN", "GROSS", "GROUT", "GROVE", "GROWL", "GROWN", "GROWS",
    "GRUEL", "GRUFF", "GRUNT", "GUARD", "GUESS", "GUEST", "GUIDE", "GUILD", "GUILT", "GUISE",
    "GULFS", "GULPS", "GUMMY", "GUPPY", "GUSTY", "HABIT", "HACKS", "HAIKU", "HAILS", "HAIRS",
    "HAIRY", "HALLS", "HALTS", "HANDS", "HANDY", "HANGS", "HAPPY", "HARDY", "HARMS", "HARSH",
    "HASTE", "HASTY", "HATCH", "HATED", "HATER", "HATES", "HAULS", "HAUNT", "HAVEN", "HAVOC",
    "HAWKS", "HEADS", "HEALS", "HEAPS", "HEARD", "HEARS", "HEART", "HEATS", "HEAVY", "HEDGE",
    "HEELS", "HEFTY", "HEIRS", "HELLO", "HELPS", "HENCE", "HERBS", "HERDS", "HIDES", "HIGHS",
    "HILLS", "HILTS", "HINDS", "HINTS", "HIRED", "HIRES", "HITCH", "HIVES", "HOARD", "HOBBY",
    "HOCKS", "HOLDS", "HOLES", "HOLLY", "HOMES", "HONEY", "HOODS", "HOOFS", "HOOKS", "HOOPS",
    "HOOTS", "HOPED", "HOPES", "HORNS", "HORSE", "HOSES", "HOSTS", "HOTEL", "HOUND", "HOURS",
    "HOUSE", "HOVER", "HOWLS", "HUFFY", "HUMAN", "HUMID", "HUMOR", "HUMPS", "HUNCH", "HUNTS",
    "HURLS", "HURRY", "HURTS", "HUTCH", "HYENA", "HYMNS", "HYPED", "HYPES", "ICING", "ICONS",
    "IDEAL", "IDEAS", "IDIOM", "IDIOT", "IDOLS", "IMAGE", "IMPLY", "INBOX", "INCUR", "INDEX",
    "INDIE", "INEPT", "INERT", "INFER", "INKED", "INLAW", "INLET", "INNER", "INPUT", "INTRO",
    "IRONY", "ISSUE", "ITEMS", "IVORY", "JADED", "JAILS", "JAZZY", "JEANS", "JELLY", "JERKS",
    "JETTY", "JEWEL", "JIFFY", "JIGGY", "JINKS", "JOINS", "JOINT", "JOKES", "JOLLY", "JOWLS",
    "JUDGE", "JUICE", "JUICY", "JUMBO", "JUMPS", "JUNKY", "KAYAK", "KEBAB", "KEEPS", "KELLY",
    "KERBS", "KICKS", "KILLS", "KILNS", "KINDS", "KINGS", "KINKS", "KIOSK", "KITES", "KITTY",
    "KNEAD", "KNEEL", "KNEES", "KNELT", "KNIFE", "KNITS", "KNOBS", "KNOCK", "KNOTS", "KNOWN",
    "KNOWS", "KOALA", "LABEL", "LABOR", "LACKS", "LACED", "LADEN", "LADLE", "LAKES", "LAMBS",
    "LAMPS", "LANCE", "LANDS", "LANES", "LARGE", "LARVA", "LASER", "LASSO", "LASTS", "LATCH",
    "LATER", "LAUGH", "LAYER", "LEADS", "LEAFY", "LEAKY", "LEANS", "LEARN", "LEASE", "LEAST",
    "LEAVE", "LEDGE", "LEFTS", "LEGAL", "LEMON", "LEVEL", "LEVER", "LIGHT", "LIKED", "LIKES",
    "LILAC", "LIMBO", "LIMIT", "LINED", "LINEN", "LINER", "LINES", "LINKS", "LIONS", "LISTS",
    "LIVED", "LIVER", "LIVES", "LOADS", "LOAFS", "LOANS", "LOBBY", "LOCAL", "LOCKS", "LODGE",
    "LOFTY", "LOGIC", "LOGIN", "LOOKS", "LOOMS", "LOOPS", "LOOSE", "LORDS", "LOSES", "LOSER",
    "LOTUS", "LOVED", "LOVER", "LOVES", "LOWER", "LUCKY", "LUMPY", "LUNAR", "LUNCH", "LUNGS",
    "LURED", "LURES", "LYING", "LYMPH", "LYRIC", "MACRO", "MADAM", "MADLY", "MAGIC", "MAGMA",
    "MAIDS", "MAILS", "MAJOR", "MAKER", "MAKES", "MALES", "MALLS", "MANOR", "MAPLE", "MARCH",
    "MARKS", "MARRY", "MARSH", "MASKS", "MATCH", "MATED", "MATES", "MATHS", "MATTE", "MAYBE",
    "MAYOR", "MEALS", "MEANS", "MEANT", "MEATS", "MEDAL", "MEDIA", "MEETS", "MELON", "MELTS",
    "MEMOS", "MENUS", "MERCY", "MERGE", "MERIT", "MERRY", "MESSY", "METAL", "METER", "METRO",
    "MICRO", "MIGHT", "MILES", "MILKS", "MILLS", "MINDS", "MINED", "MINER", "MINES", "MINKS",
    "MINOR", "MINTS", "MINUS", "MIXED", "MIXER", "MIXES", "MOATS", "MODAL", "MODEL", "MODEM",
    "MODES", "MOIST", "MOLDS", "MONEY", "MONKS", "MONTH", "MOODS", "MOONY", "MOORS", "MOOSE",
    "MOPED", "MOPES", "MORAL", "MORPH", "MORSE", "MOTHS", "MOTOR", "MOTTO", "MOULD", "MOUND",
    "MOUNT", "MOUSE", "MOUSY", "MOUTH", "MOVED", "MOVER", "MOVES", "MOVIE", "MOWED", "MOWER",
    "MUCUS", "MUDDY", "MULCH", "MUMMY", "MUNCH", "MURAL", "MURKY", "MUSIC", "MUSKY", "MUSTY",
    "MUTED", "MUTES", "MYTHS", "NAILS", "NAKED", "NAMED", "NAMES", "NANNY", "NASAL", "NASTY",
    "NAVAL", "NAVEL", "NEEDS", "NEEDY", "NERVE", "NERDY", "NESTS", "NEVER", "NEWLY", "NIGHT",
    "NINJA", "NINTH", "NIPPY", "NOBLE", "NODES", "NOISE", "NOISY", "NOMAD", "NORMS", "NORTH",
    "NOSED", "NOSES", "NOTED", "NOTES", "NOVEL", "NURSE", "NUTTY", "NYLON", "OASIS", "OATHS",
    "OBESE", "OBEYS", "OCCUR", "OCEAN", "OCTAL", "ODDER", "OFFER", "OFTEN", "OILED", "OILER",
    "OLDER", "OLIVE", "OMEGA", "ONION", "ONSET", "OOZED", "OOZES", "OPERA", "OPTIC", "ORBIT",
    "ORDER", "ORGAN", "OTHER", "OTTER", "OUGHT", "OUNCE", "OUTER", "OVALS", "OVARY", "OVENS",
    "OVERS", "OWING", "OWNED", "OWNER", "OXIDE", "OZONE", "PACED", "PACER", "PACES", "PACKS",
    "PACTS", "PADDY", "PAGER", "PAGES", "PAILS", "PAINS", "PAINT", "PAIRS", "PALES", "PALMS",
    "PANDA", "PANEL", "PANIC", "PANTS", "PAPER", "PARKS", "PARTS", "PARTY", "PASTA", "PASTE",
    "PASTY", "PATCH", "PATHS", "PATIO", "PAUSE", "PAVED", "PAVES", "PAWED", "PAWNS", "PAYEE",
    "PAYER", "PEACE", "PEACH", "PEAKS", "PEARL", "PEARS", "PEASE", "PEATS", "PEDAL", "PEEKS",
    "PEELS", "PEERS", "PENNY", "PERCH", "PERKS", "PERMS", "PETTY", "PHASE", "PHONE", "PHOTO",
    "PIANO", "PICKS", "PICKY", "PIECE", "PIERS", "PIETY", "PIGGY", "PILES", "PILLS", "PILOT",
    "PINCH", "PINED", "PINES", "PINKS", "PINKY", "PINTS", "PIPES", "PITCH", "PITHY", "PIVOT",
    "PIXEL", "PIZZA", "PLACE", "PLAID", "PLAIN", "PLANE", "PLANK", "PLANS", "PLANT", "PLATE",
    "PLAYS", "PLAZA", "PLEAD", "PLEAT", "PLOTS", "PLOWS", "PLUCK", "PLUGS", "PLUMB", "PLUMP",
    "PLUMS", "PLUNK", "PLUSH", "POEMS", "POETS", "POINT", "POISE", "POKER", "POLAR", "POLES",
    "POLLS", "PONDS", "POOLS", "PORCH", "PORED", "PORES", "PORTS", "POSED", "POSES", "POSTS",
    "POUCH", "POUND", "POURS", "POUTS", "POWER", "PRAWN", "PRESS", "PRICE", "PRIDE", "PRIME",
    "PRINT", "PRIOR", "PRISM", "PRIVY", "PRIZE", "PROBE", "PROOF", "PROPS", "PROSE", "PROUD",
    "PROVE", "PROWL", "PSALM", "PUDGY", "PUFFS", "PUFFY", "PULLS", "PULSE", "PUMPS", "PUNCH",
    "PUNKS", "PUPIL", "PUPPY", "PURGE", "PURLS", "PURSE", "PUSHY", "PUTTY", "PYGMY", "QUACK",
    "QUAIL", "QUAKE", "QUALM", "QUART", "QUASI", "QUEEN", "QUEER", "QUERY", "QUEST", "QUEUE",
    "QUICK", "QUIET", "QUILL", "QUILT", "QUIRK", "QUITE", "QUITS", "QUOTA", "QUOTE", "RABBI",
    "RABID", "RACED", "RACER", "RACES", "RACKS", "RADAR", "RADIO", "RAFTS", "RAIDS", "RAILS",
    "RAINS", "RAINY", "RAISE", "RAKED", "RAKES", "RALLY", "RANCH", "RANGE", "RANKS", "RAPID",
    "RARER", "RATES", "RATIO", "RATTY", "RAVED", "RAVEN", "RAVES", "RAZOR", "REACH", "READS",
    "READY", "REALM", "REAMS", "REBEL", "RECAP", "RECUR", "REDID", "REEDS", "REEFS", "REEKS",
    "REELS", "REFER", "REFRY", "REGAL", "REIGN", "RELAX", "RELAY", "RELIC", "REMIX", "REPAY",
    "REPLY", "RESET", "RESIN", "RETRY", "REUSE", "RHYME", "RIBBY", "RICED", "RIDER", "RIDES",
    "RIDGE", "RIFLE", "RIGHT", "RIGID", "RILED", "RILLS", "RINDS", "RINGS", "RINKS", "RINSE",
    "RIOTS", "RIPEN", "RIPER", "RISEN", "RISER", "RISES", "RISKS", "RISKY", "RITES", "RIVAL",
    "RIVER", "ROADS", "ROAMS", "ROARS", "ROAST", "ROBED", "ROBES", "ROBOT", "ROCKS", "ROCKY",
    "ROLES", "ROLLS", "ROOFS", "ROOMS", "ROOMY", "ROOST", "ROOTS", "ROPED", "ROPES", "ROSES",
    "ROTOR", "ROUGE", "ROUGH", "ROUND", "ROUTE", "ROUTS", "ROVER", "ROYAL", "RUGBY", "RUINS",
    "RULED", "RULER", "RULES", "RUMOR", "RUNGS", "RUNNY", "RURAL", "RUSHY", "RUSTY", "SADLY",
    "SAFER", "SAFES", "SAGES", "SAILS", "SAINT", "SALAD", "SALES", "SALLY", "SALON", "SALTS",
    "SALTY", "SANDY", "SASSY", "SAUCE", "SAUCY", "SAUNA", "SAVED", "SAVER", "SAVES", "SAVOR",
    "SAWED", "SAXES", "SCALE", "SCALP", "SCAMS", "SCANS", "SCARE", "SCARF", "SCARY", "SCENE",
    "SCENT", "SCOPE", "SCORE", "SCORN", "SCOTS", "SCOUT", "SCOWL", "SCRAP", "SCREW", "SCRUB",
    "SCUBA", "SEALS", "SEAMS", "SEATS", "SEEDS", "SEEMS", "SEEPS", "SELLS", "SEMIS", "SENDS",
    "SENSE", "SEPIA", "SERVE", "SETUP", "SEVEN", "SEVER", "SEWED", "SEWER", "SHADE", "SHADY",
    "SHAFT", "SHAKE", "SHAKY", "SHALE", "SHALL", "SHAME", "SHANK", "SHAPE", "SHARD", "SHARE",
    "SHARK", "SHARP", "SHAVE", "SHAWL", "SHEAF", "SHEAR", "SHEDS", "SHEEP", "SHEER", "SHEET",
    "SHELF", "SHELL", "SHIFT", "SHINE", "SHINY", "SHIPS", "SHIRT", "SHOAL", "SHOCK", "SHOES",
    "SHONE", "SHOOK", "SHOOT", "SHOPS", "SHORE", "SHORN", "SHORT", "SHOTS", "SHOUT", "SHOVE",
    "SHOWN", "SHOWS", "SHOWY", "SHRED", "SHREW", "SHRUB", "SHRUG", "SHUCK", "SHUNS", "SHUSH",
    "SHUTS", "SIDED", "SIDES", "SIEGE", "SIGHT", "SIGMA", "SIGNS", "SILKY", "SILLY", "SILTS",
    "SINCE", "SINKS", "SIREN", "SISSY", "SITES", "SITED", "SIXTH", "SIXTY", "SIZED", "SIZES",
    "SKATE", "SKEWS", "SKIDS", "SKIES", "SKILL", "SKIMP", "SKINS", "SKIPS", "SKIRT", "SKULK",
    "SKULL", "SKUNK", "SLACK", "SLAIN", "SLAMS", "SLANG", "SLANT", "SLASH", "SLATE", "SLAVE",
    "SLEEK", "SLEEP", "SLEET", "SLEPT", "SLICE", "SLICK", "SLIDE", "SLIME", "SLIMY", "SLING",
    "SLINK", "SLIPS", "SLITS", "SLOBS", "SLOPE", "SLOTS", "SLUGS", "SLUMP", "SLUNG", "SLUNK",
    "SLURP", "SLUSH", "SMALL", "SMART", "SMASH", "SMEAR", "SMELL", "SMELT", "SMILE", "SMIRK",
    "SMOCK", "SMOKE", "SMOKY", "SNACK", "SNAGS", "SNAIL", "SNAKE", "SNAKY", "SNAPS", "SNARE",
    "SNARL", "SNEAK", "SNEER", "SNIDE", "SNIFF", "SNIPS", "SNORE", "SNORT", "SNOUT", "SNOWS",
    "SNOWY", "SNUCK", "SNUFF", "SNUGS", "SOAPY", "SOARS", "SOBER", "SOCKS", "SODAS", "SOFAS",
    "SOGGY", "SOILS", "SOLAR", "SOLVE", "SONAR", "SONGS", "SONIC", "SORRY", "SORTS", "SOULS",
    "SOUND", "SOUPS", "SOUPY", "SOURS", "SOUTH", "SPACE", "SPADE", "SPARE", "SPARK", "SPASM",
    "SPAWN", "SPEAK", "SPEAR", "SPECS", "SPEED", "SPELL", "SPEND", "SPENT", "SPICE", "SPICY",
    "SPIED", "SPIES", "SPIKE", "SPIKY", "SPILL", "SPINE", "SPINY", "SPIRE", "SPITS", "SPLIT",
    "SPOIL", "SPOKE", "SPOOF", "SPOOK", "SPOOL", "SPOON", "SPORT", "SPOTS", "SPRAY", "SPREE",
    "SPRIG", "SPUNK", "SPURS", "SQUAD", "SQUAT", "SQUIB", "STACK", "STAFF", "STAGE", "STAID",
    "STAIN", "STAIR", "STAKE", "STALE", "STALK", "STALL", "STAMP", "STAND", "STANK", "STAPH",
    "STARE", "STARK", "STARS", "START", "STASH", "STATE", "STATS", "STAYS", "STEAD", "STEAK",
    "STEAL", "STEAM", "STEED", "STEEL", "STEEP", "STEER", "STEMS", "STEPS", "STERN", "STICK",
    "STIFF", "STILL", "STILT", "STING", "STINK", "STINT", "STOCK", "STOIC", "STOKE", "STOLE",
    "STOMP", "STONE", "STONY", "STOOD", "STOOL", "STOOP", "STORE", "STORK", "STORM", "STORY",
    "STOUT", "STOVE", "STRAP", "STRAW", "STRAY", "STRIP", "STUCK", "STUDS", "STUFF", "STUMP",
    "STUNG", "STUNK", "STUNT", "STYLE", "SUGAR", "SUITE", "SUITS", "SULKY", "SULLY", "SUMPS",
    "SUNNY", "SUPER", "SURGE", "SURLY", "SWABS", "SWAMP", "SWANS", "SWAPS", "SWARM", "SWASH",
    "SWATS", "SWAYS", "SWEAR", "SWEAT", "SWEEP", "SWEET", "SWELL", "SWEPT", "SWIFT", "SWIMS",
    "SWINE", "SWING", "SWIPE", "SWIRL", "SWISH", "SWISS", "SWOON", "SWOOP", "SWORD", "SWORE",
    "SWORN", "SWUNG", "SYNTH", "SYRUP", "TABLE", "TABOO", "TACIT", "TACKS", "TACKY", "TACOS",
    "TAILS", "TAINT", "TAKEN", "TAKER", "TAKES", "TALES", "TALKS", "TALLY", "TALON", "TAMED",
    "TAMES", "TANKS", "TAPED", "TAPER", "TAPES", "TARDY", "TASTE", "TASTY", "TATTY", "TAXES",
    "TAXIS", "TEACH", "TEAMS", "TEARS", "TEARY", "TEASE", "TEDDY", "TEENS", "TEETH", "TELLS",
    "TEMPO", "TENDS", "TENSE", "TENTH", "TENTS", "TEPID", "TERMS", "TESTS", "TEXTS", "THANK",
    "THAWS", "THEFT", "THEIR", "THEME", "THERE", "THESE", "THICK", "THIEF", "THIGH", "THING",
    "THINK", "THIRD", "THOSE", "THREE", "THREW", "THROW", "THRUM", "THUGS", "THUMB", "THUMP",
    "TIARA", "TIDAL", "TIDES", "TIGER", "TIGHT", "TILED", "TILES", "TILTS", "TIMED", "TIMER",
    "TIMES", "TIMID", "TINGE", "TINTS", "TIPSY", "TIRED", "TITAN", "TITLE", "TOADS", "TOAST",
    "TODAY", "TODDY", "TOKEN", "TOLLS", "TOMBS", "TONED", "TONGS", "TOOLS", "TOOTH", "TOPAZ",
    "TOPIC", "TORCH", "TORSO", "TOTAL", "TOTEM", "TOUCH", "TOUGH",     "TOURS", "TOWEL", "TOWER", "TOWNS", "TOXIC", "TRACK", "TRACT", "TRADE", "TRAIL", "TRAIN",
    "TRAIT", "TRAMP", "TRANS", "TRAPS", "TRASH", "TREAT", "TREES", "TREND", "TRIAL", "TRIBE",
    "TRICK", "TRIED", "TRIES", "TRIMS", "TRIPS", "TRITE", "TROLL", "TROOP", "TROUT", "TRUCE",
    "TRUCK", "TRULY", "TRUMP", "TRUNK", "TRUST", "TRUTH", "TRYST", "TUBES", "TUCKS", "TUFTS",
    "TULIP", "TUMID", "TUNED", "TUNES", "TUNIC", "TURBO", "TURNS", "TUTOR", "TWANG", "TWEED",
    "TWICE", "TWIGS", "TWINE", "TWINS", "TWIST", "TYPED", "TYPES", "TYPOS", "ULTRA", "UMBRA",
    "UNCLE", "UNCUT", "UNDER", "UNDUE", "UNFED", "UNFIT", "UNIFY", "UNION", "UNITE", "UNITS",
    "UNITY", "UNLIT", "UNMET", "UNSET", "UNTIL", "UNWED", "UPEND", "UPPER", "UPSET", "URBAN",
    "URGED", "URGES", "URINE", "USAGE", "USERS", "USHER", "USING", "USUAL", "UTTER", "VALID",
    "VALUE", "VALVE", "VAULT", "VEERS", "VEILS", "VEINS", "VENUE", "VERBS", "VERSE", "VESTS",
    "VEXED", "VIBES", "VICAR", "VIDEO", "VIEWS", "VIGOR", "VILLA", "VINES", "VINYL", "VIOLA",
    "VIPER", "VIRAL", "VIRUS", "VISIT", "VISOR", "VISTA", "VITAL", "VIVID", "VOCAL", "VODKA",
    "VOGUE", "VOICE", "VOIDS", "VOMIT", "VOTED", "VOTER", "VOTES", "VOUCH", "VOWED", "VOWEL",
    "WACKY", "WADES", "WAGER", "WAGES", "WAGON", "WAIST", "WAITS", "WAKED", "WAKES", "WALKS",
    "WALLS", "WALTZ", "WANDS", "WANES", "WANTS", "WARDS", "WARES", "WARMS", "WARNS", "WARPS",
    "WARTS", "WASTE", "WATCH", "WATER", "WATTS", "WAVED", "WAVER", "WAVES", "WAXED", "WAXES",
    "WEARY", "WEAVE", "WEDGE", "WEEDS", "WEEKS", "WEIGH", "WEIRD", "WELLS", "WELSH", "WENCH",
    "WHALE", "WHARF", "WHEAT", "WHEEL", "WHELP", "WHERE", "WHICH", "WHIFF", "WHILE", "WHIMS",
    "WHINE", "WHINY", "WHIPS", "WHIRL", "WHISK", "WHIST", "WHITE", "WHOLE", "WHOMP", "WHOOP",
    "WHOSE", "WIDEN", "WIDER", "WIDOW", "WIDTH", "WIELD", "WIGHT", "WILLS", "WIMPY", "WINCE",
    "WINCH", "WINDS", "WINDY", "WINED", "WINES", "WINGS", "WINKS", "WIPED", "WIPER", "WIPES",
    "WIRED", "WIRES", "WISED", "WISER", "WISPY", "WITCH", "WIVES", "WOKEN", "WOMAN", "WOMEN",
    "WOODS", "WOODY", "WOOED", "WOOLS", "WOOLY", "WORDS", "WORDY", "WORKS", "WORLD", "WORMS",
    "WORMY", "WORRY", "WORSE", "WORST", "WORTH", "WOULD", "WOUND", "WOVEN", "WRACK", "WRAPS",
    "WRATH", "WREAK", "WRECK", "WREST", "WRING", "WRIST", "WRITE", "WRONG", "WROTE", "WRUNG",
    "YACHT", "YANKS", "YARDS", "YARNS", "YAWNS", "YEARS", "YEAST", "YELLS", "YELPS", "YIELD",
    "YODEL", "YOUNG", "YOURS", "YOUTH", "YUMMY", "ZEBRA", "ZEROS", "ZESTS", "ZINCS", "ZIPPY",
    "ZONES", "ZOOMS"
]

# --- ONLY CHANGE #1: Build FIVE_LETTER_WORDS as union of dict (if available) + your list ---
try:
    from english_words import get_english_words_set
    _valid = get_english_words_set(['web2'], lower=False, alpha=True)
    dict_five = {w.upper() for w in _valid if len(w) == 5 and w.isalpha()}
except ImportError:
    dict_five = set()

FIVE_LETTER_WORDS = dict_five | {w.upper() for w in WORD_LIST if len(w) == 5 and w.isalpha()}


def get_random_word():
    """Get a random sequence from the database"""
    return random.choice(WORD_LIST).upper()

def check_pattern_match(target, guess):
    """Analyze input against target pattern and return numerical scores"""
    result = []
    target_chars = list(target)
    guess_chars = list(guess)
    
    # First pass: mark exact matches (score = 1)
    for i in range(5):
        if guess_chars[i] == target_chars[i]:
            result.append(1)
            target_chars[i] = None
            guess_chars[i] = None
        else:
            result.append(0)
    
    # Second pass: mark partial matches (score = 0.5)
    for i in range(5):
        if guess_chars[i] is not None:
            if guess_chars[i] in target_chars:
                result[i] = 0.5
                target_chars[target_chars.index(guess_chars[i])] = None
    
    return result

# --- ONLY CHANGE #2: Safer validator using the unified FIVE_LETTER_WORDS ---
def is_valid_sequence(sequence):
    """Check if sequence is valid (5 letters, alphabetic, real word)"""
    s = sequence.strip().upper()
    if len(s) != 5:
        return False, "Input must be exactly 5 characters"
    if not s.isalpha():
        return False, "Input must contain only letters"
    if s not in FIVE_LETTER_WORDS:
        return False, "Invalid sequence"
    return True, ""


def display_analysis_grid(sequences, scores):
    """Display the analysis grid with numerical scores"""
    if not sequences:
        return
    
    for attempt_num, (sequence, score) in enumerate(zip(sequences, scores), 1):
        result_text = " ".join([f"{char} ({value})" for char, value in zip(sequence, score)])
        st.text(f"Run {attempt_num}: {result_text}")

# Initialize session state
if 'target_sequence' not in st.session_state:
    st.session_state.target_sequence = get_random_word()
    st.session_state.attempts = 0
    st.session_state.sequences = []
    st.session_state.scores = []
    st.session_state.analysis_complete = False
    st.session_state.analysis_successful = False

# App interface
st.markdown("# Analysis")

# Analysis grid
if st.session_state.sequences:
    st.subheader("Results")
    display_analysis_grid(st.session_state.sequences, st.session_state.scores)

# Input section
if not st.session_state.analysis_complete and st.session_state.attempts < 6:
    st.subheader("Input")

    # Put the label above both columns so the input has no in-column label height
    st.markdown("Enter")

    col1, col2 = st.columns([4, 1])
    with col1:
        sequence = st.text_input(
            "",  # no label here
            max_chars=5,
            value="",
            key=f"sequence_input_{st.session_state.attempts}",
            label_visibility="collapsed"
        ).upper()
    with col2:
        analyze_clicked = st.button("Analyze", type="primary", use_container_width=True)

    if analyze_clicked:
        if sequence:
            is_valid, error_msg = is_valid_sequence(sequence)
            if is_valid:
                st.session_state.attempts += 1
                score = check_pattern_match(st.session_state.target_sequence, sequence)
                st.session_state.sequences.append(sequence)
                st.session_state.scores.append(score)

                if all(value == 1 for value in score):
                    st.session_state.analysis_successful = True
                    st.session_state.analysis_complete = True
                    st.success(
                        f"Achieved! Target: {st.session_state.target_sequence} | "
                        f"Iterations: {st.session_state.attempts}"
                    )
                elif st.session_state.attempts >= 6:
                    st.session_state.analysis_complete = True
                    st.error(f"Analysis limit reached. Target sequence: {st.session_state.target_sequence}")
                st.rerun()
            else:
                st.error(error_msg)
        else:
            st.error("Please enter a sequence!")


# Statistics
col1, col2 = st.columns(2)

with col1:
    st.metric("Iterations Used", f"{st.session_state.attempts}")

with col2:
    if st.session_state.analysis_complete:
        status = "Successful" if st.session_state.analysis_successful else "Incomplete"
        st.metric("Status", status)
    else:
        st.metric("Status", "Processing")

# Controls
st.subheader("Controls")
col1, col2 = st.columns(2)

with col1:
    if st.button("Reset Analysis"):
        st.session_state.target_sequence = get_random_word()
        st.session_state.attempts = 0
        st.session_state.sequences = []
        st.session_state.scores = []
        st.session_state.analysis_complete = False
        st.session_state.analysis_successful = False
        st.rerun()

with col2:
    if st.button("Reveal Target"):
        st.warning(f"Target sequence: **{st.session_state.target_sequence}**")

# Optional debug section
if st.checkbox("Show Technical Details"):
    st.markdown("**System Information:**")
    st.write(f"Target: {st.session_state.target_sequence}")
    st.write(f"Database size: {len(WORD_LIST)} sequences")
    if st.session_state.sequences:
        st.write(f"Sequences tested: {st.session_state.sequences}")
        st.write(f"Score matrix: {st.session_state.scores}")

