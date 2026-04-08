import json
import uuid

quotes = [
    # Naval Ravikant
    ("Peace", "Peace is happiness at rest, and happiness is peace in motion.", "Are you chasing happiness or cultivating peace?", "Naval Ravikant", "Life"),
    ("Desire", "Desire is a contract you make with yourself to be unhappy until you get what you want.", "What contract of unhappiness can you tear up today?", "Naval Ravikant", "Simplicity"),
    ("Wealth", "Wealth is having assets that earn while you sleep.", "Are you building wealth or just trading time for money?", "Naval Ravikant", "Work"),

    # Jiddu Krishnamurti
    ("Observation", "The highest form of human intelligence is to observe yourself without judgment.", "Can you watch your thoughts today without criticizing them?", "Jiddu Krishnamurti", "Solitude"),
    ("Freedom", "Freedom from the desire for an answer is essential to the understanding of a problem.", "Can you sit with a problem without rushing to solve it?", "Jiddu Krishnamurti", "Life"),

    # George Bernard Shaw
    ("Creating yourself", "Life isn't about finding yourself. Life is about creating yourself.", "What aspect of yourself are you actively creating right now?", "George Bernard Shaw", "Life"),
    ("Youth", "Youth is wasted on the young.", "How can you bring youthful energy to your current age?", "George Bernard Shaw", "Time"),

    # Oscar Wilde
    ("Being yourself", "Be yourself; everyone else is already taken.", "Where are you trying to be someone you're not?", "Oscar Wilde", "Solitude"),
    ("Experience", "Experience is simply the name we give our mistakes.", "What valuable 'experience' have you gained recently?", "Oscar Wilde", "Life"),

    # Friedrich Nietzsche
    ("Why and How", "He who has a why to live for can bear almost any how.", "What is your 'why'?", "Friedrich Nietzsche", "Life"),
    ("The abyss", "And if thou gaze long into an abyss, the abyss will also gaze into thee.", "What dark thoughts are you allowing to consume you?", "Friedrich Nietzsche", "Solitude"),

    # Arthur Schopenhauer
    ("Talent vs Genius", "Talent hits a target no one else can hit; Genius hits a target no one else can see.", "Are you aiming for the visible or the invisible?", "Arthur Schopenhauer", "Work"),
    ("Compassion", "Compassion is the basis of morality.", "How can you show more compassion today?", "Arthur Schopenhauer", "Relationships"),

    # Simone de Beauvoir
    ("One's life", "Change your life today. Don't gamble on the future, act now, without delay.", "What action are you delaying?", "Simone de Beauvoir", "Time"),

    # Jean-Paul Sartre
    ("Freedom", "Man is condemned to be free; because once thrown into the world, he is responsible for everything he does.", "Are you taking full responsibility for your freedom?", "Jean-Paul Sartre", "Life"),

    # Sylvia Plath
    ("The fig tree", "I took a deep breath and listened to the old brag of my heart. I am, I am, I am.", "Can you simply appreciate the fact that you exist right now?", "Sylvia Plath", "Life"),

    # Rumi
    ("The Guest House", "This being human is a guest house. Every morning a new arrival.", "How are you treating the 'guests' (emotions) arriving today?", "Rumi", "Life"),
    ("Silence", "Listen to silence. It has so much to say.", "What is the silence telling you?", "Rumi", "Solitude"),

    # Lao Tzu
    ("Knowing others", "Knowing others is intelligence; knowing yourself is true wisdom.", "How well do you know yourself?", "Lao Tzu", "Solitude"),
    ("Mastering yourself", "Mastering others is strength; mastering yourself is true power.", "Where do you need to exercise more self-mastery?", "Lao Tzu", "Work"),

    # Marcus Aurelius
    ("Revenge", "The best revenge is not to be like your enemy.", "Are you adopting the negative traits of those who wrong you?", "Marcus Aurelius", "Relationships"),
    ("Quality of life", "The happiness of your life depends upon the quality of your thoughts.", "What is the quality of your current thoughts?", "Marcus Aurelius", "Life"),

    # Epictetus
    ("Two ears, one mouth", "We have two ears and one mouth so that we can listen twice as much as we speak.", "Are you listening enough?", "Epictetus", "Relationships"),

    # Seneca
    ("Living", "As is a tale, so is life: not how long it is, but how good it is, is what matters.", "Is your tale a good one so far?", "Seneca", "Life"),

    # Ovid
    ("Endurance", "Endure and persist; this pain will turn to your good by and by.", "What current pain do you need to simply endure?", "Ovid", "Life"),

    # Horace
    ("Seize the day", "Carpe diem, quam minimum credula postero. (Seize the day, put very little trust in tomorrow.)", "How are you seizing today?", "Horace", "Time"),

    # Virgil
    ("Fortune", "Fortune favors the bold.", "Where do you need to be bolder?", "Virgil", "Work"),

    # Cicero
    ("A room without books", "A room without books is like a body without a soul.", "What are you feeding your mind with?", "Cicero", "Life"),

    # Sun Tzu
    ("Winning", "The supreme art of war is to subdue the enemy without fighting.", "How can you resolve a current conflict peacefully?", "Sun Tzu", "Relationships"),
    ("Knowing the enemy", "If you know the enemy and know yourself, you need not fear the result of a hundred battles.", "Do you truly understand what you are up against?", "Sun Tzu", "Work"),

    # Miyamoto Musashi
    ("The Way", "There is nothing outside of yourself that can ever enable you to get better, stronger, richer, quicker, or smarter. Everything is within.", "Are you looking outside for what is already inside?", "Miyamoto Musashi", "Solitude"),

    # Haruki Murakami
    ("The storm", "And once the storm is over, you won't remember how you made it through, how you managed to survive. You won't even be sure, whether the storm is really over. But one thing is certain. When you come out of the storm, you won't be the same person who walked in. That's what this storm's all about.", "How is the current storm changing you?", "Haruki Murakami", "Life"),

    # Gabriel García Márquez
    ("Smiling", "Don't cry because it's over, smile because it happened.", "What ending can you view with a smile of gratitude?", "Gabriel García Márquez", "Time"),

    # Jorge Luis Borges
    ("Paradise", "I have always imagined that Paradise will be a kind of library.", "Where is your paradise?", "Jorge Luis Borges", "Solitude")
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