## 14. Introduction to Reinforcement Learning

## Key Points

#### 1. 🎯 Reinforcement Learning Problem  
- The goal is to learn a policy $\pi: S \to A$ that maximizes the expected discounted return $G_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \cdots$, where $0 \leq \gamma < 1$ is the discount factor.  
- The environment is modeled as a Markov Decision Process (MDP) with states $S$, actions $A$, transition function $\delta$, and reward function $r$.  
- The Markov assumption states that the next state $s_{t+1}$ and reward $r_t$ depend only on the current state $s_t$ and action $a_t$.

#### 2. 📈 Value Functions and Policies  
- The state-value function $V^\pi(s)$ gives the expected return starting from state $s$ following policy $\pi$.  
- The optimal value function $V^*(s)$ gives the maximum expected return achievable from state $s$.  
- The optimal policy can be derived as $\pi^*(s) = \arg\max_a [r(s,a) + \gamma V^*(\delta(s,a))]$ if $\delta$ and $r$ are known.

#### 3. 🔍 Q-Function  
- The Q-function $Q(s,a)$ estimates the expected return of taking action $a$ in state $s$ and then following the optimal policy.  
- The optimal policy can be chosen as $\pi^*(s) = \arg\max_a Q(s,a)$ without knowing $\delta$ or $r$.  
- Learning $Q$ allows model-free decision making.

#### 4. ⚖️ Exploration vs Exploitation  
- Exploitation means choosing the action with the highest estimated value.  
- Exploration means choosing random actions to discover better strategies.  
- The ε-greedy method selects the greedy action with probability $1 - \epsilon$ and a random action with probability $\epsilon$.

#### 5. 🔄 Q-Learning Update Rule  
- The Q-learning update rule is:  

$$
  \hat{Q}(s,a) \leftarrow r + \gamma \max_{a'} \hat{Q}(s', a')
$$
  
- $s'$ is the next state after taking action $a$ in state $s$, and $r$ is the immediate reward.  
- Q-values are initialized to zero and updated iteratively as the agent interacts with the environment.

#### 6. 🌐 Non-Deterministic Environments  
- In stochastic environments, Q-learning uses a learning rate $\alpha_n$ to update Q-values incrementally:  

$$
  \hat{Q}_n(s,a) \leftarrow (1 - \alpha_n) \hat{Q}_{n-1}(s,a) + \alpha_n [r + \gamma \max_{a'} \hat{Q}_{n-1}(s', a')]
$$
  
- $\alpha_n$ often decreases with the number of visits to $(s,a)$, e.g., $\alpha_n = \frac{1}{1 + \text{visits}_n(s,a)}$.  
- This ensures convergence of Q-learning in stochastic settings.

#### 7. 🧩 Families of RL Algorithms  
- **Dynamic Programming:** Requires a complete and accurate model of the environment; based on Bellman equations.  
- **Monte Carlo Methods:** Learn from complete episodes without needing a model; require episodes to terminate.  
- **Temporal Difference Methods (e.g., Q-learning):** Model-free, incremental learning methods that do not require episodes to end; more complex to analyze but widely used.



<br>

