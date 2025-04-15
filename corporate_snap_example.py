# corporate_snap_example.py
"""
A totally realistic simulation of corporate restructuring
using the power of thanosPy.

WARNING: May contain traces of dark humor and existential dread
         about middle management decisions.
"""

import math
import random
import time

import thanospy

# --- Configuration ---
# Let's make today's rebalancing reproducible, unlike actual corporate decisions.
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# Our "highly valued" team members
employees = [
    "Alice (Marketing)",
    "Bob (Sales)",
    "Charlie (Engineering)",
    "David (Engineering)",
    "Eve (HR)",
    "Frank (Sales)",
    "Grace (Marketing)",
    "Heidi (Finance)",
    "Ivy (Engineering)",
    "Judy (HR)",
    "Kevin (Sales)",
    "Linda (Finance)",
    "Mallory (Security... oops?)",  # Maybe she shouldn't have been on this list
    "Nancy (Engineering)",
    "Oscar (Marketing)",
]

print("=" * 40)
print("     Thanos Corp - Q3 Synergy Update")
print("=" * 40)
print(f"\nCurrent Team Size: {len(employees)}")
print("Our Dedicated Workforce:")
for emp in employees:
    print(f"- {emp}")
print("-" * 40)

print("\nManagement senses... an imbalance in the workforce.")
time.sleep(1.5)
print("Time for some 'optimization' and 'right-sizing'...")
time.sleep(1.5)
print("Consulting the Infinity Gauntlet... uh, I mean, the HR Mandate...")
time.sleep(2)
print("\nCommencing resource balancing protocol...")
print("    *snap*")
time.sleep(1)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(1)


# The moment of truth! Apply the snap.
survivors = thanospy.snap(employees)

# Calculate expected survivors (as per thanospy logic)
expected_remaining = math.ceil(len(employees) / 2)

print("\n" + "=" * 40)
print("     Post-Restructuring Alignment")
print("=" * 40)

print(f"\nOriginal Headcount: {len(employees)}")
print(f"Target Headcount (approx 50%): {expected_remaining}")
print(f"Actual Remaining Headcount: {len(survivors)}")

if len(survivors) == expected_remaining:
    print("\nThe team is now... perfectly balanced. As all things should be.")
else:
    # This shouldn't happen with the current logic, but good to have a catch
    print(
        "\nHmm, the balance is slightly off. Someone check the gauntlet's calibration."
    )

print("\nRemaining Team Members (The Lucky Ones?):")
if survivors:
    for emp in sorted(survivors):  # Sort for easier viewing
        print(f"- {emp}")
else:
    print(
        "- ...Dust and echoes..."
    )  # In case everyone got snapped (unlikely for lists > 0)

print("\n" + "=" * 40)
print("   Please update your org charts accordingly.")
print("=" * 40)

# You might want to run this multiple times (without the fixed seed)
# to see different random outcomes, just like real layoffs!
# print(f"\n(Seed used: {RANDOM_SEED})")
