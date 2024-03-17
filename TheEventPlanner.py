attendees = int(input("Enter number of attendees: "))
food_choice = input("Would you like to include vegetarian food on your menu? Type y or n: ").lower()
venue = "large hall"; other_services = "large audio system" if attendees > 100 else "conference room"
caterer = "Veggie Delight Caterers" if food_choice == "y" else "Gourmet Meals Caterers"
print(f"Suggested Venue: {venue}. We also offer {other_services} based on your guest list size. We recommend {caterer} to cater your wedding.")

# Task 2: Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees.

# Task 3: Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
