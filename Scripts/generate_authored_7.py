import json
import uuid

quotes = [
    # Eckhart Tolle
    ("The present moment", "Realize deeply that the present moment is all you have. Make the NOW the primary focus of your life.", "Are you treating this moment as a means to an end?", "Eckhart Tolle", "Time"),
    ("Acceptance", "Whatever the present moment contains, accept it as if you had chosen it.", "Can you stop fighting what is already happening?", "Eckhart Tolle", "Simplicity"),

    # Pema Chödrön
    ("Fear", "Fear is a natural reaction to moving closer to the truth.", "What truth might your current fear be pointing toward?", "Pema Chödrön", "Life"),
    ("Groundlessness", "The trick is to keep exploring and not bail out, even when we find out that something is not what we thought.", "Can you stay with the feeling of uncertainty today?", "Pema Chödrön", "Solitude"),

    # Jon Kabat-Zinn
    ("Mindfulness", "You can't stop the waves, but you can learn to surf.", "How are you trying to stop the waves instead of learning to ride them?", "Jon Kabat-Zinn", "Simplicity"),
    ("Wherever you go", "Wherever you go, there you are.", "Are you trying to run away from something that is inside you?", "Jon Kabat-Zinn", "Solitude"),

    # Brené Brown
    ("Vulnerability", "Vulnerability is not winning or losing; it's having the courage to show up and be seen when we have no control over the outcome.", "Where do you need to show up today?", "Brené Brown", "Relationships"),
    ("Belonging", "True belonging doesn't require us to change who we are; it requires us to be who we are.", "Are you changing yourself to fit in?", "Brené Brown", "Solitude"),

    # Ram Dass
    ("Walking each other home", "We're all just walking each other home.", "How can you be a better companion to someone today?", "Ram Dass", "Relationships"),
    ("Quiet mind", "The quieter you become, the more you can hear.", "What might you hear if you quieted your mind right now?", "Ram Dass", "Solitude"),

    # Tara Brach
    ("Radical Acceptance", "Radical Acceptance is the willingness to experience ourselves and our life as it is.", "What part of yourself are you refusing to accept?", "Tara Brach", "Life"),
    ("The pause", "A pause is a suspension of activity, a time of temporary disengagement when the gears of the mind and body can shift.", "Can you take a mindful pause right now?", "Tara Brach", "Simplicity"),

    # Jack Kornfield
    ("Forgiveness", "Forgiveness is giving up all hope of a better past.", "What past event do you need to stop hoping will change?", "Jack Kornfield", "Time"),
    ("The heart", "If your compassion does not include yourself, it is incomplete.", "Are you treating yourself as kindly as you treat others?", "Jack Kornfield", "Relationships"),

    # Sharon Salzberg
    ("Beginning again", "Mindfulness isn't about never being distracted; it's about remembering to begin again.", "Can you simply begin again right now?", "Sharon Salzberg", "Simplicity"),
    
    # Rainer Maria Rilke
    ("The questions", "Be patient toward all that is unsolved in your heart and try to love the questions themselves.", "Can you live with the question instead of forcing an answer?", "Rainer Maria Rilke", "Solitude"),
    ("Letting go", "Let everything happen to you: beauty and terror. Just keep going. No feeling is final.", "Can you allow yourself to feel this fully without panicking?", "Rainer Maria Rilke", "Life"),

    # C.S. Lewis
    ("Hardships", "Hardships often prepare ordinary people for an extraordinary destiny.", "How might your current hardship be preparing you?", "C.S. Lewis", "Life"),
    ("Getting older", "You are never too old to set another goal or to dream a new dream.", "What new dream is waiting for you?", "C.S. Lewis", "Time"),

    # Paulo Coelho
    ("The journey", "It's the possibility of having a dream come true that makes life interesting.", "What possibility is making your life interesting today?", "Paulo Coelho", "Life"),
    ("Tears", "Tears are words that need to be written.", "What are your tears trying to say?", "Paulo Coelho", "Solitude"),

    # Elizabeth Gilbert
    ("Curiosity", "The universe buries strange jewels deep within us all, and then stands back to see if we can find them.", "What hidden jewel are you searching for within yourself?", "Elizabeth Gilbert", "Work"),
    
    # Virginia Woolf
    ("Self", "I am rooted, but I flow.", "How can you maintain your roots while remaining flexible?", "Virginia Woolf", "Nature & Seasons"),
    
    # Jane Austen
    ("Self-knowledge", "There is nothing I would not do for those who are really my friends. I have no notion of loving people by halves.", "Are you loving with your whole heart?", "Jane Austen", "Relationships"),

    # Toni Morrison
    ("Freedom", "The function of freedom is to free someone else.", "Who can you help free today?", "Toni Morrison", "Work"),
    
    # James Baldwin
    ("Facing things", "Not everything that is faced can be changed, but nothing can be changed until it is faced.", "What are you refusing to face?", "James Baldwin", "Life"),

    # Kahlil Gibran (additional)
    ("Reason and passion", "Your reason and your passion are the rudder and the sails of your seafaring soul.", "Are your rudder and sails working together?", "Khalil Gibran", "Life"),

    # Anne Frank
    ("Goodness", "How wonderful it is that nobody need wait a single moment before starting to improve the world.", "What small improvement can you make right now?", "Anne Frank", "Work"),

    # Nelson Mandela
    ("Courage", "I learned that courage was not the absence of fear, but the triumph over it.", "Where can you triumph over a small fear today?", "Nelson Mandela", "Life"),

    # Winston Churchill
    ("Success", "Success is not final, failure is not fatal: it is the courage to continue that counts.", "Can you find the courage to simply continue?", "Winston Churchill", "Work"),

    # Marie Curie
    ("Understanding", "Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less.", "What do you need to understand better to reduce your fear?", "Marie Curie", "Life"),

    # Albert Einstein
    ("Miracles", "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.", "Which way are you living today?", "Albert Einstein", "Nature & Seasons"),

    # Rosa Parks
    ("Doing what must be done", "I have learned over the years that when one's mind is made up, this diminishes fear; knowing what must be done does away with fear.", "What is something you know you must do?", "Rosa Parks", "Work"),

    # Martin Luther King Jr. (additional)
    ("Faith", "Faith is taking the first step even when you don't see the whole staircase.", "Can you take just one step today?", "Martin Luther King Jr.", "Life"),

    # Florence Nightingale
    ("No excuses", "I attribute my success to this - I never gave or took any excuse.", "What excuse can you drop today?", "Florence Nightingale", "Work"),
    
    # Carl Rogers
    ("Acceptance and change", "The curious paradox is that when I accept myself just as I am, then I can change.", "Can you fully accept yourself exactly as you are right now?", "Carl Rogers", "Solitude"),

    # Rollo May
    ("Freedom and responsibility", "Freedom is man's capacity to take a hand in his own development. It is our capacity to mold ourselves.", "How are you molding yourself today?", "Rollo May", "Life"),

    # Abraham Maslow
    ("Growth", "In any given moment we have two options: to step forward into growth or step back into safety.", "Which way are you stepping right now?", "Abraham Maslow", "Work")
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