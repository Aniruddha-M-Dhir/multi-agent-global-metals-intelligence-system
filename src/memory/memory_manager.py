"""
Memory Manager
Stores and loads simple user preferences such as preferred currency or metals.
Uses a lightweight JSON file for demonstration.
"""

import json
import os

PREFS_FILE = os.path.join(os.path.dirname(__file__), "user_preferences.json")

class MemoryManager:

    def __init__(self):
        # Load preferences on startup
        self.preferences = self.load_preferences()

    def load_preferences(self):
        """
        Load the JSON file safely.
        """
        if not os.path.exists(PREFS_FILE):
            return {}

        try:
            with open(PREFS_FILE, "r") as f:
                return json.load(f)
        except:
            return {}

    def save_preferences(self):
        """
        Saves the current preferences to the JSON file.
        """
        try:
            with open(PREFS_FILE, "w") as f:
                json.dump(self.preferences, f, indent=4)
        except Exception as e:
            print("Error saving preferences:", e)

    def set_preference(self, key, value):
        """
        Add or update a preference.
        """
        self.preferences[key] = value
        self.save_preferences()

    def get_preference(self, key, default=None):
        """
        Retrieve a preference.
        """
        return self.preferences.get(key, default)

