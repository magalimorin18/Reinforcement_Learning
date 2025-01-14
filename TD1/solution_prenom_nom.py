# -*- coding: utf-8 -*-
import gym.envs.toy_text.frozen_lake as fl
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter

np.set_printoptions(precision=3)
NBR_EPISODES = 50000
HORIZON = 200
GAMMA = 0.9
SEED = int("whatAnAwesomePracticalSession", base=36) % 2 ** 31

# Create environment
env = fl.FrozenLakeEnv()  # gym.make('FrozenLake-v1')
env.seed(SEED)


def to_s(row, col):
    return row * env.ncol + col


def to_row_col(s):
    col = s % env.ncol
    row = s // env.ncol
    return row, col


def print_values(v):
    for row in range(env.nrow):
        for col in range(env.ncol):
            s = f"{v[to_s(row, col)]:.3}"
            print(s, end=' ' * (8 - len(s)))
        print("")


def convert_time(t1, t2):
    return f"Running time: {t2 - t1:.4f} sec\n"


# Question 4
print("\n\n######################")
print("##### Question 4 #####")
print("######################\n")
print("EXPECTED VALUE METHOD\n")


def value_function_expected(pi):
    v_pi = np.zeros(env.nS)
    for s in range(env.nS):
        v_s = 0
        s_c = s
        env.isd = np.zeros(env.nS)
        env.isd[s] = 1
        env.reset()
        for _ in range(NBR_EPISODES):
            env.reset()
            done = False
            t = 0
            discount = 1
            while not done and t < HORIZON:
                t += 1
                s_c, r, done, _ = env.step(pi[s_c])
                v_s += discount * r
                discount *= GAMMA
        v_pi[s] = v_s / NBR_EPISODES
    return v_pi


simple_pi = fl.RIGHT * np.ones(env.nS)
starting_time = perf_counter()
V_simple_pi = value_function_expected(simple_pi)
print(convert_time(starting_time, perf_counter()))
print(f"Value estimate of the starting point: {V_simple_pi[0]:.3f}")
print(f"Value function of the always RIGHT policy:\n")
print_values(V_simple_pi)

# reset the original isd
env.isd = np.zeros(env.nS)
env.isd[0] = 1

# pdb.set_trace()
# Question 5
print("\n######################")
print("##### Question 5 #####")
print("######################\n")
print("LINEAR SYSTEM METHOD\n")


def value_function(pi):
    """
    pi : int array
    For each index i, pi[i] is the action (int) chosen in state i

    return:
    ------
    V_pi : float array
    For each index i, V_pi[i] is the value (float) of the state i
    """
    return None


simple_pi = fl.RIGHT * np.ones(env.nS)
starting_time = perf_counter()
V_simple_pi = value_function(simple_pi)
print(convert_time(starting_time, perf_counter()))
print(f"Value estimate of the starting point: {V_simple_pi[0]:.3f}")
print(f"Value function of the always RIGHT policy:\n")
print_values(V_simple_pi)

# pdb.set_trace()
# Question 6
print("\n######################")
print("##### Question 6 #####")
print("######################\n")
print("BELLMAN OPERATOR METHOD\n")


def value_function_2(pi, epsilon, max_iter):
    """
    pi : int array
    For each index i, pi[i] is the action (int) chosen in state i

    epsilon : float
    Used as a threshold for the stopping rule

    max_iter : int
    Hard threshold on the number of loops

    return:
    ------
    V_pi : float array
    For each index i, V_pi[i] is the value (float) of the state i
    """
    # Compute both the reward vector r_pi and
    # transition matrix P_pi associated to the policy on the given env
    return v_pi, delta_inf


starting_time = perf_counter()
V_simple_pi, Delta_inf = value_function_2(simple_pi, 1e-4, 10000)
print(convert_time(starting_time, perf_counter()))
print(f"Value function of the always RIGHT policy:\n")
print_values(V_simple_pi)

plt.figure()
plt.title("Semi-log graph of $n \mapsto || V_{n+1} - V_n ||_\infty $ \n\
The Linearity of this graph proves exponential convergence")
plt.semilogy(Delta_inf)
plt.xlabel("Iterate")
plt.ylabel(r'$|| V_{n+1} - V_n ||_\infty$')
plt.savefig('question6.png')
print(f"\nNumber of iterations: {Delta_inf.size}")
print(f"Last residual {Delta_inf[-1]:.6f}")

# pdb.set_trace()
# Question 7
print("\n######################")
print("##### Question 7 #####")
print("######################\n")
print("OPTIMAL BELLMAN OPERATOR\n")


def value_function_optimal(epsilon, max_iter):
    """
    epsilon : float
    Used as a threshold for the stopping rule

    max_iter : int
    Hard threshold on the number of loops

    returns:
    -------
    V_opt : float array, (env.nS,) size
    Optimal value function on the FrozenLake MDP given a discount GAMMA
    V_opt[state index] = Value of that state
    """
    return v_opt, delta_inf


starting_time = perf_counter()
V_opt, Delta_inf = value_function_optimal(1e-4, 10000)
print(convert_time(starting_time, perf_counter()))
print(f"Optimal value function:\n")
print_values(V_opt)

