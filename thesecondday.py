# [] Ekrana bir şey yazdırması
# [] İnternetten 300 kelimelik bir liste oluşturmak
# [] Bu listeyi ekrana bastır, düzgünce alındığından emin ol
# [] Rastgele bir sayı üret
# [] Listeden bu rastgele sayıya denk gelen sıradaki kelimeyi bastır
# [] Kullanıcıdan konsol üzerinden input almayı test et
# [] Alınan inputu konsola bastır

print("Kelime Seçme Oyununa Hoş Geldiniz")
english_words = english_words = [
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

def print_kelimeler(words):
    for index, word in enumerate(words, start=1):
        print(f"{index}. {word}")

print_kelimeler(english_words)

try:
    secim = int(input("Lütfen bir sayı girin (1 ile 300 arasında): ".format(len(english_words))))
    if 0 <= secim < len(english_words):
        print("Seçilen kelime:", english_words[secim])
    else:
        print("Hata: Geçersiz sayı girdiniz. Lütfen 1 ile 300 arasında bir sayı girin.".format(len(english_words)))
except ValueError:
        print("Hata: Sayı girmelisiniz. Lütfen tekrar deneyin.")