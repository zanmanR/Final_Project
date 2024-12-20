pokemon_data = {
    "bulbasaur": {"HP": 45, "Moves": ["Tackle (30)", "Vine Whip (45)"], "Evolution": "Ivysaur"},
    "ivysaur": {"HP": 60, "Moves": ["Razor Leaf (55)", "Seed Bomb (80)"], "Evolution": "Venusaur"},
    "venusaur": {"HP": 150, "Moves": ["Solar Beam (120)", "Sludge Bomb (90)"], "Evolution": None},

    "charmander": {"HP": 39, "Moves": ["Scratch (40)", "Ember (40)"], "Evolution": "Charmeleon"},
    "charmeleon": {"HP": 58, "Moves": ["Flamethrower (90)", "Fire Fang (65)"], "Evolution": "Charizard"},
    "charizard": {"HP": 150, "Moves": ["Fire Blast (110)", "Air Slash (75)"], "Evolution": None},

    "squirtle": {"HP": 44, "Moves": ["Tackle (40)", "Water Gun (40)"], "Evolution": "Wartortle"},
    "wartortle": {"HP": 59, "Moves": ["Bubble Beam (65)", "Bite (60)"], "Evolution": "Blastoise"},
    "blastoise": {"HP": 150, "Moves": ["Hydro Pump (110)", "Ice Beam (90)"], "Evolution": None},

    "caterpie": {"HP": 45, "Moves": ["Tackle (40)", "String Shot (0)"], "Evolution": "metapod"},
    "metapod": {"HP": 50, "Moves": ["Harden (0)", "Tackle (40)"], "Evolution": "butterfree"},
    "butterfree": {"HP": 90, "Moves": ["Gust (40)", "Psychic (90)"], "Evolution": None},

    "weedle": {"HP": 40, "Moves": ["Poison Sting (15)", "String Shot (0)"], "Evolution": "Kakuna"},
    "kakuna": {"HP": 45, "Moves": ["Harden (0)", "Tackle (40)"], "Evolution": "beedrill"},
    "beedrill": {"HP": 65, "Moves": ["Twineedle (50)", "Poison Jab (80)"], "Evolution": None},

    "pidgey": {"HP": 40, "Moves": ["Tackle (40)", "Gust (40)"], "Evolution": "Pidgeotto"},
    "pidgeotto": {"HP": 63, "Moves": ["Wing Attack (60)", "Quick Attack (40)"], "Evolution": "Pidgeot"},
    "pidgeot": {"HP": 83, "Moves": ["Hurricane (110)", "Air Slash (75)"], "Evolution": None},

    "rattata": {"HP": 30, "Moves": ["Tackle (40)", "Bite (60)"], "Evolution": "Raticate"},
    "raticate": {"HP": 55, "Moves": ["Hyper Fang (80)", "Crunch (80)"], "Evolution": None},

    "spearow": {"HP": 40, "Moves": ["Peck (35)", "Fury Attack (15 per hit)"], "Evolution": "Fearow"},
    "fearow": {"HP": 65, "Moves": ["Drill Peck (80)", "Aerial Ace (60)"], "Evolution": None},

    "ekans": {"HP": 35, "Moves": ["Poison Sting (15)", "Wrap (15)"], "Evolution": "Arbok"},
    "arbok": {"HP": 60, "Moves": ["Bite (60)", "Sludge Bomb (90)"], "Evolution": None},

    "pikachu": {"HP": 35, "Moves": ["Thunder Shock (40)", "Quick Attack (40)"], "Evolution": "Raichu"},
    "raichu": {"HP": 60, "Moves": ["Thunderbolt (90)", "Iron Tail (100)"], "Evolution": None},

    "sandshrew": {"HP": 50, "Moves": ["Scratch (40)", "Sand Attack (0)"], "Evolution": "Sandslash"},
    "nandslash": {"HP": 75, "Moves": ["Earthquake (100)", "Slash (70)"], "Evolution": None},

    "nidoran♀": {"HP": 55, "Moves": ["Scratch (40)", "Poison Sting (15)"], "Evolution": "Nidorina"},
    "nidorina": {"HP": 70, "Moves": ["Double Kick (30 per hit)", "Bite (60)"], "Evolution": "Nidoqueen"},
    "nidoqueen": {"HP": 90, "Moves": ["Earthquake (100)", "Sludge Bomb (90)"], "Evolution": None},

    "nidoran♂": {"HP": 46, "Moves": ["Peck (35)", "Poison Sting (15)"], "Evolution": "Nidorino"},
    "nidorino": {"HP": 61, "Moves": ["Horn Attack (65)", "Poison Jab (80)"], "Evolution": "Nidoking"},
    "nidoking": {"HP": 81, "Moves": ["Earthquake (100)", "Megahorn (120)"], "Evolution": None},

    "clefairy": {"HP": 70, "Moves": ["Pound (40)", "Moonblast (95)"], "Evolution": "Clefable"},
    "clefable": {"HP": 95, "Moves": ["Moonblast (95)", "Dazzling Gleam (80)"], "Evolution": None},

    "vulpix": {"HP": 38, "Moves": ["Ember (40)", "Quick Attack (40)"], "Evolution": "Ninetales"},
    "ninetales": {"HP": 73, "Moves": ["Flamethrower (90)", "Will-O-Wisp (0)"], "Evolution": None},

    "jigglypuff": {"HP": 115, "Moves": ["Pound (40)", "Sing (0)"], "Evolution": "Wigglytuff"},
    "wigglytuff": {"HP": 140, "Moves": ["Hyper Voice (90)", "Dazzling Gleam (80)"], "Evolution": None},

    "zubat": {"HP": 40, "Moves": ["Bite (60)", "Wing Attack (60)"], "Evolution": "Golbat"},
    "golbat": {"HP": 75, "Moves": ["Poison Fang (50)", "Air Cutter (60)"], "Evolution": None},

    "oddish": {"HP": 45, "Moves": ["Absorb (20)", "Acid (40)"], "Evolution": "Gloom"},
    "gloom": {"HP": 60, "Moves": ["Razor Leaf (55)", "Poison Powder (0)"], "Evolution": "Vileplume"},
    "vileplume": {"HP": 75, "Moves": ["Solar Beam (120)", "Sludge Bomb (90)"], "Evolution": None},

    "paras": {"HP": 35, "Moves": ["Scratch (40)", "Stun Spore (0)"], "Evolution": "Parasect"},
    "parasect": {"HP": 60, "Moves": ["X-Scissor (80)", "Spore (0)"], "Evolution": None},
    
    "venonat": {"HP": 60, "Moves": ["Confusion (50)", "Psybeam (65)"], "Evolution": "Venomoth"},
    "venomoth": {"HP": 70, "Moves": ["Bug Buzz (90)", "Poison Fang (50)"], "Evolution": None},

    "diglett": {"HP": 10, "Moves": ["Scratch (40)", "Mud-Slap (20)"], "Evolution": "Dugtrio"},
    "dugtrio": {"HP": 35, "Moves": ["Earthquake (100)", "Rock Slide (75)"], "Evolution": None},

    "meowth": {"HP": 40, "Moves": ["Scratch (40)", "Bite (60)"], "Evolution": "Persian"},
    "persian": {"HP": 65, "Moves": ["Slash (70)", "Play Rough (90)"], "Evolution": None},

    "psyduck": {"HP": 50, "Moves": ["Water Gun (40)", "Confusion (50)"], "Evolution": "Golduck"},
    "golduck": {"HP": 80, "Moves": ["Hydro Pump (110)", "Psychic (90)"], "Evolution": None},

    "mankey": {"HP": 40, "Moves": ["Karate Chop (50)", "Low Kick (50)"], "Evolution": "Primeape"},
    "primeape": {"HP": 65, "Moves": ["Cross Chop (100)", "Close Combat (120)"], "Evolution": None},

    "growlithe": {"HP": 55, "Moves": ["Bite (60)", "Ember (40)"], "Evolution": "Arcanine"},
    "arcanine": {"HP": 90, "Moves": ["Flare Blitz (120)", "Extreme Speed (80)"], "Evolution": None},

    "poliwag": {"HP": 40, "Moves": ["Water Gun (40)", "Bubble (40)"], "Evolution": "Poliwhirl"},
    "poliwhirl": {"HP": 65, "Moves": ["Bubble Beam (65)", "Body Slam (85)"], "Evolution": "Poliwrath"},
    "poliwrath": {"HP": 90, "Moves": ["Hydro Pump (110)", "Dynamic Punch (100)"], "Evolution": None},

    "abra": {"HP": 25, "Moves": ["Teleport (0)", "Hidden Power (60)"], "Evolution": "Kadabra"},
    "kadabra": {"HP": 40, "Moves": ["Confusion (50)", "Psybeam (65)"], "Evolution": "Alakazam"},
    "alakazam": {"HP": 55, "Moves": ["Psychic (90)", "Shadow Ball (80)"], "Evolution": None},

    "machop": {"HP": 70, "Moves": ["Karate Chop (50)", "Low Kick (50)"], "Evolution": "Machoke"},
    "machoke": {"HP": 80, "Moves": ["Seismic Toss (60)", "Cross Chop (100)"], "Evolution": "Machamp"},
    "machamp": {"HP": 90, "Moves": ["Dynamic Punch (100)", "Close Combat (120)"], "Evolution": None},

    "bellsprout": {"HP": 50, "Moves": ["Vine Whip (45)", "Wrap (15)"], "Evolution": "Weepinbell"},
    "weepinbell": {"HP": 65, "Moves": ["Acid (40)", "Razor Leaf (55)"], "Evolution": "Victreebel"},
    "victreebel": {"HP": 80, "Moves": ["Leaf Blade (90)", "Sludge Bomb (90)"], "Evolution": None},

    "tentacool": {"HP": 40, "Moves": ["Acid (40)", "Bubble Beam (65)"], "Evolution": "Tentacruel"},
    "tentacruel": {"HP": 80, "Moves": ["Hydro Pump (110)", "Sludge Wave (95)"], "Evolution": None},

    "geodude": {"HP": 40, "Moves": ["Tackle (40)", "Rock Throw (50)"], "Evolution": "Graveler"},
    "graveler": {"HP": 55, "Moves": ["Rock Slide (75)", "Earthquake (100)"], "Evolution": "Golem"},
    "golem": {"HP": 80, "Moves": ["Stone Edge (100)", "Earthquake (100)"], "Evolution": None},
    
    "ponyta": {"HP": 50, "Moves": ["Ember (40)", "Stomp (65)"], "Evolution": "Rapidash"},
    "rapidash": {"HP": 65, "Moves": ["Fire Blast (110)", "Flare Blitz (120)"], "Evolution": None},

    "slowpoke": {"HP": 90, "Moves": ["Water Gun (40)", "Confusion (50)"], "Evolution": "Slowbro"},
    "slowbro": {"HP": 95, "Moves": ["Psychic (90)", "Surf (90)"], "Evolution": None},

    "magnemite": {"HP": 25, "Moves": ["Thunder Shock (40)", "Spark (65)"], "Evolution": "Magneton"},
    "magneton": {"HP": 50, "Moves": ["Thunderbolt (90)", "Zap Cannon (120)"], "Evolution": None},

    "farfetch'd": {"HP": 52, "Moves": ["Fury Cutter (40)", "Air Slash (75)"], "Evolution": None},

    "doduo": {"HP": 35, "Moves": ["Peck (35)", "Quick Attack (40)"], "Evolution": "Dodrio"},
    "dodrio": {"HP": 60, "Moves": ["Drill Peck (80)", "Tri Attack (80)"], "Evolution": None},

    "seel": {"HP": 65, "Moves": ["Headbutt (70)", "Aqua Tail (90)"], "Evolution": "Dewgong"},
    "dewgong": {"HP": 90, "Moves": ["Ice Beam (90)", "Surf (90)"], "Evolution": None},

    "grimer": {"HP": 80, "Moves": ["Sludge (65)", "Pound (40)"], "Evolution": "Muk"},
    "muk": {"HP": 105, "Moves": ["Sludge Bomb (90)", "Gunk Shot (120)"], "Evolution": None},

    "shellder": {"HP": 30, "Moves": ["Tackle (40)", "Icicle Spear (25 per hit)"], "Evolution": "Cloyster"},
    "cloyster": {"HP": 50, "Moves": ["Ice Beam (90)", "Hydro Pump (110)"], "Evolution": None},

    "gastly": {"HP": 30, "Moves": ["Lick (30)", "Night Shade (Varies)"], "Evolution": "Haunter"},
    "haunter": {"HP": 45, "Moves": ["Shadow Ball (80)", "Dark Pulse (80)"], "Evolution": "Gengar"},
    "gengar": {"HP": 60, "Moves": ["Shadow Ball (80)", "Sludge Bomb (90)"], "Evolution": None},

    "onix": {"HP": 35, "Moves": ["Rock Throw (50)", "Sandstorm (0)"], "Evolution": None},

    "drowzee": {"HP": 60, "Moves": ["Confusion (50)", "Psybeam (65)"], "Evolution": "Hypno"},
    "hypno": {"HP": 85, "Moves": ["Psychic (90)", "Zen Headbutt (80)"], "Evolution": None},

    "krabby": {"HP": 30, "Moves": ["Bubble (40)", "Vice Grip (55)"], "Evolution": "Kingler"},
    "kingler": {"HP": 55, "Moves": ["Crabhammer (100)", "Stomp (65)"], "Evolution": None},

    "voltorb": {"HP": 40, "Moves": ["Tackle (40)", "Spark (65)"], "Evolution": "Electrode"},
    "electrode": {"HP": 60, "Moves": ["Thunderbolt (90)", "Explosion (Varies)"], "Evolution": None},

    "exeggcute": {"HP": 60, "Moves": ["Confusion (50)", "Stun Spore (0)"], "Evolution": "Exeggutor"},
    "exeggutor": {"HP": 95, "Moves": ["Solar Beam (120)", "Psychic (90)"], "Evolution": None},

    "cubone": {"HP": 50, "Moves": ["Bone Club (65)", "Headbutt (70)"], "Evolution": "Marowak"},
    "marowak": {"HP": 60, "Moves": ["Earthquake (100)", "Bonemerang (50 per hit)"], "Evolution": None},
    
    "hitmonlee": {"HP": 50, "Moves": ["High Jump Kick (130)", "Brick Break (75)"], "Evolution": None},
    "hitmonchan": {"HP": 50, "Moves": ["Fire Punch (75)", "Ice Punch (75)"], "Evolution": None},

    "lickitung": {"HP": 90, "Moves": ["Lick (30)", "Body Slam (85)"], "Evolution": None},

    "koffing": {"HP": 40, "Moves": ["Tackle (40)", "Sludge (65)"], "Evolution": "Weezing"},
    "weezing": {"HP": 65, "Moves": ["Sludge Bomb (90)", "Explosion (250)"], "Evolution": None},

    "rhyhorn": {"HP": 80, "Moves": ["Stomp (65)", "Rock Blast (25 per hit)"], "Evolution": "Rhydon"},
    "rhydon": {"HP": 105, "Moves": ["Earthquake (100)", "Stone Edge (100)"], "Evolution": None},

    "chansey": {"HP": 250, "Moves": ["Pound (40)", "Hyper Beam (150)"], "Evolution": None},

    "tangela": {"HP": 65, "Moves": ["Vine Whip (45)", "Stun Spore (0)"], "Evolution": None},

    "kangaskhan": {"HP": 105, "Moves": ["Comet Punch (18 per hit)", "Dizzy Punch (70)"], "Evolution": None},

    "horsea": {"HP": 30, "Moves": ["Bubble (40)", "Water Gun (40)"], "Evolution": "Seadra"},
    "seadra": {"HP": 55, "Moves": ["Hydro Pump (110)", "Dragon Pulse (85)"], "Evolution": None},

    "goldeen": {"HP": 45, "Moves": ["Peck (35)", "Water Pulse (60)"], "Evolution": "Seaking"},
    "seaking": {"HP": 80, "Moves": ["Waterfall (80)", "Horn Drill (OHKO)"], "Evolution": None},

    "staryu": {"HP": 30, "Moves": ["Water Gun (40)", "Rapid Spin (50)"], "Evolution": "Starmie"},
    "starmie": {"HP": 60, "Moves": ["Hydro Pump (110)", "Psychic (90)"], "Evolution": None},

    "mr.mime": {"HP": 40, "Moves": ["Confusion (50)", "Barrier (0)"], "Evolution": None},

    "scyther": {"HP": 70, "Moves": ["Slash (70)", "X-Scissor (80)"], "Evolution": None},

    "jynx": {"HP": 65, "Moves": ["Ice Punch (75)", "Psychic (90)"], "Evolution": None},

    "electabuzz": {"HP": 65, "Moves": ["Thunder Punch (75)", "Thunderbolt (90)"], "Evolution": None},

    "magmar": {"HP": 65, "Moves": ["Flamethrower (90)", "Fire Punch (75)"], "Evolution": None},

    "pinsir": {"HP": 65, "Moves": ["X-Scissor (80)", "Submission (80)"], "Evolution": None},

    "tauros": {"HP": 75, "Moves": ["Tackle (40)", "Earthquake (100)"], "Evolution": None},

    "magikarp": {"HP": 20, "Moves": ["Splash (0)", "Tackle (40)"], "Evolution": "Gyarados"},
    "gyarados": {"HP": 95, "Moves": ["Hydro Pump (110)", "Crunch (80)"], "Evolution": None},

    "lapras": {"HP": 130, "Moves": ["Ice Beam (90)", "Surf (90)"], "Evolution": None},

    "ditto": {"HP": 48, "Moves": ["Transform (0)", "Struggle (50)"], "Evolution": None},

    "eevee": {"HP": 55, "Moves": ["Tackle (40)", "Bite (60)"], "Evolution": "Vaporeon, Jolteon, Flareon"},
    "vaporeon": {"HP": 130, "Moves": ["Hydro Pump (110)", "Ice Beam (90)"], "Evolution": None},
    "jolteon": {"HP": 65, "Moves": ["Thunderbolt (90)", "Pin Missile (25 per hit)"], "Evolution": None},
    "flareon": {"HP": 65, "Moves": ["Flamethrower (90)", "Fire Blast (110)"], "Evolution": None},

    "porygon": {"HP": 65, "Moves": ["Tackle (40)", "Psybeam (65)"], "Evolution": None},

    "omanyte": {"HP": 35, "Moves": ["Water Gun (40)", "Ancient Power (60)"], "Evolution": "Omastar"},
    "omastar": {"HP": 70, "Moves": ["Hydro Pump (110)", "Rock Slide (75)"], "Evolution": None},

    "kabuto": {"HP": 30, "Moves": ["Scratch (40)", "Absorb (20)"], "Evolution": "Kabutops"},
    "kabutops": {"HP": 60, "Moves": ["X-Scissor (80)", "Rock Slide (75)"], "Evolution": None},

    "aerodactyl": {"HP": 80, "Moves": ["Wing Attack (60)", "Rock Slide (75)"], "Evolution": None},

    "snorlax": {"HP": 160, "Moves": ["Body Slam (85)", "Hyper Beam (150)"], "Evolution": None},

    "articuno": {"HP": 90, "Moves": ["Ice Beam (90)", "Hurricane (110)"], "Evolution": None},
    "zapdos": {"HP": 90, "Moves": ["Thunderbolt (90)", "Drill Peck (80)"], "Evolution": None},
    "moltres": {"HP": 90, "Moves": ["Flamethrower (90)", "Hurricane (110)"], "Evolution": None},

    "dratini": {"HP": 41, "Moves": ["Twister (40)", "Wrap (15)"], "Evolution": "dragonair"},
    "dragonair": {"HP": 61, "Moves": ["Dragon Pulse (85)", "Aqua Tail (90)"], "Evolution": "dragonite"},
    "dragonite": {"HP": 91, "Moves": ["Outrage (120)", "Hurricane (110)"], "Evolution": None},

    "mewtwo": {"HP": 106, "Moves": ["Psychic (90)", "Shadow Ball (80)"], "Evolution": None},
    "mew": {"HP": 100, "Moves": ["Psychic (90)", "Ancient Power (60)"], "Evolution": None}
    
    "shayan": {"HP": 200000000000000, "Moves": ["stupid (40)", "little stupid (15)"], "Evolution": "yousuf"},
    "yousuf": {"HP": 12, "Moves": ["really stupid (85)", "super stupid (90)"], "Evolution": "faizan"},
    "faizan": {"HP": 69000, "Moves": ["sigma (12 million)", "super sigma (110 million)"], "Evolution": None},

    }
