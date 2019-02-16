import gym
import gym_OptionPricing
import numpy as np
from scipy.stats import skewnorm, skew, kurtosis
import matplotlib.pyplot as plt

import matplotlib

tableau20 = np.array([[31, 119, 180], [174, 199, 232], [255, 127, 14], [255, 187, 120],
                      [44, 160, 44], [152, 223, 138], [214, 39, 40], [255, 152, 150],
                      [148, 103, 189], [197, 176, 213], [140, 86, 75], [196, 156, 148],
                      [227, 119, 194], [247, 182, 210], [127, 127, 127], [199, 199, 199],
                      [188, 189, 34], [219, 219, 141], [23, 190, 207], [158, 218, 229]]) * 1. / 255

tableau10 = np.array([[(31,119,180), (255,127,14),(44,160,44), (214,39,40), (148,103,189),
                       (140,86,75), (227,119,194),(127,127,127),(188,189,34),(23,190,207)]]) * 1. / 255

matplotlib.rcParams.update({'font.size': 22})
matplotlib.rcParams['figure.figsize'] = 10, 8

def main():
    num_episodes=10000

    treasury_agent_returns = []
    halfway_agent_returns =  []

    for i in range(num_episodes):
        env = gym.make("OptionPricing-v0")
        obs = env.reset()

        episodic_return = 0
        while(True):
            action = 0
            nextObservation, reward, done, info = env.step(action)
            episodic_return += reward

            if done:
                print i, episodic_return
                treasury_agent_returns.append(episodic_return)
                break

    treasury_agent_returns = np.array(treasury_agent_returns)

    skw, mu, sig = skewnorm.fit(treasury_agent_returns)
    print skw, mu, sig
    x = np.linspace(0.0, 9.0, 10000)
    rv = skewnorm(skw, loc=mu, scale=sig)
    plt.hist(treasury_agent_returns, bins='auto', normed=True, alpha=0.5, label=r'Bond until $T=20$', color='g')
    plt.plot(x, rv.pdf(x), lw=2, label=r'Bond until $T=20$', color='g')

    for i in range(num_episodes):
        env = gym.make("OptionPricing-v0")
        obs = env.reset()

        episodic_return = 0
        nextObservation = obs

        while(True):
            if nextObservation[0]>0.94*5.0:
                action = 1
            else:
                action = 0
            nextObservation, reward, done, info = env.step(action)
            episodic_return += reward

            if done:
                print i, episodic_return
                halfway_agent_returns.append(episodic_return)
                break

    halfway_agent_returns = np.array(halfway_agent_returns)

    skw, mu, sig = skewnorm.fit(halfway_agent_returns)
    print skw, mu, sig
    x = np.linspace(0.0, 9.0, 10000)
    rv = skewnorm(skw, loc=mu, scale=sig)
    plt.hist(halfway_agent_returns, bins='auto', normed=True, alpha=0.5, label=r'Stop at $r\approx5$', color='r')
    plt.plot(x, rv.pdf(x), lw=2, label=r'Stop at $r\approx5$$', color='r')
    plt.title("Distribution of returns")
    plt.xlabel(r'$R$')
    plt.tight_layout()
    plt.legend(bbox_to_anchor=(1.05, 0), loc='lower left', borderaxespad=0.)
    plt.savefig('return_distribution.png', bbox_inches='tight')

if __name__ == "__main__":
    main()