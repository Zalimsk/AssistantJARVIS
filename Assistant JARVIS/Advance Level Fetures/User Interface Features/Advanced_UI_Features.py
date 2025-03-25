import json

class UserInterfaceFeatures:
    def __init__(self):
        self.features = {
            "Core Features": [
                "Intuitive Dashboard: User-friendly interface for easy navigation.",
                "Customization Options: Users can customize layouts and themes.",
                "Responsive Design: Interface adapts to different screen sizes seamlessly.",
                "Keyboard Shortcuts: Quick access to frequently used features."
            ],
            "Accessibility Features": [
                "Tooltips and Help Icons: Contextual help for new users.",
                "Accessibility Options: Features for visually impaired users, like screen readers."
            ],
            "Navigation and Usability": [
                "Navigation Menus: Clear and structured menus for easy access.",
                "Search Functionality: Quick search bar for finding information.",
                "Consistent Layout: Similar design across all pages for familiarity.",
                "Feedback Mechanisms: Notifications for user actions."
            ],
            "Advanced Features": [
                "Adaptive Layouts: UI adjusts based on user preferences.",
                "Gesture Support: Touch and swipe gestures for navigation on mobile devices.",
                "Dark Mode: Option for a dark theme to reduce eye strain.",
                "Real-time Collaboration Tools: Allowing multiple users to interact simultaneously."
            ]
        }

    def display_features(self):
        print("User Interface Features:")
        for category, items in self.features.items():
            print(f"\n{category}:")
            for feature in items:
                print(f" - {feature}")

    def add_feature(self, category, feature):
        if category in self.features:
            self.features[category].append(feature)
            print(f"Added feature to {category}: {feature}")
        else:
            print(f"Category '{category}' not found.")

    def remove_feature(self, category, feature):
        if category in self.features and feature in self.features[category]:
            self.features[category].remove(feature)
            print(f"Removed feature from {category}: {feature}")
        else:
            print(f"Feature '{feature}' not found in category '{category}'.")

    def get_feature_count(self):
        total_features = sum(len(items) for items in self.features.values())
        print(f"Total features available: {total_features}")

    def search_feature(self, keyword):
        print(f"\nSearching for '{keyword}':")
        found = False
        for category, items in self.features.items():
            for feature in items:
                if keyword.lower() in feature.lower():
                    print(f" - {feature}")
                    found = True
        if not found:
            print("No features found.")

    def sort_features(self):
        for category in self.features:
            self.features[category].sort()
        print("Features sorted alphabetically within each category.")

    def save_to_file(self, filename='ui_features.json'):
        with open(filename, 'w') as f:
            json.dump(self.features, f, indent=4)
        print(f"Features saved to {filename}.")

    def load_from_file(self, filename='ui_features.json'):
        try:
            with open(filename, 'r') as f:
                self.features = json.load(f)
            print(f"Features loaded from {filename}.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

if __name__ == "__main__":
    ui_features = UserInterfaceFeatures()
    ui_features.display_features()

    # Example of user interaction
    while True:
        action = input("\nChoose an action: add, remove, search, sort, save, load, exit: ").strip().lower()
        
        if action == "add":
            category = input("Enter category: ")
            feature = input("Enter feature: ")
            ui_features.add_feature(category, feature)
        elif action == "remove":
            category = input("Enter category: ")
            feature = input("Enter feature: ")
            ui_features.remove_feature(category, feature)
        elif action == "search":
            keyword = input("Enter keyword to search: ")
            ui_features.search_feature(keyword)
        elif action == "sort":
            ui_features.sort_features()
        elif action == "save":
            ui_features.save_to_file()
        elif action == "load":
            ui_features.load_from_file()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")

    ui_features.get_feature_count()
