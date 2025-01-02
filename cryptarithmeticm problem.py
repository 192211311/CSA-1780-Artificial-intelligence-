from itertools import permutations

def solve_cryptarithmetic(word1, word2, result_word):
    letters = set(word1 + word2 + result_word)
    if len(letters) > 10:
        return "Too many letters."
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result_word[0]] == 0:
            continue
        num1 = int("".join(str(mapping[c]) for c in word1))
        num2 = int("".join(str(mapping[c]) for c in word2))
        num_result = int("".join(str(mapping[c]) for c in result_word))
        if num1 + num2 == num_result:
            return f"{word1} = {num1}, {word2} = {num2}, {result_word} = {num_result}"
    return "No solution."

word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result_word = input("Enter result word: ").upper()

print(solve_cryptarithmetic(word1, word2, result_word))
