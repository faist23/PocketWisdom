import json
import uuid

quotes = [
    ("Getting started", "The secret of getting ahead is getting started.", "What task are you putting off starting?", "Mark Twain", "Work"),
    ("Imagined troubles", "I have been through some terrible things in my life, some of which actually happened.", "How much of your worry is based on imagination rather than reality?", "Mark Twain", "Simplicity"),
    ("Important days", "The two most important days in your life are the day you are born and the day you find out why.", "Are you actively searching for your 'why'?", "Mark Twain", "Life"),
    ("Courage and fear", "Courage is resistance to fear, mastery of fear, not absence of fear.", "Where do you need to show courage despite feeling afraid?", "Mark Twain", "Life"),
    
    ("Facing the sun", "Keep your face always toward the sunshine - and shadows will fall behind you.", "Are you looking towards the light or focusing on the shadows?", "Walt Whitman", "Nature & Seasons"),
    ("Curiosity", "Be curious, not judgmental.", "How can you replace a judgment with curiosity today?", "Walt Whitman", "Relationships"),
    ("Containing multitudes", "Do I contradict myself? Very well then I contradict myself, (I am large, I contain multitudes).", "Can you accept the contradictions within yourself?", "Walt Whitman", "Life"),
    ("Growing in open air", "Now I see the secret of making the best person: it is to grow in the open air and to eat and sleep with the earth.", "When did you last spend meaningful time outside?", "Walt Whitman", "Nature & Seasons"),

    ("Living deliberately", "I went to the woods because I wished to live deliberately, to front only the essential facts of life.", "What is one non-essential thing you can strip away today?", "Henry David Thoreau", "Solitude"),
    ("Simplifying", "Our life is frittered away by detail. Simplify, simplify.", "Where can you simplify your daily routine?", "Henry David Thoreau", "Simplicity"),
    ("The direction of dreams", "Go confidently in the direction of your dreams. Live the life you have imagined.", "What small step can you take toward your imagined life?", "Henry David Thoreau", "Life"),
    ("Inner pathways", "As a single footstep will not make a path on the earth, so a single thought will not make a pathway in the mind.", "What thoughts are you consistently practicing?", "Henry David Thoreau", "Life"),

    ("Running with stars", "Dwell on the beauty of life. Watch the stars, and see yourself running with them.", "Can you pause tonight to appreciate the vastness above you?", "Marcus Aurelius", "Nature & Seasons"),
    ("A happy life", "Very little is needed to make a happy life; it is all within yourself, in your way of thinking.", "Are you searching for happiness outside of your own mind?", "Marcus Aurelius", "Simplicity"),
    ("The act of courage", "Sometimes even to live is an act of courage.", "Can you give yourself credit simply for continuing on?", "Seneca", "Life"),
    ("Preparation and opportunity", "Luck is what happens when preparation meets opportunity.", "Are you preparing yourself for the opportunities you seek?", "Seneca", "Work"),
    ("Few wants", "Wealth consists not in having great possessions, but in having few wants.", "What want can you let go of to feel wealthier today?", "Epictetus", "Simplicity"),
    ("Becoming what you want", "First say to yourself what you would be; and then do what you have to do.", "Who are you telling yourself you want to be?", "Epictetus", "Work")
]

# Load existing wisdom
try:
    with open("PocketWisdom/Resources/wisdom.json", "r") as f:
        existing = json.load(f)
except FileNotFoundError:
    existing = []

cards = []
for title, body, reflection, author, category in quotes:
    cards.append({
        "id": str(uuid.uuid4()),
        "category": category,
        "title": title,
        "body": body,
        "reflection": reflection,
        "author": author
    })

merged = existing + cards
with open("PocketWisdom/Resources/wisdom.json", "w") as f:
    json.dump(merged, f, indent=2)

print(f"Generated {len(quotes)} authored cards. Total cards: {len(merged)}")
