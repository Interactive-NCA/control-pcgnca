### 🔮 About experiment(s)

---

|                          | Experiment 2                              |
|:-------------------------|:------------------------------------------|
| experiment_id            | 2                                         |
| description              | Baseline, no fixed tiles 5000 generations |
| game                     | zelda                                     |
| model_name               | NCA                                       |
| step_size                | 0.05                                      |
| fix_seeds                | False                                     |
| n_init_states            | 10                                        |
| n_steps                  | 50                                        |
| n_aux_chans              | 8                                         |
| binary_channel           | False                                     |
| fixed_tiles              | False                                     |
| fixed_tiles_difficulty   | easy                                      |
| fixed_tiles_archive_size | 100                                       |
| evolve_strategy          | default                                   |
| overwrite                | False                                     |
| playability_weight       | 1                                         |
| reliability_weight       | 1                                         |
| bcs                      | ['symmetry', 'path_length']               |
| bcs_bounds               | [[0, 1], [0, 271]]                        |
| n_models_per_bc          | [100, 100]                                |
| n_tiles                  | 5                                         |
| grid_dim                 | 16                                        |

### 🔖 Training Process Summary

---

|                          |   Experiment 2 |
|:-------------------------|---------------:|
| N. Solutions             |     2433       |
| N. Solutions Possible    |    10000       |
| Perc. of Archive Filled  |       24       |
| Number of generations    |     5001       |
| OBJECTIVE Sum (QD score) |    -8866.07    |
| OBJECTIVE Mean           |       -3.64409 |
| OBJECTIVE Std            |        4.77793 |
| OBJECTIVE Min            |      -27.6485  |
| OBJECTIVE Max            |       -0       |

|           | Experiment 2                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-2/training_summary/objective.png) |

<br/>

|          | Experiment 2                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-2/archive_snaps/timeline.gif) |

<br/>

### 👀 Training differences in Objs and BCs trained and evaluated on seeds with and without fixed seeds

---

👉 **bc0_diff**

|               |   Experiment 2 |
|:--------------|---------------:|
| bc0_diff mean |       0.134312 |
| bc0_diff min  |       0        |
| bc0_diff 25%  |       0.053125 |
| bc0_diff 50%  |       0.112109 |
| bc0_diff 75%  |       0.195801 |
| bc0_diff max  |       0.476562 |


👉 **bc1_diff**

|               |   Experiment 2 |
|:--------------|---------------:|
| bc1_diff mean |     0.00626667 |
| bc1_diff min  |     0          |
| bc1_diff 25%  |     0          |
| bc1_diff 50%  |     0          |
| bc1_diff 75%  |     0          |
| bc1_diff max  |     2.6        |


👉 **obj_diff**

|               |   Experiment 2 |
|:--------------|---------------:|
| obj_diff mean |    0.392259    |
| obj_diff min  |    0.000318046 |
| obj_diff 25%  |    0.159453    |
| obj_diff 50%  |    0.254487    |
| obj_diff 75%  |    0.55098     |
| obj_diff max  |    3.90978     |


### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 2 |
|:-------------------------|---------------:|
| N. Solutions             |     1511       |
| N. Solutions Possible    |    10000       |
| Perc. of Archive Filled  |       15       |
| Number of generations    |     5001       |
| OBJECTIVE Sum (QD score) |    -6736.1     |
| OBJECTIVE Mean           |       -4.45804 |
| OBJECTIVE Std            |        5.56771 |
| OBJECTIVE Min            |      -28.25    |
| OBJECTIVE Max            |       -0       |

|           | Experiment 2                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-2/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 2 |
|:---------------------------|---------------:|
| N. Solutions               |  1511          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |    15          |
| Number of generations      |  5001          |
| PLAYABILITY Sum (QD score) |   -14.0363     |
| PLAYABILITY Mean           |    -0.00928944 |
| PLAYABILITY Std            |     0.0559176  |
| PLAYABILITY Min            |    -0.752633   |
| PLAYABILITY Max            |    -0          |

|             | Experiment 2                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-2/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 2 |
|:---------------------------|---------------:|
| N. Solutions               |     1511       |
| N. Solutions Possible      |    10000       |
| Perc. of Archive Filled    |       15       |
| Number of generations      |     5001       |
| RELIABILITY Sum (QD score) |    -6721.18    |
| RELIABILITY Mean           |       -4.44817 |
| RELIABILITY Std            |        5.56698 |
| RELIABILITY Min            |      -28.202   |
| RELIABILITY Max            |       -0       |

|             | Experiment 2                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-2/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 2 |
|:-------------------------|---------------:|
| N. Solutions             |     1520       |
| N. Solutions Possible    |    10000       |
| Perc. of Archive Filled  |       15       |
| Number of generations    |     5001       |
| OBJECTIVE Sum (QD score) |    -6947.1     |
| OBJECTIVE Mean           |       -4.57046 |
| OBJECTIVE Std            |        5.62018 |
| OBJECTIVE Min            |      -29.6146  |
| OBJECTIVE Max            |       -0       |

|           | Experiment 2                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-2/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 2 |
|:---------------------------|---------------:|
| N. Solutions               |  1520          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |    15          |
| Number of generations      |  5001          |
| PLAYABILITY Sum (QD score) |   -14.6301     |
| PLAYABILITY Mean           |    -0.00962508 |
| PLAYABILITY Std            |     0.0573548  |
| PLAYABILITY Min            |    -0.761626   |
| PLAYABILITY Max            |    -0          |

|             | Experiment 2                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-2/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 2 |
|:---------------------------|---------------:|
| N. Solutions               |     1520       |
| N. Solutions Possible      |    10000       |
| Perc. of Archive Filled    |       15       |
| Number of generations      |     5001       |
| RELIABILITY Sum (QD score) |    -6932.11    |
| RELIABILITY Mean           |       -4.5606  |
| RELIABILITY Std            |        5.61983 |
| RELIABILITY Min            |      -29.6059  |
| RELIABILITY Max            |       -0       |

|             | Experiment 2                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-2/evaluation_summary/reliability.png) |

<br/>

