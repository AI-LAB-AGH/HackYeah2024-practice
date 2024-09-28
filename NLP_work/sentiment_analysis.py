import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class SentimentAnalysis:
    def __init__(self, transcript_path):
        self.id2label = {0: "negative", 1: "neutral", 2: "positive"}
        self.tokenizer = AutoTokenizer.from_pretrained("Voicelab/herbert-base-cased-sentiment")
        self.model = AutoModelForSequenceClassification.from_pretrained("Voicelab/herbert-base-cased-sentiment")
        with open(transcript_path, "r") as f:
            self.transcript = f.read()

    def predict(self):
        encoding = self.tokenizer(
            self.transcript,
            add_special_tokens=True,
            return_token_type_ids=True,
            truncation=True,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt',
        )

        output = self.model(**encoding).logits.to("cpu").detach().numpy()
        prediction = self.id2label[np.argmax(output)]
        prediction_values = output
        prediction_values = self.softmax(prediction_values)
        return (prediction, prediction_values)

    def softmax(self, x):
        x = np.array(x)
        exp_x = np.exp(x - np.max(x))
        return exp_x / np.sum(exp_x)


