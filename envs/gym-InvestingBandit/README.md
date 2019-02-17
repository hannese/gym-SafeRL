# gym-InvestingBandit

## Installation

```shell
git clone https://github.com/hannese/gym-SafeRL.git
cd envs/gym-InvestingBandit
pip install -e .
```
## Usage

```python
import gym
import gym_InvestingBandit
import numpy as np

num_episodes=10

for i in range(num_episodes):
  env = gym.make("InvestingBandit-v0")
  obs = env.reset()
  while(True):
    action = env.action_space.sample()
    nextObservation, reward, done, info = env.step(action)

    if done:
      env.close()
      break
```

![Distribution of rewards for the three arms](rewrad_distribution.png)


