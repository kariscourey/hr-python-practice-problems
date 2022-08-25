# Complete the make_sentences function that accepts three
# lists.
#   * subjects contains a list of subjects for three-word sentences
#   * verbs contains a list of verbs for three-word sentences
#   * objects contains a list of objects for three-word sentences
# The make_sentences function should return all possible sentences
# that can be made from the words in each list
#
# Examples:
#   * subjects: ["I"]
#     verbs:    ["play"]
#     objects:  ["Portal"]
#     returns:  ["I play Portal"]
#   * subjects: ["I", "You"]
#     verbs:    ["play"]
#     objects:  ["Portal", "Sable"]
#     returns:  ["I play Portal", "I play Sable",
#                "You play Portal", "You play Sable"]
#   * subjects: ["I", "You"]
#     verbs:    ["play", "watch"]
#     objects:  ["Portal", "Sable"]
#     returns:  ["I play Portal", "I play Sable",
#                "I watch Portal", "I watch Sable",
#                "You play Portal", "You play Sable"
#                "You watch Portal", "You watch Sable"]
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def make_sentences(subjects, verbs, objects):

    # Init var
    sentences = []

    for subject in subjects:  # I
        for verb in verbs:  # play
            for object in objects:  # Portal
                sentence = subject + " " + verb + " " + object
                sentences.append(sentence)  # runs len(sub) * len(verb)
                # * len(sent) # times ... when you concetenate,
                # it makes a new string

    return sentences


# Init var
subjects = ['I', 'We']
verbs = ['play', 'watch', 'turn on']
objects = ['Skyrim', 'DnD', 'BOTW']

# Invoke and print
print(make_sentences(subjects, verbs, objects))
