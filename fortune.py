import random

print("🔮 Welcome to Bharath Kumar Borra's Fortune Teller (21JE0219) 🔮")

mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "Great things await you, Bharath Kumar Borra! Keep smiling.",
        "Your joy will spread like sunshine today!",
        "Happiness attracts success—stay radiant!"
    ],
    "sad": [
        "Storms don’t last forever. Better days are coming.",
        "Your tears water the seeds of your future strength.",
        "Be kind to yourself—this too shall pass."
    ],
    "neutral": [
        "Balance brings clarity. Stay steady.",
        "Sometimes peace is the greatest fortune.",
        "A calm mind leads to clear decisions."
    ],
    "stressed": [
        "Take a deep breath, Bharath Kumar Borra. You’ve got this!",
        "Don't forget to rest—strength returns with calm.",
        "Stress is temporary. Courage is forever."
    ]
}

if mood in fortunes:
    print(f"✨ Your fortune: {random.choice(fortunes[mood])} ✨")
else:
    print("❌ Unknown mood. Try again with happy, sad, neutral, or stressed.")