plt.figure()
plt.title("Semi-log graph of $n \mapsto || V_{n+1} - V_n ||_\infty $ \n\
The Linearity of this graph proves exponential convergence")
plt.semilogy(Delta_inf)
plt.xlabel("Iterate")
plt.ylabel(r"$|| V_{n+1} - V_n ||_\infty$")
plt.savefig('question7.png')
print(f"\nNumber of iterations: {Delta_inf.size}")
print(f"Last residual {Delta_inf[-1]:.6f}")

# pdb.set_trace()
# Question 8
print("\n######################")
print("##### Question 8 #####")
print("######################\n")
print("VALUE ITERATION\n")


def value_iteration(epsilon, max_iter):
    """
    epsilon : float
    Used as a threshold for the stopping rule

    max_iter : int
    Hard threshold on the number of loops

    returns:
    -------
    pi : int array, size (env.nS,)
    An optimal policy
    """
    return pi_opt


ARROWS = {
    fl.RIGHT: "→",
    fl.LEFT: "←",
    fl.UP: "↑",
    fl.DOWN: "↓"
}


def print_policy(pi):
    for row in range(env.nrow):
        for col in range(env.ncol):
            print(ARROWS[pi[to_s(row, col)]], end='')
        print("")


starting_time = perf_counter()
Pi_opt = value_iteration(1e-4, 1000)
print(convert_time(starting_time, perf_counter()))
print("An optimal policy is:\n")
print_policy(Pi_opt)

# pdb.set_trace()
# Question 9
print("\n######################")
print("##### Question 9 #####")
print("######################\n")
print("POLICY ITERATION\n")


# The danger of Policy Iteration lies in the stopping criterion
# If not careful, one might end up with an algorithm that does not
# terminate and oscillates between optimal policies
# Even if it is computationally more expensive, we sometimes rather
# compare value functions of the policies than policies from one iterate
# to another.

# An easy improvement on the following code would be to use
# a warm start for policy evaluation steps (if iteration methods is used)
# That is to say, using the previously computed value function
# as the first step for the next policy evaluation


def policy_improvement(v):
    """
    V : float array, size (env.nS,)
    Value function of a policy

    returns:
    -------
    pi : int array, size (env.nS,)
    A policy that is greedy with respect to V
    """
    return pi


def policy_iteration(max_iter):
    """
    epsilon : float
    Used as a threshold for the stopping rule

    max_iter : int
    Hard threshold on the number of loops

    returns:
    -------
    pi : int array, size (env.nS,)
    An optimal policy
    """
    return pi


starting_time = perf_counter()
Pi_opt = policy_iteration(1000)
print(convert_time(starting_time, perf_counter()))
print("An optimal policy is:\n")
print_policy(Pi_opt)

# pdb.set_trace()
# Question 11
print("\n#######################")
print("##### Question 11 #####")
print("#######################\n")
print("OPTIMAL Q-BELLMAN OPERATOR METHOD\n")


def state_value_function_optimal(epsilon, max_iter):
    """
    epsilon : float
    Used as a threshold for the stopping rule

    max_iter : int
    Hard threshold on the number of loops

    returns:
    -------
    q_opt : float array, (env.nS, env.nA) size
    Optimal state-action value function on the FrozenLake MDP
    given a discount GAMMA
    q_opt[state index][action index] = state-action value of that state
    """
    return q_opt, delta_inf


starting_time = perf_counter()
Q_opt, Delta_inf = state_value_function_optimal(1e-4, 100)
print(convert_time(starting_time, perf_counter()))
# print(Q_opt)
V_opt = None
print(f"Optimal value function:\n")
print_values(V_opt)

plt.figure()
plt.title("Semi-log graph of $n \mapsto || Q_{n+1} - Q_n ||_\infty $ \n\
The Linearity of this graph proves exponential convergence")
plt.semilogy(Delta_inf)
plt.xlabel("Iterate")
plt.ylabel(r"$|| Q_{n+1} - Q_n ||_\infty$")
plt.savefig('question11.png')
print(f"\nNumber of iterations: {Delta_inf.size}")
print(f"Last residual {Delta_inf[-1]:.6f}")

# Question 12
print("\n#######################")
print("##### Question 12 #####")
print("#######################\n")

Pi_opt = np.argmax(Q_opt, axis=1)
print("\nAn optimal policy is:\n")
print_policy(Pi_opt)


# Question 13
print("\n#######################")
print("##### Question 13 #####")
print("#######################\n")
print("RENDER A TRAJECTORY\n")


# render policy
def trajectory(pi, max_moves=20):
    done = False
    i = 0
    env.reset()
    cumulative_reward = 0
    discount = 1
    while not done and i < max_moves:
        i += 1
        _, r, done, _ = env.step(pi[env.s])
        cumulative_reward += discount*r
        discount *= GAMMA
        env.render()
        print('')
    return cumulative_reward


cr = trajectory(Pi_opt)
print("\nThe GOAL has been reached! Congrats! :-)")
print(f"The cumulative discounted reward along the above trajectory is: {cr:.3f}\n")

