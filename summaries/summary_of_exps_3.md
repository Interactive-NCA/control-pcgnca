### 🔮 About experiment(s)

---

|                          | Experiment 3                        |
|:-------------------------|:------------------------------------|
| experiment_id            | 3                                   |
| description              | Test of new bc - number of enemies. |
| game                     | zelda                               |
| model_name               | NCA                                 |
| step_size                | 0.05                                |
| fix_seeds                | False                               |
| n_init_states            | 10                                  |
| n_steps                  | 30                                  |
| n_aux_chans              | 8                                   |
| binary_channel           | True                                |
| fixed_tiles              | True                                |
| fixed_tiles_difficulty   | easy                                |
| fixed_tiles_archive_size | 100                                 |
| evolve_strategy          | obj_based_on_swft                   |
| overwrite                | True                                |
| playability_weight       | 1                                   |
| reliability_weight       | 1                                   |
| bcs                      | ['n_enemies', 'path_length']        |
| bcs_bounds               | [[0, 3], [0, 271]]                  |
| n_models_per_bc          | [4, 100]                            |
| n_tiles                  | 5                                   |
| grid_dim                 | 16                                  |

### 🔖 Training Process Summary

---

|                          |   Experiment 3 |
|:-------------------------|---------------:|
| N. Solutions             |      1         |
| N. Solutions Possible    |    400         |
| Perc. of Archive Filled  |      0         |
| Number of generations    |      5         |
| OBJECTIVE Sum (QD score) |     -0.0200787 |
| OBJECTIVE Mean           |     -0.0200787 |
| OBJECTIVE Std            |    nan         |
| OBJECTIVE Min            |     -0.0200787 |
| OBJECTIVE Max            |     -0.0200787 |

|           | Experiment 3                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-3/training_summary/objective.png) |

<br/>

|          | Experiment 3                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-3/archive_snaps/timeline.gif) |

<br/>

### 👀 Training differences in Objs and BCs trained and evaluated on seeds with and without fixed seeds

---

👉 **bc0_diff**

|               |   Experiment 3 |
|:--------------|---------------:|
| bc0_diff mean |              0 |
| bc0_diff min  |              0 |
| bc0_diff 25%  |              0 |
| bc0_diff 50%  |              0 |
| bc0_diff 75%  |              0 |
| bc0_diff max  |              0 |


👉 **bc1_diff**

|               |   Experiment 3 |
|:--------------|---------------:|
| bc1_diff mean |              0 |
| bc1_diff min  |              0 |
| bc1_diff 25%  |              0 |
| bc1_diff 50%  |              0 |
| bc1_diff 75%  |              0 |
| bc1_diff max  |              0 |


👉 **obj_diff**

|               |   Experiment 3 |
|:--------------|---------------:|
| obj_diff mean |     1.01153    |
| obj_diff min  |     0.00399852 |
| obj_diff 25%  |     0.217913   |
| obj_diff 50%  |     0.711171   |
| obj_diff 75%  |     1.87677    |
| obj_diff max  |     2.80431    |


### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 3 |
|:-------------------------|---------------:|
| N. Solutions             |       1        |
| N. Solutions Possible    |     400        |
| Perc. of Archive Filled  |       0        |
| Number of generations    |       5        |
| OBJECTIVE Sum (QD score) |      -0.039247 |
| OBJECTIVE Mean           |      -0.039247 |
| OBJECTIVE Std            |     nan        |
| OBJECTIVE Min            |      -0.039247 |
| OBJECTIVE Max            |      -0.039247 |

|           | Experiment 3                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-3/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |       1        |
| N. Solutions Possible      |     400        |
| Perc. of Archive Filled    |       0        |
| Number of generations      |       5        |
| PLAYABILITY Sum (QD score) |      -0.039247 |
| PLAYABILITY Mean           |      -0.039247 |
| PLAYABILITY Std            |     nan        |
| PLAYABILITY Min            |      -0.039247 |
| PLAYABILITY Max            |      -0.039247 |

|             | Experiment 3                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-3/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |              1 |
| N. Solutions Possible      |            400 |
| Perc. of Archive Filled    |              0 |
| Number of generations      |              5 |
| RELIABILITY Sum (QD score) |              0 |
| RELIABILITY Mean           |              0 |
| RELIABILITY Std            |            nan |
| RELIABILITY Min            |             -0 |
| RELIABILITY Max            |             -0 |

|             | Experiment 3                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-3/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 3 |
|:-------------------------|---------------:|
| N. Solutions             |        1       |
| N. Solutions Possible    |      400       |
| Perc. of Archive Filled  |        0       |
| Number of generations    |        5       |
| OBJECTIVE Sum (QD score) |       -1.89448 |
| OBJECTIVE Mean           |       -1.89448 |
| OBJECTIVE Std            |      nan       |
| OBJECTIVE Min            |       -1.89448 |
| OBJECTIVE Max            |       -1.89448 |

|           | Experiment 3                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-3/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |        1       |
| N. Solutions Possible      |      400       |
| Perc. of Archive Filled    |        0       |
| Number of generations      |        5       |
| PLAYABILITY Sum (QD score) |       -1.89448 |
| PLAYABILITY Mean           |       -1.89448 |
| PLAYABILITY Std            |      nan       |
| PLAYABILITY Min            |       -1.89448 |
| PLAYABILITY Max            |       -1.89448 |

|             | Experiment 3                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-3/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |              1 |
| N. Solutions Possible      |            400 |
| Perc. of Archive Filled    |              0 |
| Number of generations      |              5 |
| RELIABILITY Sum (QD score) |              0 |
| RELIABILITY Mean           |              0 |
| RELIABILITY Std            |            nan |
| RELIABILITY Min            |             -0 |
| RELIABILITY Max            |             -0 |

|             | Experiment 3                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-3/evaluation_summary/reliability.png) |

<br/>

