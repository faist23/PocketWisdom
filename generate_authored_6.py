import json
import uuid

quotes = [
    # Rumi
    ("The wound", "The wound is the place where the Light enters you.", "Where are you hurting, and what might it be teaching you?", "Rumi", "Life"),
    ("Seeking", "What you seek is seeking you.", "What are you truly seeking in your life?", "Rumi", "Life"),
    ("The breeze at dawn", "The breeze at dawn has secrets to tell you. Don't go back to sleep.", "What quiet messages are you missing in the rush of the morning?", "Rumi", "Nature & Seasons"),
    ("Letting go", "Be empty of worrying. Think of who created thought.", "Can you let go of one worry today?", "Rumi", "Simplicity"),
    
    # Buddha
    ("The mind", "The mind is everything. What you think you become.", "What are your most frequent thoughts?", "Buddha", "Life"),
    ("Peace", "Peace comes from within. Do not seek it without.", "Where have you been seeking peace externally?", "Buddha", "Solitude"),
    ("Holding on", "You can only lose what you cling to.", "What are you currently clinging to?", "Buddha", "Simplicity"),
    ("The present", "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.", "Where is your mind right now?", "Buddha", "Time"),

    # Confucius
    ("Moving forward", "It does not matter how slowly you go as long as you do not stop.", "Where do you feel stalled, but can just take one small step?", "Confucius", "Work"),
    ("Simplicity", "Life is really simple, but we insist on making it complicated.", "How are you complicating your life right now?", "Confucius", "Simplicity"),
    ("The journey", "Wherever you go, go with all your heart.", "Are you fully present in your current endeavors?", "Confucius", "Life"),

    # Lao Tzu
    ("The journey of a thousand miles", "A journey of a thousand miles begins with a single step.", "What is the single step you need to take today?", "Lao Tzu", "Work"),
    ("Letting go", "When I let go of what I am, I become what I might be.", "What old identity is holding you back?", "Lao Tzu", "Life"),
    ("Water", "Nothing in the world is more flexible and yielding than water. Yet when it attacks the firm and the strong, none can withstand it.", "Where could you be more yielding?", "Lao Tzu", "Nature & Seasons"),

    # Ralph Waldo Emerson
    ("To be yourself", "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", "Where are you conforming when you should be yourself?", "Ralph Waldo Emerson", "Solitude"),
    ("Pacing", "Adopt the pace of nature: her secret is patience.", "Where in your life do you need more patience?", "Ralph Waldo Emerson", "Nature & Seasons"),
    ("Action", "Do not go where the path may lead, go instead where there is no path and leave a trail.", "Where can you carve your own path?", "Ralph Waldo Emerson", "Work"),

    # John Muir
    ("The mountains", "The mountains are calling and I must go.", "What quiet place in nature is calling to you?", "John Muir", "Nature & Seasons"),
    ("The universe", "When one tugs at a single thing in nature, he finds it attached to the rest of the world.", "How are your actions connected to the world around you?", "John Muir", "Nature & Seasons"),

    # Emily Dickinson
    ("Hope", "Hope is the thing with feathers that perches in the soul.", "What gives you hope in difficult times?", "Emily Dickinson", "Life"),
    ("Forever", "Forever is composed of nows.", "Are you making the most of this 'now'?", "Emily Dickinson", "Time"),

    # Maya Angelou
    ("Being normal", "If you are always trying to be normal, you will never know how amazing you can be.", "What unique trait of yours are you hiding?", "Maya Angelou", "Life"),
    ("Making a living", "You can only become truly accomplished at something you love.", "Do you love what you are devoting your time to?", "Maya Angelou", "Work"),

    # Viktor Frankl
    ("Meaning in suffering", "In some ways suffering ceases to be suffering at the moment it finds a meaning.", "Can you find meaning in your current struggles?", "Viktor E. Frankl", "Life"),
    ("Choosing attitude", "Everything can be taken from a man but one thing: the last of the human freedoms—to choose one’s attitude in any given set of circumstances.", "What attitude are you choosing today?", "Viktor E. Frankl", "Solitude"),

    # Carl Jung
    ("Looking inside", "Who looks outside, dreams; who looks inside, awakes.", "When did you last look inside yourself?", "Carl Jung", "Solitude"),
    ("Acceptance", "We cannot change anything until we accept it.", "What is something you are struggling to accept?", "Carl Jung", "Life"),

    # Alan Watts
    ("The future", "No valid plans for the future can be made by those who have no capacity for living now.", "Are you sacrificing today for a hypothetical tomorrow?", "Alan Watts", "Time"),
    ("The universe", "You are an aperture through which the universe is looking at and exploring itself.", "How does this perspective change your view of yourself?", "Alan Watts", "Life"),

    # Thich Nhat Hanh
    ("The present moment", "The present moment is filled with joy and happiness. If you are attentive, you will see it.", "What small joy can you notice in this moment?", "Thich Nhat Hanh", "Time"),
    ("Walking", "Walk as if you are kissing the Earth with your feet.", "Can you move more mindfully today?", "Thich Nhat Hanh", "Nature & Seasons"),

    # Dalai Lama
    ("Silence", "Sometimes one creates a dynamic impression by saying something, and sometimes one creates as significant an impression by remaining silent.", "When might silence be your best response?", "Dalai Lama", "Relationships"),
    ("Happiness", "Happiness is not something ready made. It comes from your own actions.", "What actions are you taking to cultivate happiness?", "Dalai Lama", "Life"),

    # Mary Oliver
    ("Attention", "To pay attention, this is our endless and proper work.", "What are you paying attention to right now?", "Mary Oliver", "Work"),
    ("Your wild life", "Tell me, what is it you plan to do with your one wild and precious life?", "What is your plan for your precious life?", "Mary Oliver", "Life"),

    # Khalil Gibran
    ("Joy and sorrow", "Your joy is your sorrow unmasked.", "Can you see the connection between your joys and your sorrows?", "Khalil Gibran", "Life"),
    ("Work is love", "Work is love made visible.", "Is your work a reflection of what you love?", "Khalil Gibran", "Work"),

    # Rabindranath Tagore
    ("The butterfly", "The butterfly counts not months but moments, and has time enough.", "Are you counting time instead of experiencing moments?", "Rabindranath Tagore", "Time"),
    ("Stars", "If you cry because the sun has gone out of your life, your tears will prevent you from seeing the stars.", "What stars are you missing by focusing on the dark?", "Rabindranath Tagore", "Nature & Seasons"),

    # Hermann Hesse
    ("Finding", "When someone is seeking, it happens quite easily that he only sees the thing that he is seeking.", "Are you blinded by your own search?", "Hermann Hesse", "Life"),
    ("The river", "The river is everywhere at the same time, at the source and at the mouth... in the ocean and in the mountains, everywhere.", "Can you appreciate the continuous flow of life?", "Hermann Hesse", "Nature & Seasons"),

    # Albert Camus
    ("Autumn", "Autumn is a second spring when every leaf is a flower.", "What beauty can you find in endings or transitions?", "Albert Camus", "Nature & Seasons"),
    ("Inner strength", "In the midst of winter, I found there was, within me, an invincible summer.", "What is your invincible summer?", "Albert Camus", "Life"),
    
    # Epictetus
    ("Control", "There is only one way to happiness and that is to cease worrying about things which are beyond the power of our will.", "What are you worrying about that you cannot control?", "Epictetus", "Simplicity"),
    
    # Seneca
    ("Time", "It is not that we have a short time to live, but that we waste a lot of it.", "How are you wasting your time today?", "Seneca", "Time"),
    ("Difficulties", "Difficulties strengthen the mind, as labor does the body.", "How is your current difficulty making you stronger?", "Seneca", "Life"),
    
    # Marcus Aurelius
    ("Morning thoughts", "When you arise in the morning, think of what a precious privilege it is to be alive.", "Did you pause to appreciate waking up today?", "Marcus Aurelius", "Time"),
    ("The soul's color", "The soul becomes dyed with the color of its thoughts.", "What color are your thoughts today?", "Marcus Aurelius", "Solitude"),
    
    # Mahatma Gandhi
    ("Change", "Be the change that you wish to see in the world.", "How can you embody the change you want to see?", "Mahatma Gandhi", "Work"),
    ("Finding yourself", "The best way to find yourself is to lose yourself in the service of others.", "Who can you serve today?", "Mahatma Gandhi", "Relationships"),
    
    # Mother Teresa
    ("Small things", "Not all of us can do great things. But we can do small things with great love.", "What small thing can you do with great love today?", "Mother Teresa", "Work"),
    
    # Aristotle
    ("Excellence", "We are what we repeatedly do. Excellence, then, is not an act, but a habit.", "What habits are you repeating today?", "Aristotle", "Work"),
    
    # Plato
    ("Kindness", "Be kind, for everyone you meet is fighting a harder battle.", "How can you extend kindness to someone today?", "Plato", "Relationships"),
    
    # Socrates
    ("Wonder", "Wisdom begins in wonder.", "What did you wonder about today?", "Socrates", "Life"),
    
    # Leonardo da Vinci
    ("Simplicity", "Simplicity is the ultimate sophistication.", "How can you simplify a complex problem in your life?", "Leonardo da Vinci", "Simplicity"),
    
    # Antoine de Saint-Exupéry
    ("The invisible", "And now here is my secret, a very simple secret: It is only with the heart that one can see rightly; what is essential is invisible to the eye.", "What essential thing are you missing by only using your eyes?", "Antoine de Saint-Exupéry", "Life"),
    
    # J.R.R. Tolkien
    ("Wandering", "Not all those who wander are lost.", "Are you allowing yourself space to simply wander?", "J.R.R. Tolkien", "Solitude"),
    
    # Helen Keller
    ("Facing the sun", "Keep your face to the sunshine and you cannot see a shadow.", "Are you focusing on the bright side of your current situation?", "Helen Keller", "Nature & Seasons"),
    
    # William Shakespeare
    ("Expectation", "Expectation is the root of all heartache.", "What expectations can you let go of today?", "William Shakespeare", "Relationships"),
    
    # Bruce Lee
    ("Flowing water", "Empty your mind, be formless. Shapeless, like water.", "How can you be more adaptable today?", "Bruce Lee", "Simplicity")
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