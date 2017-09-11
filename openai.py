import gym

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
