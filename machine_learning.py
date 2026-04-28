from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features:
# [Tech, Social, Sport, Academic, Wellness]

X = [
    [1,0,0,0,0],  # Coding Society Meetup
    [0,0,0,1,0],  # Career Fair 2025
    [0,1,0,0,0],  # Board Game Night
    [1,0,0,1,0],  # Women in STEM Panel
    [0,0,1,0,0],  # 5K Campus Run
    [0,1,0,0,0],  # Midnight Movie Marathon
    [1,0,0,0,0],  # Hackathon Build for Good
    [0,0,0,0,1],  # Yoga on the Lawn
    [0,1,0,1,0],  # Study Buddy Matching
]

y = [
    "Coding Society Meetup",
    "Career Fair 2025",
    "Board Game Night",
    "Women in STEM Panel",
    "5K Campus Run",
    "Midnight Movie Marathon",
    "Hackathon: Build for Good",
    "Yoga on the Lawn",
    "Study Buddy Matching"
]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# KNN Model
model = KNeighborsClassifier(n_neighbors=1)

# Train model
model.fit(X_train, y_train)

# Predict test data
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Sarah likes Tech + Social
sarah = [[1,1,0,0,0]]

recommendation = model.predict(sarah)

print("Recommended Event for Sarah Mitchell:", recommendation[0])
