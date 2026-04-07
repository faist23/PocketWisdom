import json
import uuid

quotes = [
    ("The unspoken", "You do not always need to fill the silence with another person. Shared quiet is a sign of trust.", "Who can you sit quietly with?", None),
    ("The apology", "An apology without a change in behavior is simply a manipulation.", "Where do you need to see a change?", None),
    ("The seasons of friendship", "Not all friendships are built to last a lifetime. Some are beautiful for exactly one season.", "What seasonal friendship are you grateful for?", None),
    ("The effort", "A relationship should not feel like an endless negotiation. The good ones flow.", "Which relationship feels effortless?", None),
    ("The grace", "Give people the grace to be imperfect. You require that same grace yourself.", "Who needs your grace today?", None),
    ("The listener", "Listening to understand is fundamentally different than listening to reply.", "When did you last truly listen?", None),
    ("The distance", "Distance does not break a strong connection, but it reveals a weak one.", "What connection has survived the distance?", None),
    ("The boundary", "Setting a boundary is an act of love. It tells the other person how to stay in your life.", "What boundary needs communicating?", None),
    ("The release", "You cannot hold onto someone who is determined to walk away.", "Who are you trying to hold onto?", None),
    ("The celebration", "Pay close attention to who genuinely celebrates your success.", "Who claps the loudest for you?", None),
    ("The history", "A shared history is valuable, but it is not a reason to stay in a harmful dynamic.", "What history are you holding onto out of obligation?", None),
    ("The mirror", "The people closest to you are often mirrors reflecting your own character back to you.", "What do your closest relationships reflect?", None),
    ("The simple text", "A quick message to say 'I was thinking of you' can change someone's entire week.", "Who can you text right now?", None),
    ("The attention", "Your undivided attention is the rarest and most valuable gift you can offer.", "Who deserves your full attention today?", None),
    ("The assumption", "Assuming the best of someone's intentions saves a tremendous amount of unnecessary pain.", "Where can you assume positive intent?", None),
    ("The familiar", "There is a profound comfort in being entirely known by someone else.", "Who knows you best?", None),
    ("The argument", "In a good relationship, it is the two of you against the problem, not you against each other.", "What problem needs a unified front?", None),
    ("The small things", "Love is rarely found in grand gestures. It is built in the daily, mundane acts of care.", "What small act of care did you receive today?", None),
    ("The drift", "It is natural for people to drift apart as they grow. It does not mean the connection was a failure.", "Who have you drifted from peacefully?", None),
    ("The honesty", "A hard truth delivered with kindness is always better than a comforting lie.", "What hard truth needs to be spoken?", None),
    ("The arrival", "Notice how your body feels when a specific person enters the room. Your body knows.", "Who makes your shoulders drop when they arrive?", None),
    ("The empty cup", "You cannot pour into someone else's life if your own cup is completely empty.", "How are you refilling your own cup?", None),
    ("The quiet support", "Sometimes the best support is just sitting beside someone in the dark.", "Who needs you to just sit with them?", None),
    ("The comparison", "Your relationship does not need to look like anyone else's relationship.", "What is uniquely yours?", None),
    ("The acceptance", "You cannot change another person. You can only love them, or leave them.", "Where are you trying to force a change?", None),
    ("The invitation", "An invitation is a risk. Be gentle with people who invite you into their lives.", "Who has recently invited you in?", None),
    ("The easy laugh", "A shared sense of humor is a powerful glue.", "Who makes you laugh effortlessly?", None),
    ("The reunion", "The best reunions feel as though no time has passed at all.", "Who can you pick right back up with?", None),
    ("The space", "A healthy relationship provides enough space for both people to grow as individuals.", "Do you have enough space?", None),
    ("The hidden burden", "Everyone you meet is carrying a burden you know absolutely nothing about.", "How does this change the way you interact?", None),
    ("The default", "Make kindness your default reaction.", "Where is your default something else?", None),
    ("The shared meal", "Breaking bread with someone is one of the oldest forms of connection.", "Who can you share a meal with?", None),
    ("The old wounds", "Do not bleed on people who did not cut you.", "Are you projecting an old wound?", None),
    ("The foundation", "Trust takes years to build, seconds to break, and a lifetime to repair.", "Where is your trust absolute?", None),
    ("The letting go", "Forgiving someone does not mean you have to invite them back to your table.", "Who have you forgiven from a distance?", None),
    ("The small circle", "As you age, your circle gets smaller, but the connections grow much deeper.", "Who is in your inner circle?", None),
    ("The soft landing", "A true friend provides a soft landing when the world has been hard.", "Who is your soft landing?", None),
    ("The unspoken expectation", "An unspoken expectation is simply a premeditated resentment.", "What expectation needs to be voiced?", None),
    ("The right words", "You do not always need to have the right words. 'I am here' is often enough.", "Who needs to hear that you are there?", None),
    ("The reflection", "We see in others what we recognize in ourselves.", "What beauty do you recognize in someone else?", None),
    ("The slow fade", "Sometimes a relationship doesn't explode; it just slowly fades away. That is okay.", "What fade are you accepting?", None),
    ("The simple request", "Asking for what you need is the kindest thing you can do for a partner.", "What do you need to ask for?", None),
    ("The loyalty", "Loyalty is not blind obedience. It is telling the truth when it is difficult.", "Who do you trust to tell you the truth?", None),
    ("The energy", "Notice the people who give you energy, and the people who drain it.", "Who gives you energy?", None),
    ("The common ground", "You do not have to agree on everything to treat someone with profound respect.", "Where can you find common ground?", None),
    ("The chosen family", "The family you choose is just as valid as the family you were born into.", "Who is your chosen family?", None),
    ("The pause", "Before you react in anger, take one breath. It changes everything.", "Where do you need a breath?", None),
    ("The open door", "Leave the door open for the people who truly matter.", "Is your door open?", None),
    ("The long view", "A momentary disagreement is a tiny blip on a lifelong timeline.", "Does this disagreement actually matter?", None),
    ("The anchor", "Some people are anchors, holding you steady in the storm.", "Who is your anchor?", None)
]

# Load existing wisdom
with open("PocketWisdom/Resources/wisdom.json", "r") as f:
    existing = json.load(f)

cards = []
for title, body, reflection, author in quotes:
    cards.append({
        "id": str(uuid.uuid4()),
        "category": "Relationships",
        "title": title,
        "body": body,
        "reflection": reflection,
        "author": author
    })

merged = existing + cards
with open("PocketWisdom/Resources/wisdom.json", "w") as f:
    json.dump(merged, f, indent=2)

print(f"Generated 50 Relationships cards. Total cards: {len(merged)}")
