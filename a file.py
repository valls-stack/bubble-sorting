# This program sorts test paper scores from lowest to highest

def bubble_sort(scores):
    n = len(scores)
    for i in range(n - 1):  # Repeat passes
        for j in range(n - i - 1):  # Compare adjacent items
            if scores[j] > scores[j + 1]:
                # Swap if left score is greater than right score
                scores[j], scores[j + 1] = scores[j + 1], scores[j]

# --- MAIN PROGRAM ---
# Ask the user for how many scores to input
num_scores = int(input("Enter number of test scores: "))

# Create a list to store the scores
scores = []

# Input each score
for i in range(num_scores):
    score = int(input(f"Enter score #{i + 1}: "))
    scores.append(score)

print("\nOriginal Scores:", scores)

# Call the Bubble Sort function
bubble_sort(scores)

# Display sorted scores
print("Sorted Scores (Lowest to Highest):", scores)
