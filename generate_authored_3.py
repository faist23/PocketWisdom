import json
import uuid

quotes = [
    ("The unsaid", "Better to trip with the feet than with the tongue.", "What are you about to say that doesn't need to be said?", "Zeno of Citium", "Relationships"),
    ("The true work", "First say to yourself what you would be; and then do what you have to do.", "What do you have to do today to be who you want to be?", "Epictetus", "Work"),
    ("The quiet walk", "All truly great thoughts are conceived while walking.", "When can you take a quiet walk today?", "Friedrich Nietzsche", "Solitude"),
    ("The acceptance", "He who does not content himself with what he has, would not be contented with what he would like to have.", "Can you find contentment exactly where you are?", "Socrates", "Simplicity"),
    ("The morning light", "Every morning we are born again. What we do today is what matters most.", "What will you do with today's new beginning?", "Buddha", "Time"),
    ("The inner citadel", "People seek retreats for themselves in the country, by the sea, or in the mountains... But this is entirely the trait of a base person, when you can, at any moment, retreat into yourself.", "Have you retreated inward today?", "Marcus Aurelius", "Solitude"),
    ("The single task", "To do two things at once is to do neither.", "What is the one thing you need to focus on right now?", "Publilius Syrus", "Work"),
    ("The comparison", "Do not spoil what you have by desiring what you have not.", "Are you spoiling the present by looking at someone else's life?", "Epicurus", "Life"),
    ("The gentle rain", "The drop of rain maketh a hole in the stone, not by violence, but by oft falling.", "What quiet persistence are you practicing?", "Hugh Latimer", "Nature & Seasons"),
    ("The unforced life", "Tension is who you think you should be. Relaxation is who you are.", "Where are you holding tension right now?", "Chinese Proverb", "Life"),
    ("The long view", "Time is a created thing. To say 'I don't have time,' is like saying, 'I don't want to.'", "What are you choosing not to make time for?", "Lao Tzu", "Time"),
    ("The quiet connection", "We have two ears and one mouth so that we can listen twice as much as we speak.", "Who needs you to simply listen to them today?", "Epictetus", "Relationships"),
    ("The present", "Life is what happens to us while we are making other plans.", "Are you missing today because you are planning for tomorrow?", "Allen Saunders", "Life"),
    ("The heavy load", "There is only one way to happiness and that is to cease worrying about things which are beyond the power of our will.", "What is beyond your control that you need to put down?", "Epictetus", "Simplicity"),
    ("The changing seasons", "To be interested in the changing seasons is a happier state of mind than to be hopelessly in love with spring.", "Can you appreciate the season you are in right now?", "George Santayana", "Nature & Seasons"),
    ("The deep breath", "Whenever you are angry, be assured that it is not only a present evil, but that you have increased a habit.", "Can you take a breath and break the habit?", "Epictetus", "Life"),
    ("The true measure", "A man is rich in proportion to the number of things which he can afford to let alone.", "What can you afford to just let alone?", "Henry David Thoreau", "Simplicity"),
    ("The quiet room", "I have often wondered how it is that every man loves himself more than all the rest of men, but yet sets less value on his own opinion of himself than on the opinion of others.", "Why do you value their opinion more than your own?", "Marcus Aurelius", "Solitude"),
    ("The steady pace", "It does not matter how slowly you go as long as you do not stop.", "Are you judging your pace instead of your persistence?", "Confucius", "Work"),
    ("The letting go", "He is a wise man who does not grieve for the things which he has not, but rejoices for those which he has.", "What do you have right now that you can rejoice over?", "Epictetus", "Life"),
    ("The inner quiet", "Silence is the sleep that nourishes wisdom.", "Are you getting enough silent sleep?", "Francis Bacon", "Solitude"),
    ("The simple truth", "Nature is pleased with simplicity. And nature is no dummy.", "How can you align more with nature's simplicity?", "Isaac Newton", "Nature & Seasons"),
    ("The reflection", "We do not learn from experience... we learn from reflecting on experience.", "What recent experience needs your reflection?", "John Dewey", "Life"),
    ("The daily work", "Nothing is particularly hard if you divide it into small jobs.", "What big thing can you divide into a small job today?", "Henry Ford", "Work"),
    ("The unknown", "You can never cross the ocean unless you have the courage to lose sight of the shore.", "What familiar shore do you need to lose sight of?", "Christopher Columbus", "Life"),
    ("The gentle word", "Kind words do not cost much. Yet they accomplish much.", "Who can you offer a kind word to today?", "Blaise Pascal", "Relationships"),
    ("The true failure", "The only real mistake is the one from which we learn nothing.", "What did your last mistake teach you?", "Henry Ford", "Life"),
    ("The simple life", "Simplicity is the final achievement. After one has played a vast quantity of notes and more notes, it is simplicity that emerges as the crowning reward of art.", "Are you playing too many notes?", "Frederic Chopin", "Simplicity"),
    ("The waiting", "All human wisdom is summed up in two words: wait and hope.", "Are you capable of simply waiting?", "Alexandre Dumas", "Time"),
    ("The present focus", "You must be completely awake in the present to enjoy the gift of your life.", "Are you awake to this exact moment?", "Thich Nhat Hanh", "Time")
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
