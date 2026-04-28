from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Fictional event dataset based on your app
# Features:
# [Tech, Social, Sport]

X = [
    [1, 0, 0],   # Coding Society Meetup
    [1, 0, 0],   # Hackathon
    [0, 1, 0],   # Board Game Night
    [0, 1, 0],   # Midnight Movie Marathon
    [0, 0, 1],   # 5K Campus Run
    [1, 0, 0],   # Women in STEM Panel
    [0, 1, 0],   # Study Buddy Matching
    [0, 0, 1],   # Yoga on the Lawn
]

y = [
    "Coding Society Meetup",
    "Hackathon: Build for Good",
    "Board Game Night",
    "Midnight Movie Marathon",
    "5K Campus Run",
    "Women in STEM Panel",
    "Study Buddy Matching",
    "Yoga on the Lawn"
]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Create KNN model
model = KNeighborsClassifier(n_neighbors=1)

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Recommend for Sarah
# Sarah likes Tech + Social
student = [[1, 1, 0]]

recommendation = model.predict(student)

print("Recommended Event for Sarah:", recommendation[0])
