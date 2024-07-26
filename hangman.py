print("Adam Asmaca Oyununa Hoş Geldiniz")
import random

def select_word():
    words = [
        "apple", "banana", "cherry", "date", "eggplant", "fig", "grape", "honeydew",
        "iceberg", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "pear",
        "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon",
        "xigua", "yellowfin", "zucchini", "airplane", "balloon", "cruise", "dirigible",
        "elevator", "ferry", "glider", "hang-glider", "helicopter", "jumbo", "kayak",
        "lorry", "monorail", "narrowboat", "oceanliner", "parachute", "quadcopter", "rocket",
        "submarine", "tanker", "ultralight", "velocipede", "wheelbarrow", "yacht", "zeppelin",
        "acorn", "bark", "cactus", "daisy", "elm", "fern", "grass", "hickory", "ivy", "juniper",
        "kiwi", "lily", "maple", "nutmeg", "oak", "palm", "quince", "rose", "sequoia", "tulip",
        "umbrella", "violet", "willow", "xylosma", "yew", "zinnia", "astronaut", "botanist",
        "chemist", "dentist", "engineer", "firefighter", "geologist", "historian", "journalist",
        "mechanic", "nurse", "optometrist", "pilot", "quartermaster", "radiologist", "scientist",
        "technician", "urologist", "veterinarian", "welder", "xenobiologist", "yardmaster",
        "zoologist", "alphabet", "book", "calendar", "dictionary", "encyclopedia", "folder",
        "guidebook", "handbook", "index", "journal", "kaleidoscope", "ledger", "magazine",
        "newspaper", "outline", "periodical", "quotation", "report", "storybook", "textbook",
        "utopia", "volume", "workbook", "yearbook", "zealot", "abacus", "bracelet", "compass",
        "earrings", "fingernail", "gloves", "handkerchief", "idol", "jewelry", "keychain",
        "locket", "medallion", "necklace", "ornament", "pendant", "quilt", "ring", "scarf",
        "tiara", "umbrella", "veil", "wallet", "x-ray", "yarmulke", "zipper", "amber", "blossom", "cascade", "dandelion", "eclipse", "flannel", "glimmer", "hurricane",
        "incense", "jasmine", "kaleidoscope", "lagoon", "marigold", "nebula", "oasis", "peacock",
        "quasar", "raindrop", "serenade", "tundra", "unicorn", "volcano", "wisteria", "xylophone",
        "yonder", "zephyr", "alchemy", "bazaar", "cascade", "dynamo", "echo", "flint", "galaxy",
        "harmony", "illusion", "jubilee", "karma", "labyrinth", "mystic", "nirvana", "oracle",
        "paradox", "quintessence", "rhapsody", "serenity", "talisman", "utopia", "vortex", "whisper",
        "zenith", "aquamarine", "beryl", "coral", "dewdrop", "emerald", "fractal", "garnet", "hazel",
        "iris", "jade", "kryptonite", "lapis", "moonstone", "nugget", "opal", "pebble", "quartz",
        "ruby", "sapphire", "topaz", "umbrage", "verdant", "willow", "xenon", "yellowstone", "zircon",
        "agate", "bison", "cobalt", "daffodil", "ember", "falcon", "gazelle", "hyacinth", "indigo",
        "jaguar", "kangaroo", "lemur", "magnolia", "nasturtium", "otter", "peony", "quokka", "raccoon",
        "sunflower", "tamarind", "umbrella", "violet", "wombat", "xerus", "yucca", "zebra", "Antelope",
        "Antelope", "Blueprint", "Cascade", "Daffodil", "Euphoria", "Flamingo", "Geyser", "Harmony",
        "Iceberg", "Jaguar", "Kite", "Lavender", "Monsoon", "Nebula", "Oasis", "Panther",
        "Quasar", "Radiant", "Sahara", "Thunder", "Umbrella", "Valley", "Wombat", "Xenon",
        "Yellowtail", "Zephyr", "Archipelago", "Basilisk", "Cinnamon", "Diadem", "Eucalyptus", "Fjord",
        "Garnet", "Hyacinth", "Incandescent", "Jasmine", "Krypton", "Lagoon", "Marzipan", "Nectar",
        "Opulent", "Pinnacle", "Quicksilver", "Rendezvous", "Saffron", "Teardrop", "Utopia"
    ]
    
    return random.choice(words).lower()

def display_hangman(tries):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                '''
    ]
    return stages[tries]

def hangman():
    word = select_word()
    guessed_letters = []
    guessed_word = ["_"] * len(word)
    tries = 6
    print(display_hangman(tries))

    while tries > 0 and "_" in guessed_word:
        print("Tahmin edilen kelime: " + " ".join(guessed_word))
        guess = input("Bir harf tahmin edin: ").lower()

        if guess in guessed_letters:
            print("Bu harfi zaten tahmin ettiniz.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Doğru tahmin!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("Yanlış tahmin!")
            tries -= 1

        print(display_hangman(tries))

    if "_" not in guessed_word:
        print("Tebrikler! Kelimeyi doğru tahmin ettiniz: " + word)
    else:
        print("Oyun bitti. Doğru kelime '{}' idi.".format(word))

hangman()