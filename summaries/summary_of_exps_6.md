### 🔮 About experiment(s)

---

|                          | Experiment 6                                          |
|:-------------------------|:------------------------------------------------------|
| experiment_id            | 6                                                     |
| description              | Easy 10000, saving seeds, 5000 generations, padding 1 |
| game                     | zelda                                                 |
| model_name               | NCA                                                   |
| step_size                | 0.05                                                  |
| fix_seeds                | False                                                 |
| n_init_states            | 10                                                    |
| n_steps                  | 50                                                    |
| n_aux_chans              | 8                                                     |
| binary_channel           | True                                                  |
| fixed_tiles              | True                                                  |
| fixed_tiles_difficulty   | easy                                                  |
| fixed_tiles_archive_size | 10000                                                 |
| evolve_strategy          | obj_based_on_swft                                     |
| padding_type             | 1                                                     |
| overwrite                | True                                                  |
| playability_weight       | 1                                                     |
| reliability_weight       | 1                                                     |
| bcs                      | ['symmetry', 'path_length']                           |
| bcs_bounds               | [[0, 1], [0, 271]]                                    |
| n_models_per_bc          | [100, 100]                                            |
| n_tiles                  | 5                                                     |
| grid_dim                 | 16                                                    |

### 🔖 Training Process Summary

---

|                          |   Experiment 6 |
|:-------------------------|---------------:|
| N. Solutions             |     189        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       2        |
| Number of generations    |    4901        |
| OBJECTIVE Sum (QD score) |     -19.4353   |
| OBJECTIVE Mean           |      -0.102832 |
| OBJECTIVE Std            |       0.887768 |
| OBJECTIVE Min            |     -12.0871   |
| OBJECTIVE Max            |      -0        |

|           | Experiment 6                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-6/training_summary/objective.png) |

<br/>

|          | Experiment 6                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-6/archive_snaps/timeline.gif) |

<br/>

### 👀 Training differences in Objs and BCs trained and evaluated on seeds with and without fixed seeds

---

👉 **bc0_diff**

|               |   Experiment 6 |
|:--------------|---------------:|
| bc0_diff mean |      0.23128   |
| bc0_diff min  |      0         |
| bc0_diff 25%  |      0.0503906 |
| bc0_diff 50%  |      0.177148  |
| bc0_diff 75%  |      0.39668   |
| bc0_diff max  |      0.735156  |


👉 **bc1_diff**

|               |   Experiment 6 |
|:--------------|---------------:|
| bc1_diff mean |      0.0427867 |
| bc1_diff min  |      0         |
| bc1_diff 25%  |      0         |
| bc1_diff 50%  |      0         |
| bc1_diff 75%  |      0         |
| bc1_diff max  |     16         |


👉 **obj_diff**

|               |   Experiment 6 |
|:--------------|---------------:|
| obj_diff mean |    0.81396     |
| obj_diff min  |    9.22736e-06 |
| obj_diff 25%  |    0.174719    |
| obj_diff 50%  |    0.744117    |
| obj_diff 75%  |    1.33932     |
| obj_diff max  |    8.53772     |


### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 6 |
|:-------------------------|---------------:|
| N. Solutions             |      27        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       0        |
| Number of generations    |    4901        |
| OBJECTIVE Sum (QD score) |     -21.9811   |
| OBJECTIVE Mean           |      -0.814114 |
| OBJECTIVE Std            |       2.52849  |
| OBJECTIVE Min            |     -11.9961   |
| OBJECTIVE Max            |      -0        |

|           | Experiment 6                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-6/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |      27        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       0        |
| Number of generations      |    4901        |
| PLAYABILITY Sum (QD score) |      -3.64182  |
| PLAYABILITY Mean           |      -0.134882 |
| PLAYABILITY Std            |       0.34834  |
| PLAYABILITY Min            |      -1.74385  |
| PLAYABILITY Max            |      -0        |

|             | Experiment 6                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-6/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |      27        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       0        |
| Number of generations      |    4901        |
| RELIABILITY Sum (QD score) |     -18.3151   |
| RELIABILITY Mean           |      -0.678335 |
| RELIABILITY Std            |       2.53746  |
| RELIABILITY Min            |     -11.9855   |
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
| N. Solutions             |     73         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      1         |
| Number of generations    |   4901         |
| OBJECTIVE Sum (QD score) |    -66.8419    |
| OBJECTIVE Mean           |     -0.915643  |
| OBJECTIVE Std            |      1.4328    |
| OBJECTIVE Min            |     -8.27947   |
| OBJECTIVE Max            |     -0.0260926 |

|           | Experiment 6                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-6/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |     73         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |   4901         |
| PLAYABILITY Sum (QD score) |    -43.6916    |
| PLAYABILITY Mean           |     -0.598515  |
| PLAYABILITY Std            |      0.738817  |
| PLAYABILITY Min            |     -2.11753   |
| PLAYABILITY Max            |     -0.0224409 |

|             | Experiment 6                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-6/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 6 |
|:---------------------------|---------------:|
| N. Solutions               |    73          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     1          |
| Number of generations      |  4901          |
| RELIABILITY Sum (QD score) |   -22.079      |
| RELIABILITY Mean           |    -0.302452   |
| RELIABILITY Std            |     1.3621     |
| RELIABILITY Min            |    -8.25585    |
| RELIABILITY Max            |    -0.00191366 |

|             | Experiment 6                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-6/evaluation_summary/reliability.png) |

<br/>

