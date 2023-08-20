from model import *

spell = SpellChecker()
s = []
start = time.time()
states = None
next_char = tf.constant(["love :"])
result = [next_char]

for n in range(100):
    next_char, states = one_step_model.generate_one_step(
        next_char, states=states
    )
    result.append(next_char)

result = tf.strings.join(result)
end = time.time()
misspelled = result[0].numpy().decode("utf-8")
yo = convertTuple(misspelled)
poem = yo.split()
for word in poem:
    s2 = spell.correction(word)
    s.append(s2)

words_per_line = 5

word_list = [word for word in s if word is not None]

for i in range(0, len(word_list), words_per_line):
    chunk = word_list[i:i + words_per_line]
    line = ' '.join(chunk)
    print(line)
    engine.say(line)
    engine.runAndWait()
    

print("\nRun time:", end - start)