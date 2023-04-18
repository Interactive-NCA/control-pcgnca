### 🔮 About experiment(s)

---

|                          | Experiment 8                               |
|:-------------------------|:-------------------------------------------|
| experiment_id            | 8                                          |
| description              | Ludek testing whether the diversity works. |
| game                     | zelda                                      |
| model_name               | NCA                                        |
| step_size                | 0.05                                       |
| fix_seeds                | False                                      |
| n_init_states            | 10                                         |
| n_steps                  | 30                                         |
| n_aux_chans              | 8                                          |
| binary_channel           | True                                       |
| fixed_tiles              | True                                       |
| fixed_tiles_difficulty   | easy                                       |
| fixed_tiles_archive_size | 100                                        |
| evolve_strategy          | obj_based_on_swft                          |
| padding_type             | 0                                          |
| overwrite                | True                                       |
| playability_weight       | 1                                          |
| reliability_weight       | 1                                          |
| include_diversity        | True                                       |
| bcs                      | ['symmetry', 'path_length']                |
| bcs_bounds               | [[0, 1], [0, 271]]                         |
| n_models_per_bc          | [100, 100]                                 |
| n_tiles                  | 5                                          |
| grid_dim                 | 16                                         |

### 🔖 Training Process Summary

---

|                          |   Experiment 8 |
|:-------------------------|---------------:|
| N. Solutions             |      74        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       1        |
| Number of generations    |       5        |
| OBJECTIVE Sum (QD score) |     256.791    |
| OBJECTIVE Mean           |       3.47015  |
| OBJECTIVE Std            |       1.34297  |
| OBJECTIVE Min            |       0.246578 |
| OBJECTIVE Max            |       5.58264  |

|           | Experiment 8                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-8/training_summary/objective.png) |

<br/>

|          | Experiment 8                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-8/archive_snaps/timeline.gif) |

<br/>

### 👀 Training differences in Objs and BCs trained and evaluated on seeds with and without fixed seeds

---

👉 **bc0_diff**

|               |   Experiment 8 |
|:--------------|---------------:|
| bc0_diff mean |      0.106391  |
| bc0_diff min  |      0         |
| bc0_diff 25%  |      0.034375  |
| bc0_diff 50%  |      0.0798828 |
| bc0_diff 75%  |      0.154004  |
| bc0_diff max  |      0.426562  |


👉 **bc1_diff**

|               |   Experiment 8 |
|:--------------|---------------:|
| bc1_diff mean |     0.00533333 |
| bc1_diff min  |     0          |
| bc1_diff 25%  |     0          |
| bc1_diff 50%  |     0          |
| bc1_diff 75%  |     0          |
| bc1_diff max  |     2.1        |


👉 **obj_diff**

|               |   Experiment 8 |
|:--------------|---------------:|
| obj_diff mean |       0.844543 |
| obj_diff min  |       0        |
| obj_diff 25%  |       0.26287  |
| obj_diff 50%  |       0.666709 |
| obj_diff 75%  |       1.1324   |
| obj_diff max  |       4.52559  |


### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 8 |
|:-------------------------|---------------:|
| N. Solutions             |       39       |
| N. Solutions Possible    |    10000       |
| Perc. of Archive Filled  |        0       |
| Number of generations    |        5       |
| OBJECTIVE Sum (QD score) |      133.386   |
| OBJECTIVE Mean           |        3.42016 |
| OBJECTIVE Std            |        1.54417 |
| OBJECTIVE Min            |        0.33441 |
| OBJECTIVE Max            |        5.75413 |

|           | Experiment 8                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-8/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 8 |
|:---------------------------|---------------:|
| N. Solutions               |     39         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      0         |
| Number of generations      |      5         |
| PLAYABILITY Sum (QD score) |    -40.8059    |
| PLAYABILITY Mean           |     -1.0463    |
| PLAYABILITY Std            |      0.664739  |
| PLAYABILITY Min            |     -2.40997   |
| PLAYABILITY Max            |     -0.0271654 |

|             | Experiment 8                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-8/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 8 |
|:---------------------------|---------------:|
| N. Solutions               |    39          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     0          |
| Number of generations      |     5          |
| RELIABILITY Sum (QD score) |    -0.80252    |
| RELIABILITY Mean           |    -0.0205774  |
| RELIABILITY Std            |     0.0100102  |
| RELIABILITY Min            |    -0.062133   |
| RELIABILITY Max            |    -0.00546875 |

|             | Experiment 8                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-8/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 8 |
|:-------------------------|---------------:|
| N. Solutions             |      41        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       0        |
| Number of generations    |       5        |
| OBJECTIVE Sum (QD score) |     127.444    |
| OBJECTIVE Mean           |       3.10838  |
| OBJECTIVE Std            |       1.88721  |
| OBJECTIVE Min            |      -0.697146 |
| OBJECTIVE Max            |       5.70268  |

|           | Experiment 8                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-8/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 8 |
|:---------------------------|---------------:|
| N. Solutions               |     41         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      0         |
| Number of generations      |      5         |
| PLAYABILITY Sum (QD score) |    -36.1685    |
| PLAYABILITY Mean           |     -0.882157  |
| PLAYABILITY Std            |      0.703846  |
| PLAYABILITY Min            |     -2.35344   |
| PLAYABILITY Max            |     -0.0295276 |

|             | Experiment 8                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-8/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 8 |
|:---------------------------|---------------:|
| N. Solutions               |    41          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     0          |
| Number of generations      |     5          |
| RELIABILITY Sum (QD score) |    -0.692398   |
| RELIABILITY Mean           |    -0.0168878  |
| RELIABILITY Std            |     0.0135149  |
| RELIABILITY Min            |    -0.079369   |
| RELIABILITY Max            |    -0.00195312 |

|             | Experiment 8                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-8/evaluation_summary/reliability.png) |

<br/>

