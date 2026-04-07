import json
import uuid

quotes = [
    ("The empty room", "An empty room is not lonely. It is entirely yours.", "How do you fill your empty rooms?", None),
    ("The quiet morning", "Waking up before the rest of the world is a private victory.", "What do you do with your quiet morning?", None),
    ("The solo walk", "Walking without a companion allows you to finally hear your own thoughts.", "What did you hear on your last solo walk?", None),
    ("The unshared moment", "Some moments are too beautiful to be shared. They are meant only for you.", "What beautiful thing did you keep to yourself today?", None),
    ("The closed door", "Closing the door to your room is an act of self-preservation.", "When did you last close the door?", None),
    ("The private joke", "A joke that only you understand is still worth laughing at.", "What made you laugh quietly today?", None),
    ("The solitary meal", "Eating a meal alone is an opportunity to truly taste the food.", "What was the best part of your last solitary meal?", None),
    ("The unplugged day", "Turning off your phone is the modern equivalent of retreating to the mountains.", "When can you retreat tomorrow?", None),
    ("The inner voice", "Your inner voice only speaks when the external noise is turned off.", "What is your inner voice trying to say?", None),
    ("The alone time", "Time spent alone is an investment in your relationship with yourself.", "Are you investing enough time in yourself?", None),
    ("The companion", "You must become a person you enjoy spending time with.", "Do you enjoy your own company?", None),
    ("The quiet night", "The silence of a midnight house is profoundly comforting.", "What brings you comfort at night?", None),
    ("The solo journey", "Traveling alone forces you to trust your own navigation.", "Where are you navigating alone right now?", None),
    ("The unobserved life", "There is a deep peace in doing something when absolutely no one is watching.", "What do you do when no one is watching?", None),
    ("The retreat", "Retreating is not surrendering. It is regrouping.", "Is it time to regroup?", None),
    ("The empty calendar", "A weekend with zero plans is a blank canvas for your soul.", "How will you paint your next blank weekend?", None),
    ("The solitary hobby", "A hobby that requires only you is a sanctuary.", "What is your solitary sanctuary?", None),
    ("The quiet observer", "Sitting on a park bench and simply watching the world go by is a radical act.", "When did you last simply watch the world?", None),
    ("The self-reliance", "Knowing you can handle things on your own removes the desperation from your relationships.", "What have you handled completely on your own?", None),
    ("The silent drive", "Driving with the radio off provides space for the mind to wander.", "Where does your mind wander in the silence?", None),
    ("The singular focus", "Solitude allows you to give your entire attention to a single task.", "What deserves your entire attention today?", None),
    ("The private grief", "Some sorrows can only be processed alone in the dark.", "What are you processing in the dark?", None),
    ("The solo celebration", "You do not need an audience to celebrate a personal victory.", "What quiet victory can you celebrate today?", None),
    ("The deep rest", "True rest often requires complete isolation.", "When did you last rest completely alone?", None),
    ("The unfiltered self", "You are only completely yourself when no one else is in the room.", "Who are you when the room is empty?", None),
    ("The quiet cup", "Drinking your morning coffee in silence is a sacred ritual.", "What is your sacred daily ritual?", None),
    ("The empty page", "Writing in a journal that no one will ever read is true freedom.", "What do you need to write on an empty page?", None),
    ("The solitary thought", "A thought that is never spoken aloud is still a valid thought.", "What is your quietest thought today?", None),
    ("The personal boundary", "Solitude is the ultimate physical boundary.", "How are you protecting your physical boundaries?", None),
    ("The quiet confidence", "Confidence built in solitude cannot be shaken by a crowd.", "Where do you feel unshakeable?", None),
    ("The singular choice", "Deciding what to do without needing anyone's input is a quiet power.", "What decision is entirely yours?", None),
    ("The solo project", "Building something with only your own two hands is deeply satisfying.", "What are you building alone?", None),
    ("The private space", "Every person needs a physical space that is entirely their own.", "Where is your private space?", None),
    ("The silent retreat", "A day without speaking is a day of profound listening.", "What would you hear if you stopped speaking?", None),
    ("The lone tree", "A tree standing alone in a field often grows the strongest branches.", "How has standing alone made you stronger?", None),
    ("The quiet mind", "Solitude is not just physical isolation; it is a quiet mind.", "How do you quiet your mind?", None),
    ("The personal pace", "When you are alone, you can move exactly as fast or as slow as you want.", "What is your natural pace?", None),
    ("The solo rest", "Laying on the floor staring at the ceiling is a perfectly valid activity.", "When can you just stare at the ceiling?", None),
    ("The private tears", "Crying alone allows you to feel the full weight of your sadness without managing someone else's comfort.", "What weight are you carrying?", None),
    ("The quiet decision", "The most important decisions of your life are usually made in complete solitude.", "What quiet decision are you pondering?", None),
    ("The single path", "Some paths are too narrow to walk side-by-side.", "What narrow path are you walking?", None),
    ("The solo sunset", "Watching the sun go down alone is a reminder of your place in the universe.", "What reminds you of your place in the world?", None),
    ("The private reading", "Reading a book in a quiet room is a conversation with the author across time.", "Who are you conversing with today?", None),
    ("The quiet strength", "There is a specific kind of strength that only develops when you have no one else to lean on.", "When did you discover your quiet strength?", None),
    ("The solitary walk", "A walk in the woods alone is a return to your original nature.", "When did you last return to nature?", None),
    ("The solo endeavor", "Not everything needs to be a team effort.", "What is better done alone?", None),
    ("The quiet reflection", "Looking back on your life requires a quiet room.", "What are you reflecting on today?", None),
    ("The personal sanctuary", "Your mind should be a sanctuary you can retreat to at any time.", "Is your mind a sanctuary?", None),
    ("The single breath", "Breathing in the cold air of a quiet morning reminds you that you are alive.", "Are you noticing your breath?", None),
    ("The solitary peace", "Peace is usually found in the quiet spaces between people.", "Where are your quiet spaces?", None)
]

# Load existing wisdom
with open("PocketWisdom/Resources/wisdom.json", "r") as f:
    existing = json.load(f)

cards = []
for title, body, reflection, author in quotes:
    cards.append({
        "id": str(uuid.uuid4()),
        "category": "Solitude",
        "title": title,
        "body": body,
        "reflection": reflection,
        "author": author
    })

merged = existing + cards
with open("PocketWisdom/Resources/wisdom.json", "w") as f:
    json.dump(merged, f, indent=2)

print(f"Generated 50 Solitude cards. Total cards: {len(merged)}")
