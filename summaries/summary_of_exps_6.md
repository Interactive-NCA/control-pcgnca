### 🔮 About experiment(s)

---

|                          | Experiment 6                                                       |
|:-------------------------|:-------------------------------------------------------------------|
| experiment_id            | 6                                                                  |
| description              | Baseline model reproducing Sam's experiment. (including diversity) |
| game                     | zelda                                                              |
| model_name               | NCA                                                                |
| step_size                | 0.05                                                               |
| n_init_states            | 10                                                                 |
| n_steps                  | 50                                                                 |
| n_aux_chans              | 3                                                                  |
| binary_channel           | False                                                              |
| fixed_tiles              | False                                                              |
| fixed_tiles_difficulty   | easy                                                               |
| fixed_tiles_archive_size | 100                                                                |
| evolve_strategy          | default                                                            |
| padding_type             | 0                                                                  |
| overwrite                | True                                                               |
| playability_weight       | 1                                                                  |
| reliability_weight       | 1                                                                  |
| include_diversity        | True                                                               |
| bcs                      | ['symmetry', 'path_length']                                        |
| bcs_bounds               | [[0, 1], [0, 271]]                                                 |
| n_models_per_bc          | [100, 100]                                                         |
| n_tiles                  | 8                                                                  |
| grid_dim                 | 16                                                                 |

### 🔖 Training Process Summary

---

|                          |   Experiment 6 |
|:-------------------------|---------------:|
| N. Solutions             |      81        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       1        |
| Number of generations    |       5        |
| OBJECTIVE Sum (QD score) |     242.203    |
| OBJECTIVE Mean           |       2.99016  |
| OBJECTIVE Std            |       2.25185  |
| OBJECTIVE Min            |      -0.953753 |
| OBJECTIVE Max            |       6.51966  |

|           | Experiment 6                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-6/training_summary/objective.png) |

<br/>

|          | Experiment 6                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-6/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 6 |
|:-------------------------|---------------:|
| N. Solutions             |       53       |
| N. Solutions Possible    |    10000       |
| Perc. of Archive Filled  |        1       |
| Number of generations    |        5       |
| OBJECTIVE Sum (QD score) |      165.765   |
| OBJECTIVE Mean           |        3.12763 |
| OBJECTIVE Std            |        2.20108 |
| OBJECTIVE Min            |       -1.01757 |
| OBJECTIVE Max            |        6.43138 |

|           | Experiment 6                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-6/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |     53         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |      5         |
| PLAYABILITY Sum (QD score) |    -41.2804    |
| PLAYABILITY Mean           |     -0.778876  |
| PLAYABILITY Std            |      0.517766  |
| PLAYABILITY Min            |     -2.6815    |
| PLAYABILITY Max            |     -0.0370079 |

|             | Experiment 6                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-6/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |    53          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     1          |
| Number of generations      |     5          |
| RELIABILITY Sum (QD score) |    -0.983203   |
| RELIABILITY Mean           |    -0.018551   |
| RELIABILITY Std            |     0.0119361  |
| RELIABILITY Min            |    -0.070409   |
| RELIABILITY Max            |    -0.00259111 |

|             | Experiment 6                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-6/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 6 |
|:-------------------------|---------------:|
| N. Solutions             |      52        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       1        |
| Number of generations    |       5        |
| OBJECTIVE Sum (QD score) |     168.767    |
| OBJECTIVE Mean           |       3.24553  |
| OBJECTIVE Std            |       2.10657  |
| OBJECTIVE Min            |      -0.684441 |
| OBJECTIVE Max            |       6.56572  |

|           | Experiment 6                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-6/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |     52         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |      5         |
| PLAYABILITY Sum (QD score) |    -39.4673    |
| PLAYABILITY Mean           |     -0.758987  |
| PLAYABILITY Std            |      0.431572  |
| PLAYABILITY Min            |     -1.64843   |
| PLAYABILITY Max            |     -0.0401575 |

|             | Experiment 6                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-6/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |    52          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     1          |
| Number of generations      |     5          |
| RELIABILITY Sum (QD score) |    -0.955343   |
| RELIABILITY Mean           |    -0.018372   |
| RELIABILITY Std            |     0.0123935  |
| RELIABILITY Min            |    -0.0660145  |
| RELIABILITY Max            |    -0.00292317 |

|             | Experiment 6                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-6/evaluation_summary/reliability.png) |

<br/>

