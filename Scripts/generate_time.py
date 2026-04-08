import json
import uuid

quotes = [
    ("The pace", "Walking slowly does not mean you will never arrive. It means you will not be exhausted when you do.", "Where are you walking too fast?", None),
    ("The hour", "An hour spent doing nothing is not a wasted hour. It is a necessary reset.", "When can you schedule an hour of nothing?", None),
    ("The deadline", "Most deadlines are entirely imaginary.", "What imaginary deadline is stressing you out?", None),
    ("The past", "You cannot edit the past, no matter how much time you spend reading it.", "What chapter are you ready to stop re-reading?", None),
    ("The future", "Worrying about tomorrow simply ruins today.", "What future event is stealing your current peace?", None),
    ("The waiting room", "Waiting is only frustrating if you believe you should already be somewhere else.", "Can you simply be in the waiting room?", None),
    ("The slow growth", "A tree does not grow in a day, but it is growing every day.", "What slow progress are you overlooking?", None),
    ("The late start", "You are not too late. You are exactly where you need to be to begin.", "What is it time to begin?", None),
    ("The urgency", "If it is truly urgent, someone will call. Otherwise, it can wait.", "What are you treating as urgent that is actually just an interruption?", None),
    ("The present", "The present moment is the only place where anything actually happens.", "Are you here right now?", None),
    ("The lost time", "Time spent enjoying yourself is not lost time.", "What did you enjoy doing today?", None),
    ("The hurry", "Hurrying usually causes more problems than it solves.", "What mistake did hurrying cause recently?", None),
    ("The long term", "In ten years, this current emergency will be entirely forgotten.", "How much does this actually matter?", None),
    ("The pause", "A five-minute pause can change the trajectory of an entire afternoon.", "Can you take five minutes right now?", None),
    ("The evening", "The evening is not an extension of the workday. It is the beginning of your time.", "How do you claim your evening?", None),
    ("The morning", "A slow morning is a protective shield against a chaotic day.", "How can you slow down your morning?", None),
    ("The passing years", "The years feel fast, but the days are long. Pay attention to the days.", "What did you notice about today?", None),
    ("The schedule", "A full schedule is often a sign of a scattered mind, not a productive life.", "What can you remove from your schedule?", None),
    ("The timeless", "Some things—like a good conversation or a sunset—exist completely outside of time.", "What timeless thing did you experience recently?", None),
    ("The rush hour", "You do not have to participate in the rush hour, physically or mentally.", "How can you step out of the rush?", None),
    ("The right time", "There is rarely a perfect time. There is only the time you decide to act.", "What are you waiting for the 'perfect time' to do?", None),
    ("The memory", "A memory is simply a moment you decided to keep.", "What moment will you keep from today?", None),
    ("The aging", "Aging is a privilege denied to many. Wear your years with gratitude.", "What are you grateful to have lived long enough to see?", None),
    ("The season", "Every season has an end. This one will, too.", "Are you in a difficult season or a joyful one?", None),
    ("The half hour", "You can accomplish an incredible amount of reading, resting, or walking in just thirty minutes.", "How will you spend your next free half hour?", None),
    ("The delay", "A delay is often a hidden layer of protection.", "What delay actually helped you?", None),
    ("The fast forward", "You cannot fast forward through the difficult parts without also missing the growth.", "What are you trying to fast forward through?", None),
    ("The ancient", "Standing next to something very old—a tree, a mountain, an ocean—puts your own timeline into perspective.", "What ancient thing puts your life in perspective?", None),
    ("The ticking clock", "The clock only ticks loudly when you are listening to it.", "What helps you forget about the clock?", None),
    ("The early arrival", "Arriving ten minutes early provides a quiet buffer before the world demands your attention.", "When can you arrive early just to sit?", None),
    ("The transition", "The time between ending one thing and starting another is sacred.", "Do you allow yourself transition time?", None),
    ("The long game", "Small, daily efforts outpace massive, occasional bursts of energy every time.", "What small daily effort are you committed to?", None),
    ("The rewind", "You cannot rewind the tape. You can only decide what happens in the next scene.", "What happens next?", None),
    ("The empty afternoon", "An empty afternoon is a luxury, not a failure of planning.", "Do you have any empty afternoons this week?", None),
    ("The rhythm", "Find your own rhythm. You do not have to march to the beat of the loudest drum.", "What is your natural rhythm?", None),
    ("The sunset", "The day ends whether you finished everything on your list or not.", "Can you let the day end peacefully?", None),
    ("The decade", "Think about who you were ten years ago. You have already lived multiple lives.", "What version of yourself are you currently living?", None),
    ("The overnight", "Many problems solve themselves if you simply sleep on them.", "What problem needs to be slept on?", None),
    ("The brief encounter", "A ten-second interaction can lift someone's entire day.", "Who did you lift up today?", None),
    ("The marathon", "Life is a marathon, but it is entirely acceptable to walk for a few miles.", "Where do you need to walk instead of run?", None),
    ("The time machine", "A photograph is a simple time machine. Use it to visit, not to live.", "What photograph brings you comfort?", None),
    ("The patience", "Patience is not simply waiting; it is how you behave while you wait.", "How are you behaving in the waiting?", None),
    ("The generation", "You are the bridge between the generations before you and the generations after.", "What are you passing on?", None),
    ("The unmeasured time", "The best moments in life are the ones where you completely lose track of time.", "When was the last time you lost track of time?", None),
    ("The slow fade", "Change rarely happens overnight. It is a slow fade from one state to another.", "What is slowly fading in your life?", None),
    ("The boundary of today", "Today's energy is only meant for today's problems.", "Are you spending today's energy on tomorrow?", None),
    ("The deep breath", "A single deep breath takes only a few seconds, but it resets your entire nervous system.", "Take a deep breath right now.", None),
    ("The time well spent", "Time is only wasted if you believe it was wasted.", "What 'wasted' time was actually exactly what you needed?", None),
    ("The quiet ticking", "Let the clock tick. You do not have to keep pace with it.", "Can you let time pass without trying to use it?", None),
    ("The enduring", "What is true today will likely be true tomorrow.", "What constant truth anchors you?", None)
]

# Load existing wisdom
with open("PocketWisdom/Resources/wisdom.json", "r") as f:
    existing = json.load(f)

cards = []
for title, body, reflection, author in quotes:
    cards.append({
        "id": str(uuid.uuid4()),
        "category": "Time",
        "title": title,
        "body": body,
        "reflection": reflection,
        "author": author
    })

merged = existing + cards
with open("PocketWisdom/Resources/wisdom.json", "w") as f:
    json.dump(merged, f, indent=2)

print(f"Generated 50 Time cards. Total cards: {len(merged)}")
