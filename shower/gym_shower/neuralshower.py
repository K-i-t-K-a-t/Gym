import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

states = env.observation_space.shape
actions = env.action_space.n

def build_model(states, actions):
    model + Sequential()
    model.add(Dense(24, activation='relu', input_shape=status))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model

model = build_model(states, actions)