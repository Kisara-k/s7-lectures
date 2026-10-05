## 14. Introduction to Reinforcement Learning

## Questions

#### 1. What are key characteristics of problems suitable for reinforcement learning?  
A) Rewards are often delayed rather than immediate  
B) The environment is always fully observable  
C) There is an opportunity for active exploration  
D) The agent always has a complete model of the environment  

#### 2. In the Markov Decision Process (MDP) framework, which assumptions hold true?  
A) The next state depends only on the current state and action  
B) Rewards depend on the entire history of states and actions  
C) Transition and reward functions may be stochastic  
D) The agent must know the transition function δ and reward function r  

#### 3. Why is the Q-function preferred over the value function V* when the environment model is unknown?  
A) Q-function allows choosing optimal actions without knowing δ or r  
B) V* requires knowledge of the transition function δ to perform lookahead  
C) Q-function directly estimates the expected return of state-action pairs  
D) V* can be learned without any interaction with the environment  

#### 4. Which of the following statements about ε-greedy exploration are correct?  
A) With probability ε, a random action is selected from all possible actions including the greedy one  
B) The probability of selecting a greedy action is always exactly 1 - ε  
C) Exploration helps prevent the agent from getting stuck in suboptimal policies  
D) ε-greedy methods guarantee convergence to the optimal policy regardless of ε value  

#### 5. Consider the Q-learning update rule for nondeterministic environments:  
Q̂n(s, a) ← (1 - αn) Q̂n-1(s, a) + αn [r + γ maxa' Q̂n-1(s', a')]  
Which of the following are true about the learning rate αn?  
A) αn decreases as the number of visits to (s, a) increases  
B) αn is constant throughout training to ensure stable learning  
C) αn controls how much new experience influences the Q-value update  
D) αn must be zero for convergence of Q-learning  

#### 6. Which of the following are true about the reinforcement learning problem’s goal?  
A) To learn a policy π that maximizes the expected discounted return from any state  
B) To learn a direct mapping from states to rewards without considering actions  
C) The discount factor γ must be strictly greater than 1 for future rewards to be prioritized  
D) The policy π maps states to actions, but no explicit training examples of ⟨s, a⟩ pairs are available  

#### 7. Which statements correctly describe the differences between Dynamic Programming, Monte Carlo, and Temporal Difference methods?  
A) Dynamic Programming requires a complete and accurate model of the environment  
B) Monte Carlo methods learn incrementally from partial experiences without a model  
C) Temporal Difference methods combine ideas from both Monte Carlo and Dynamic Programming  
D) Temporal Difference methods require a model of the environment to update values  

#### 8. In the example of learning to play Backgammon with TD-Gammon, which of the following are true?  
A) The agent was trained by playing millions of games against itself  
B) Immediate rewards were given only at the end of the game (+100 for win, -100 for loss)  
C) The agent used a supervised learning approach with labeled training data  
D) The learned policy reached performance approximately equal to the best human players  

#### 9. Regarding the exploration-exploitation tradeoff, which of the following are correct?  
A) Exploitation involves selecting the action with the highest estimated value most of the time  
B) Exploration involves selecting actions randomly to discover potentially better policies  
C) Pure exploitation without exploration can lead to suboptimal long-term performance  
D) Exploration is unnecessary if the agent has a perfect model of the environment  

#### 10. Which of the following statements about the Markov assumption in reinforcement learning are correct?  
A) The next state and reward depend only on the current state and action, not on past states  
B) The Markov assumption implies the environment is deterministic  
C) The Markov assumption simplifies the learning problem by reducing dependencies  
D) The agent must always know the Markov transition function δ to apply reinforcement learning methods



<br>

## Answers

#### 1. What are key characteristics of problems suitable for reinforcement learning?  
A) ✓ Rewards are often delayed rather than immediate — Delayed rewards are a hallmark of RL problems.  
B) ✗ The environment is always fully observable — RL often deals with partially observable states.  
C) ✓ There is an opportunity for active exploration — Exploration is essential to learn optimal policies.  
D) ✗ The agent always has a complete model of the environment — Often the model is unknown or incomplete.  

**Correct:** A, C


#### 2. In the Markov Decision Process (MDP) framework, which assumptions hold true?  
A) ✓ The next state depends only on the current state and action — This is the Markov assumption.  
B) ✗ Rewards depend on the entire history of states and actions — Rewards depend only on current state and action.  
C) ✓ Transition and reward functions may be stochastic — δ and r can be nondeterministic.  
D) ✗ The agent must know the transition function δ and reward function r — The agent may not know these functions.  

**Correct:** A, C


