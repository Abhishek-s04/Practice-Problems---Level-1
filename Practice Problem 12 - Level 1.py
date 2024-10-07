'''Write a python function to generate and return the list of all possible sentences created from the given lists of Subject, Verb and Object.
Note: The sentence should contain only one subject, verb and object each.'''
def generate_sentences(subjects, verbs, objects):
    sentence_list = []  # Initialize an empty list to hold the sentences
    
    # Iterate through each combination of subject, verb, and object
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                # Create a sentence and append it to the sentence_list
                sentence = f"{subject} {verb} {obj}"
                sentence_list.append(sentence)
    
    return sentence_list

# Example input lists
subjects = ["I", "You"]
verbs = ["love", "play"]
objects = ["Hockey", "Football"]

# Generate and print the list of sentences
print(generate_sentences(subjects, verbs, objects))
