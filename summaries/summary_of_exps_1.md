### 🔮 About experiment(s)

---

|                          | Experiment 1                    |
|:-------------------------|:--------------------------------|
| experiment_id            | 1                               |
| description              | Test for shape of in and output |
| game                     | zelda                           |
| model_name               | NCA                             |
| step_size                | 0.05                            |
| fix_seeds                | False                           |
| n_init_states            | 10                              |
| n_steps                  | 30                              |
| n_aux_chans              | 8                               |
| binary_channel           | True                            |
| fixed_tiles              | True                            |
| fixed_tiles_difficulty   | manual                          |
| fixed_tiles_archive_size | 100                             |
| overwrite                | True                            |
| n_models_per_dim         | 100                             |
| playability_weight       | 1                               |
| reliability_weight       | 1                               |
| bcs                      | ['symmetry', 'path-length']     |
| bcs_bounds               | [[0, 1], [0, 271]]              |
| n_tiles                  | 5                               |
| grid_dim                 | 16                              |

### 🔖 Training Process Summary

---

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |     80         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      1         |
| Number of generations    |     12         |
| OBJECTIVE Sum (QD score) |    -24.174     |
| OBJECTIVE Mean           |     -0.302175  |
| OBJECTIVE Std            |      1.10696   |
| OBJECTIVE Min            |     -7.50384   |
| OBJECTIVE Max            |     -0.0274528 |

|           | Experiment 1                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/training_summary/objective.png) |

<br/>

|          | Experiment 1                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-1/archive_snaps/timeline.gif) |

<br/>

### 👀 Training differences in Objs and BCs trained and evaluated on seeds with and without fixed seeds

---

👉 **bc0_diff**

|               |   Experiment 1 |
|:--------------|---------------:|
| bc0_diff mean |      0.170649  |
| bc0_diff min  |      0         |
| bc0_diff 25%  |      0.0535156 |
| bc0_diff 50%  |      0.117578  |
| bc0_diff 75%  |      0.272852  |
| bc0_diff max  |      0.626953  |


👉 **bc1_diff**

|               |   Experiment 1 |
|:--------------|---------------:|
| bc1_diff mean |        3.99343 |
| bc1_diff min  |        0       |
| bc1_diff 25%  |        0       |
| bc1_diff 50%  |        0       |
| bc1_diff 75%  |        5.6     |
| bc1_diff max  |       25.7     |


👉 **obj_diff**

|               |   Experiment 1 |
|:--------------|---------------:|
| obj_diff mean |     2.42144    |
| obj_diff min  |     0.00140965 |
| obj_diff 25%  |     0.230569   |
| obj_diff 50%  |     0.814547   |
| obj_diff 75%  |     5.29012    |
| obj_diff max  |     9.31454    |


### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |     35         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      0         |
| Number of generations    |     12         |
| OBJECTIVE Sum (QD score) |    -69.2232    |
| OBJECTIVE Mean           |     -1.97781   |
| OBJECTIVE Std            |      3.2332    |
| OBJECTIVE Min            |    -10.4632    |
| OBJECTIVE Max            |     -0.0273854 |

|           | Experiment 1                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |    35          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     0          |
| Number of generations      |    12          |
| PLAYABILITY Sum (QD score) |    -4.37415    |
| PLAYABILITY Mean           |    -0.124976   |
| PLAYABILITY Std            |     0.259651   |
| PLAYABILITY Min            |    -1.43831    |
| PLAYABILITY Max            |    -0.00708661 |

|             | Experiment 1                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |    35          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     0          |
| Number of generations      |    12          |
| RELIABILITY Sum (QD score) |   -64.7698     |
| RELIABILITY Mean           |    -1.85057    |
| RELIABILITY Std            |     3.28135    |
| RELIABILITY Min            |   -10.3822     |
| RELIABILITY Max            |    -0.00358014 |

|             | Experiment 1                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |     53         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      1         |
| Number of generations    |     12         |
| OBJECTIVE Sum (QD score) |    -34.9231    |
| OBJECTIVE Mean           |     -0.658927  |
| OBJECTIVE Std            |      0.782526  |
| OBJECTIVE Min            |     -4.38379   |
| OBJECTIVE Max            |     -0.0332452 |

|           | Experiment 1                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |     53         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |     12         |
| PLAYABILITY Sum (QD score) |    -29.7148    |
| PLAYABILITY Mean           |     -0.560656  |
| PLAYABILITY Std            |      0.588373  |
| PLAYABILITY Min            |     -2.14843   |
| PLAYABILITY Max            |     -0.0248031 |

|             | Experiment 1                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |    53          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     1          |
| Number of generations      |    12          |
| RELIABILITY Sum (QD score) |    -5.08923    |
| RELIABILITY Mean           |    -0.0960232  |
| RELIABILITY Std            |     0.596845   |
| RELIABILITY Min            |    -4.35898    |
| RELIABILITY Max            |    -0.00117188 |

|             | Experiment 1                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/evaluation_summary/reliability.png) |

<br/>

