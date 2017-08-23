import gym
import numpy as np
import random
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean, median
from collections import Counter

LR = 1e-3
env = gym.make('CartPole-v0')
env.reset()
goal_step = 500
score_requirement = 50
initial_games = 10000

# __random_game
def random_game():
  for episode in range(5):
    env.reset()
    for t in range(goal_step):
      env.render()
      action = env.action_space.sample()
      observation, reward, done, info = env.step(action)
      if done:
        break

# __start
def start():
  random_game()


if __name__ == '__main__':
  start()