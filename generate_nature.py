import json
import uuid

quotes = [
    ("Winter trees", "A tree does not apologize for losing its leaves in winter. It simply rests.", "Where do you need permission to rest?", None),
    ("The river", "A river cuts through rock not because of its power, but because of its persistence.", "What quiet persistence are you practicing?", None),
    ("Spring's arrival", "Spring never rushes, yet everything is eventually in bloom.", "What is slowly blooming in your life?", None),
    ("The tide", "The tide goes out just as predictably as it comes in. Both are necessary.", "Are you trying to hold onto a high tide?", None),
    ("Fallen leaves", "Nature uses what falls away to nourish what will grow next.", "What recent loss is quietly nourishing you?", None),
    ("The mountain", "The mountain remains unchanged by the weather passing over it.", "What is your mountain?", None),
    ("Wildflowers", "A wildflower does not compare itself to the flower next to it. It just blooms.", "Where are you unnecessarily comparing yourself?", None),
    ("The storm", "After every violent storm, the air is remarkably clear.", "What clarity has a recent storm brought you?", None),
    ("Deep roots", "The tallest trees need the deepest roots to survive the wind.", "What grounds you when the wind blows?", None),
    ("The sunrise", "You do not have to earn the sunrise. It is given freely every day.", "What else is given freely to you?", None),
    ("Autumn's lesson", "Autumn shows us how beautiful it can be to let things go.", "What are you holding onto past its season?", None),
    ("The seed", "A seed spends its most transformative days entirely in the dark.", "What is transforming in your own darkness?", None),
    ("The moon", "The moon is whole even when we can only see a sliver of it.", "Can you accept that you are whole, even on partial days?", None),
    ("The forest path", "A straight path through the forest is rarely the most interesting one.", "What detour are you currently walking?", None),
    ("The rain", "The earth does not resist the rain; it simply absorbs what it needs.", "What do you need to absorb right now?", None),
    ("The horizon", "The horizon is not a boundary, but an invitation to keep walking.", "What is calling you forward?", None),
    ("The valley", "The view from the peak is beautiful, but the water and the growth are in the valley.", "What is growing in your current valley?", None),
    ("The seasons", "You cannot skip winter to get to spring faster.", "Are you trying to rush through a cold season?", None),
    ("The moss", "Moss grows quietly, softening the hardest stones over time.", "What hard thing in your life is slowly softening?", None),
    ("The clouds", "Clouds do not permanently block the sun; they only pass in front of it.", "What temporary cloud is passing over you?", None),
    ("The current", "Water flows around obstacles, not through them.", "What obstacle can you simply flow around today?", None),
    ("The night sky", "The stars are always there, even when the city lights hide them.", "What constant truth are you struggling to see right now?", None),
    ("The garden", "You cannot force a tomato to ripen by pulling on its stem.", "What are you trying to force?", None),
    ("The sparrow", "The bird sings not because it has an answer, but because it has a song.", "What is your song today?", None),
    ("The drought", "A period of drought makes the eventual rain feel like a miracle.", "What are you thirsting for?", None),
    ("The ember", "A buried ember can stay warm through the longest, coldest night.", "What quiet hope are you keeping alive?", None),
    ("The breeze", "You cannot catch the wind, but you can feel it pass.", "What fleeting moment did you notice today?", None),
    ("The frost", "Frost preserves the ground so it can hold the thaw.", "What is currently being preserved in you?", None),
    ("The canopy", "The leaves at the top get the most sun, but the roots at the bottom hold everything together.", "Are you tending to your roots?", None),
    ("The dew", "Morning dew disappears quickly, yet it sustains the grass.", "What small thing sustained you this morning?", None),
    ("The migration", "Birds do not resist the changing season; they move with it.", "Are you resisting a necessary change?", None),
    ("The canyon", "A canyon is formed by thousands of years of gentle water.", "What gentle habit is shaping your life?", None),
    ("The dawn", "The darkest part of the night is right before the dawn.", "Are you in the dark before the light?", None),
    ("The soil", "Good soil requires patience, compost, and time.", "What are you cultivating right now?", None),
    ("The echo", "An echo reminds us that what we put out into the world returns to us.", "What are you sending out today?", None),
    ("The fire", "A fire needs space between the logs to breathe and burn.", "Where do you need more space in your life?", None),
    ("The hibernation", "Many creatures survive winter by simply going to sleep.", "Is it time for you to rest?", None),
    ("The pebble", "A single pebble changes the course of a tiny stream.", "What small action changed your day?", None),
    ("The clearing", "A clearing in the woods provides space to see the sky.", "Where is your clearing?", None),
    ("The sunset", "No two sunsets are identical, and yet they are all beautiful.", "What unique beauty did you witness today?", None),
    ("The thaw", "The spring thaw is messy, muddy, and entirely necessary for new life.", "Are you navigating a messy transition?", None),
    ("The silence", "A snow-covered field absorbs sound, creating a profound silence.", "Where do you find profound silence?", None),
    ("The shade", "In the heat of summer, a shaded tree is a sanctuary.", "Who or what provides you sanctuary?", None),
    ("The footprint", "Every footprint left on a trail is eventually washed away.", "Are you worried about a mistake that will soon fade?", None),
    ("The branch", "A branch must bend in the wind, or it will break.", "Where are you refusing to bend?", None),
    ("The tide pool", "A tide pool holds an entire ecosystem in a tiny space.", "What makes up your own small ecosystem?", None),
    ("The harvest", "You cannot harvest what you did not plant.", "What are you planting today?", None),
    ("The mist", "Mist obscures the distance but reveals the immediate surroundings.", "What is immediately in front of you right now?", None),
    ("The coastline", "The coast is always changing, shaped daily by the sea.", "How are you being shaped today?", None),
    ("The wilderness", "There is a wildness in nature that cannot be tamed, only respected.", "What wild part of yourself are you learning to respect?", None)
]

# Load existing wisdom
with open("PocketWisdom/Resources/wisdom.json", "r") as f:
    existing = json.load(f)

cards = []
for title, body, reflection, author in quotes:
    cards.append({
        "id": str(uuid.uuid4()),
        "category": "Nature & Seasons",
        "title": title,
        "body": body,
        "reflection": reflection,
        "author": author
    })

merged = existing + cards
with open("PocketWisdom/Resources/wisdom.json", "w") as f:
    json.dump(merged, f, indent=2)

print(f"Generated 50 Nature & Seasons cards. Total cards: {len(merged)}")
