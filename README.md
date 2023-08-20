# AI-Poem-Generator-RNN
An enchanting Recurrent Neural Network (RNN) model designed to generate captivating poems. Trained on the eloquent prose of Robert Green's '48 Laws of Power,' this repository is your gateway to the world of AI-powered poetry

https://github.com/SivaVimel/AI-Poem-Generator-RNN/assets/87802556/cc2e0ea0-0321-4233-b614-653ea8b3d33d

---

Ladies and gentlemen,

Today, I am thrilled to introduce you to a fascinating world of text generation using a Recurrent Neural Network, or RNN for short. In this demonstration, we'll explore how RNNs can generate text, delve into the training process, and witness the incredible creative potential of artificial intelligence.

Our primary objective is to generate text that appears coherent, meaningful, and even artistic. We'll accomplish this by training our RNN on a dataset of text, in this case, Robert Green's writing on the '48 Laws of Power.' It's important to note that our model operates on the character level, which means it doesn't understand words or their meanings. It's all about patterns and probabilities.

Now, let's take a closer look at the steps involved:

1. **Data Preparation**: First, we examine the dataset to understand the characters and their uniqueness. Then, we preprocess the text by converting it into a numerical format. We use the `tf.keras.layers.StringLookup` layer to map characters to numeric IDs and vice versa.

2. **Training Data**: To train our model, we need pairs of inputs and labels. At each time step, the input is a character, and the label is the next character in the sequence. We chunk the text into sequences, and each sequence becomes an input and label pair.

3. **Model Building**: Our model consists of several key components:
   - `tf.keras.layers.Embedding`: This layer converts character IDs into vectors.
   - `tf.keras.layers.GRU`: A type of Recurrent Neural Network.
   - `tf.keras.layers.Dense`: The output layer, predicting the next character.

4. **Training**: We use a custom training loop to train our model. The loop tracks gradients, calculates loss, and updates the model using an optimizer. We're not using 'teacher-forcing,' so our model learns to recover from its own mistakes.

5. **Text Generation**: Once the model is trained, we can use it to generate text. We do this by repeatedly feeding a seed text into the model and predicting the next character. This process continues, and we accumulate characters to form longer sequences.

The results are often intriguing. The model can generate text with proper capitalization and paragraph breaks, resembling a Shakespearean style. However, with a limited number of training epochs, it may not always create coherent sentences.

There are many ways to enhance the results. You can increase the number of training epochs, experiment with different start strings, adjust parameters like temperature to control randomness, or even add more RNN layers for accuracy.

In the end, this technology opens the door to exciting possibilities in natural language generation, creative writing, and more. It's a testament to the power of machine learning.

I encourage you to explore further, experiment with different texts, and unleash your creativity with this remarkable tool. The possibilities are as vast as your imagination.

Thank you for joining us on this journey into the world of text generation with RNNs. Now, let's witness our model's poetic talents in action!

![Screenshot 2023-08-18 224817](https://github.com/SivaVimel/AI-Poem-Generator-RNN/assets/87802556/7a7489d4-43b9-4390-9c32-11aaffac1518)

![Screenshot 2023-08-18 234943](https://github.com/SivaVimel/AI-Poem-Generator-RNN/assets/87802556/b3fc9afe-d767-49d8-9720-45ac5352af80)


![Snake animation](https://github.com/gogulkrish/snak-/blob/main/rafaballerini-output/github-contribution-grid-snake.svg)
