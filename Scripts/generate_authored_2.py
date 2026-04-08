import json
import uuid

quotes = [
    ("The present moment", "The present moment is filled with joy and happiness. If you are attentive, you will see it.", "Are you attentive to this moment?", "Thich Nhat Hanh", "Time"),
    ("Worry", "He who fears he shall suffer, already suffers what he fears.", "What are you suffering over before it even happens?", "Michel de Montaigne", "Simplicity"),
    ("The wealth of the soul", "Wealth consists not in having great possessions, but in having few wants.", "What do you want that you can easily live without?", "Epictetus", "Simplicity"),
    ("The quiet mind", "To a mind that is still, the whole universe surrenders.", "How can you still your mind today?", "Lao Tzu", "Solitude"),
    ("The unhurried life", "Adopt the pace of nature: her secret is patience.", "Where can you adopt the pace of nature?", "Ralph Waldo Emerson", "Nature & Seasons"),
    ("The true measure", "It is not the daily increase but daily decrease. Hack away at the unessential.", "What unessential thing can you hack away?", "Bruce Lee", "Simplicity"),
    ("The open heart", "Your task is not to seek for love, but merely to seek and find all the barriers within yourself that you have built against it.", "What barrier can you dismantle today?", "Rumi", "Relationships"),
    ("The journey", "A journey of a thousand miles begins with a single step.", "What is the single step you need to take?", "Lao Tzu", "Work"),
    ("The reflection", "Everything that irritates us about others can lead us to an understanding of ourselves.", "What is your irritation teaching you?", "Carl Jung", "Relationships"),
    ("The present", "We are very good at preparing to live, but not very good at living.", "Are you preparing to live, or are you living?", "Thich Nhat Hanh", "Life"),
    ("The quiet voice", "The soul usually knows what to do to heal itself. The challenge is to silence the mind.", "How can you silence your mind?", "Caroline Myss", "Solitude"),
    ("The gift of time", "You must live in the present, launch yourself on every wave, find your eternity in each moment.", "Are you finding eternity in this moment?", "Henry David Thoreau", "Time"),
    ("The essential", "To find out what is truly individual in ourselves, profound reflection is needed; and suddenly we realize how uncommonly difficult the discovery of individuality is.", "Are you taking time for profound reflection?", "Carl Jung", "Solitude"),
    ("The letting go", "Some of us think holding on makes us strong, but sometimes it is letting go.", "What makes you stronger by letting go?", "Hermann Hesse", "Life"),
    ("The simple life", "Our life is frittered away by detail. Simplify, simplify.", "Where can you simplify?", "Henry David Thoreau", "Simplicity"),
    ("The inner peace", "Nobody can bring you peace but yourself.", "Are you relying on someone else for your peace?", "Ralph Waldo Emerson", "Solitude"),
    ("The silence", "Silence is a source of great strength.", "Are you drawing strength from silence?", "Lao Tzu", "Solitude"),
    ("The enduring", "What lies behind us and what lies before us are tiny matters compared to what lies within us.", "Are you focused on what lies within?", "Ralph Waldo Emerson", "Life"),
    ("The perspective", "If you are distressed by anything external, the pain is not due to the thing itself, but to your estimate of it.", "Can you change your estimate of the situation?", "Marcus Aurelius", "Life"),
    ("The focus", "Concentrate every minute like a Roman—like a man—on doing what's in front of you with precise and genuine seriousness.", "What is right in front of you?", "Marcus Aurelius", "Work"),
    ("The judgment", "When you judge another, you do not define them, you define yourself.", "What do your judgments say about you?", "Wayne Dyer", "Relationships"),
    ("The beginning", "The secret of getting ahead is getting started.", "What do you need to start?", "Mark Twain", "Work"),
    ("The true wealth", "He is richest who is content with the least.", "Are you content with what you have?", "Socrates", "Simplicity"),
    ("The unknown", "The oldest and strongest emotion of mankind is fear, and the oldest and strongest kind of fear is fear of the unknown.", "What unknown are you fearing?", "H.P. Lovecraft", "Life"),
    ("The stillness", "Within you, there is a stillness and a sanctuary to which you can retreat at any time and be yourself.", "Have you visited your sanctuary today?", "Hermann Hesse", "Solitude"),
    ("The acceptance", "Accept the things to which fate binds you, and love the people with whom fate brings you together, but do so with all your heart.", "Who are you bound to love today?", "Marcus Aurelius", "Relationships"),
    ("The daily life", "How we spend our days is, of course, how we spend our lives.", "How are you spending today?", "Annie Dillard", "Time"),
    ("The obstacle", "A gem cannot be polished without friction, nor a man perfected without trials.", "What trial is polishing you?", "Seneca", "Life"),
    ("The true freedom", "Freedom is the only worthy goal in life. It is won by disregarding things that lie beyond our control.", "What can you stop trying to control?", "Epictetus", "Simplicity"),
    ("The changing world", "The universe is change; our life is what our thoughts make it.", "What are your thoughts making of your life today?", "Marcus Aurelius", "Life"),
    ("The simple truth", "Truth is ever to be found in simplicity, and not in the multiplicity and confusion of things.", "Where is the simplicity in your current confusion?", "Isaac Newton", "Simplicity"),
    ("The solitude", "I live in that solitude which is painful in youth, but delicious in the years of maturity.", "Is your solitude delicious?", "Albert Einstein", "Solitude"),
    ("The silent tree", "Trees are poems that the earth writes upon the sky.", "What poem is the earth writing for you today?", "Kahlil Gibran", "Nature & Seasons"),
    ("The slow walk", "An early-morning walk is a blessing for the whole day.", "Have you taken a walk today?", "Henry David Thoreau", "Time"),
    ("The letting go", "Breathe. Let go. And remind yourself that this very moment is the only one you know you have for sure.", "Can you let go and just be in this moment?", "Oprah Winfrey", "Time"),
    ("The reflection", "Life can only be understood backwards; but it must be lived forwards.", "Are you trying to understand the future before living it?", "Søren Kierkegaard", "Life"),
    ("The unseen", "The most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.", "What beautiful thing are you feeling today?", "Helen Keller", "Life"),
    ("The inner self", "Who looks outside, dreams; who looks inside, awakes.", "Are you awake to your inner self?", "Carl Jung", "Solitude"),
    ("The patience", "Rivers know this: there is no hurry. We shall get there some day.", "What are you rushing toward?", "A.A. Milne", "Nature & Seasons"),
    ("The friendship", "A single rose can be my garden... a single friend, my world.", "Who is the friend that makes up your world?", "Leo Buscaglia", "Relationships"),
    ("The peace", "Peace comes from within. Do not seek it without.", "Where are you seeking peace?", "Buddha", "Solitude"),
    ("The simple joy", "Find ecstasy in life; the mere sense of living is joy enough.", "Are you enjoying the mere sense of living?", "Emily Dickinson", "Life"),
    ("The quiet heart", "Keep your heart clear and transparent, and you will never be bound.", "What is clouding your heart today?", "Paramahansa Yogananda", "Simplicity"),
    ("The unwritten", "There is no greater agony than bearing an untold story inside you.", "What story needs to be told?", "Maya Angelou", "Life"),
    ("The daily grace", "Every day we are engaged in a miracle which we don't even recognize: a blue sky, white clouds, green leaves, the black, curious eyes of a child.", "What miracle did you fail to recognize today?", "Thich Nhat Hanh", "Nature & Seasons"),
    ("The gentle approach", "Nothing is so strong as gentleness, nothing so gentle as real strength.", "Where can you apply gentleness today?", "Francis de Sales", "Relationships"),
    ("The silence", "In the attitude of silence the soul finds the path in a clearer light.", "What path is the silence illuminating?", "Mahatma Gandhi", "Solitude"),
    ("The simplicity", "Simplicity is the ultimate sophistication.", "How can you be more sophisticated through simplicity?", "Leonardo da Vinci", "Simplicity"),
    ("The steady mind", "A mind that is unruffled by the changes of the world is a mind that is free.", "Is your mind ruffled by the world today?", "Bhagavad Gita", "Solitude"),
    ("The clear path", "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.", "Where is your mind concentrated right now?", "Buddha", "Time")
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
