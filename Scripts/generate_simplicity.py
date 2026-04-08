import json
import uuid

quotes = [
    ("The closet", "A full closet does not make it easier to get dressed. It usually makes it harder.", "What options are you ready to remove?", None),
    ("The calendar", "A blank space on your calendar is not a void to be filled. It is room to breathe.", "Where is there room to breathe this week?", None),
    ("The menu", "A restaurant with a three-item menu is confident. A restaurant with a hundred items is anxious.", "Where in your life are you offering too many choices?", None),
    ("The suitcase", "You always pack more than you need, and you always survive with less than you packed.", "What are you carrying that you don't actually need?", None),
    ("The silence", "Silence is not the absence of sound, but the absence of noise.", "What noise can you turn off right now?", None),
    ("The clear desk", "A clear desk does not mean you have no work. It means you are ready to begin.", "What physical space needs clearing?", None),
    ("The default", "Setting a default choice removes the fatigue of deciding every single day.", "What simple decision can you automate?", None),
    ("The subtraction", "Improvement is almost always found in subtraction, not addition.", "What could you subtract today to make things better?", None),
    ("The quiet room", "A quiet room with a comfortable chair is often more luxurious than a crowded resort.", "Where is your quiet room?", None),
    ("The single task", "Doing one thing at a time is the ultimate rebellion against a fractured world.", "Can you do just one thing right now?", None),
    ("The unread book", "You do not have to finish a book that you are not enjoying.", "What obligation are you ready to abandon?", None),
    ("The old sweater", "The sweater you reach for every evening is the only one that actually matters.", "What reliably brings you comfort?", None),
    ("The plain truth", "The truth is rarely complicated. The lies we tell to avoid it are what tangle us.", "What plain truth are you avoiding?", None),
    ("The open window", "An open window and fresh air will solve more problems than you think.", "When did you last let the fresh air in?", None),
    ("The simple answer", "A simple 'no' requires far less maintenance than a complicated 'maybe'.", "Who needs a simple 'no' from you?", None),
    ("The ingredient", "The best meals rely on the quality of a few ingredients, not the quantity of spices.", "What are your essential ingredients for a good day?", None),
    ("The routine", "A boring routine is the foundation of a creative life.", "What boring routine supports you?", None),
    ("The walk", "A walk without a destination or a podcast is a rare and powerful thing.", "Can you walk just to walk today?", None),
    ("The enough", "Knowing exactly what 'enough' looks like is the key to lasting peace.", "What does 'enough' look like for you?", None),
    ("The empty shelf", "An empty shelf is full of possibility. A cluttered shelf is full of the past.", "What possibility are you making room for?", None),
    ("The small circle", "You only need a few people who truly understand you.", "Who is in your small circle?", None),
    ("The basics", "When you feel lost, return to the basics: sleep, water, and sunlight.", "Which basic need requires your attention?", None),
    ("The unfollow", "Curating your inputs is just as important as curating your diet.", "Who or what do you need to quietly unfollow?", None),
    ("The quiet evening", "A quiet evening at home is not a missed opportunity; it is a successful day.", "Are you protecting your quiet evenings?", None),
    ("The simple joy", "The first cup of coffee in the morning is a joy that never diminishes.", "What simple joy do you rely on?", None),
    ("The fewer words", "If you can say it in ten words, do not use fifty.", "Where are you over-explaining yourself?", None),
    ("The clean surface", "Wiping down the counter is a small act of respect for tomorrow morning.", "How can you respect tomorrow morning?", None),
    ("The single tab", "Close the browser tabs you are keeping open 'just in case'.", "What 'just in case' are you holding onto?", None),
    ("The old friend", "You do not have to explain your context to an old friend. You just start talking.", "Who requires no explanation?", None),
    ("The clear path", "The simplest path forward is usually the one you are avoiding.", "What simple path is right in front of you?", None),
    ("The declutter", "Decluttering is not just about organizing things; it is about organizing your attention.", "Where is your attention scattered?", None),
    ("The physical object", "Holding a physical book is fundamentally different than scrolling a screen.", "What physical object grounds you?", None),
    ("The empty page", "An empty page is not a demand for brilliance; it is an invitation to begin.", "What are you ready to begin?", None),
    ("The single focus", "You can do anything, but you cannot do everything at the same time.", "What is your single focus today?", None),
    ("The quiet mind", "A quiet mind is the result of letting go, not of holding on tighter.", "What are you gripping too tightly?", None),
    ("The basic tool", "The best tool is usually the simplest one that gets the job done.", "What complicated tool can you replace with a simple one?", None),
    ("The subtraction", "When in doubt, take something away.", "What is the first thing you should take away?", None),
    ("The open space", "You need open space in your schedule to allow for the unexpected.", "How much open space do you have today?", None),
    ("The simple plea", "You do not always need a grand philosophy. Sometimes you just need a nap.", "Do you just need a nap?", None),
    ("The quiet corner", "Every home needs a quiet corner where nothing is required of you.", "Where is your quiet corner?", None),
    ("The single decision", "Make the decision that makes all the other decisions easier.", "What is the keystone decision you need to make?", None),
    ("The empty hands", "You must empty your hands before you can pick up something new.", "What are you putting down?", None),
    ("The simple boundary", "A boundary does not need to be an argument. It can just be a statement.", "What statement do you need to make?", None),
    ("The quiet confidence", "True confidence does not need to announce itself.", "Where do you feel quietly confident?", None),
    ("The essential", "Strip away the non-essential until only the necessary remains.", "What is truly necessary right now?", None),
    ("The simple truth", "The truth is usually the simplest explanation.", "What is the simple truth of your current situation?", None),
    ("The quiet exit", "You can leave the party without making an announcement.", "What are you ready to quietly exit?", None),
    ("The empty sky", "An empty blue sky is beautiful exactly because there is nothing in it.", "Can you appreciate the emptiness?", None),
    ("The simple act", "The simple act of washing the dishes can be a meditation.", "What chore can be your meditation today?", None),
    ("The quiet arrival", "The best moments often arrive quietly, without any fanfare.", "What quiet moment did you notice today?", None)
]

# Load existing wisdom
with open("PocketWisdom/Resources/wisdom.json", "r") as f:
    existing = json.load(f)

cards = []
for title, body, reflection, author in quotes:
    cards.append({
        "id": str(uuid.uuid4()),
        "category": "Simplicity",
        "title": title,
        "body": body,
        "reflection": reflection,
        "author": author
    })

merged = existing + cards
with open("PocketWisdom/Resources/wisdom.json", "w") as f:
    json.dump(merged, f, indent=2)

print(f"Generated 50 Simplicity cards. Total cards: {len(merged)}")
