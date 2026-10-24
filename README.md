# Stock Market Sentiment Analysis

A Python prototype that pulls stock prices and related tweets, cleans the tweet text with NLP tools, and sets up a simple model to classify sentiment as positive or negative.

> **Project status:** Working prototype. The sentiment model currently uses placeholder labels, so its accuracy is not meaningful yet. See [Limitations](#limitations) and [Next Steps](#next-steps).

## What It Does

1. **Collects stock prices** from Yahoo Finance (using `yfinance`) and plots the closing price over time.
2. **Collects tweets** about a stock (for example, "AAPL stock") through the Twitter API (using `tweepy`).
3. **Cleans the tweet text**: removes links and emojis, converts to lowercase, tokenizes with a BERT tokenizer, and reduces words to their base form with spaCy.
4. **Converts words to numbers** using pre-trained GloVe word embeddings (100 dimensions).
5. **Classifies sentiment** (positive or negative) with a logistic regression model and prints the accuracy.

## Tools Used

| Purpose | Tool |
|---|---|
| Stock data | yfinance, pandas |
| Tweets | tweepy (Twitter API) |
| Text cleaning | clean-text, spaCy, BERT tokenizer (Hugging Face transformers) |
| Word embeddings | GloVe (6B, 100d) |
| Model and evaluation | scikit-learn (logistic regression) |
| Charts | matplotlib |

## Getting Started

### Requirements

- Python 3.9 or newer
- A Twitter (X) developer account with API access
- The GloVe file `glove.6B.100d.txt` (download from the [Stanford GloVe page](https://nlp.stanford.edu/projects/glove/))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# 2. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Install the libraries
pip install yfinance pandas numpy matplotlib scikit-learn tweepy transformers spacy clean-text

# 4. Download the spaCy English model
python -m spacy download en_core_web_sm
```

### Set Up Your Keys

Open the main script and replace the placeholder values with your own Twitter API keys:

```python
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
```

Do not upload your real keys to GitHub. Store them in environment variables or a `.env` file that is listed in `.gitignore`.

Place `glove.6B.100d.txt` in the project folder (or update `glove_file_path` in the script).

### Run

```bash
python main.py
```

The script will:
- Show a chart of the stock's closing price (the default is AAPL from 2020 to 2022).
- Fetch 100 recent tweets about the stock.
- Print the model accuracy at the end.

To change the stock or dates, edit the `download_stock_data(...)` and `fetch_tweets(...)` calls in the main section of the script.

## Project Structure

| Function | What it does |
|---|---|
| `download_stock_data` | Downloads historical prices for a ticker |
| `authenticate_twitter` | Connects to the Twitter API |
| `fetch_tweets` | Gets tweets that match a search query |
| `preprocess_text` | Cleans, tokenizes and simplifies tweet text |
| `load_glove_embeddings` | Loads the GloVe word vectors |
| `get_embeddings` | Turns words into vectors (unknown words become zeros) |
| `sentiment_classification` | Trains logistic regression and predicts sentiment |
| `visualize_stock_data` | Plots the closing price |

## Limitations

Being clear about what this prototype does not do yet:

- **The sentiment labels are random placeholders.** The script creates them with a random generator so the pipeline can run end to end. Because of this, the printed accuracy does not reflect real performance.
- **It does not predict stock prices yet.** It collects price data and analyses tweet sentiment, but the two are not combined into a price forecast.
- **Small sample.** It uses 100 tweets for one stock by default.
- **Twitter API access** is required and may depend on your API plan.

## Next Steps

- Train on a real labeled financial sentiment dataset instead of random labels.
- Combine daily sentiment scores with price data to study how sentiment relates to price movement.
- Try a time-series model (such as LSTM) for price prediction.
- Move API keys to environment variables.
- Add a `requirements.txt` file and a short results section.

## License

Add a license of your choice (for example, MIT).
