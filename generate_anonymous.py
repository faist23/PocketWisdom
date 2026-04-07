import json
import uuid

quotes = [
    ("The quiet corner", "I have found that all human intentionality is born of a desire to simply be at rest.", "What is your underlying desire?", "Unknown", "Solitude"),
    ("The morning light", "In the morning, before the mind is fully awake, there is a space of pure existence.", "Can you linger in that space tomorrow?", "Unknown", "Time"),
    ("The river's path", "A river does not ask permission to flow.", "Where do you need to flow without permission?", "Unknown", "Nature & Seasons"),
    ("The unsaid apology", "Sometimes the most profound apologies are the ones communicated through changed behavior.", "How are your actions apologizing?", "Unknown", "Relationships"),
    ("The simple task", "Mundane tasks anchor the mind in the present.", "What mundane task anchors you?", "Unknown", "Work"),
    ("The quiet house", "A house that is quiet is a house that is resting.", "Is your house resting?", "Unknown", "Solitude"),
    ("The empty calendar", "The most beautiful days are often the ones with nothing planned.", "When is your next empty day?", "Unknown", "Time"),
    ("The unforced smile", "A smile that happens naturally is a window to the soul.", "What made you smile naturally today?", "Unknown", "Life"),
    ("The old photograph", "Looking at old photographs reminds us that we have survived all our past versions.", "What past version of yourself are you grateful for?", "Unknown", "Life"),
    ("The silent agreement", "A mutual understanding rarely needs words.", "Who do you share a silent agreement with?", "Unknown", "Relationships"),
    ("The unhurried meal", "Eating slowly is a form of gratitude.", "Can you eat your next meal without rushing?", "Unknown", "Simplicity"),
    ("The rain on the roof", "The sound of rain is a lullaby from the earth.", "What sound brings you comfort?", "Unknown", "Nature & Seasons"),
    ("The blank page", "A blank page is not a void; it is a space for creation.", "What are you creating?", "Unknown", "Work"),
    ("The unexpected detour", "Detours often lead to the most interesting destinations.", "What detour are you on right now?", "Unknown", "Life"),
    ("The quiet strength", "Endurance is often a quiet, steady thing.", "What are you quietly enduring?", "Unknown", "Life"),
    ("The unshared thought", "Not every thought needs to be spoken or acted upon. Some just need to be observed.", "What thought are you simply observing?", "Unknown", "Solitude"),
    ("The simple truth", "The simplest explanation is usually the most accurate.", "What is the simple truth of your situation?", "Unknown", "Simplicity"),
    ("The setting sun", "A sunset is a daily reminder that endings can be beautiful.", "What beautiful ending are you experiencing?", "Unknown", "Nature & Seasons"),
    ("The true friend", "A true friend is someone who makes it easy to believe in yourself.", "Who makes it easy to believe in yourself?", "Unknown", "Relationships"),
    ("The steady hand", "Calmness is contagious.", "Who are you spreading calmness to?", "Unknown", "Life"),
    ("The unforced breath", "Your breath is an anchor to the present moment.", "Take a slow, unforced breath.", "Unknown", "Time"),
    ("The quiet morning", "The early morning belongs to no one.", "How do you spend your early mornings?", "Unknown", "Solitude"),
    ("The simple joy", "Joy is often found in the things we overlook.", "What joy are you overlooking?", "Unknown", "Simplicity"),
    ("The changing tide", "Like the tide, our emotions rise and fall. We just need to ride them out.", "What emotion are you riding out?", "Unknown", "Life"),
    ("The unspoken bond", "Some connections are felt deeply but never articulated.", "What unspoken bond do you cherish?", "Unknown", "Relationships"),
    ("The empty room", "An empty room is a space waiting to be filled with life.", "How will you fill your empty room?", "Unknown", "Simplicity"),
    ("The slow walk", "Walking without a destination is a form of meditation.", "When can you take a slow walk?", "Unknown", "Time"),
    ("The unread book", "The books on your shelf that you haven't read are promises to your future self.", "What promise are you keeping?", "Unknown", "Life"),
    ("The quiet night", "The night is a time for the world to heal.", "Are you allowing yourself to heal?", "Unknown", "Nature & Seasons"),
    ("The simple act", "Doing one thing well is better than doing ten things poorly.", "What one thing can you do well today?", "Unknown", "Work"),
    ("The unspoken truth", "The truth is often felt before it is known.", "What truth are you feeling right now?", "Unknown", "Life"),
    ("The unforced life", "Allow life to unfold rather than trying to force it.", "What are you trying to force?", "Unknown", "Life"),
    ("The quiet mind", "A quiet mind is a fertile ground for creativity.", "How do you cultivate a quiet mind?", "Unknown", "Solitude"),
    ("The simple pleasure", "A cup of tea, a good book, a quiet corner.", "What are your simple pleasures?", "Unknown", "Simplicity"),
    ("The unexpected gift", "Sometimes the best gifts are the ones we didn't know we needed.", "What unexpected gift have you received?", "Unknown", "Life"),
    ("The unhurried conversation", "A conversation without an agenda is a rare and beautiful thing.", "When was your last unhurried conversation?", "Unknown", "Relationships"),
    ("The silent tree", "A tree does not boast of its strength; it simply stands.", "Where are you simply standing?", "Unknown", "Nature & Seasons"),
    ("The empty space", "Empty space in our lives allows room for new things to grow.", "Where do you need more empty space?", "Unknown", "Simplicity"),
    ("The slow morning", "A slow morning sets the tone for a peaceful day.", "How can you slow down tomorrow morning?", "Unknown", "Time"),
    ("The unspoken understanding", "When words fail, presence speaks.", "Who needs your presence today?", "Unknown", "Relationships"),
    ("The quiet observer", "To observe without judgment is a profound act of love.", "Can you observe without judging?", "Unknown", "Life"),
    ("The simple meal", "A simple meal prepared with care is a feast.", "What simple meal brings you joy?", "Unknown", "Simplicity"),
    ("The changing seasons", "Each season has its own unique beauty and purpose.", "What is the purpose of this season in your life?", "Unknown", "Nature & Seasons"),
    ("The unforced connection", "True connection happens effortlessly.", "Where do you feel effortless connection?", "Unknown", "Relationships"),
    ("The quiet retreat", "We all need a place to retreat and recharge.", "Where is your retreat?", "Unknown", "Solitude"),
    ("The slow progress", "Slow progress is still progress.", "Where are you making slow progress?", "Unknown", "Work"),
    ("The unspoken gratitude", "Gratitude is an attitude, not just a feeling.", "What are you quietly grateful for?", "Unknown", "Life"),
    ("The simple life", "Simplicity is a state of mind.", "Is your mind simple?", "Unknown", "Simplicity"),
    ("The quiet reflection", "Reflection is the key to understanding.", "What are you reflecting on today?", "Unknown", "Life"),
    ("The empty cup", "You must empty your cup to receive more.", "What do you need to empty from your cup?", "Unknown", "Life")
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

print(f"Generated {len(quotes)} anonymous reflection cards. Total cards: {len(merged)}")
