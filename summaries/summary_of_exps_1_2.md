### 🔮 About experiment(s)

---

|                          | Experiment 1                                | Experiment 2                                                        |
|:-------------------------|:--------------------------------------------|:--------------------------------------------------------------------|
| experiment_id            | 1                                           | 2                                                                   |
| description              | This is a test experiment, nothing special. | This is one tests whether we can load manually created fixed tiles. |
| game                     | zelda                                       | zelda                                                               |
| model_name               | NCA                                         | NCA                                                                 |
| step_size                | 0.05                                        | 0.05                                                                |
| fix_seeds                | False                                       | False                                                               |
| n_init_states            | 10                                          | 10                                                                  |
| n_steps                  | 30                                          | 30                                                                  |
| n_aux_chans              | 8                                           | 8                                                                   |
| binary_channel           | True                                        | True                                                                |
| fixed_tiles              | True                                        | True                                                                |
| fixed_tiles_difficulty   | easy                                        | manual                                                              |
| fixed_tiles_archive_size | 1000                                        | 100                                                                 |
| overwrite                | True                                        | True                                                                |
| n_models_per_dim         | 100                                         | 100                                                                 |
| playability_weight       | 1                                           | 1                                                                   |
| reliability_weight       | 1                                           | 1                                                                   |
| bcs                      | ['symmetry', 'path-length']                 | ['symmetry', 'path-length']                                         |
| bcs_bounds               | [[0, 1], [0, 271]]                          | [[0, 1], [0, 271]]                                                  |
| n_tiles                  | 5                                           | 5                                                                   |
| grid_dim                 | 16                                          | 16                                                                  |

### 🔖 Training Process Summary

---

|                          |   Experiment 1 |   Experiment 2 |
|:-------------------------|---------------:|---------------:|
| N. Solutions             |     79         |     75         |
| N. Solutions Possible    |  10000         |  10000         |
| Perc. of Archive Filled  |      1         |      1         |
| Number of generations    |     26         |     16         |
| OBJECTIVE Sum (QD score) |     -5.44681   |    -11.1835    |
| OBJECTIVE Mean           |     -0.068947  |     -0.149114  |
| OBJECTIVE Std            |      0.223749  |      0.259704  |
| OBJECTIVE Min            |     -2.01949   |     -1.47361   |
| OBJECTIVE Max            |     -0.0254606 |     -0.0382159 |

|           | Experiment 1                                                      | Experiment 2                                                      |
|:----------|:------------------------------------------------------------------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/training_summary/objective.png) | ![](../experiments/ExperimentId-2/training_summary/objective.png) |

<br/>

|          | Experiment 1                                                  | Experiment 2                                                  |
|:---------|:--------------------------------------------------------------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-1/archive_snaps/timeline.gif) | ![](../experiments/ExperimentId-2/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |   Experiment 2 |
|:-------------------------|---------------:|---------------:|
| N. Solutions             |     12         |     15         |
| N. Solutions Possible    |  10000         |  10000         |
| Perc. of Archive Filled  |      0         |      0         |
| Number of generations    |     26         |     16         |
| OBJECTIVE Sum (QD score) |     -2.94066   |    -13.4832    |
| OBJECTIVE Mean           |     -0.245055  |     -0.89888   |
| OBJECTIVE Std            |      0.568398  |      1.71618   |
| OBJECTIVE Min            |     -2.04084   |     -6.90923   |
| OBJECTIVE Max            |     -0.0306722 |     -0.0427899 |

|           | Experiment 1                                                                    | Experiment 2                                                                    |
|:----------|:--------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/objective.png) | ![](../experiments/ExperimentId-2/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |     12         |      15        |
| N. Solutions Possible      |  10000         |   10000        |
| Perc. of Archive Filled    |      0         |       0        |
| Number of generations      |     26         |      16        |
| PLAYABILITY Sum (QD score) |     -2.72141   |      -6.37049  |
| PLAYABILITY Mean           |     -0.226784  |      -0.424699 |
| PLAYABILITY Std            |      0.568607  |       0.438058 |
| PLAYABILITY Min            |     -2.0243    |      -1.36454  |
| PLAYABILITY Max            |     -0.0141732 |      -0.011811 |

|             | Experiment 1                                                                      | Experiment 2                                                                      |
|:------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/playability.png) | ![](../experiments/ExperimentId-2/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |    12          |    15          |
| N. Solutions Possible      | 10000          | 10000          |
| Perc. of Archive Filled    |     0          |     0          |
| Number of generations      |    26          |    16          |
| RELIABILITY Sum (QD score) |    -0.21666    |    -7.09795    |
| RELIABILITY Mean           |    -0.018055   |    -0.473197   |
| RELIABILITY Std            |     0.0056342  |     1.77722    |
| RELIABILITY Min            |    -0.0244539  |    -6.89742    |
| RELIABILITY Max            |    -0.00390625 |    -0.00191366 |

|             | Experiment 1                                                                      | Experiment 2                                                                      |
|:------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-2/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |   Experiment 2 |
|:-------------------------|---------------:|---------------:|
| N. Solutions             |      33        |      43        |
| N. Solutions Possible    |   10000        |   10000        |
| Perc. of Archive Filled  |       0        |       0        |
| Number of generations    |      26        |      16        |
| OBJECTIVE Sum (QD score) |     -89.4145   |     -61.5838   |
| OBJECTIVE Mean           |      -2.70953  |      -1.43218  |
| OBJECTIVE Std            |       0.538216 |       0.926552 |
| OBJECTIVE Min            |      -3.18764  |      -3.01719  |
| OBJECTIVE Max            |      -0.550844 |      -0.025975 |

|           | Experiment 1                                                        | Experiment 2                                                        |
|:----------|:--------------------------------------------------------------------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/evaluation_summary/objective.png) | ![](../experiments/ExperimentId-2/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |      33        |     43         |
| N. Solutions Possible      |   10000        |  10000         |
| Perc. of Archive Filled    |       0        |      0         |
| Number of generations      |      26        |     16         |
| PLAYABILITY Sum (QD score) |     -88.7062   |    -60.7691    |
| PLAYABILITY Mean           |      -2.68807  |     -1.41323   |
| PLAYABILITY Std            |       0.535436 |      0.923939  |
| PLAYABILITY Min            |      -3.16802  |     -3         |
| PLAYABILITY Max            |      -0.543307 |     -0.0248031 |

|             | Experiment 1                                                          | Experiment 2                                                          |
|:------------|:----------------------------------------------------------------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/evaluation_summary/playability.png) | ![](../experiments/ExperimentId-2/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |     33         |     43         |
| N. Solutions Possible      |  10000         |  10000         |
| Perc. of Archive Filled    |      0         |      0         |
| Number of generations      |     26         |     16         |
| RELIABILITY Sum (QD score) |     -0.697741  |     -0.718884  |
| RELIABILITY Mean           |     -0.0211437 |     -0.0167182 |
| RELIABILITY Std            |      0.0186271 |      0.0140657 |
| RELIABILITY Min            |     -0.0645466 |     -0.0592979 |
| RELIABILITY Max            |     -0         |     -0         |

|             | Experiment 1                                                          | Experiment 2                                                          |
|:------------|:----------------------------------------------------------------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-2/evaluation_summary/reliability.png) |

<br/>

