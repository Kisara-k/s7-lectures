## 14. Introduction to Reinforcement Learning

## Questions

#### 1. What are key characteristics of problems suitable for reinforcement learning?  
A) The agent always has a complete model of the environment  
B) Rewards are often delayed rather than immediate  
C) There is an opportunity for active exploration  
D) The environment is always fully observable  

#### 2. In the Markov Decision Process (MDP) framework, which assumptions hold true?  
A) Transition and reward functions may be stochastic  
B) The next state depends only on the current state and action  
C) Rewards depend on the entire history of states and actions  
D) The agent must know the transition function δ and reward function r  

#### 3. Why is the Q-function preferred over the value function V* when the environment model is unknown?  
A) Q-function allows choosing optimal actions without knowing δ or r  
B) Q-function directly estimates the expected return of state-action pairs  
C) V* requires knowledge of the transition function δ to perform lookahead  
D) V* can be learned without any interaction with the environment  

#### 4. Which of the following statements about ε-greedy exploration are correct?  
A) ε-greedy methods guarantee convergence to the optimal policy regardless of ε value  
B) Exploration helps prevent the agent from getting stuck in suboptimal policies  
C) The probability of selecting a greedy action is always exactly 1 - ε  
D) With probability ε, a random action is selected from all possible actions including the greedy one  

#### 5. For the Q-learning update Q̂n(s, a) ← (1 - αn) Q̂n-1(s, a) + αn [r + γ maxa' Q̂n-1(s', a')], which statements about the learning rate αn are true?  
A) αn decreases as the number of visits to (s, a) increases  
B) αn must be zero for convergence of Q-learning  
C) αn is constant throughout training to ensure stable learning  
D) αn controls how much new experience influences the Q-value update  

#### 6. Which of the following are true about the reinforcement learning problem’s goal?  
A) To learn a policy π that maximizes the expected discounted return from any state  
B) The policy π maps states to actions, but no explicit training examples of ⟨s, a⟩ pairs are available  
C) To learn a direct mapping from states to rewards without considering actions  
D) The discount factor γ must be strictly greater than 1 for future rewards to be prioritized  

#### 7. Which statements correctly describe the differences between Dynamic Programming, Monte Carlo, and Temporal Difference methods?  
A) Dynamic Programming requires a complete and accurate model of the environment  
B) Monte Carlo methods learn incrementally from partial experiences without a model  
C) Temporal Difference methods combine ideas from both Monte Carlo and Dynamic Programming  
D) Temporal Difference methods require a model of the environment to update values  

#### 8. In the example of learning to play Backgammon with TD-Gammon, which of the following are true?  
A) Immediate rewards were given only at the end of the game (+100 for win, -100 for loss)  
B) The agent used a supervised learning approach with labeled training data  
C) The agent was trained by playing millions of games against itself  
D) The learned policy reached performance approximately equal to the best human players  

#### 9. Regarding the exploration-exploitation tradeoff, which of the following are correct?  
A) Exploration involves selecting actions randomly to discover potentially better policies  
B) Exploitation involves selecting the action with the highest estimated value most of the time  
C) Pure exploitation without exploration can lead to suboptimal long-term performance  
D) Exploration is unnecessary if the agent has a perfect model of the environment  

#### 10. Which of the following statements about the Markov assumption in reinforcement learning are correct?  
A) The Markov assumption simplifies the learning problem by reducing dependencies  
B) The agent must always know the Markov transition function δ to apply reinforcement learning methods  
C) The next state and reward depend only on the current state and action, not on past states  
D) The Markov assumption implies the environment is deterministic  



<br>

## Answers

#### 1. What are key characteristics of problems suitable for reinforcement learning?  
A) ✗ The agent always has a complete model of the environment — Often the model is unknown or incomplete.  
B) ✓ Rewards are often delayed rather than immediate — Delayed rewards are a hallmark of RL problems.  
C) ✓ There is an opportunity for active exploration — Exploration is essential to learn optimal policies.  
D) ✗ The environment is always fully observable — RL often deals with partially observable states.  

**Correct:** B, C


#### 2. In the Markov Decision Process (MDP) framework, which assumptions hold true?  
A) ✓ Transition and reward functions may be stochastic — δ and r can be nondeterministic.  
B) ✓ The next state depends only on the current state and action — This is the Markov assumption.  
C) ✗ Rewards depend on the entire history of states and actions — Rewards depend only on current state and action.  
D) ✗ The agent must know the transition function δ and reward function r — The agent may not know these functions.  

**Correct:** A, B


