import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the multilingual BERT model and tokenizer
model_name = "bert-base-multilingual-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Set the device (GPU or CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Prepare some example text data in different languages
texts = ["This is a positive English sentence.", "Esto es una oración negativa en español."]
labels = [1, 0]  # 1 for positive, 0 for negative (example binary classification task)

# Tokenize and encode the input data
inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
inputs = {k: v.to(device) for k, v in inputs.items()}

# Forward pass through the model
outputs = model(**inputs, labels=torch.tensor(labels, dtype=torch.long, device=device))

# Calculate the loss and logits
loss = outputs.loss
logits = outputs.logits

print(f"Loss: {loss}, Logits: {logits}")
