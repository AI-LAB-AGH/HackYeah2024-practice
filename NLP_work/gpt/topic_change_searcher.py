import torch
from transformers import BertTokenizer, BertForNextSentencePrediction
from NLP_work.gpt.GPT import GPT


class Topic_change_searcher:
    def __init__(self, path):
        self.tokenizer = BertTokenizer.from_pretrained('dkleczek/bert-base-polish-uncased-v1')
        self.model = BertForNextSentencePrediction.from_pretrained('dkleczek/bert-base-polish-uncased-v1')
        with open(path, "r") as f:
            self.transcript = f.read()

    def predict_next_sentence(self, sentence_a, sentence_b):
        encoding = self.tokenizer.encode_plus(sentence_a, sentence_b, return_tensors='pt')
        outputs = self.model(**encoding)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=1)
        next_sentence_prob = probs[0][0].item()  # Probability of being the next sentence
        not_next_sentence_prob = probs[0][1].item()  # Probability of not being the next sentence
        return next_sentence_prob

    def predict(self):
        topic_changes = []
        transcript = GPT().clean_transcript(self.transcript).strip()
        sentences = transcript.split(".")
        sentences = [sentence for sentence in sentences if sentence]
        for i in range(len(sentences) - 1):
            sentence_a = sentences[i]
            sentence_b = sentences[i + 1]
            value = self.predict_next_sentence(sentence_a, sentence_b)
            if value < 0.95:
                topic_changes.append(sentence_b)
        if len(topic_changes) == 0:
            return "brak"
        else:
            return "\n".join(topic_changes)



