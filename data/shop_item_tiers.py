from data.item_names import name_id
from data.item import Item
import args

tiers = [None] * Item.ITEM_TYPE_COUNT
weights = [None] * Item.ITEM_TYPE_COUNT

tiers[Item.TOOL] = [
    [
    ],
    [
        name_id["NoiseBlaster"],
        name_id["Bio Blaster"],
        name_id["Flash"],
        name_id["AutoCrossbow"],
        name_id["Debilitator"],
    ],
    [
        name_id["Chain Saw"],
        name_id["Drill"],
        name_id["Air Anchor"],
    ],
    [
    ],
    [
    ],
]
weights[Item.TOOL] = [0, 0.7, 0.3, 0, 0]

tiers[Item.WEAPON] = [
    [
        name_id["Dirk"],
        name_id["MithrilKnife"],
        name_id["Air Lancet"],
        name_id["MithrilBlade"],
        name_id["RegalCutlass"],
        name_id["Epee"],
        name_id["Mithril Pike"],
        name_id["Trident"],
        name_id["Stout Spear"],
        name_id["Imperial"],
        name_id["Kodachi"],
        name_id["Blossom"],
        name_id["Hardened"],
        name_id["Ashura"],
        name_id["Kotetsu"],
        name_id["Forged"],
        name_id["Murasame"],
        name_id["Mithril Rod"],
        name_id["Chocobo Brsh"],
        name_id["DaVinci Brsh"],
        name_id["Shuriken"],
        name_id["Cards"],
        name_id["Darts"],
        name_id["MetalKnuckle"],
        name_id["Mithril Claw"],
        name_id["Kaiser"],
        name_id["Poison Claw"],
    ],
    [
        name_id["Guardian"],
        name_id["ThiefKnife"],
        name_id["Rune Edge"],
        name_id["Flame Sabre"],
        name_id["Blizzard"],
        name_id["ThunderBlade"],
        name_id["Break Blade"],
        name_id["Drainer"],
        name_id["Crystal"],
        name_id["Falchion"],
        name_id["Soul Sabre"],
        name_id["Ogre Nix"],
        name_id["Atma Weapon"],
        name_id["Partisan"],
        name_id["Gold Lance"],
        name_id["Aura"],
        name_id["Strato"],
        name_id["Heal Rod"],
        name_id["Poison Rod"],
        name_id["Gravity Rod"],
        name_id["Punisher"],
        name_id["Magical Brsh"],
        name_id["Rainbow Brsh"],
        name_id["Ninja Star"],
        name_id["Flail"],
        name_id["Full Moon"],
        name_id["Morning Star"],
        name_id["Boomerang"],
        name_id["Rising Sun"],
        name_id["Bone Club"],
        name_id["Trump"],
        name_id["Dice"],
        name_id["Fire Knuckle"],
        name_id["Dragon Claw"],
    ],
    [
        name_id["Assassin"],
        name_id["Man Eater"],
        name_id["SwordBreaker"],
        name_id["Graedus"],
        name_id["Excalibur"],
        name_id["Scimitar"],
        name_id["Imp Halberd"],
        name_id["Striker"],
        name_id["Stunner"],
        name_id["Tempest"],
        name_id["Sky Render"],
        name_id["Fire Rod"],
        name_id["Ice Rod"],
        name_id["Thunder Rod"],
        name_id["Tack Star"],
        name_id["Hawk Eye"],
        name_id["Wing Edge"],
        name_id["Doom Darts"],
        name_id["Tiger Fangs"],
    ],
    [
        name_id["Enhancer"],
        name_id["Pearl Lance"],
        name_id["Aura Lance"],
        name_id["Pearl Rod"],
        name_id["Magus Rod"],
        name_id["Sniper"],
    ],
    [
        name_id["ValiantKnife"],
        name_id["Illumina"],
        name_id["Ragnarok"],
        name_id["Fixed Dice"],
    ],
]
weights[Item.WEAPON] = [0.25, 0.40, 0.28, 0.068, 0.002]

tiers[Item.ARMOR] = [
    [
        name_id["LeatherArmor"],
        name_id["Cotton Robe"],
        name_id["Kung Fu Suit"],
        name_id["Iron Armor"],
        name_id["Silk Robe"],
        name_id["Mithril Vest"],
        name_id["Ninja Gear"],
        name_id["Mithril Mail"],
        name_id["Gold Armor"],
        name_id["Power Sash"],
    ],
    [
        name_id["White Dress"],
        name_id["Gaia Gear"],
        name_id["Light Robe"],
        name_id["Diamond Vest"],
        name_id["DiamondArmor"],
        name_id["Dark Gear"],
        name_id["Crystal Mail"],
        name_id["Tabby Suit"],
        name_id["Chocobo Suit"],
    ],
    [
        name_id["Mirage Vest"],
        name_id["Red Jacket"],
        name_id["Tao Robe"],
        name_id["Czarina Gown"],
        name_id["Imp's Armor"],
        name_id["Moogle Suit"],
    ],
    [
        name_id["Force Armor"],
        name_id["Genji Armor"],
        name_id["Nutkin Suit"],
        name_id["BehemothSuit"],
    ],
    [
        name_id["Minerva"],
        name_id["Snow Muffler"],
    ],
]
weights[Item.ARMOR] = [0.20, 0.42, 0.30, 0.078, 0.002]

