from gym.envs.registration import register
 
register(id='BouncingBall-v0', 
    entry_point='gym_bouncingball.envs:BouncingBallEnv', 
)