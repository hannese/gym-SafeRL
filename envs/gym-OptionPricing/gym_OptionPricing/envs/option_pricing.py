import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class OptionPricingEnv(gym.Env):

    """ OptionPricing environment
     0) wait,
     1) stop,
    http://www.jmlr.org/papers/volume18/15-636/15-636.pdf
    """

    def __init__(self):
        self.f_u = 2
        self.f_d = 0.5
        self.p = 0.35
        self.p_h = 0.2
        self.T = 20
        self.p_r = 1-0.5 ** (1./self.T)
        self.gamma = 0.95
        self.K = 5.0

        self.s_0 = [1, 0]
        self.s = self.s_0
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Tuple((
            spaces.Box(low=0., high=self.K, shape=(1,), dtype=np.float32),
            spaces.Discrete(1)))
        self.seed()
        self.reset()

    def step(self, action):
        assert self.action_space.contains(action)

        done = False

        if np.random.rand() < self.p_r:
            action = not action

        if action or (self.s[1] >= self.T):     # Stop
            reward = min(self.K, self.s[0])
            self.s = self.s_0
            done = True

        elif (not action): # Wait
            factor = np.random.choice([self.f_u, self.f_d], p=[self.p, 1-self.p])
            self.s = [self.gamma * min(factor * self.s[0], self.K), self.s[1]+1]
            reward = self.p_h

        return self.s, reward, done, {}

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        self.s = self.s_0
        return self.s

