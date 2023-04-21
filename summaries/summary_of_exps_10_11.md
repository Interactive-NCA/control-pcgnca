### 🔮 About experiment(s)

---

|                          | Experiment 10                                                                        | Experiment 11                                       |
|:-------------------------|:-------------------------------------------------------------------------------------|:----------------------------------------------------|
| experiment_id            | 10                                                                                   | 11                                                  |
| description              | Same as baseline except: use of MANUAL fixed tiles, padding type 1 and no diversity. | Same as baseline except we are not using diversity. |
| game                     | zelda                                                                                | zelda                                               |
| model_name               | NCA                                                                                  | NCA                                                 |
| step_size                | 0.05                                                                                 | 0.05                                                |
| n_init_states            | 10                                                                                   | 10                                                  |
| n_steps                  | 50                                                                                   | 50                                                  |
| n_aux_chans              | 3                                                                                    | 3                                                   |
| binary_channel           | True                                                                                 | False                                               |
| fixed_tiles              | True                                                                                 | False                                               |
| fixed_tiles_difficulty   | manual                                                                               | manual                                              |
| fixed_tiles_archive_size | 100                                                                                  | 100                                                 |
| evolve_strategy          | default                                                                              | default                                             |
| padding_type             | 1                                                                                    | 0                                                   |
| overwrite                | True                                                                                 | True                                                |
| playability_weight       | 1                                                                                    | 1                                                   |
| reliability_weight       | 1                                                                                    | 1                                                   |
| include_diversity        | False                                                                                | False                                               |
| bcs                      | ['symmetry', 'path_length']                                                          | ['symmetry', 'path_length']                         |
| bcs_bounds               | [[0, 1], [0, 271]]                                                                   | [[0, 1], [0, 271]]                                  |
| n_models_per_bc          | [100, 100]                                                                           | [100, 100]                                          |
| n_tiles                  | 8                                                                                    | 8                                                   |
| grid_dim                 | 16                                                                                   | 16                                                  |

### 🔖 Training Process Summary

---

|                          |   Experiment 10 |   Experiment 11 |
|:-------------------------|----------------:|----------------:|
| N. Solutions             |    1010         |      142        |
| N. Solutions Possible    |   10000         |    10000        |
| Perc. of Archive Filled  |      10         |        1        |
| Number of generations    |     196         |      196        |
| OBJECTIVE Sum (QD score) |   -5922.52      |     -244.685    |
| OBJECTIVE Mean           |      -5.86388   |       -1.72314  |
| OBJECTIVE Std            |       2.15804   |        2.58474  |
| OBJECTIVE Min            |     -11.1384    |       -8.75687  |
| OBJECTIVE Max            |      -0.0298507 |       -0.019685 |

|           | Experiment 10                                                      | Experiment 11                                                      |
|:----------|:-------------------------------------------------------------------|:-------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-10/training_summary/objective.png) | ![](../experiments/ExperimentId-11/training_summary/objective.png) |

<br/>

