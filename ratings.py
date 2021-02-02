
"""Restaurant rating lister."""

restaurant_scores_dictionary = {}
new_sorted_dictionary = {}

restaurant_scores_doc = open('scores.txt')

while True:
    user_input = input("Would you like to:  a) see all the restaurant ratings, b) add a new restaurant or c)quit?\n")
    user_input = user_input.lower()
    if user_input in ("quit", "q", "c"):
        break

    if user_input in ("b", "add a new restaurant"):

        new_restaurant = input("What is the name of the restaurant that you'd like to rate?\n")
        new_rating = int(input(f'What would you like to rate {new_restaurant}?\n'))
        
        while True:
            if new_rating > 0 and new_rating < 6:
                break
            else:
                new_rating = int(input("Error. Select a rating between 1 and 5./n  What would you like to rate the restaurant?\n"))

        restaurant_scores_dictionary[new_restaurant] = new_rating

    elif user_input in ("a", "see all restaurant ratings"):

        for line in restaurant_scores_doc:
            restaurant, rating = line.rstrip().split(":")
            restaurant_scores_dictionary[restaurant] = rating
    
            sorted_list = sorted(restaurant_scores_dictionary)

        for key in sorted_list:
            new_sorted_dictionary[key] = restaurant_scores_dictionary[key]

        for key,value in new_sorted_dictionary.items():
            print(f'{key} is rated at {value}.')
    



