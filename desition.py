print("===== SMART DECISION SYSTEM =====")

# -------------------------------
# MODULE 1: LIE DETECTOR
# -------------------------------
print("\n--- Module 1: Lie Detector ---")

age = int(input("Enter your age: "))
birth_year = int(input("Enter your birth year: "))

current_year = 2026
calculated_age = current_year - birth_year

if age == calculated_age:
    print("✅ Your data is consistent.")
else:
    print("⚠️ Inconsistency detected!")
    if age > calculated_age:
        print("👉 You entered a higher age than expected.")
    else:
        print("👉 You entered a lower age than expected.")

# -------------------------------
# MODULE 2: PERSONALITY TEST
# -------------------------------
print("\n--- Module 2: Personality Test ---")

score = 0

q1 = input("Do you like socializing? (yes/no): ")
q2 = input("Do you enjoy reading books? (yes/no): ")
q3 = input("Do you like adventures? (yes/no): ")

if q1 == "yes":
    score += 2
else:
    score += 1

if q2 == "yes":
    score += 2
else:
    score += 1

if q3 == "yes":
    score += 2
else:
    score += 1

print("Your score:", score)

if score >= 5:
    print("🌟 You are an EXTROVERT!")
elif score == 4:
    print("🙂 You are BALANCED!")
else:
    print("🌙 You are an INTROVERT!")

# -------------------------------
# MODULE 3: RULE ENGINE (Loan Approval)
# -------------------------------
print("\n--- Module 3: Rule Engine ---")

income = int(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))

if income > 50000 and credit_score > 700:
    print("✅ Loan Approved (High confidence)")
elif income > 30000 and credit_score > 600:
    print("⚠️ Loan Approved (Medium confidence)")
elif income > 20000 and credit_score > 500:
    print("❗ Loan Pending Review")
else:
    print("❌ Loan Rejected")

# Nested condition
if income > 50000:
    if credit_score > 750:
        print("💎 Premium Customer Benefits Activated")

# -------------------------------
# MODULE 4: DATA VALIDATION
# -------------------------------
print("\n--- Module 4: Data Validation ---")

email = input("Enter your email: ")
password = input("Enter your password: ")

if "@" in email and "." in email:
    print("✅ Email looks valid")
else:
    print("❌ Invalid email format")

if len(password) >= 8:
    print("✅ Strong password length")
    if any(char.isdigit() for char in password):
        print("🔢 Password contains numbers")
    else:
        print("⚠️ Add numbers to strengthen password")
else:
    print("❌ Password too short")

# -------------------------------
# MODULE 5: SIMULATION (Health Game)
# -------------------------------
print("\n--- Module 5: Simulation Game ---")

health = 100
hunger = 50

print("Starting Health:", health)
print("Starting Hunger:", hunger)

action = input("Choose action (eat/work/rest): ")

if action == "eat":
    hunger -= 20
    health += 10
    print("🍔 You ate food")
elif action == "work":
    hunger += 20
    health -= 15
    print("💼 You worked hard")
elif action == "rest":
    health += 20
    print("🛌 You rested well")
else:
    print("❌ Invalid action")

# More conditions
if hunger > 80:
    health -= 20
    print("⚠️ Too hungry! Health decreasing")

if health <= 0:
    print("💀 Game Over! Health reached 0")
elif health > 100:
    print("💪 Excellent health condition!")
else:
    print("🙂 You are still alive and playing")

print("\nFinal Health:", health)
print("Final Hunger:", hunger)

# -------------------------------
# FINAL SUMMARY USING DICTIONARY
# -------------------------------
print("\n--- Final Summary ---")

user_data = {
    "Age": age,
    "Birth Year": birth_year,
    "Personality Score": score,
    "Income": income,
    "Credit Score": credit_score,
    "Health": health,
    "Hunger": hunger
}

print("📊 User Data Summary:")
for key in user_data:
    print(key, ":", user_data[key])

print("\n===== SYSTEM COMPLETE =====")