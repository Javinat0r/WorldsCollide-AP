def name():
    return "Challenges"

def parse(parser):
    challenges = parser.add_argument_group("Challenges")
    challenges.add_argument("-nmc", "--no-moogle-charms", action = "store_true",
                            help = "Moogle Charms will not appear in coliseum/auction/shops/chests/events")
    challenges.add_argument("-nee", "--no-exp-eggs", action = "store_true",
                            help = "Exp. Eggs will not appear in coliseum/auction/shops/chests/events")
    challenges.add_argument("-nil", "--no-illuminas", action = "store_true",
                            help = "Illuminas will not appear in coliseum/auction/shops/chests/events")
    challenges.add_argument("-nu", "--no-ultima", action = "store_true",
                            help = "Ultima cannot be learned from espers/items/natural magic")
    challenges.add_argument("-nfps", "--no-free-paladin-shields", action = "store_true",
                            help = "Paladin/Cursed Shields will not appear in coliseum/auction/shops/chests/events (Narshe WOR exclusive)")
    challenges.add_argument("-nfce", "--no-free-characters-espers", action = "store_true",
                            help = "Remove character/esper rewards from: Auction House, Collapsing House, Figaro Castle Throne, Gau's Father's House, Kohlingen Inn, Narshe Weapon Shop, Sealed Gate, South Figaro Basement")
    challenges.add_argument("-pd", "--permadeath", action = "store_true",
                            help = "Life spells cannot be learned. Fenix Downs unavailable (except from starting items). Buckets/inns/tents/events do not revive characters. Phoenix casts Life 3 on party instead of Life")

def process(args):
    pass

def flags(args):
    flags = ""

    if args.no_moogle_charms:
        flags += " -nmc"
    if args.no_exp_eggs:
        flags += " -nee"
    if args.no_illuminas:
        flags += " -nil"
    if args.no_ultima:
        flags += " -nu"
    if args.no_free_paladin_shields:
        flags += " -nfps"
    if args.no_free_characters_espers:
        flags += " -nfce"
    if args.permadeath:
        flags += " -pd"

    return flags

def options(args):
    ultima = "Original"
    if args.no_ultima:
        ultima = "N/A"
    elif args.ultima_254_mp:
        ultima = "254 MP"

    return [
        ("No Moogle Charms", args.no_moogle_charms),
        ("No Exp Eggs", args.no_exp_eggs),
        ("No Illuminas", args.no_illuminas),
        ("No Sprint Shoes", args.no_sprint_shoes),
        ("No Free Paladin Shields", args.no_free_paladin_shields),
        ("No Free Characters/Espers", args.no_free_characters_espers),
        ("Permadeath", args.permadeath),
        ("Ultima", ultima),
        ("Remove Learnable Spells", args.remove_learnable_spell_ids),
    ]
        
    return opts
def _format_spells_log_entries(spell_ids):
    from constants.spells import id_spell
    spell_entries = []
    for spell_id in spell_ids:
        spell_entries.append(("", id_spell[spell_id]))
    return spell_entries


def menu(args):
    entries = options(args)
    for index, entry in enumerate(entries):
        key, value = entry
        if key == "No Free Paladin Shields":
            entries[index] = ("No Free Paladin Shlds", entry[1])
        elif key == "No Free Characters/Espers":
            entries[index] = ("No Free Chars/Espers", entry[1])
    return (name(), entries)

def log(args):
    from log import format_option
    log = [name()]

    entries = options(args)
    for entry in entries:
        log.append(format_option(*entry))

    return log
