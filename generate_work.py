import json
import uuid

quotes = [
    ("The inbox", "An empty inbox is a temporary state, not a reflection of your worth.", "What actually matters outside of your messages?", None),
    ("Urgency", "Most things presented as urgent are simply poorly planned by someone else.", "What is actually urgent today?", None),
    ("The ladder", "Climbing the ladder is only useful if it leans against the right wall.", "Where is your effort leading you?", None),
    ("Status", "Status is a heavy coat to wear every single day.", "When do you feel comfortable taking it off?", None),
    ("The pivot", "It is entirely acceptable to change careers when you realize you are succeeding at something you don't want to do.", "What are you succeeding at that doesn't fulfill you?", None),
    ("Rest as work", "Rest is not the absence of work; it is the requirement for it.", "Are you treating rest as a necessity?", None),
    ("The meeting", "Many hours are lost discussing the work instead of simply doing the work.", "What conversation could be an action?", None),
    ("Expertise", "True expertise is knowing what to ignore.", "What noise are you currently ignoring?", None),
    ("The grind", "The grind will take as much of you as you are willing to give.", "Where are you drawing the line today?", None),
    ("Retirement", "You do not have to wait until retirement to experience a quiet Tuesday afternoon.", "How can you claim a quiet hour this week?", None),
    ("Boundaries", "A boundary is simply deciding what you will not do.", "What is one thing you will not do today?", None),
    ("The sprint", "You cannot sprint a marathon without collapsing before the finish line.", "Are you pacing yourself for the long run?", None),
    ("Validation", "External validation is a moving target.", "How do you validate your own effort?", None),
    ("The title", "Your job title describes how you spend your hours, not who you are.", "Who are you when you log off?", None),
    ("Good work", "Sometimes good work is simply finishing the task and going home.", "What task is ready to just be finished?", None),
    ("The legacy", "Very few people will remember the presentations you gave. They will remember how you treated them.", "How are you treating the people around you?", None),
    ("The off switch", "The ability to disconnect completely is a skill that must be practiced.", "When was the last time you were entirely unreachable?", None),
    ("The plateau", "A career plateau is often just a stable, comfortable place to rest and build a life.", "Can you appreciate the stability?", None),
    ("The promotion", "A promotion that costs you your peace is not a promotion.", "What is the actual cost of your ambition?", None),
    ("Deep work", "Two hours of uninterrupted focus will accomplish more than eight hours of fragmented attention.", "When can you carve out two hours?", None),
    ("The outcome", "You can control your effort, but you rarely control the final outcome.", "Are you at peace with your effort?", None),
    ("The hustle", "Hustle culture often glorifies exhaustion instead of efficiency.", "Where can you be more efficient and less exhausted?", None),
    ("The machine", "The organization will keep running whether you answer the email tonight or tomorrow morning.", "What can wait until tomorrow?", None),
    ("The mentor", "A good mentor shows you what is possible; a great mentor shows you what is unnecessary.", "What unnecessary thing can you stop doing?", None),
    ("The break", "The best ideas often arrive when you have stopped trying to force them.", "When did you last step away from the problem?", None),
    ("The standard", "Your personal standard of excellence is more important than the company's metrics.", "What does excellent work look like to you?", None),
    ("The pivot", "Quitting a bad strategy is not failure; it is wisdom.", "What strategy is no longer serving you?", None),
    ("The priority", "If everything is a priority, then nothing is a priority.", "What is the single most important task today?", None),
    ("The audience", "You do not need to perform your productivity for anyone.", "Can you just do the work quietly?", None),
    ("The finish line", "There is always another project. The finish line is an illusion.", "How do you celebrate the small completions?", None),
    ("The crisis", "A lack of planning on their part does not constitute an emergency on yours.", "Are you absorbing someone else's stress?", None),
    ("The weekend", "The weekend is meant for recovery, not preparation for Monday.", "Are you actually resting on your days off?", None),
    ("The long game", "A sustainable career is built on a foundation of adequate sleep.", "Are you resting enough to sustain your ambition?", None),
    ("The output", "Your worth is not measured by your daily output.", "How do you measure a good day?", None),
    ("The feedback", "Constructive feedback is a tool, not a final judgment of your character.", "How can you use the tool and discard the judgment?", None),
    ("The transition", "The drive home is the airlock between who you are at work and who you are at home.", "How do you transition out of work mode?", None),
    ("The yes", "Every 'yes' at work is a 'no' to something else.", "What are you saying 'no' to right now?", None),
    ("The metric", "Not everything valuable can be measured on a spreadsheet.", "What valuable contribution are you making that cannot be tracked?", None),
    ("The quiet", "A quiet office is a luxury that should be fiercely protected.", "How do you protect your quiet time?", None),
    ("The default", "Make 'no' your default answer until you have time to consider the request.", "What request needs more consideration before you accept?", None),
    ("The routine", "A boring, predictable workday is often a sign of competence.", "Are you comfortable with a boring day?", None),
    ("The error", "A mistake at work is simply a data point for future decisions.", "What did your last mistake teach you?", None),
    ("The balance", "Work-life balance is not a daily achievement; it is a long-term average.", "How is your balance averaging out this month?", None),
    ("The exit", "Knowing when to leave a room, a project, or a job is a superpower.", "What are you ready to leave behind?", None),
    ("The reward", "The reward for doing good work should not be more work.", "How do you reward yourself for a job well done?", None),
    ("The transition", "You do not need to monetize your hobbies.", "What do you do simply because you enjoy it?", None),
    ("The speed", "Going slower often results in fewer mistakes and better work.", "Where can you slow down today?", None),
    ("The comparison", "Your Chapter 2 cannot be compared to someone else's Chapter 20.", "What are you building right now?", None),
    ("The presence", "When you are at work, work. When you are home, be home.", "Where is your attention right now?", None),
    ("The shift", "The desire for impact eventually replaces the desire for recognition.", "What impact are you making quietly?", None)
]

# Load existing wisdom
with open("PocketWisdom/Resources/wisdom.json", "r") as f:
    existing = json.load(f)

cards = []
for title, body, reflection, author in quotes:
    cards.append({
        "id": str(uuid.uuid4()),
        "category": "Work",
        "title": title,
        "body": body,
        "reflection": reflection,
        "author": author
    })

merged = existing + cards
with open("PocketWisdom/Resources/wisdom.json", "w") as f:
    json.dump(merged, f, indent=2)

print(f"Generated 50 work cards. Total cards: {len(merged)}")
