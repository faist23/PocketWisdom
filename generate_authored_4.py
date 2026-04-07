import json
import uuid

quotes = [
    ("The quiet work", "I want to be with those who know secret things or else alone.", "Who are you sharing your secrets with?", "Rainer Maria Rilke", "Solitude"),
    ("The slow blooming", "And the day came when the risk to remain tight in a bud was more painful than the risk it took to blossom.", "What is finally ready to blossom?", "Anais Nin", "Life"),
    ("The present wind", "I am not afraid of storms, for I am learning how to sail my ship.", "What storm are you learning to navigate?", "Louisa May Alcott", "Life"),
    ("The empty hands", "In order to understand the world, one has to turn away from it on occasion.", "Is it time to turn away for a moment?", "Albert Camus", "Solitude"),
    ("The quiet mind", "The mind is everything. What you think you become.", "What are you becoming today?", "Buddha", "Life"),
    ("The unforced growth", "Nature does not demand that we be perfect, only that we grow.", "Are you demanding perfection or allowing growth?", "Unknown", "Nature & Seasons"),
    ("The gentle power", "Nothing is softer or more flexible than water, yet nothing can resist it.", "Where can you apply the gentle persistence of water?", "Lao Tzu", "Nature & Seasons"),
    ("The true self", "Be yourself; everyone else is already taken.", "Where are you trying to be someone else?", "Oscar Wilde", "Simplicity"),
    ("The long journey", "It does not matter how many times you fall, but how many times you rise.", "Are you ready to rise again?", "Confucius", "Life"),
    ("The silent companion", "Silence is a true friend who never betrays.", "Are you making friends with silence?", "Confucius", "Solitude"),
    ("The clear vision", "The soul that sees beauty may sometimes walk alone.", "What beauty are you seeing on your solitary walk?", "Johann Wolfgang von Goethe", "Solitude"),
    ("The simple path", "Walk as if you are kissing the Earth with your feet.", "How gently are you walking today?", "Thich Nhat Hanh", "Nature & Seasons"),
    ("The deep root", "Storms make trees take deeper roots.", "What storm is deepening your roots right now?", "Dolly Parton", "Life"),
    ("The quiet harbor", "A ship in harbor is safe, but that is not what ships are built for.", "Are you staying in the harbor too long?", "John A. Shedd", "Life"),
    ("The unwasted time", "Time you enjoy wasting is not wasted time.", "What did you enjoy 'wasting' time on recently?", "Marthe Troly-Curtin", "Time"),
    ("The inner wealth", "Wealth is the ability to fully experience life.", "Are you fully experiencing today?", "Henry David Thoreau", "Simplicity"),
    ("The silent understanding", "The most important thing in communication is hearing what isn't said.", "What is someone trying to tell you without words?", "Peter Drucker", "Relationships"),
    ("The slow observation", "To acquire knowledge, one must study; but to acquire wisdom, one must observe.", "What are you observing today?", "Marilyn vos Savant", "Simplicity"),
    ("The steady flame", "Keep a little fire burning; however small, however hidden.", "What fire are you keeping alive?", "Cormac McCarthy", "Life"),
    ("The unburdened life", "To be truly free, one must first be unburdened by the opinions of others.", "Whose opinion is burdening you?", "Unknown", "Simplicity"),
    ("The present gift", "The past is a ghost, the future a dream. All we ever have is now.", "Are you living in the ghost, the dream, or the now?", "Bill Cosby", "Time"),
    ("The quiet victory", "Sometimes simply getting through the day is a victory worth celebrating.", "Did you get through the day?", "Unknown", "Life"),
    ("The unspoken truth", "Truth does not require a loud voice to be heard.", "What quiet truth do you know?", "Unknown", "Simplicity"),
    ("The resting place", "There is a time for many words, and there is also a time for sleep.", "Is it time to sleep?", "Homer", "Solitude"),
    ("The open road", "The road is always there. You just have to decide when to walk it.", "When will you start walking?", "Unknown", "Life"),
    ("The steady hand", "Patience is bitter, but its fruit is sweet.", "Are you willing to taste the bitter to get the sweet?", "Jean-Jacques Rousseau", "Time"),
    ("The unmeasured life", "Not everything that counts can be counted, and not everything that can be counted counts.", "What unmeasurable thing counts the most to you?", "Albert Einstein", "Simplicity"),
    ("The quiet dawn", "Every dawn is a new contract with life.", "What is your contract today?", "Unknown", "Time"),
    ("The simple act", "Great acts are made up of small deeds.", "What small deed can you do today?", "Lao Tzu", "Work"),
    ("The unforced smile", "A smile is the universal welcome.", "Who can you welcome today?", "Max Eastman", "Relationships"),
    ("The deep breath", "Breath is the bridge which connects life to consciousness.", "Are you connected right now?", "Thich Nhat Hanh", "Life"),
    ("The silent woods", "In every walk with nature one receives far more than he seeks.", "When did you last walk with nature?", "John Muir", "Nature & Seasons"),
    ("The quiet water", "Still waters run deep.", "What depth are you hiding beneath your stillness?", "Proverb", "Solitude"),
    ("The simple truth", "The truth is rarely pure and never simple.", "Can you accept the complexity of the truth?", "Oscar Wilde", "Life"),
    ("The unwritten page", "You are the author of your own life story.", "What are you writing today?", "Unknown", "Life"),
    ("The quiet power", "Quiet people have the loudest minds.", "What is loud in your mind today?", "Stephen Hawking", "Solitude"),
    ("The unforced pace", "Do not push the river; it will flow by itself.", "What are you trying to push?", "Barry Stevens", "Nature & Seasons"),
    ("The simple life", "Live simply so that others may simply live.", "How can you live more simply?", "Mahatma Gandhi", "Simplicity"),
    ("The quiet evening", "The evening sings in a voice of amber.", "Can you hear the evening's voice?", "Wallace Stevens", "Time"),
    ("The unshared sorrow", "Every heart has its secret sorrows which the world knows not.", "Are you carrying a secret sorrow?", "Henry Wadsworth Longfellow", "Solitude"),
    ("The simple joy", "Joy is what happens to us when we allow ourselves to recognize how good things really are.", "What is really good right now?", "Marianne Williamson", "Life"),
    ("The quiet reflection", "Without deep reflection one knows from daily life that one exists for other people.", "Are you existing for yourself or others?", "Albert Einstein", "Relationships"),
    ("The unspoken bond", "Friendship is a single soul dwelling in two bodies.", "Who shares your soul?", "Aristotle", "Relationships"),
    ("The simple act", "The smallest act of kindness is worth more than the grandest intention.", "What small act can you do?", "Oscar Wilde", "Relationships"),
    ("The unmeasured time", "Time flies over us, but leaves its shadow behind.", "What shadow has time left on you?", "Nathaniel Hawthorne", "Time"),
    ("The quiet resolve", "Courage doesn't always roar. Sometimes courage is the quiet voice at the end of the day saying, 'I will try again tomorrow.'", "Are you willing to try again tomorrow?", "Mary Anne Radmacher", "Life"),
    ("The simple question", "The important thing is not to stop questioning.", "What are you questioning today?", "Albert Einstein", "Life"),
    ("The unforced path", "The journey is the reward.", "Are you enjoying the journey?", "Chinese Proverb", "Life"),
    ("The quiet acceptance", "What you resist, persists.", "What are you resisting?", "Carl Jung", "Life"),
    ("The unwritten future", "The future depends on what you do today.", "What are you doing today to shape tomorrow?", "Mahatma Gandhi", "Time")
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