|          | Experiment 10                                                  | Experiment 11                                                  |
|:---------|:---------------------------------------------------------------|:---------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-10/archive_snaps/timeline.gif) | ![](../experiments/ExperimentId-11/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 10 |   Experiment 11 |
|:-------------------------|----------------:|----------------:|
| N. Solutions             |      435        |       82        |
| N. Solutions Possible    |    10000        |    10000        |
| Perc. of Archive Filled  |        4        |        1        |
| Number of generations    |      196        |      196        |
| OBJECTIVE Sum (QD score) |    -3338.91     |      -28.076    |
| OBJECTIVE Mean           |       -7.67565  |       -0.34239  |
| OBJECTIVE Std            |        3.08762  |        1.06077  |
| OBJECTIVE Min            |      -11.546    |       -6.34927  |
| OBJECTIVE Max            |       -0.037329 |       -0.019685 |

|           | Experiment 10                                                                    | Experiment 11                                                                    |
|:----------|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/objective.png) | ![](../experiments/ExperimentId-11/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 10 |   Experiment 11 |
|:---------------------------|----------------:|----------------:|
| N. Solutions               |     435         |      82         |
| N. Solutions Possible      |   10000         |   10000         |
| Perc. of Archive Filled    |       4         |       1         |
| Number of generations      |     196         |     196         |
| PLAYABILITY Sum (QD score) |    -127.392     |     -10.355     |
| PLAYABILITY Mean           |      -0.292855  |      -0.12628   |
| PLAYABILITY Std            |       0.189543  |       0.141325  |
| PLAYABILITY Min            |      -0.763298  |      -0.938289  |
| PLAYABILITY Max            |      -0.0102362 |      -0.0129921 |

|             | Experiment 10                                                                      | Experiment 11                                                                      |
|:------------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/playability.png) | ![](../experiments/ExperimentId-11/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 10 |   Experiment 11 |
|:---------------------------|----------------:|----------------:|
| N. Solutions               |    435          |       82        |
| N. Solutions Possible      |  10000          |    10000        |
| Perc. of Archive Filled    |      4          |        1        |
| Number of generations      |    196          |      196        |
| RELIABILITY Sum (QD score) |  -3204.66       |      -17.4838   |
| RELIABILITY Mean           |     -7.36703    |       -0.213217 |
| RELIABILITY Std            |      3.03339    |        1.0722   |
| RELIABILITY Min            |    -11.1014     |       -6.32919  |
| RELIABILITY Max            |     -0.00429688 |       -0        |

|             | Experiment 10                                                                      | Experiment 11                                                                      |
|:------------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-11/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 10 |   Experiment 11 |
|:-------------------------|----------------:|----------------:|
| N. Solutions             |      100        |       85        |
| N. Solutions Possible    |    10000        |    10000        |
| Perc. of Archive Filled  |        1        |        1        |
| Number of generations    |      196        |      196        |
| OBJECTIVE Sum (QD score) |      -24.844    |      -44.1547   |
| OBJECTIVE Mean           |       -0.24844  |       -0.519468 |
| OBJECTIVE Std            |        0.202222 |        1.45655  |
| OBJECTIVE Min            |       -0.87649  |       -6.68631  |
| OBJECTIVE Max            |       -0.026667 |       -0.019685 |

|           | Experiment 10                                                        | Experiment 11                                                        |
|:----------|:---------------------------------------------------------------------|:---------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-10/evaluation_summary/objective.png) | ![](../experiments/ExperimentId-11/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 10 |   Experiment 11 |
|:---------------------------|----------------:|----------------:|
| N. Solutions               |     100         |      85         |
| N. Solutions Possible      |   10000         |   10000         |
| Perc. of Archive Filled    |       1         |       1         |
| Number of generations      |     196         |     196         |
| PLAYABILITY Sum (QD score) |     -22.826     |     -11.1456    |
| PLAYABILITY Mean           |      -0.22826   |      -0.131125  |
| PLAYABILITY Std            |       0.193185  |       0.147225  |
| PLAYABILITY Min            |      -0.86811   |      -0.620604  |
| PLAYABILITY Max            |      -0.0228346 |      -0.0125984 |

|             | Experiment 10                                                          | Experiment 11                                                          |
|:------------|:-----------------------------------------------------------------------|:-----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-10/evaluation_summary/playability.png) | ![](../experiments/ExperimentId-11/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 10 |   Experiment 11 |
|:---------------------------|----------------:|----------------:|
| N. Solutions               |     100         |       85        |
| N. Solutions Possible      |   10000         |    10000        |
| Perc. of Archive Filled    |       1         |        1        |
| Number of generations      |     196         |      196        |
| RELIABILITY Sum (QD score) |      -1.14474   |      -32.7256   |
| RELIABILITY Mean           |      -0.0114474 |       -0.385007 |
| RELIABILITY Std            |       0.0142396 |        1.42435  |
| RELIABILITY Min            |      -0.0816584 |       -6.30716  |
| RELIABILITY Max            |      -0         |       -0        |

|             | Experiment 10                                                          | Experiment 11                                                          |
|:------------|:-----------------------------------------------------------------------|:-----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-10/evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-11/evaluation_summary/reliability.png) |

<br/>

