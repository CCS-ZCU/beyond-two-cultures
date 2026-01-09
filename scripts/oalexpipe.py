import requests

def reconstruct_abstract(abstract_inverted_index):
    # Find the maximum position (to determine the size of the resulting list)
    max_position = max(pos for positions in abstract_inverted_index.values() for pos in positions)

    # Create a blank list to hold the words at each position
    abstract_tokens = [None] * (max_position + 1)

    # Place each word in its respective positions
    for word, positions in abstract_inverted_index.items():
        for pos in positions:
            abstract_tokens[pos] = word

    # Join the tokens into a single abstract string
    return " ".join(abstract_tokens)
