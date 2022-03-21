from gym.envs.registration import register

register(id='Shower-v0',
    entry_point='gym_shower.envs:ShowerEnv',
)