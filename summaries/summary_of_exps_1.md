### 🔮 About experiment(s)

---

|                          | Experiment 1                                |
|:-------------------------|:--------------------------------------------|
| experiment_id            | 1                                           |
| description              | This is a test experiment, nothing special. |
| game                     | zelda                                       |
| model_name               | NCA                                         |
| step_size                | 0.05                                        |
| fix_seeds                | False                                       |
| n_init_states            | 10                                          |
| n_steps                  | 30                                          |
| n_aux_chans              | 8                                           |
| binary_channel           | True                                        |
| fixed_tiles              | True                                        |
| fixed_tiles_difficulty   | easy                                        |
| fixed_tiles_archive_size | 1000                                        |
| overwrite                | True                                        |
| n_models_per_dim         | 100                                         |
| playability_weight       | 1                                           |
| reliability_weight       | 1                                           |
| bcs                      | ['symmetry', 'path-length']                 |
| bcs_bounds               | [[0, 1], [0, 271]]                          |
| n_tiles                  | 5                                           |
| grid_dim                 | 16                                          |

### 🔖 Training Process Summary

---

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |     79         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      1         |
| Number of generations    |     26         |
| OBJECTIVE Sum (QD score) |     -5.44681   |
| OBJECTIVE Mean           |     -0.068947  |
| OBJECTIVE Std            |      0.223749  |
| OBJECTIVE Min            |     -2.01949   |
| OBJECTIVE Max            |     -0.0254606 |

|           | Experiment 1                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/training_summary/objective.png) |

<br/>

|          | Experiment 1                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-1/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |     12         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      0         |
| Number of generations    |     26         |
| OBJECTIVE Sum (QD score) |     -2.94066   |
| OBJECTIVE Mean           |     -0.245055  |
| OBJECTIVE Std            |      0.568398  |
| OBJECTIVE Min            |     -2.04084   |
| OBJECTIVE Max            |     -0.0306722 |

|           | Experiment 1                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |     12         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      0         |
| Number of generations      |     26         |
| PLAYABILITY Sum (QD score) |     -2.72141   |
| PLAYABILITY Mean           |     -0.226784  |
| PLAYABILITY Std            |      0.568607  |
| PLAYABILITY Min            |     -2.0243    |
| PLAYABILITY Max            |     -0.0141732 |

|             | Experiment 1                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |    12          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     0          |
| Number of generations      |    26          |
| RELIABILITY Sum (QD score) |    -0.21666    |
| RELIABILITY Mean           |    -0.018055   |
| RELIABILITY Std            |     0.0056342  |
| RELIABILITY Min            |    -0.0244539  |
| RELIABILITY Max            |    -0.00390625 |

|             | Experiment 1                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |      33        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       0        |
| Number of generations    |      26        |
| OBJECTIVE Sum (QD score) |     -89.4145   |
| OBJECTIVE Mean           |      -2.70953  |
| OBJECTIVE Std            |       0.538216 |
| OBJECTIVE Min            |      -3.18764  |
| OBJECTIVE Max            |      -0.550844 |

|           | Experiment 1                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |      33        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       0        |
| Number of generations      |      26        |
| PLAYABILITY Sum (QD score) |     -88.7062   |
| PLAYABILITY Mean           |      -2.68807  |
| PLAYABILITY Std            |       0.535436 |
| PLAYABILITY Min            |      -3.16802  |
| PLAYABILITY Max            |      -0.543307 |

|             | Experiment 1                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |     33         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      0         |
| Number of generations      |     26         |
| RELIABILITY Sum (QD score) |     -0.697741  |
| RELIABILITY Mean           |     -0.0211437 |
| RELIABILITY Std            |      0.0186271 |
| RELIABILITY Min            |     -0.0645466 |
| RELIABILITY Max            |     -0         |

|             | Experiment 1                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/evaluation_summary/reliability.png) |

<br/>

