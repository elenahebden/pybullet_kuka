import os
import numpy as np
import time
import pybullet_multigoal_gym as pmg

num_episodes = 32
env = pmg.make_env(task='block_rearrange',
                   gripper='parallel_jaw',
                   grip_informed_goal=False,
                   num_block=4,
                   render=True,
                   visualize_target=True,
                   binary_reward=True,
                   joint_control=False,
                   max_episode_steps=10000,
                   image_observation=False,
                   use_curriculum=True,
                   task_decomposition=False,
                   num_goals_to_generate=num_episodes)

env.activate_curriculum_update()
obs = env.reset(test=False)
time_done = False
while not time_done:
    # time.sleep(0.1)
    # action = env.action_space.sample() * 0
    # action[-1] = -1
    # obs, reward, time_done, info = env.step(action)
    # if time_done:
    #     env.reset(test=False)
    #     time_done = False
    # env.set_sub_goal(0)
    # print(env.desired_goal)
    # env.set_sub_goal(1)
    # print(env.desired_goal)
    # env.set_sub_goal(2)
    # print(env.desired_goal)
    # env.set_sub_goal(3)
    # print(env.desired_goal)
    # env.set_sub_goal(4)
    # print(env.desired_goal)
    # env.set_sub_goal(5)
    # print(env.desired_goal)
    # env.set_sub_goal(6)
    # print(env.desired_goal)
    # env.set_sub_goal(7)
    # print(env.desired_goal)
    env.reset(test=False)
