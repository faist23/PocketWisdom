import json
import uuid
import os

new_quotes = [
    # --- LIFE (35) ---
    (
        "Rarity of Living",
        "To live is the rarest thing in the world. Most people exist, that is all.",
        "What makes you feel truly alive rather than just existing?",
        "Oscar Wilde",
        "Life"
    ),
    (
        "Mind's Creation",
        "The mind is everything. What you think you become.",
        "How are your thoughts shaping your current reality?",
        "Buddha",
        "Life"
    ),
    (
        "The Strength of Why",
        "He who has a why to live can bear almost any how.",
        "What is the central purpose that keeps you moving through hardship?",
        "Friedrich Nietzsche",
        "Life"
    ),
    (
        "True Wisdom",
        "Knowing others is intelligence; knowing yourself is true wisdom.",
        "What part of your own nature did you understand more clearly today?",
        "Lao Tzu",
        "Life"
    ),
    (
        "Nightly Inquiry",
        "Every night before going to sleep, ask yourself: what weakness did I overcome today?",
        "What small victory did you achieve today over a personal vulnerability?",
        "Seneca",
        "Life"
    ),
    (
        "Loving the Questions",
        "Be patient toward all that is unsolved in your heart and try to love the questions themselves.",
        "What unresolved question in your life can you learn to sit with peacefully?",
        "Rainer Maria Rilke",
        "Life"
    ),
    (
        "Power of Response",
        "It's not what happens to you, but how you react to it that matters.",
        "Think of a recent setback. How did your reaction change its impact?",
        "Epictetus",
        "Life"
    ),
    (
        "Inner Challenge",
        "When we are no longer able to change a situation, we are challenged to change ourselves.",
        "What difficult situation in your life requires you to adapt your own attitude?",
        "Viktor E. Frankl",
        "Life"
    ),
    (
        "Unfold Your Myth",
        "Don't be satisfied with stories, how things have gone with others. Unfold your own myth.",
        "What unique path are you carving out that belongs solely to you?",
        "Rumi",
        "Life"
    ),
    (
        "Wisdom's Companion",
        "Patience is the companion of wisdom.",
        "Where in your life do you need to cultivate more gentle patience?",
        "Saint Augustine",
        "Life"
    ),
    (
        "Give Me Truth",
        "Rather than love, than money, than fame, give me truth.",
        "What core truth are you holding onto that guides your daily decisions?",
        "Henry David Thoreau",
        "Life"
    ),
    (
        "Joining the Dance",
        "The only way to make sense out of change is to plunge into it, move with it, and join the dance.",
        "What transition are you currently resisting instead of flowing with?",
        "Alan Watts",
        "Life"
    ),
    (
        "Conscious Choice",
        "I am not what happened to me, I am what I choose to become.",
        "What choice will you make today that defines who you are becoming?",
        "Carl Jung",
        "Life"
    ),
    (
        "Inner Harmony",
        "He who lives in harmony with himself lives in harmony with the universe.",
        "What internal conflict can you resolve to find peace within your heart?",
        "Marcus Aurelius",
        "Life"
    ),
    (
        "The Light Within",
        "It is during our darkest moments that we must focus to see the light.",
        "Where can you find a small glimmer of hope in a current challenge?",
        "Aristotle",
        "Life"
    ),
    (
        "The Greatest Glory",
        "Our greatest glory is not in never falling, but in rising every time we fall.",
        "Think of a time you bounced back. What did that teach you about your strength?",
        "Confucius",
        "Life"
    ),
    (
        "Living Consciously",
        "An unexamined life is not worth living.",
        "What daily habit or belief is worth questioning today?",
        "Socrates",
        "Life"
    ),
    (
        "Depth of Life",
        "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived.",
        "How can you bring a small act of honor or compassion to your day?",
        "Ralph Waldo Emerson",
        "Life"
    ),
    (
        "Unfearing Heart",
        "The only thing we have to fear is fear itself.",
        "What fear is holding you back from taking a meaningful step?",
        "Franklin D. Roosevelt",
        "Life"
    ),
    (
        "Perfect Peace",
        "Peace comes from within. Do not seek it without.",
        "What quiet practice brings you back to your inner center of peace?",
        "Buddha",
        "Life"
    ),
    (
        "Endless Dreams",
        "You are never too old to set another goal or to dream a new dream.",
        "What new goal or aspiration is quietly forming in your heart?",
        "C.S. Lewis",
        "Life"
    ),
    (
        "Eyes of the Traveler",
        "The traveler sees what he sees, the tourist sees what he has come to see.",
        "How can you look at your familiar surroundings today with the fresh, unbiased eyes of a traveler?",
        "G.K. Chesterton",
        "Life"
    ),
    (
        "Privilege of Becoming",
        "The privilege of a lifetime is to become who you truly are.",
        "In what way did you act as your most authentic self today?",
        "Carl Jung",
        "Life"
    ),
    (
        "Familiar Suffering",
        "People have a hard time letting go of their suffering. Out of a fear of the unknown, they prefer suffering that is familiar.",
        "What familiar worry or pain are you holding onto simply because it is familiar?",
        "Thich Nhat Hanh",
        "Life"
    ),
    (
        "Lightness of Being",
        "Man suffers only because he takes seriously what the gods made for fun.",
        "What heavy concern can you lighten today by finding a bit of playfulness in it?",
        "Alan Watts",
        "Life"
    ),
    (
        "Strength in Release",
        "Some of us think holding on makes us strong, but sometimes it is letting go.",
        "What attachment or expectation are you ready to let go of to find your true strength?",
        "Hermann Hesse",
        "Life"
    ),
    (
        "Weapon Against Stress",
        "The greatest weapon against stress is our ability to choose one thought over another.",
        "When a stressful thought arises today, what peaceful thought will you choose to replace it?",
        "William James",
        "Life"
    ),
    (
        "Character and Destiny",
        "Character is destiny.",
        "What choice will you make today that strengthens the character you wish to build?",
        "Heraclitus",
        "Life"
    ),
    (
        "Chosen Paths",
        "We choose our joys and our sorrows long before we experience them.",
        "What mindset are you choosing right now that will shape your future experiences?",
        "Khalil Gibran",
        "Life"
    ),
    (
        "Active Living",
        "True philosophy is not a matter of talking, but of active living.",
        "How can you put one of your deeply held principles into practice today?",
        "Seneca",
        "Life"
    ),
    (
        "Mastery of Self",
        "No man is free who is not master of himself.",
        "In what area can you exercise greater self-discipline to find your true freedom?",
        "Epictetus",
        "Life"
    ),
    (
        "Correcting the Mind",
        "If you correct your mind, the rest of your life will fall into place.",
        "What negative pattern in your thinking is ready to be corrected today?",
        "Lao Tzu",
        "Life"
    ),
    (
        "Art of Seeing",
        "The question is not what you look at, but what you see.",
        "What beautiful detail did you notice in your ordinary surroundings today?",
        "Henry David Thoreau",
        "Life"
    ),
    (
        "The Power in the Space",
        "Between stimulus and response there is a space. In that space is our power to choose our response. In our response lies our growth and our freedom.",
        "In your next interaction, can you find the tiny pause between what is said and how you reply?",
        "Viktor E. Frankl",
        "Life"
    ),
    (
        "Happiness Over Dignity",
        "I would always rather be happy than dignified.",
        "Where can you let go of trying to look perfect and just enjoy the moment?",
        "Charlotte Brontë",
        "Life"
    ),

    # --- SIMPLICITY (20) ---
    (
        "Calm and Modest",
        "A calm and modest life brings more happiness than the pursuit of success combined with constant restlessness.",
        "Where can you choose calm over a restless pursuit today?",
        "Albert Einstein",
        "Simplicity"
    ),
    (
        "Unburdening the Mind",
        "Simplicity is the ultimate sophistication.",
        "What area of your life or thinking is ready for some simplification?",
        "Leonardo da Vinci",
        "Simplicity"
    ),
    (
        "Purity of Action",
        "In character, in manner, in style, in all things, the supreme excellence is simplicity.",
        "How can you perform your tasks today with more directness and less fuss?",
        "Henry Wadsworth Longfellow",
        "Simplicity"
    ),
    (
        "Richness of Less",
        "Simplicity is making the journey of this life with just enough baggage.",
        "What material or mental baggage can you safely leave behind today?",
        "Charles Dudley Warner",
        "Simplicity"
    ),
    (
        "The Simple Art",
        "The art of art, the glory of expression and the sunshine of the light of letters, is simplicity.",
        "How can you express your thoughts more clearly and directly today?",
        "Walt Whitman",
        "Simplicity"
    ),
    (
        "Nothing in Excess",
        "Moderation in all things is the secret to a peaceful life.",
        "Where in your life would a little moderation bring you immediate relief?",
        "Plato",
        "Simplicity"
    ),
    (
        "Uncluttered Living",
        "Clutter is the physical representation of unaddressed decisions.",
        "What physical or mental space can you clear to invite fresh energy?",
        "Unknown",
        "Simplicity"
    ),
    (
        "Plain Living",
        "Plain living and high thinking are the best companions.",
        "How can you live more simply today to free up your mental bandwidth?",
        "William Wordsworth",
        "Simplicity"
    ),
    (
        "Great in Small",
        "To be simple is to be great.",
        "What small, simple act of yours has the potential for great impact today?",
        "Ralph Waldo Emerson",
        "Simplicity"
    ),
    (
        "Simple Desires",
        "He is richest who is content with the least, for content is the wealth of nature.",
        "What simple pleasure brought you the most contentment today?",
        "Socrates",
        "Simplicity"
    ),
    (
        "The Quiet Center",
        "The more simple we are, the more peaceful we become.",
        "How does simplifying your surroundings affect your internal quiet?",
        "Thomas à Kempis",
        "Simplicity"
    ),
    (
        "Pure Presence",
        "Life is simple. We complicate it by chasing what we do not need.",
        "What is one thing you are chasing that you could let go of?",
        "Lao Tzu",
        "Simplicity"
    ),
    (
        "The Gift of Simplicity",
        "Tis the gift to be simple, tis the gift to be free.",
        "In what way does simplicity feel like a release of weight for you?",
        "Shaker Hymn",
        "Simplicity"
    ),
    (
        "Natural Elegance",
        "Simplicity is the keynote of all true elegance.",
        "How can you bring a touch of simple elegance to your environment?",
        "Coco Chanel",
        "Simplicity"
    ),
    (
        "Minimal Demands",
        "It is the heart that makes a man rich. He is rich according to what he is, not according to what he has.",
        "What part of your character defines your true wealth?",
        "Henry David Beecher",
        "Simplicity"
    ),
    (
        "The Sufficient Prayer",
        "If the only prayer you ever say in your entire life is thank you, it will be enough.",
        "In what way can you express a simple, deep 'thank you' for your life today?",
        "Meister Eckhart",
        "Simplicity"
    ),
    (
        "Inner Quietness",
        "Simplicity of life, even the simplest, is a great protector of our peace.",
        "What is one complication you can remove from your day to protect your quietness?",
        "Unknown",
        "Simplicity"
    ),
    (
        "True Poverty of Want",
        "It is not the man who has too little, but the man who craves more, that is poor.",
        "Where can you stop craving more and appreciate the completeness of today?",
        "Seneca",
        "Simplicity"
    ),
    (
        "Quiet Needs",
        "The standard of simple living is to need little and enjoy much.",
        "What is a free, simple activity that brings you high enjoyment?",
        "Lao Tzu",
        "Simplicity"
    ),
    (
        "Unbound Heart",
        "A simple heart finds the shortest path to peace.",
        "How can you unburden your heart from complex worries today?",
        "Thomas à Kempis",
        "Simplicity"
    ),

    # --- TIME (20) ---
    (
        "The Door to All Moments",
        "The present moment is the only moment available to us, and it is the door to all moments.",
        "What does it feel like to bring your entire attention to this single breath?",
        "Thich Nhat Hanh",
        "Time"
    ),
    (
        "Mind on the Present",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
        "When your mind drifts to yesterday or tomorrow, how do you gently anchor it back?",
        "Buddha",
        "Time"
    ),
    (
        "Priceless Time",
        "Time is the wisest counselor of all.",
        "What problem in your life would benefit from the perspective of time?",
        "Pericles",
        "Time"
    ),
    (
        "The Swift Stream",
        "Time is a sort of river of passing events, and strong is its current.",
        "Instead of fighting the current of events, how can you float with it today?",
        "Marcus Aurelius",
        "Time"
    ),
    (
        "Value of Today",
        "One today is worth two tomorrows.",
        "What meaningful action can you take today instead of postponing it?",
        "Benjamin Franklin",
        "Time"
    ),
    (
        "Lost Time",
        "Lost time is never found again.",
        "Where have you been spending your time that feels like a waste?",
        "Benjamin Franklin",
        "Time"
    ),
    (
        "The Present Wealth",
        "The present is the only thing that has no end.",
        "How does focusing on the current second change your experience of time?",
        "Erwin Schrödinger",
        "Time"
    ),
    (
        "Time for Wisdom",
        "Time brings all things to pass.",
        "What truth has time made clear to you that you couldn't see before?",
        "Aeschylus",
        "Time"
    ),
    (
        "Making Room",
        "Time is a created thing. To say 'I don't have time' is to say 'I don't want to.'",
        "What is something you claim to lack time for that you actually just avoid?",
        "Lao Tzu",
        "Time"
    ),
    (
        "The Illusion of Time",
        "The distinction between the past, present and future is only a stubbornly persistent illusion.",
        "How does it feel to realize that this moment is all that ever truly exists?",
        "Albert Einstein",
        "Time"
    ),
    (
        "Living Now",
        "Never let the future disturb you. You will meet it, if you must, with the same weapons of reason which today arm you against the present.",
        "What future worry can you set down, trusting your future self to handle it?",
        "Marcus Aurelius",
        "Time"
    ),
    (
        "The Patient Wait",
        "Time is the companion of patience.",
        "Where do you need to allow time to do its work instead of forcing a result?",
        "Saint Augustine",
        "Time"
    ),
    (
        "The Present Gift",
        "Realize deeply that the present moment is all you ever have.",
        "How does recognizing the value of the 'now' alter your priorities?",
        "Eckhart Tolle",
        "Time"
    ),
    (
        "Seize the Day",
        "Carpe diem, quam minimum credula postero.",
        "How can you make the most of today without relying on tomorrow?",
        "Horace",
        "Time"
    ),
    (
        "The Moving Finger",
        "The Moving Finger writes; and, having writ, moves on.",
        "What past event is it time to stop wishing you could rewrite?",
        "Omar Khayyam",
        "Time"
    ),
    (
        "The Constant Flow",
        "No man ever steps in the same river twice, for it's not the same river and he's not the same man.",
        "How have you grown and changed since this time last year?",
        "Heraclitus",
        "Time"
    ),
    (
        "The Best Day",
        "Write it on your heart that every day is the best day in the year.",
        "What simple thing can you appreciate about today to make it a great day?",
        "Ralph Waldo Emerson",
        "Time"
    ),
    (
        "Morning Beginner",
        "Be willing to be a beginner every single morning.",
        "What fresh, unburdened perspective can you bring to your actions this morning?",
        "Meister Eckhart",
        "Time"
    ),
    (
        "Understanding Backwards",
        "Life can only be understood backwards; but it must be lived forwards.",
        "Looking back at a past struggle, how does it make sense in the context of who you are today?",
        "Søren Kierkegaard",
        "Time"
    ),
    (
        "All Things Passing",
        "Let nothing disturb thee, nothing affright thee; all things are passing.",
        "What temporary concern can you release today, knowing it will soon pass?",
        "Saint Teresa of Avila",
        "Time"
    ),

    # --- SOLITUDE (20) ---
    (
        "Quiet Self-Sufficiency",
        "I love to be alone. I never found the companion that was so companionable as solitude.",
        "What do you discover about yourself when there is no one else around?",
        "Henry David Thoreau",
        "Solitude"
    ),
    (
        "The Sacred Sanctuary",
        "Solitude is a silent storm that breaks down all our dead branches; yet it sends our living roots deeper into the living heart of the earth.",
        "How does quiet reflection help you feel more grounded in who you are?",
        "Khalil Gibran",
        "Solitude"
    ),
    (
        "Meeting Yourself",
        "Your solitude will be a support and a home for you, even in the midst of very unfamiliar circumstances.",
        "How can you make your inner world a more welcoming place to rest?",
        "Rainer Maria Rilke",
        "Solitude"
    ),
    (
        "The Root of Creation",
        "Solitude is the playfield of consciousness.",
        "What creative ideas or insights arise when your mind is undisturbed?",
        "Deepak Chopra",
        "Solitude"
    ),
    (
        "Inner Sanctuary",
        "Nowhere can man find a quieter or more untroubled retreat than in his own soul.",
        "How can you access your inner retreat in the middle of a busy day?",
        "Marcus Aurelius",
        "Solitude"
    ),
    (
        "The Sound of Silence",
        "In the attitude of silence the soul finds the pathway in a clearer light.",
        "What does the silence around you reveal when you stop generating noise?",
        "Mahatma Gandhi",
        "Solitude"
    ),
    (
        "Deep Solitude",
        "True solitude is not the absence of others, but the presence of oneself.",
        "How can you bring a deeper awareness of your own presence to this moment?",
        "Thomas Merton",
        "Solitude"
    ),
    (
        "Quiet Growth",
        "Great things are done in quiet, not in noise and fury.",
        "What quiet effort are you making that doesn't need external applause?",
        "William Wordsworth",
        "Solitude"
    ),
    (
        "The Thinker's Space",
        "Without great solitude no serious work is possible.",
        "How can you schedule a small window of uninterrupted space this week?",
        "Pablo Picasso",
        "Solitude"
    ),
    (
        "Restoring the Soul",
        "Solitude is the soil in which genius is planted, creativity grows, and legend lives.",
        "How does a period of quiet help restore your creative energy?",
        "Unknown",
        "Solitude"
    ),
    (
        "Sitting Quietly",
        "All of humanity's problems stem from man's inability to sit quietly in a room alone.",
        "What makes sitting quietly with your own thoughts challenging for you?",
        "Blaise Pascal",
        "Solitude"
    ),
    (
        "Facing Yourself",
        "One can be instructed in society, one is inspired only in solitude.",
        "What unique inspiration has come to you during a moment of quiet reflection?",
        "Johann Wolfgang von Goethe",
        "Solitude"
    ),
    (
        "The Inner Companion",
        "He is never less alone than when alone.",
        "In what ways have you learned to become a friend to yourself?",
        "Cicero",
        "Solitude"
    ),
    (
        "The Great Pause",
        "Quiet the mind, and the soul will speak.",
        "What is your inner voice trying to tell you that the noise is drowning out?",
        "Ma Jaya Sati Bhagavati",
        "Solitude"
    ),
    (
        "Solitary Splendor",
        "Solitude is the place of purification.",
        "What mental clutter does a few minutes of quiet help you clear away?",
        "Martin Buber",
        "Solitude"
    ),
    (
        "The Journey Within",
        "The only journey is the one within.",
        "What part of your inner landscape are you currently exploring?",
        "Rainer Maria Rilke",
        "Solitude"
    ),
    (
        "The Solitary Jewel",
        "Solitude is one of the most precious jewels you can ever possess.",
        "How can you protect a few minutes of quiet today to enjoy this precious jewel?",
        "John O'Donohue",
        "Solitude"
    ),
    (
        "Existing is Enough",
        "I exist as I am, that is enough.",
        "Can you sit quietly for a moment and just feel the deep sufficiency of being alive?",
        "Walt Whitman",
        "Solitude"
    ),
    (
        "True Solitude View",
        "Quiet spaces allow the soul to breathe and catch up with the body.",
        "In what way does today's quiet help align your physical and mental states?",
        "Unknown",
        "Solitude"
    ),
    (
        "The Self Sanctuary",
        "Only in quiet waters do things reflect undistorted.",
        "How can you calm your mind today so you can see your true reflection?",
        "Lao Tzu",
        "Solitude"
    ),

    # --- RELATIONSHIPS (20) ---
    (
        "Lifting Associations",
        "Associate with people who are likely to improve you.",
        "Who in your circle inspires you to grow and be a better person?",
        "Seneca",
        "Relationships"
    ),
    (
        "Uplifting Presence",
        "Keep company only with people who uplift you, whose presence calls forth your best.",
        "Whose presence in your life consistently makes you feel supported and valued?",
        "Epictetus",
        "Relationships"
    ),
    (
        "Strength of Kindness",
        "Tenderness and kindness are not signs of weakness and despair, but manifestations of strength and resolution.",
        "In what relationship can you offer a gentle touch of tenderness today?",
        "Khalil Gibran",
        "Relationships"
    ),
    (
        "The Mirror of Friend",
        "A friend is one who knows us, but loves us anyway.",
        "Who knows your flaws completely yet remains a source of steady warmth?",
        "Fr. Jerome Cummings",
        "Relationships"
    ),
    (
        "Shared Load",
        "Shared joy is double joy; shared sorrow is half sorrow.",
        "Who can you reach out to today to share a joy or lighten a burden?",
        "Swedish Proverb",
        "Relationships"
    ),
    (
        "Cultivating Others",
        "Let us be grateful to people who make us happy, they are the charming gardeners who make our souls blossom.",
        "Who has helped your spirit blossom recently, and have you thanked them?",
        "Marcel Proust",
        "Relationships"
    ),
    (
        "The Deepest Connection",
        "We are all travelers in the wilderness of this world, and the best we can find in our travels is an honest friend.",
        "Who represents a steady, honest anchor for you in this busy world?",
        "Robert Louis Stevenson",
        "Relationships"
    ),
    (
        "Listening as Love",
        "The first duty of love is to listen.",
        "How can you practice deeper, more generous listening in your next conversation?",
        "Paul Tillich",
        "Relationships"
    ),
    (
        "The Art of Kindness",
        "Kindness is the language which the deaf can hear and the blind can see.",
        "What small, unspoken act of kindness can you offer to a stranger today?",
        "Mark Twain",
        "Relationships"
    ),
    (
        "The True Gift",
        "The greatest gift you can give another is the purity of your attention.",
        "Where can you put away distractions to give someone your absolute presence?",
        "Thich Nhat Hanh",
        "Relationships"
    ),
    (
        "Understanding First",
        "If you want to be understood, seek first to understand.",
        "In a current disagreement, how can you focus on understanding the other side?",
        "Stephen Covey",
        "Relationships"
    ),
    (
        "Love and Courage",
        "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.",
        "Where in your life do you feel the strength or courage that love brings?",
        "Lao Tzu",
        "Relationships"
    ),
    (
        "Mutual Respect",
        "Respect is love in plain clothes.",
        "How can you show a deep mark of respect to someone you interact with today?",
        "Frankie Byrne",
        "Relationships"
    ),
    (
        "Noble Friendships",
        "Friendship is a single soul dwelling in two bodies.",
        "What does the deep union of true friendship mean for your daily path?",
        "Aristotle",
        "Relationships"
    ),
    (
        "Forgiveness and Peace",
        "Forgiveness is the fragrance that the violet sheds on the heel that has crushed it.",
        "What old grievance is it time to let go of for your own peace of mind?",
        "Mark Twain",
        "Relationships"
    ),
    (
        "Attention as Generosity",
        "Attention is the rarest and purest form of generosity.",
        "Who in your life deserves your undivided, generous attention today?",
        "Simone Weil",
        "Relationships"
    ),
    (
        "Vastness and Love",
        "For small creatures such as we the vastness is bearable only through love.",
        "Who in your life makes the vast, complex world feel safe and meaningful?",
        "Carl Sagan",
        "Relationships"
    ),
    (
        "True Humility",
        "Humility is not thinking less of yourself, it's thinking of yourself less.",
        "How can you focus your attention entirely on someone else's needs or joy today?",
        "C.S. Lewis",
        "Relationships"
    ),
    (
        "Deep Listening",
        "Deep listening is the kind of listening that can help relieve the suffering of another person.",
        "Think of someone who is going through a hard time. How can you listen to them without judgment?",
        "Thich Nhat Hanh",
        "Relationships"
    ),
    (
        "Joy in Others",
        "To find joy in the joy of others is the secret of happiness.",
        "Whose success or happiness can you celebrate whole-heartedly today?",
        "George Bernanos",
        "Relationships"
    ),

    # --- WORK (10) ---
    (
        "Perfect Job",
        "Pleasure in the job puts perfection in the work.",
        "What aspect of your daily tasks brings you the most genuine satisfaction?",
        "Aristotle",
        "Work"
    ),
    (
        "Work and Love",
        "Work is love made visible.",
        "How can you infuse a feeling of care and purpose into your current project?",
        "Khalil Gibran",
        "Work"
    ),
    (
        "The Quiet Craft",
        "Do your work with your whole heart, and you will succeed - there is so little competition.",
        "Where can you bring a deeper level of wholehearted dedication to your task?",
        "Elbert Hubbard",
        "Work"
    ),
    (
        "The Fruit of Labor",
        "The fruit of your own labor is the sweetest of all pleasures.",
        "Take a moment to appreciate something useful you built or accomplished recently.",
        "Vauvenargues",
        "Work"
    ),
    (
        "Steady Application",
        "Genius is one percent inspiration and ninety-nine percent perspiration.",
        "What small, consistent effort are you willing to put in today toward a big goal?",
        "Thomas Edison",
        "Work"
    ),
    (
        "Labor of Care",
        "No work is insignificant. All labor that uplifts humanity has dignity and importance.",
        "How does your daily work contribute, even in a small way, to the lives of others?",
        "Martin Luther King Jr.",
        "Work"
    ),
    (
        "Focused Effort",
        "Concentrate all your thoughts upon the work at hand. The sun's rays do not burn until brought to a focus.",
        "How can you eliminate distractions to focus intensely on your work right now?",
        "Alexander Graham Bell",
        "Work"
    ),
    (
        "Action as Foundation",
        "Action is the foundational key to all success.",
        "What small, concrete action can you take today to move a project forward?",
        "Pablo Picasso",
        "Work"
    ),
    (
        "The Simple Task",
        "Nothing is particularly hard if you divide it into small jobs.",
        "How can you break down a daunting task into tiny, manageable steps today?",
        "Henry Ford",
        "Work"
    ),
    (
        "Inner Satisfaction",
        "The reward of a thing well done is to have done it.",
        "How can you find fulfillment in the process of your work rather than the praise?",
        "Ralph Waldo Emerson",
        "Work"
    ),
    (
        "The Unseen Target",
        "Talent hits a target no one else can hit; Genius hits a target no one else can see.",
        "What unique vision or path are you working toward that others might not see yet?",
        "Arthur Schopenhauer",
        "Work"
    ),
    (
        "Beauty of Your Doing",
        "Let the beauty of what you love be what you do.",
        "How can you bring the things you love into the daily actions of your work?",
        "Rumi",
        "Work"
    ),

    # --- NATURE & SEASONS (10) ---
    (
        "Nature's Pace",
        "Adopt the pace of nature: her secret is patience.",
        "Where can you slow down and trust that things will ripen in their own time?",
        "Ralph Waldo Emerson",
        "Nature & Seasons"
    ),
    (
        "The Healing Earth",
        "In all things of nature there is something of the marvelous.",
        "What marvelous details in the natural world did you notice today?",
        "Aristotle",
        "Nature & Seasons"
    ),
    (
        "Simple Restoration",
        "Look deep into nature, and then you will understand everything better.",
        "How does spending a few minutes outdoors help clarify your thoughts?",
        "Albert Einstein",
        "Nature & Seasons"
    ),
    (
        "The Rhythms of Nature",
        "To everything there is a season, and a time to every purpose under the heaven.",
        "What phase or season of life do you find yourself in right now?",
        "Ecclesiastes",
        "Nature & Seasons"
    ),
    (
        "Wild Beauty",
        "I believe that a leaf of grass is no less than the journey-work of the stars.",
        "How can you reconnect with the wild, unpolished beauty of the earth today?",
        "Walt Whitman",
        "Nature & Seasons"
    ),
    (
        "Nature's Quiet Voice",
        "Nature never rushes, yet everything is accomplished.",
        "What part of your life needs to be allowed to grow naturally and slowly?",
        "Lao Tzu",
        "Nature & Seasons"
    ),
    (
        "The Changing Leaves",
        "Live in each season as it passes; breathe the air, drink the drink, taste the fruit, and resign yourself to the influence of the earth.",
        "How can you align your habits to better match the current season of the year?",
        "Henry David Thoreau",
        "Nature & Seasons"
    ),
    (
        "Sky and Mountain",
        "The mountains are calling and I must go.",
        "What natural landscape makes you feel the most small, humble, and peaceful?",
        "John Muir",
        "Nature & Seasons"
    ),
    (
        "Forest Wisdom",
        "You will find something more in woods than in books. Stones and trees will teach you that which you will never hear from masters.",
        "What lesson has a quiet moment in nature taught you that books could not?",
        "Saint Bernard",
        "Nature & Seasons"
    ),
    (
        "The Clean Wind",
        "Keep close to Nature's heart... and break clear away, once in a while, and climb a mountain or spend a week in the woods. Wash your spirit clean.",
        "When was the last time you let the fresh air wash away your daily worries?",
        "John Muir",
        "Nature & Seasons"
    ),
    (
        "Coloring the Sky",
        "Clouds come floating into my life, no longer to carry rain or usher storm, but to add color to my sunset sky.",
        "How can you view a recent difficulty as a way to add depth and color to your life story?",
        "Rabindranath Tagore",
        "Nature & Seasons"
    )
]

file_path = "/Users/craigfaist/Desktop/weatherApp/PocketWisdom/PocketWisdom/Resources/wisdom.json"

if not os.path.exists(file_path):
    print(f"Error: {file_path} does not exist.")
    exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    wisdom = json.load(f)

# Build a set of existing normalized bodies to avoid duplicates
existing_bodies = {quote["body"].strip().lower() for quote in wisdom if "body" in quote}

added_count = 0
duplicates_skipped = 0

for title, body, reflection, author, category in new_quotes:
    normalized_body = body.strip().lower()
    if normalized_body in existing_bodies:
        duplicates_skipped += 1
        continue
    
    wisdom.append({
        "id": str(uuid.uuid4()).upper(),
        "category": category,
        "title": title,
        "body": body,
        "reflection": reflection,
        "author": author
    })
    existing_bodies.add(normalized_body)
    added_count += 1

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(wisdom, f, indent=2, ensure_ascii=False)

print(f"Successfully finished processing!")
print(f"- Total quotes compiled: {len(new_quotes)}")
print(f"- Unique quotes successfully added: {added_count}")
print(f"- Duplicate quotes skipped: {duplicates_skipped}")
print(f"- New total quotes in wisdom.json: {len(wisdom)}")
