## 14. Introduction to Reinforcement Learning

## Study Notes

### 1. 🤖 Introduction to Reinforcement Learning (RL)

Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment. Unlike supervised learning, where the model learns from labeled examples, RL involves learning from the consequences of actions through rewards or penalties. The goal is for the agent to learn a policy—a strategy for choosing actions—that maximizes the total reward it receives over time.

RL has become increasingly important in various real-world applications. For example, in **autonomous driving**, RL helps vehicles learn how to navigate complex environments safely and efficiently by trial and error. In **robotics**, RL can teach robots to perform tasks like pushing objects to target locations, even when the environment is dynamic or partially unknown. In **games**, RL has shown remarkable success, such as DeepMind’s Deep Q-Network (DQN) algorithm that mastered Atari games, surpassing human-level performance.

The key challenge in RL is that rewards are often **delayed**—the agent might take many actions before seeing the outcome—and the environment may be only **partially observable** or **stochastic** (random). This makes learning optimal behavior a complex but fascinating problem.


### 2. 🎯 The Reinforcement Learning Problem and Markov Decision Processes (MDP)

At the heart of RL is the **Reinforcement Learning Problem**: how can an agent learn to choose actions that maximize its cumulative reward over time?

To formalize this, RL problems are often modeled as a **Markov Decision Process (MDP)**. An MDP consists of:

- A **finite set of states (S)** representing all possible situations the agent can be in.
- A **set of actions (A)** the agent can take.
- At each discrete time step $t$, the agent observes the current state $s_t \in S$ and selects an action $a_t \in A$.
- The agent then receives an immediate **reward** $r_t$ and transitions to a new state $s_{t+1}$.

The **Markov assumption** means that the next state and reward depend only on the current state and action, not on the full history. Formally, $s_{t+1} = \delta(s_t, a_t)$ and $r_t = r(s_t, a_t)$, where $\delta$ and $r$ are transition and reward functions, which may be stochastic (random) and unknown to the agent.

The agent’s task is to learn a **policy** $\pi: S \to A$, a mapping from states to actions, that maximizes the **expected return**—the sum of discounted future rewards:


$$
G_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \cdots
$$


Here, $\gamma$ (0 ≤ γ < 1) is the **discount factor** that determines how much future rewards are worth compared to immediate rewards. A smaller $\gamma$ means the agent cares more about immediate rewards, while a $\gamma$ close to 1 means it values long-term rewards.


### 3. 📈 Value Functions and Optimal Policies

To solve the RL problem, the agent needs a way to evaluate how good it is to be in a particular state or to take a particular action in a state. This is where **value functions** come in.

- The **state-value function** $V^\pi(s)$ gives the expected return starting from state $s$ and following policy $\pi$.
- The **optimal value function** $V^*(s)$ gives the maximum expected return achievable from state $s$ by any policy.

If the agent knew $V^*(s)$, it could choose the best action $a$ in state $s$ by looking ahead:


$$
\pi^*(s) = \arg\max_a \left[ r(s, a) + \gamma V^*(\delta(s, a)) \right]
$$


This means the agent picks the action that maximizes the immediate reward plus the discounted value of the next state.

However, this approach requires knowing the transition function $\delta$ and reward function $r$, which are often unknown.


### 4. 🔍 The Q-Function: Learning Without a Model

To overcome the need for knowing $\delta$ and $r$, RL introduces the **Q-function** or **action-value function** $Q(s, a)$. This function estimates the expected return of taking action $a$ in state $s$ and then following the optimal policy thereafter.

The key advantage of learning $Q$ is that the agent can select the best action directly:


$$
\pi^*(s) = \arg\max_a Q(s, a)
$$


This means the agent doesn’t need to know the environment’s dynamics explicitly; it just needs to learn the values of state-action pairs through experience.


### 5. ⚖️ Exploration vs Exploitation: Balancing Learning and Using Knowledge

A fundamental challenge in RL is the **exploration-exploitation trade-off**:

- **Exploitation** means choosing the action that currently seems best based on what the agent has learned so far.
- **Exploration** means trying out less certain or random actions to discover potentially better strategies.

If the agent only exploits, it might miss better actions it hasn’t tried yet. If it only explores, it won’t use its knowledge to maximize rewards.

One common strategy to balance this is the **ε-greedy method**:

- With probability $1 - \epsilon$, the agent chooses the greedy action (the one with the highest estimated value).
- With probability $\epsilon$, the agent chooses a random action to explore.

For example, if $\epsilon = 0.2$, the agent explores 20% of the time and exploits 80% of the time.


### 6. 🔄 Learning and Updating Q-values: The Q-Learning Algorithm

The agent learns the Q-function iteratively by updating its estimates based on experience. The core update rule for Q-learning is:


$$
\hat{Q}(s, a) \leftarrow r + \gamma \max_{a'} \hat{Q}(s', a')
$$


Here:

- $s$ is the current state.
- $a$ is the action taken.
- $r$ is the immediate reward received.
- $s'$ is the next state after taking action $a$.
- $a'$ ranges over possible actions in $s'$.
- $\hat{Q}$ is the agent’s current estimate of the Q-function.

In practice, the agent initializes all Q-values to zero and updates them as it interacts with the environment. Over time, the Q-values converge to the true values, allowing the agent to act optimally.


### 7. 🌐 Handling Stochastic Environments: Non-Deterministic Cases

In many real-world problems, the environment is **non-deterministic**: the same action in the same state can lead to different next states or rewards due to randomness.

Q-learning adapts to this by using a **learning rate** $\alpha$ to update Q-values incrementally:


$$
\hat{Q}_n(s, a) \leftarrow (1 - \alpha_n) \hat{Q}_{n-1}(s, a) + \alpha_n \left[ r + \gamma \max_{a'} \hat{Q}_{n-1}(s', a') \right]
$$


Here, $\alpha_n$ controls how much the new experience influences the Q-value, often decreasing over time as the agent gains more experience. For example, $\alpha_n = \frac{1}{1 + \text{visits}_n(s, a)}$ means the learning rate decreases as the agent visits the state-action pair more often.

This approach ensures that Q-learning converges even in stochastic environments.


### 8. 🧩 Families of Reinforcement Learning Algorithms

There are several broad categories of RL algorithms, each with different assumptions and methods:

1. **Dynamic Programming (DP):**  
   These methods use the Bellman equations to compute value functions exactly, assuming a complete and accurate model of the environment is available. DP is mathematically rigorous but impractical when the environment is unknown or too large.

2. **Monte Carlo Methods:**  
   These learn from complete episodes of experience without requiring a model. They estimate value functions by averaging returns from sampled episodes. Monte Carlo methods are simple but require episodes to terminate.

3. **Temporal Difference (TD) Methods:**  
   These combine ideas from DP and Monte Carlo. TD methods, like Q-learning, learn incrementally from incomplete sequences without needing a model. They update estimates based on observed rewards and current value estimates, making them powerful and widely used in practice.


### Summary

Reinforcement Learning is a powerful framework for teaching agents to make decisions by trial and error, learning from rewards over time. It models problems as Markov Decision Processes, where the agent learns a policy to maximize cumulative rewards. Key concepts include value functions, the Q-function, and the exploration-exploitation trade-off. Q-learning is a foundational algorithm that enables learning optimal policies without knowing the environment’s dynamics, even in stochastic settings. RL algorithms fall into families like Dynamic Programming, Monte Carlo, and Temporal Difference methods, each suited to different scenarios.

This foundational understanding sets the stage for exploring more advanced RL techniques and applications in robotics, autonomous driving, gaming, and beyond.