from gym.envs.registration import register

register(
    id='OptionPricing-v0',
    entry_point='gym_OptionPricing.envs:OptionPricingEnv',
)
