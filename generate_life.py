import json
import uuid

quotes = [
    ("The middle chapters", "The middle of the story is rarely as dramatic as the beginning, but it is where the actual living happens.", "What is beautiful about the chapter you are in right now?", None),
    ("Heavy things", "You don’t have to carry everything you pick up.", "What can you set down today?", None),
    ("Arrival", "There is no final destination where everything is permanently sorted out.", "Can you be okay with things being in process?", None),
    ("Unnoticed joy", "Most of your best days passed by without you realizing they were the best days.", "What makes today a good day?", None),
    ("Changing minds", "It is a quiet relief to realize you are allowed to change your mind as you grow.", "What have you changed your mind about recently?", None),
    ("The noise", "Not every piece of information requires your reaction.", "What can you safely ignore today?", None),
    ("Tides", "Like the ocean, your energy and capacity will have high and low tides.", "Are you fighting your current tide?", None),
    ("Expectations", "Much of our disappointment comes from expecting a different reality than the one we are in.", "What happens when you accept what is actually happening?", None),
    ("Softening", "Life has a way of softening the hard edges we used to protect ourselves.", "Where have you become softer?", None),
    ("Ordinary days", "A deeply ordinary day is a profoundly successful day.", "What was the best ordinary moment today?", None),
    ("Letting go", "Some things are meant to be in your life for a season, not forever.", "What season has naturally ended?", None),
    ("The rush", "We spend so much of our lives rushing toward a future that is entirely unknown.", "What is worth savoring right now?", None),
    ("Certainty", "As you age, you realize how little you actually know for certain—and that is a comfortable place to be.", "What are you okay with not knowing?", None),
    ("Small worlds", "Your world doesn't need to be large to be deeply fulfilling.", "Who and what makes up your small world?", None),
    ("The observer", "You are the observer of your thoughts, not the thoughts themselves.", "What thoughts are passing through right now?", None),
    ("Forgiveness", "Forgiveness is often just accepting that the past cannot be changed.", "What part of the past can you leave in the past?", None),
    ("Daily bread", "Joy is usually found in the daily, repetitive acts of living.", "What repetitive task brings you a strange sense of peace?", None),
    ("The current", "Swimming against the current exhausts you. Floating carries you.", "Where are you fighting the current?", None),
    ("Unfinished business", "It is perfectly fine to have a life full of unfinished projects and unread books.", "What unfinished thing are you completely okay with?", None),
    ("Inner quiet", "The world will always be loud. The quiet has to come from within.", "How do you find your inner quiet?", None),
    ("Grace", "Give yourself the same grace you so easily extend to your oldest friends.", "Where are you being too hard on yourself?", None),
    ("The garden", "A garden doesn't bloom all year round. Neither do you.", "Are you in a season of blooming or a season of resting?", None),
    ("Good enough", "The pursuit of 'perfect' is the enemy of 'good enough'.", "Where in your life is 'good enough' absolutely perfect?", None),
    ("Comparisons", "Measuring your life against someone else's highlight reel is a guaranteed way to feel behind.", "What is uniquely beautiful about your actual life?", None),
    ("Deep roots", "Trees grow their deepest roots during the quiet, dormant winter.", "What is growing within you during this quiet time?", None),
    ("The fix", "Not everything that feels uncomfortable is a problem that needs to be fixed.", "Can you sit with the discomfort for a moment?", None),
    ("Approval", "The older you get, the less appealing the approval of strangers becomes.", "Whose opinion actually matters to you now?", None),
    ("Second halves", "The second half of life is about subtraction, not addition.", "What are you subtracting?", None),
    ("The pause", "There is immense power in a five-second pause before responding.", "Where could a pause change the outcome?", None),
    ("Accumulation", "We spend decades accumulating things, only to realize freedom lies in having less.", "What could you give away today?", None),
    ("The destination", "The joy of a walk is the walking, not the arriving.", "Where can you just walk today without needing to arrive?", None),
    ("Predictability", "There is a profound comfort in a predictable evening.", "What is your favorite predictable routine?", None),
    ("Hidden strength", "You have survived 100% of your bad days.", "What challenge did you survive that made you stronger?", None),
    ("The mirror", "How you treat the world is a reflection of how you treat yourself.", "Are you treating yourself kindly today?", None),
    ("Unspoken words", "Many things are better left unsaid.", "What did you wisely choose not to say recently?", None),
    ("The map", "There is no map for the rest of your life. You are drawing it as you go.", "What direction feels right today?", None),
    ("Shadows", "You cannot have light without casting a shadow.", "Can you accept your own shadows?", None),
    ("The weather", "You cannot control the weather, but you can choose your coat.", "How are you preparing for today's 'weather'?", None),
    ("Echoes", "The echoes of past mistakes fade when you stop shouting into the canyon.", "What echo are you ready to stop listening to?", None),
    ("The harvest", "You are currently harvesting what you planted years ago.", "What did you plant that you are grateful for now?", None),
    ("The compass", "Your intuition is a quieter, slower compass than your anxiety.", "What is your quiet intuition telling you?", None),
    ("The audience", "You are the only permanent audience member of your life.", "Are you living a life that you enjoy watching?", None),
    ("Friction", "Friction causes wear, but it also polishes stone.", "What friction is polishing you?", None),
    ("The attic", "Cleaning out the attic of your mind takes time, but the extra space is worth it.", "What old thought are you ready to throw away?", None),
    ("Sunrise", "The sun rises whether you are awake to see it or not.", "What beautiful things are happening without your participation?", None),
    ("The detour", "Sometimes the wrong train takes you to the right station.", "What detour turned out to be a blessing?", None),
    ("The script", "You do not have to read the script that was handed to you.", "What part of the script are you rewriting?", None),
    ("The anchor", "When the surface is stormy, drop an anchor to the quiet depths.", "What is your anchor?", None),
    ("The horizon", "The horizon always moves as you walk toward it.", "What are you chasing that will always move?", None),
    ("The evening", "The day is done. You cannot change it now.", "Can you let today be finished?", None)
]

cards = []
for title, body, reflection, author in quotes:
    cards.append({
        "id": str(uuid.uuid4()),
        "category": "Life",
        "title": title,
        "body": body,
        "reflection": reflection,
        "author": author
    })

with open("PocketWisdom/Resources/life_batch_1.json", "w") as f:
    json.dump(cards, f, indent=2)

print("Generated life_batch_1.json")
