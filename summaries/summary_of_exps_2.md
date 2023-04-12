### 🔮 About experiment(s)

---

|                          | Experiment 2                                                        |
|:-------------------------|:--------------------------------------------------------------------|
| experiment_id            | 2                                                                   |
| description              | This is one tests whether we can load manually created fixed tiles. |
| game                     | zelda                                                               |
| model_name               | NCA                                                                 |
| step_size                | 0.05                                                                |
| fix_seeds                | False                                                               |
| n_init_states            | 10                                                                  |
| n_steps                  | 30                                                                  |
| n_aux_chans              | 8                                                                   |
| binary_channel           | True                                                                |
| fixed_tiles              | True                                                                |
| fixed_tiles_difficulty   | manual                                                              |
| fixed_tiles_archive_size | 100                                                                 |
| overwrite                | True                                                                |
| n_models_per_dim         | 100                                                                 |
| playability_weight       | 1                                                                   |
| reliability_weight       | 1                                                                   |
| bcs                      | ['symmetry', 'path-length']                                         |
| bcs_bounds               | [[0, 1], [0, 271]]                                                  |
| n_tiles                  | 5                                                                   |
| grid_dim                 | 16                                                                  |

### 🔖 Training Process Summary

---

|                          |   Experiment 2 |
|:-------------------------|---------------:|
| N. Solutions             |     75         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      1         |
| Number of generations    |     16         |
| OBJECTIVE Sum (QD score) |    -11.1835    |
| OBJECTIVE Mean           |     -0.149114  |
| OBJECTIVE Std            |      0.259704  |
| OBJECTIVE Min            |     -1.47361   |
| OBJECTIVE Max            |     -0.0382159 |

|           | Experiment 2                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-2/training_summary/objective.png) |

<br/>

|          | Experiment 2                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-2/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 2 |
|:-------------------------|---------------:|
| N. Solutions             |     15         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      0         |
| Number of generations    |     16         |
| OBJECTIVE Sum (QD score) |    -13.4832    |
| OBJECTIVE Mean           |     -0.89888   |
| OBJECTIVE Std            |      1.71618   |
| OBJECTIVE Min            |     -6.90923   |
| OBJECTIVE Max            |     -0.0427899 |

|           | Experiment 2                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-2/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 2 |
|:---------------------------|---------------:|
| N. Solutions               |      15        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       0        |
| Number of generations      |      16        |
| PLAYABILITY Sum (QD score) |      -6.37049  |
| PLAYABILITY Mean           |      -0.424699 |
| PLAYABILITY Std            |       0.438058 |
| PLAYABILITY Min            |      -1.36454  |
| PLAYABILITY Max            |      -0.011811 |

|             | Experiment 2                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-2/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 2 |
|:---------------------------|---------------:|
| N. Solutions               |    15          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     0          |
| Number of generations      |    16          |
| RELIABILITY Sum (QD score) |    -7.09795    |
| RELIABILITY Mean           |    -0.473197   |
| RELIABILITY Std            |     1.77722    |
| RELIABILITY Min            |    -6.89742    |
| RELIABILITY Max            |    -0.00191366 |

|             | Experiment 2                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-2/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 2 |
|:-------------------------|---------------:|
| N. Solutions             |      43        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       0        |
| Number of generations    |      16        |
| OBJECTIVE Sum (QD score) |     -61.5838   |
| OBJECTIVE Mean           |      -1.43218  |
| OBJECTIVE Std            |       0.926552 |
| OBJECTIVE Min            |      -3.01719  |
| OBJECTIVE Max            |      -0.025975 |

|           | Experiment 2                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-2/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 2 |
|:---------------------------|---------------:|
| N. Solutions               |     43         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      0         |
| Number of generations      |     16         |
| PLAYABILITY Sum (QD score) |    -60.7691    |
| PLAYABILITY Mean           |     -1.41323   |
| PLAYABILITY Std            |      0.923939  |
| PLAYABILITY Min            |     -3         |
| PLAYABILITY Max            |     -0.0248031 |

|             | Experiment 2                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-2/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 2 |
|:---------------------------|---------------:|
| N. Solutions               |     43         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      0         |
| Number of generations      |     16         |
| RELIABILITY Sum (QD score) |     -0.718884  |
| RELIABILITY Mean           |     -0.0167182 |
| RELIABILITY Std            |      0.0140657 |
| RELIABILITY Min            |     -0.0592979 |
| RELIABILITY Max            |     -0         |

|             | Experiment 2                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-2/evaluation_summary/reliability.png) |

<br/>

