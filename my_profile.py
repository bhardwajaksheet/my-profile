# my_profile.py

# --- Your Details ---
name = "Aksheet Bhardwaj"
age = 20  # change to your age
birth_year = 2006  # change to yours
graduation_year = 2028
current_year = 2026

# --- Calculations ---
years_to_graduation = graduation_year - current_year
days_to_graduation = years_to_graduation * 365

# --- ML Goal ---
hours_per_day = 1.5
total_study_hours = days_to_graduation * hours_per_day

# --- Output ---
print(f"👋 Hi, I'm {name}!")
print(f"🎓 Years to graduation: {years_to_graduation} years ({days_to_graduation} days)")
print(f"📚 If I study {hours_per_day} hrs/day, I'll have {total_study_hours} hours of ML by graduation!")
print(f"🚀 Goal: MLOps + GenAI Engineer by {graduation_year}")