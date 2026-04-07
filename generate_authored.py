import json
import uuid

quotes = [
    ("The speed of life", "There is more to life than simply increasing its speed.", "Where are you trying to unnecessarily increase the speed?", "Mahatma Gandhi", "Life"),
    ("The darkness", "Only in the darkness can you see the stars.", "What stars are visible to you in this current dark moment?", "Martin Luther King Jr.", "Life"),
    ("The inner retreat", "Nowhere can man find a quieter or more untroubled retreat than in his own soul.", "When did you last visit your inner retreat?", "Marcus Aurelius", "Solitude"),
    ("True happiness", "True happiness is to enjoy the present, without anxious dependence upon the future.", "Are you anxiously depending on tomorrow?", "Seneca", "Time"),
    ("Imagined suffering", "We suffer more often in imagination than in reality.", "What are you suffering over that hasn't actually happened?", "Epictetus", "Simplicity"),
    ("The pace of nature", "Nature does not hurry, yet everything is accomplished.", "What are you rushing that will eventually finish itself?", "Lao Tzu", "Nature & Seasons"),
    ("A busy life", "Beware the barrenness of a busy life.", "What is your busyness actually producing?", "Socrates", "Work"),
    ("The right busyness", "It is not enough to be busy. So are the ants. The question is: What are we busy about?", "What are you truly busy about?", "Henry David Thoreau", "Work"),
    ("Sitting quietly", "All of humanity's problems stem from man's inability to sit quietly in a room alone.", "Can you sit quietly in a room alone today?", "Blaise Pascal", "Solitude"),
    ("Going slowly", "Smile, breathe and go slowly.", "When can you pause to simply breathe and go slowly today?", "Thich Nhat Hanh", "Simplicity"),
    ("The space between", "Between stimulus and response there is a space. In that space is our power to choose our response.", "Are you using the space before you respond?", "Viktor E. Frankl", "Life"),
    ("Inner power", "You have power over your mind - not outside events. Realize this, and you will find strength.", "What outside event are you trying to control?", "Marcus Aurelius", "Life"),
    ("Craving more", "It is not the man who has too little, but the man who craves more, that is poor.", "What are you currently craving that you don't actually need?", "Seneca", "Simplicity"),
    ("The invincible summer", "In the depth of winter, I finally learned that within me there lay an invincible summer.", "What invincible strength lies within you?", "Albert Camus", "Nature & Seasons"),
    ("The settled waters", "Let the waters settle and you will see the moon and the stars mirrored in your own being.", "Are you allowing the waters to settle?", "Rumi", "Solitude"),
    ("The unexamined life", "The unexamined life is not worth living.", "What part of your life are you avoiding examining?", "Socrates", "Life"),
    ("The obstacle", "The impediment to action advances action. What stands in the way becomes the way.", "What obstacle is actually your path forward?", "Marcus Aurelius", "Work"),
    ("The cost of things", "The price of anything is the amount of life you exchange for it.", "Are you paying too high a price for something?", "Henry David Thoreau", "Time"),
    ("The art of living", "The art of living is more like wrestling than dancing.", "Where are you wrestling right now?", "Marcus Aurelius", "Life"),
    ("The present moment", "Do not let your reflection on the whole sweep of life crush you.", "Can you just focus on the step directly in front of you?", "Marcus Aurelius", "Time")
]

# Load existing wisdom
with open("PocketWisdom/Resources/wisdom.json", "r") as f:
    existing = json.load(f)

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