tiers[Item.SHIELD] = [
    [
        name_id["Buckler"],
        name_id["Heavy Shld"],
        name_id["Mithril Shld"],
        name_id["Gold Shld"],
    ],
    [
        name_id["Diamond Shld"],
        name_id["Crystal Shld"],
    ],
    [
        name_id["TortoiseShld"],
        name_id["Force Shld"],
    ],
    [
        name_id["Aegis Shld"],
        name_id["Flame Shld"],
        name_id["Ice Shld"],
        name_id["Thunder Shld"],
        name_id["Genji Shld"],
    ],
    [
        name_id["Paladin Shld"],
    ],
]
weights[Item.SHIELD] = [0.35, 0.33, 0.17, 0.149, 0.001]

tiers[Item.HELMET] = [
    [
        name_id["Leather Hat"],
        name_id["Hair Band"],
        name_id["Plumed Hat"],
        name_id["Bandana"],
        name_id["Iron Helmet"],
        name_id["Head Band"],
        name_id["Mithril Helm"],
        name_id["Gold Helmet"],
        name_id["Tiger Mask"],
    ],
    [
        name_id["Beret"],
        name_id["Magus Hat"],
        name_id["Coronet"],
        name_id["Bard's Hat"],
        name_id["Green Beret"],
        name_id["Tiara"],
        name_id["Regal Crown"],
        name_id["Diamond Helm"],
        name_id["Dark Hood"],
        name_id["Crystal Helm"],
        name_id["Thornlet"],
        name_id["Titanium"],
    ],
    [
        name_id["Red Cap"],
        name_id["Mystery Veil"],
        name_id["Circlet"],
        name_id["Oath Veil"],
    ],
    [
        name_id["Cat Hood"],
        name_id["Genji Helmet"],
    ],
    [
    ],
]
weights[Item.HELMET] = [0.25, 0.52, 0.20, 0.03, 0]

tiers[Item.RELIC] = [
    [
        name_id["Goggles"],
        name_id["Star Pendant"],
        name_id["Jewel Ring"],
        name_id["Fairy Ring"],
        name_id["Barrier Ring"],
        name_id["MithrilGlove"],
        name_id["Cure Ring"],
        name_id["Czarina Ring"],
        name_id["Sneak Ring"],
        name_id["Relic Ring"],
        name_id["Sniper Sight"],
        name_id["Tintinabar"],
        name_id["Sprint Shoes"],
    ],
    [
        name_id["Peace Ring"],
        name_id["Amulet"],
        name_id["White Cape"],
        name_id["Guard Ring"],
        name_id["RunningShoes"],
        name_id["Cherub Down"],
        name_id["True Knight"],
        name_id["Zephyr Cape"],
        name_id["Cursed Ring"],
        name_id["Crystal Orb"],
        name_id["Thief Glove"],
        name_id["Gauntlet"],
        name_id["Hyper Wrist"],
        name_id["Beads"],
        name_id["Black Belt"],
        name_id["Coin Toss"],
        name_id["FakeMustache"],
        name_id["Back Guard"],
        name_id["Gale Hairpin"],
    ],
    [
        name_id["Wall Ring"],
        name_id["DragoonBoots"],
        name_id["Earrings"],
        name_id["Atlas Armlet"],
        name_id["Blizzard Orb"],
        name_id["Rage Ring"],
        name_id["Pod Bracelet"],
        name_id["Gold Hairpin"],
        name_id["Memento Ring"],
        name_id["Safety Bit"],
        name_id["Charm Bangle"],
    ],
    [
        name_id["Hero Ring"],
        name_id["Ribbon"],
        name_id["Muscle Belt"],
        name_id["Genji Glove"],
        name_id["Dragon Horn"],
        name_id["Merit Award"],
        name_id["Moogle Charm"],
    ],
    [
        name_id["Economizer"],
        name_id["Offering"],
        name_id["Gem Box"],
        name_id["Marvel Shoes"],
        name_id["Exp. Egg"],
    ],
]
weights[Item.RELIC] = [0.15, 0.40, 0.35, 0.096, 0.004]

tiers[Item.ITEM] = [
    [
        name_id["Tonic"],
        name_id["Potion"],
        name_id["Tincture"],
        name_id["Antidote"],
        name_id["Echo Screen"],
        name_id["Eyedrop"],
        name_id["Green Cherry"],
        name_id["Revivify"],
        name_id["Soft"],
        name_id["Magicite"],
        name_id["Fire Skean"],
        name_id["Water Edge"],
        name_id["Bolt Edge"],
        name_id["Inviz Edge"],
        name_id["Shadow Edge"],
        name_id["ArchplgoItem"],
    ],
    [
        name_id["Ether"],
        name_id["Fenix Down"],
        name_id["Sleeping Bag"],
        name_id["Tent"],
        name_id["Smoke Bomb"],
        name_id["Warp Stone"],
        name_id["Remedy"],
    ],
    [
        name_id["X-Potion"],
        name_id["X-Ether"],
    ],
    [
        name_id["Dried Meat"],
        name_id["Elixir"],
    ],
    [
        name_id["Megalixir"],
        name_id["Super Ball"],
    ],
]
weights[Item.ITEM] = [0.65, 0.30, 0.03, 0.016, 0.004]

if args.stronger_atma_weapon:
    # move stronger atma weapon from tier c to tier a
    tiers[Item.WEAPON][1].remove(name_id["Atma Weapon"])
    tiers[Item.WEAPON][3].append(name_id["Atma Weapon"])