#### 3. Why is the Q-function preferred over the value function V* when the environment model is unknown?  
A) ✓ Q-function allows choosing optimal actions without knowing δ or r — Q directly estimates state-action values.  
B) ✓ Q-function directly estimates the expected return of state-action pairs — This enables action selection without model.  
C) ✓ V* requires knowledge of the transition function δ to perform lookahead — V* needs δ for lookahead search.  
D) ✗ V* can be learned without any interaction with the environment — V* learning typically requires model or interaction.  

**Correct:** A, B, C


#### 4. Which of the following statements about ε-greedy exploration are correct?  
A) ✗ ε-greedy methods guarantee convergence to the optimal policy regardless of ε value — Convergence depends on ε decreasing or other conditions.  
B) ✓ Exploration helps prevent the agent from getting stuck in suboptimal policies — Exploration is critical to avoid local optima.  
C) ✗ The probability of selecting a greedy action is always exactly 1 - ε — It can be higher due to random selection sometimes picking greedy action.  
D) ✓ With probability ε, a random action is selected from all possible actions including the greedy one — Exploration includes all actions equally.  

**Correct:** B, D


#### 5. For the Q-learning update Q̂n(s, a) ← (1 - αn) Q̂n-1(s, a) + αn [r + γ maxa' Q̂n-1(s', a')], which statements about the learning rate αn are true?  
A) ✓ αn decreases as the number of visits to (s, a) increases — αn = 1/(1 + visits) decreases over time.  
B) ✗ αn must be zero for convergence of Q-learning — αn must be positive but decrease appropriately.  
C) ✗ αn is constant throughout training to ensure stable learning — Constant α can prevent convergence.  
D) ✓ αn controls how much new experience influences the Q-value update — It weights new vs old information.  

**Correct:** A, D


#### 6. Which of the following are true about the reinforcement learning problem’s goal?  
A) ✓ To learn a policy π that maximizes the expected discounted return from any state — This is the core RL objective.  
B) ✓ The policy π maps states to actions, but no explicit training examples of ⟨s, a⟩ pairs are available — Training data is indirect via rewards.  
C) ✗ To learn a direct mapping from states to rewards without considering actions — Actions are essential in RL.  
D) ✗ The discount factor γ must be strictly greater than 1 for future rewards to be prioritized — γ is between 0 and 1.  

**Correct:** A, B


#### 7. Which statements correctly describe the differences between Dynamic Programming, Monte Carlo, and Temporal Difference methods?  
A) ✓ Dynamic Programming requires a complete and accurate model of the environment — It uses Bellman equations with known model.  
B) ✗ Monte Carlo methods learn incrementally from partial experiences without a model — Monte Carlo learns from complete episodes, not partial.  
C) ✓ Temporal Difference methods combine ideas from both Monte Carlo and Dynamic Programming — TD uses bootstrapping and sampling.  
D) ✗ Temporal Difference methods require a model of the environment to update values — TD methods are model-free.  

**Correct:** A, C


#### 8. In the example of learning to play Backgammon with TD-Gammon, which of the following are true?  
A) ✓ Immediate rewards were given only at the end of the game (+100 for win, -100 for loss) — Rewards were sparse and terminal.  
B) ✗ The agent used a supervised learning approach with labeled training data — It used reinforcement learning, not supervised.  
C) ✓ The agent was trained by playing millions of games against itself — 1.5 million self-play games were used.  
D) ✓ The learned policy reached performance approximately equal to the best human players — TD-Gammon matched top human skill.  

**Correct:** A, C, D


#### 9. Regarding the exploration-exploitation tradeoff, which of the following are correct?  
A) ✓ Exploration involves selecting actions randomly to discover potentially better policies — Exploration tries less-known actions.  
B) ✓ Exploitation involves selecting the action with the highest estimated value most of the time — Exploitation is greedy action selection.  
C) ✓ Pure exploitation without exploration can lead to suboptimal long-term performance — Without exploration, agent may miss better policies.  
D) ✗ Exploration is unnecessary if the agent has a perfect model of the environment — Even with a model, exploration may be needed to learn.  

**Correct:** A, B, C


#### 10. Which of the following statements about the Markov assumption in reinforcement learning are correct?  
A) ✓ The Markov assumption simplifies the learning problem by reducing dependencies — It limits dependencies to current state/action.  
B) ✗ The agent must always know the Markov transition function δ to apply reinforcement learning methods — RL can learn without knowing δ.  
C) ✓ The next state and reward depend only on the current state and action, not on past states — This defines the Markov property.  
D) ✗ The Markov assumption implies the environment is deterministic — It allows stochastic transitions and rewards.  

**Correct:** A, C
