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
| N. Solutions             |     103        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       1        |
| Number of generations    |      46        |
| OBJECTIVE Sum (QD score) |     593.538    |
| OBJECTIVE Mean           |       5.76251  |
| OBJECTIVE Std            |       1.25939  |
| OBJECTIVE Min            |      -0.303325 |
| OBJECTIVE Max            |       7.3622   |

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
| N. Solutions             |      71        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       1        |
| Number of generations    |      46        |
| OBJECTIVE Sum (QD score) |     392.233    |
| OBJECTIVE Mean           |       5.52441  |
| OBJECTIVE Std            |       1.25267  |
| OBJECTIVE Min            |       0.794739 |
| OBJECTIVE Max            |       7.37434  |

|           | Experiment 6                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-6/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |     71         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |     46         |
| PLAYABILITY Sum (QD score) |    -41.8126    |
| PLAYABILITY Mean           |     -0.58891   |
| PLAYABILITY Std            |      0.199201  |
| PLAYABILITY Min            |     -1.07717   |
| PLAYABILITY Max            |     -0.0826772 |

|             | Experiment 6                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-6/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |      71        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       1        |
| Number of generations      |      46        |
| RELIABILITY Sum (QD score) |     -10.3677   |
| RELIABILITY Mean           |      -0.146025 |
| RELIABILITY Std            |       0.693825 |
| RELIABILITY Min            |      -5.74654  |
| RELIABILITY Max            |      -0        |

|             | Experiment 6                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-6/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 6 |
|:-------------------------|---------------:|
| N. Solutions             |       68       |
| N. Solutions Possible    |    10000       |
| Perc. of Archive Filled  |        1       |
| Number of generations    |       46       |
| OBJECTIVE Sum (QD score) |      395.54    |
| OBJECTIVE Mean           |        5.81677 |
| OBJECTIVE Std            |        1.00886 |
| OBJECTIVE Min            |        2.98212 |
| OBJECTIVE Max            |        7.33799 |

|           | Experiment 6                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-6/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |      68        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       1        |
| Number of generations      |      46        |
| PLAYABILITY Sum (QD score) |     -40.737    |
| PLAYABILITY Mean           |      -0.599073 |
| PLAYABILITY Std            |       0.232073 |
| PLAYABILITY Min            |      -1.39909  |
| PLAYABILITY Max            |      -0.243788 |

|             | Experiment 6                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-6/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |     68         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |     46         |
| RELIABILITY Sum (QD score) |     -2.54617   |
| RELIABILITY Mean           |     -0.0374437 |
| RELIABILITY Std            |      0.0222722 |
| RELIABILITY Min            |     -0.101168  |
| RELIABILITY Max            |     -0         |

|             | Experiment 6                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-6/evaluation_summary/reliability.png) |

<br/>

