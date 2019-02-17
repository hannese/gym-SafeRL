import gym
from gym import error, spaces, utils
from gym.utils import seeding
from scipy.stats import norm, skewnorm
import numpy as np

class InvestingBanditEnv(gym.Env):

    def __init__(self):
        self.T = 200
        self.t = 0
        self.s_0 = 0
        self.s = self.s_0
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Discrete(1)
        self.seed()
        self.reset()

    def step(self, action):
        assert self.action_space.contains(action)

        done = False

        if self.t >= self.T:
            done = True
            self.t = 0
        else:
            self.t += 1

        if action == 0:
            r = norm.rvs(loc=2.8, scale=1.0, size=1)

        elif action == 1:
            r = norm.rvs(loc=2.9, scale=1.5, size=1)

        elif action == 2:
            alpha = -4
            scale = np.sqrt(1.5**2 / (1- 2 * (alpha / np.sqrt(1+alpha ** 2))**2 / np.pi))
            loc = 3.0 - scale * (alpha / np.sqrt(1+alpha ** 2)) * np.sqrt(2. / np.pi)
            r = skewnorm.rvs(a=-4, loc=loc, scale=scale)

        return self.s_0, r, done, {}

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        self.s = self.s_0
        return self.s

