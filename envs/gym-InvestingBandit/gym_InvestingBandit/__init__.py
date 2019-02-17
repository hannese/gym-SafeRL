from gym.envs.registration import register

register(
    id='InvestingBandit-v0',
    entry_point='gym_InvestingBandit.envs:InvestingBanditEnv',
)
