import uuid
import json
import os

quotes_data = [
    # Ancient/Classic (40)
    ("The Unexamined Life", "The unexamined life is not worth living.", "Reflect on your daily choices and motivations to find true meaning.", "Socrates", "Life"),
    ("Action Over Argument", "Waste no more time arguing what a good man should be. Be one.", "Embody the virtues you admire instead of just discussing them.", "Marcus Aurelius", "Life"),
    ("Self-Knowledge", "Knowing yourself is the beginning of all wisdom.", "Take time to understand your true nature, strengths, and flaws.", "Aristotle", "Life"),
    ("The Value of Time", "It is not that we have a short time to live, but that we waste a lot of it.", "Focus your time on what truly matters to you.", "Seneca", "Time"),
    ("Listen More", "We have two ears and one mouth so that we can listen twice as much as we speak.", "Give your full attention to others before offering your own words.", "Epictetus", "Life"),
    ("Contentment", "The greatest wealth is to live content with little.", "Find joy in what you already have rather than constantly seeking more.", "Plato", "Life"),
    ("Simple Life", "Life is really simple, but we insist on making it complicated.", "Identify the complexities in your life and gently let them go.", "Confucius", "Simplicity"),
    ("Nature's Pace", "Nature does not hurry, yet everything is accomplished.", "Trust the process and allow things to unfold in their own time.", "Laozi", "Nature & Seasons"),
    ("Follow Your Heart", "Let yourself be silently drawn by the strange pull of what you really love. It will not lead you astray.", "Trust your intuition and follow your deepest passions.", "Rumi", "Relationships"),
    ("Work as Love", "Work is love made visible.", "Find ways to express care and purpose in your daily tasks.", "Khalil Gibran", "Work"),
    ("Time for Rest", "There is a time for many words, and there is also a time for sleep.", "Balance your active engagements with essential rest.", "Homer", "Life"),
    ("Internal Happiness", "Very little is needed to make a happy life; it is all within yourself, in your way of thinking.", "Cultivate a positive mindset to experience true joy.", "Marcus Aurelius", "Simplicity"),
    ("Focused Presence", "To be everywhere is to be nowhere.", "Give your full attention to one place and one task at a time.", "Seneca", "Solitude"),
    ("Rejoice in the Present", "He is a wise man who does not grieve for the things which he has not, but rejoices for those which he has.", "Practice gratitude for the blessings currently in your life.", "Epictetus", "Life"),
    ("Firm Friendship", "Be slow to fall into friendship, but when you are in, continue firm and constant.", "Invest deeply in the relationships you choose to cultivate.", "Socrates", "Relationships"),
    ("Selective Friendship", "A friend to all is a friend to none.", "Value deep connections over superficial popularity.", "Aristotle", "Relationships"),
    ("The Madness of Love", "Love is a serious mental disease.", "Acknowledge the overwhelming and transformative power of love.", "Plato", "Relationships"),
    ("Steady Progress", "It does not matter how slowly you go as long as you do not stop.", "Persist in your efforts, no matter how small the steps.", "Confucius", "Time"),
    ("Richness of Contentment", "He who is contented is rich.", "Discover the wealth that comes from needing nothing more.", "Laozi", "Simplicity"),
    ("Inner Change", "Yesterday I was clever, so I wanted to change the world. Today I am wise, so I am changing myself.", "Focus your energy on your own growth and transformation.", "Rumi", "Life"),
    ("Space in Togetherness", "Let there be spaces in your togetherness.", "Allow room for individuality and growth within your relationships.", "Khalil Gibran", "Relationships"),
    ("True Friends", "The difficulty is not so great to die for a friend, as to find a friend worth dying for.", "Cherish those rare individuals who truly understand and support you.", "Homer", "Life"),
    ("Live Each Day", "Do every act of your life as though it were the very last act of your life.", "Bring profound intentionality and care to your current actions.", "Marcus Aurelius", "Time"),
    ("Making Luck", "Luck is what happens when preparation meets opportunity.", "Do the work now so you are ready when the moment arrives.", "Seneca", "Life"),
    ("Decide and Act", "First say to yourself what you would be; and then do what you have to do.", "Define your ideal self and align your daily habits accordingly.", "Epictetus", "Life"),
    ("Enjoying Less", "The secret of happiness, you see, is not found in seeking more, but in developing the capacity to enjoy less.", "Find deep satisfaction in simple, everyday experiences.", "Socrates", "Simplicity"),
    ("Joy in Work", "Pleasure in the job puts perfection in the work.", "Seek out the aspects of your work that bring you genuine joy.", "Aristotle", "Work"),
    ("Internal Dialogue", "Thinking: the talking of the soul with itself.", "Create space for quiet reflection and inner dialogue.", "Plato", "Solitude"),
    ("Wholeheartedness", "Wherever you go, go with all your heart.", "Commit fully to your current path and experiences.", "Confucius", "Life"),
    ("Love and Strength", "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.", "Draw power from the genuine connections in your life.", "Laozi", "Relationships"),
    ("The Value of Silence", "The quieter you become, the more you are able to hear.", "Silence your mind to perceive the deeper truths around you.", "Rumi", "Solitude"),
    ("Memory and Dream", "Yesterday is but today's memory, and tomorrow is today's dream.", "Anchor yourself in the present moment, the only true reality.", "Khalil Gibran", "Time"),
    ("Shared Soul", "Two friends, two bodies with one soul inspired.", "Celebrate the profound bond of true companionship.", "Homer", "Relationships"),
    ("Power of Thoughts", "Our life is what our thoughts make it.", "Monitor your inner narrative, as it shapes your outer reality.", "Marcus Aurelius", "Life"),
    ("Present Happiness", "True happiness is to enjoy the present, without anxious dependence upon the future.", "Release your worries about tomorrow and embrace today.", "Seneca", "Simplicity"),
    ("Few Wants", "Wealth consists not in having great possessions, but in having few wants.", "Examine your desires and practice letting go of the unnecessary.", "Epictetus", "Simplicity"),
    ("Beware Busyness", "Beware the barrenness of a busy life.", "Ensure your activities are meaningful, not just a distraction.", "Socrates", "Life"),
    ("A Single Soul", "What is a friend? A single soul dwelling in two bodies.", "Cherish the deep unity found in true friendship.", "Aristotle", "Relationships"),
    ("Nature of Courage", "Courage is knowing what not to fear.", "Discern between genuine threats and imagined anxieties.", "Plato", "Life"),
    ("Love Your Job", "Choose a job you love, and you will never have to work a day in your life.", "Align your daily work with your deepest passions and values.", "Confucius", "Work"),
    
    # Literary Authors (20)
    ("Inner Vastness", "What lies behind us and what lies before us are tiny matters compared to what lies within us.", "Recognize the immense resilience and potential within your own spirit.", "Ralph Waldo Emerson", "Life"),
    ("Two Important Days", "The two most important days in your life are the day you are born and the day you find out why.", "Seek out your unique purpose and let it guide your actions.", "Mark Twain", "Life"),
    ("Simplify Life", "Our life is frittered away by detail. Simplify, simplify.", "Remove the non-essential to focus on what truly matters.", "Henry David Thoreau", "Simplicity"),
    ("Face the Sunshine", "Keep your face always toward the sunshine - and shadows will fall behind you.", "Maintain an optimistic outlook and let negativity fade away.", "Walt Whitman", "Life"),
    ("How You Made Them Feel", "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.", "Focus on kindness and the emotional impact you have on others.", "Maya Angelou", "Relationships"),
    ("Life Goes On", "In three words I can sum up everything I've learned about life: it goes on.", "Find comfort in the relentless forward momentum of life.", "Robert Frost", "Life"),
    ("Patience of Nature", "Adopt the pace of nature: her secret is patience.", "Allow things to develop in their own time without forcing them.", "Ralph Waldo Emerson", "Nature & Seasons"),
    ("Getting Started", "The secret of getting ahead is getting started.", "Take the first, small step today rather than waiting for tomorrow.", "Mark Twain", "Time"),
    ("Companionable Solitude", "I never found the companion that was so companionable as solitude.", "Embrace moments of being alone as opportunities for self-discovery.", "Henry David Thoreau", "Solitude"),
    ("Growth in Open Air", "Now I see the secret of making the best person: it is to grow in the open air and to eat and sleep with the earth.", "Reconnect with the natural world to restore your spirit.", "Walt Whitman", "Nature & Seasons"),
    ("Change Your Attitude", "If you don't like something, change it. If you can't change it, change your attitude.", "Take control of your perspective when circumstances are fixed.", "Maya Angelou", "Life"),
    ("Miles to Go", "The woods are lovely, dark and deep. But I have promises to keep, and miles to go before I sleep.", "Acknowledge your responsibilities while appreciating moments of beauty.", "Robert Frost", "Nature & Seasons"),
    ("Being Yourself", "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", "Celebrate your authenticity and resist the urge to conform.", "Ralph Waldo Emerson", "Life"),
    ("Pause and Reflect", "Whenever you find yourself on the side of the majority, it is time to pause and reflect.", "Question the consensus and ensure your choices align with your own values.", "Mark Twain", "Life"),
    ("True Wealth", "Wealth is the ability to fully experience life.", "Measure your riches in experiences and moments of connection.", "Henry David Thoreau", "Simplicity"),
    ("Glory of Expression", "Simplicity is the glory of expression.", "Strive for clarity and directness in your words and actions.", "Walt Whitman", "Simplicity"),
    ("Endless Creativity", "You can't use up creativity. The more you use, the more you have.", "Trust that your creative energy is an abundant, renewable resource.", "Maya Angelou", "Life"),
    ("Irresistible Desire", "Love is an irresistible desire to be irresistibly desired.", "Acknowledge the deep human need for mutual affection and connection.", "Robert Frost", "Relationships"),
    ("Being a Friend", "The only way to have a friend is to be one.", "Cultivate the qualities in yourself that you seek in others.", "Ralph Waldo Emerson", "Relationships"),
    ("Confident Direction", "Go confidently in the direction of your dreams! Live the life you've imagined.", "Take bold steps toward the future you envision for yourself.", "Henry David Thoreau", "Life"),
    
    # Modern Reflective (30)
    ("The Journey", "Life is a journey, not a destination.", "Appreciate the process of growth rather than rushing to the finish line.", "Unknown", "Life"),
    ("Courage and Vulnerability", "Vulnerability is not winning or losing; it's having the courage to show up and be seen when we have no control over the outcome.", "Embrace the risk of being open and authentic with others.", "Brené Brown", "Life"),
    ("The Power of Now", "Realize deeply that the present moment is all you have. Make the NOW the primary focus of your life.", "Release the past and the future to fully inhabit this moment.", "Eckhart Tolle", "Time"),
    ("Breathe and Go Slowly", "Smile, breathe and go slowly.", "In moments of stress, return to your breath and lower your pace.", "Thich Nhat Hanh", "Simplicity"),
    ("Actions Create Happiness", "Happiness is not something ready made. It comes from your own actions.", "Take responsibility for cultivating joy through your daily choices.", "Dalai Lama", "Life"),
    ("The Contract of Desire", "Desire is a contract that you make with yourself to be unhappy until you get what you want.", "Examine your desires and find peace in what you already possess.", "Naval Ravikant", "Simplicity"),
    ("Priceless Time", "Time is free, but it's priceless. You can't own it, but you can use it.", "Value your time as your most precious and finite resource.", "Unknown", "Time"),
    ("Clear is Kind", "Clear is kind. Unclear is unkind.", "Communicate honestly and directly to build trust in relationships.", "Brené Brown", "Relationships"),
    ("Space for the New", "Some changes look negative on the surface but you will soon realize that space is being created in your life for something new to emerge.", "Trust that endings are often necessary for new beginnings.", "Eckhart Tolle", "Life"),
    ("Accept Yourself", "To be beautiful means to be yourself. You don’t need to be accepted by others. You need to accept yourself.", "Validate your own worth instead of seeking external approval.", "Thich Nhat Hanh", "Relationships"),
    ("The Religion of Kindness", "My religion is very simple. My religion is kindness.", "Make compassion the guiding principle in all your interactions.", "Dalai Lama", "Relationships"),
    ("Iterated Games", "Play iterated games. All the returns in life, whether in wealth, relationships, or knowledge, come from compound interest.", "Invest in long-term relationships and consistent daily habits.", "Naval Ravikant", "Work"),
    ("Growing Through Dirt", "Every flower must grow through dirt.", "Acknowledge that periods of struggle are essential for growth.", "Unknown", "Nature & Seasons"),
    ("True Belonging", "True belonging doesn't require us to change who we are; it requires us to be who we are.", "Seek environments where you are celebrated for your authentic self.", "Brené Brown", "Solitude"),
    ("Joy from Within", "Nothing can give you joy. Joy is uncaused and arises from within as the joy of Being.", "Stop seeking external sources for happiness and look inward.", "Eckhart Tolle", "Solitude"),
    ("Alive and Possible", "Because you are alive, everything is possible.", "Recognize the boundless potential inherent in simply being here.", "Thich Nhat Hanh", "Nature & Seasons"),
    ("Purpose of Happiness", "The purpose of our lives is to be happy.", "Prioritize joy and well-being in your overarching life goals.", "Dalai Lama", "Life"),
    ("Earned Rewards", "A fit body, a calm mind, a house full of love. These things cannot be bought – they must be earned.", "Commit to the consistent effort required to build a meaningful life.", "Naval Ravikant", "Life"),
    ("Time Alone", "Sometimes you need to take a break from everyone and spend time alone, to experience, appreciate, and love yourself.", "Honor your need for solitude and self-reflection.", "Unknown", "Solitude"),
    ("Setting Boundaries", "Daring to set boundaries is about having the courage to love ourselves, even when we risk disappointing others.", "Protect your energy and well-being by clearly communicating your limits.", "Brené Brown", "Life"),
    ("Useless Worry", "Worry pretends to be necessary but serves no useful purpose.", "Notice when worry arises and choose to focus on actionable steps instead.", "Eckhart Tolle", "Life"),
    ("Freedom in Letting Go", "Letting go gives us freedom, and freedom is the only condition for happiness.", "Release your attachments to specific outcomes to find true peace.", "Thich Nhat Hanh", "Life"),
    ("Love Exceeding Need", "Remember that the best relationship is one in which your love for each other exceeds your need for each other.", "Cultivate independence alongside deep emotional connection.", "Dalai Lama", "Relationships"),
    ("Lifelong Colleagues", "If you can't see yourself working with someone for life, don't work with them for a day.", "Be intentional about the people you choose to surround yourself with.", "Naval Ravikant", "Time"),
    ("A Good Today", "Don't ruin a good today by thinking about a bad yesterday.", "Leave past regrets behind and fully engage with the present day.", "Unknown", "Life"),
    ("Meaning of Connection", "Connection is why we're here; it is what gives purpose and meaning to our lives.", "Nurture the relationships that bring depth and significance to your life.", "Brené Brown", "Relationships"),
    ("Foundation of Abundance", "Acknowledging the good that you already have in your life is the foundation for all abundance.", "Practice gratitude to open yourself to further blessings.", "Eckhart Tolle", "Simplicity"),
    ("Joy in the Present", "The present moment is filled with joy and happiness. If you are attentive, you will see it.", "Bring mindful awareness to the simple pleasures available right now.", "Thich Nhat Hanh", "Time"),
    ("Two Days", "There are only two days in the year that nothing can be done. One is called Yesterday and the other is called Tomorrow.", "Focus all your energy on what you can accomplish today.", "Dalai Lama", "Time"),
    ("Hearing Differently", "The right people will hear you differently.", "Trust that your true community will understand and value your unique voice.", "Unknown", "Relationships"),
    
    # Contemporary (10)
    ("Curiosity Over Judgment", "Be curious, not judgmental.", "Approach others with an open mind and a desire to understand.", "Unknown — Popularized by Ted Lasso", "Relationships"),
    ("Great Work", "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work.", "Pursue endeavors that align with your deepest values and passions.", "Steve Jobs", "Work"),
    ("The Goldfish", "You know what the happiest animal on Earth is? It's a goldfish. You know why? Got a 10-second memory.", "Learn to quickly let go of mistakes and perceived slights.", "Ted Lasso", "Life"),
    ("Work Hard, Be Kind", "Work hard, be kind, and amazing things will happen.", "Combine diligent effort with consistent compassion.", "Conan O'Brien", "Work"),
    ("Life Moves Fast", "Life moves pretty fast. If you don't stop and look around once in a while, you could miss it.", "Take deliberate pauses to appreciate the beauty around you.", "Ferris Bueller", "Time"),
    ("The Biggest Adventure", "The biggest adventure you can take is to live the life of your dreams.", "Dare to pursue the goals that truly excite and inspire you.", "Oprah Winfrey", "Life"),
    ("Valuing Others", "As human beings, our job in life is to help people realize how rare and valuable each one of us really is.", "Make it a daily practice to uplift and validate the people around you.", "Fred Rogers", "Relationships"),
    ("The Gift of Today", "Yesterday is history, tomorrow is a mystery, but today is a gift. That is why it is called the present.", "Cherish the current moment as a precious opportunity.", "Master Oogway", "Time"),
    ("Keep Swimming", "Just keep swimming.", "Persist through difficulties with simple, continuous forward motion.", "Dory", "Life"),
    ("Dwell on Dreams", "It does not do to dwell on dreams and forget to live.", "Ensure your visions for the future don't distract you from the present reality.", "Albus Dumbledore", "Life")
]

file_path = "PocketWisdom/Resources/wisdom.json"

with open(file_path, "r", encoding="utf-8") as f:
    wisdom = json.load(f)

for title, body, reflection, author, category in quotes_data:
    wisdom.append({
        "id": str(uuid.uuid4()),
        "title": title,
        "body": body,
        "reflection": reflection,
        "author": author,
        "category": category
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(wisdom, f, indent=2, ensure_ascii=False)

print(f"Successfully appended {len(quotes_data)} quotes to {file_path}")
