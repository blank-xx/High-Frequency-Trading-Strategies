import yfinance as yf
import tweepy
import spacy
from transformers import pipeline
import gym
from gym import spaces
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

data=yf.download("AAPL",start="2020-01-01",end="2022-01-01",interval='1m')
data.head()
import tweepy

# Setup Tweepy with API keys
auth = tweepy.OAuthHandler('FeFUDbwWWiEfTf33JvstULgYj', 'iX2IXq9XRmjI9XnVW5xUMBV3JTPnVgjLXEInuQ9gNb9Bo8aHBI')
auth.set_access_token("1838285472210014208-Z37Nidf4hPiTU2ORHGiD0BRAbmVicG", "1TEwWxUoFZJZCWjRDSswYjX5fxlGIwSnd9vV6Ty8yRfsN")
api = tweepy.API(auth)

# Fetch tweets about a stock
tweets = api.search_tweets(q="AAPL", lang="en", result_type="recent", count=100)
for tweet in tweets:
    print(tweet.text)

nlp = spacy.load('en_core_web_sm')

text = "The stock price of Apple has increased!"
doc = nlp(text)
processed_text = [token.lemma_ for token in doc if not token.is_stop]
print(processed_text)


# Analyze sentiment of financial news/tweets
sentiment_analysis = pipeline('sentiment-analysis')
result = sentiment_analysis("The stock price of AAPL surged by 5% after earnings.")
print(result)

class TradingEnv(gym.Env):
    def __init__(self, data):
        super(TradingEnv, self).__init__()
        self.data = data
        self.current_step = 0
        self.balance = 10000  # Initial balance
        self.position = 0  # No position at the start

        # Action space: Buy, Sell, Hold
        self.action_space = spaces.Discrete(3)

        # Observation space: Price, moving average, volume, sentiment
        self.observation_space = spaces.Box(low=0, high=1, shape=(5,))

    def step(self, action):
        # Implement the logic of taking an action (Buy, Sell, Hold)
        self.current_step += 1
        reward = 0
        done = False

        # Reward is the profit made from the action
        return self._next_observation(), reward, done, {}

    def _next_observation(self):
        # Return the current observation: Price, moving average, etc.
        obs = np.array([self.data[self.current_step]])
        return obs
    
class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

# Initialize the DQN
dqn = DQN(input_dim=5, output_dim=3)
optimizer = optim.Adam(dqn.parameters(), lr=0.001)