#### 3. Why is the Q-function preferred over the value function V* when the environment model is unknown?  
A) ✓ Q-function allows choosing optimal actions without knowing δ or r — Q directly estimates state-action values.  
B) ✓ V* requires knowledge of the transition function δ to perform lookahead — V* needs δ for lookahead search.  
C) ✓ Q-function directly estimates the expected return of state-action pairs — This enables action selection without model.  
D) ✗ V* can be learned without any interaction with the environment — V* learning typically requires model or interaction.  

**Correct:** A, B, C


#### 4. Which of the following statements about ε-greedy exploration are correct?  
A) ✓ With probability ε, a random action is selected from all possible actions including the greedy one — Exploration includes all actions equally.  
B) ✗ The probability of selecting a greedy action is always exactly 1 - ε — It can be higher due to random selection sometimes picking greedy action.  
C) ✓ Exploration helps prevent the agent from getting stuck in suboptimal policies — Exploration is critical to avoid local optima.  
D) ✗ ε-greedy methods guarantee convergence to the optimal policy regardless of ε value — Convergence depends on ε decreasing or other conditions.  

**Correct:** A, C


#### 5. Consider the Q-learning update rule for nondeterministic environments:  
Q̂n(s, a) ← (1 - αn) Q̂n-1(s, a) + αn [r + γ maxa' Q̂n-1(s', a')]  
Which of the following are true about the learning rate αn?  
A) ✓ αn decreases as the number of visits to (s, a) increases — αn = 1/(1 + visits) decreases over time.  
B) ✗ αn is constant throughout training to ensure stable learning — Constant α can prevent convergence.  
C) ✓ αn controls how much new experience influences the Q-value update — It weights new vs old information.  
D) ✗ αn must be zero for convergence of Q-learning — αn must be positive but decrease appropriately.  

**Correct:** A, C


#### 6. Which of the following are true about the reinforcement learning problem’s goal?  
A) ✓ To learn a policy π that maximizes the expected discounted return from any state — This is the core RL objective.  
B) ✗ To learn a direct mapping from states to rewards without considering actions — Actions are essential in RL.  
C) ✗ The discount factor γ must be strictly greater than 1 for future rewards to be prioritized — γ is between 0 and 1.  
D) ✓ The policy π maps states to actions, but no explicit training examples of ⟨s, a⟩ pairs are available — Training data is indirect via rewards.  

**Correct:** A, D


#### 7. Which statements correctly describe the differences between Dynamic Programming, Monte Carlo, and Temporal Difference methods?  
A) ✓ Dynamic Programming requires a complete and accurate model of the environment — It uses Bellman equations with known model.  
B) ✗ Monte Carlo methods learn incrementally from partial experiences without a model — Monte Carlo learns from complete episodes, not partial.  
C) ✓ Temporal Difference methods combine ideas from both Monte Carlo and Dynamic Programming — TD uses bootstrapping and sampling.  
D) ✗ Temporal Difference methods require a model of the environment to update values — TD methods are model-free.  

**Correct:** A, C


#### 8. In the example of learning to play Backgammon with TD-Gammon, which of the following are true?  
A) ✓ The agent was trained by playing millions of games against itself — 1.5 million self-play games were used.  
B) ✓ Immediate rewards were given only at the end of the game (+100 for win, -100 for loss) — Rewards were sparse and terminal.  
C) ✗ The agent used a supervised learning approach with labeled training data — It used reinforcement learning, not supervised.  
D) ✓ The learned policy reached performance approximately equal to the best human players — TD-Gammon matched top human skill.  

**Correct:** A, B, D


#### 9. Regarding the exploration-exploitation tradeoff, which of the following are correct?  
A) ✓ Exploitation involves selecting the action with the highest estimated value most of the time — Exploitation is greedy action selection.  
B) ✓ Exploration involves selecting actions randomly to discover potentially better policies — Exploration tries less-known actions.  
C) ✓ Pure exploitation without exploration can lead to suboptimal long-term performance — Without exploration, agent may miss better policies.  
D) ✗ Exploration is unnecessary if the agent has a perfect model of the environment — Even with a model, exploration may be needed to learn.  

**Correct:** A, B, C


#### 10. Which of the following statements about the Markov assumption in reinforcement learning are correct?  
A) ✓ The next state and reward depend only on the current state and action, not on past states — This defines the Markov property.  
B) ✗ The Markov assumption implies the environment is deterministic — It allows stochastic transitions and rewards.  
C) ✓ The Markov assumption simplifies the learning problem by reducing dependencies — It limits dependencies to current state/action.  
D) ✗ The agent must always know the Markov transition function δ to apply reinforcement learning methods — RL can learn without knowing δ.  

**Correct:** A, C