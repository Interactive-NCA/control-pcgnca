### 🔮 About experiment(s)

---

|                          | Experiment 3                                        |
|:-------------------------|:----------------------------------------------------|
| experiment_id            | 3                                                   |
| description              | Automatic easy fixed tiles(10000), 5000 generations |
| game                     | zelda                                               |
| model_name               | NCA                                                 |
| step_size                | 0.05                                                |
| fix_seeds                | False                                               |
| n_init_states            | 10                                                  |
| n_steps                  | 50                                                  |
| n_aux_chans              | 8                                                   |
| binary_channel           | True                                                |
| fixed_tiles              | True                                                |
| fixed_tiles_difficulty   | easy                                                |
| fixed_tiles_archive_size | 10000                                               |
| overwrite                | True                                                |
| n_models_per_dim         | 100                                                 |
| playability_weight       | 1                                                   |
| reliability_weight       | 1                                                   |
| bcs                      | ['symmetry', 'path-length']                         |
| bcs_bounds               | [[0, 1], [0, 271]]                                  |
| n_tiles                  | 5                                                   |
| grid_dim                 | 16                                                  |

### 🔖 Training Process Summary

---

|                          |   Experiment 3 |
|:-------------------------|---------------:|
| N. Solutions             |     806        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       8        |
| Number of generations    |    4601        |
| OBJECTIVE Sum (QD score) |    -107.958    |
| OBJECTIVE Mean           |      -0.133943 |
| OBJECTIVE Std            |       0.976564 |
| OBJECTIVE Min            |     -11.2487   |
| OBJECTIVE Max            |      -0        |

|           | Experiment 3                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-3/training_summary/objective.png) |

<br/>

|          | Experiment 3                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-3/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 3 |
|:-------------------------|---------------:|
| N. Solutions             |      103       |
| N. Solutions Possible    |    10000       |
| Perc. of Archive Filled  |        1       |
| Number of generations    |     4601       |
| OBJECTIVE Sum (QD score) |     -322.457   |
| OBJECTIVE Mean           |       -3.13065 |
| OBJECTIVE Std            |        3.88317 |
| OBJECTIVE Min            |      -11.4723  |
| OBJECTIVE Max            |       -0       |

|           | Experiment 3                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-3/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |    103         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |   4601         |
| PLAYABILITY Sum (QD score) |     -3.1411    |
| PLAYABILITY Mean           |     -0.0304961 |
| PLAYABILITY Std            |      0.0609924 |
| PLAYABILITY Min            |     -0.397804  |
| PLAYABILITY Max            |     -0         |

|             | Experiment 3                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-3/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |      103       |
| N. Solutions Possible      |    10000       |
| Perc. of Archive Filled    |        1       |
| Number of generations      |     4601       |
| RELIABILITY Sum (QD score) |     -319.266   |
| RELIABILITY Mean           |       -3.09967 |
| RELIABILITY Std            |        3.89938 |
| RELIABILITY Min            |      -11.4257  |
| RELIABILITY Max            |       -0       |

|             | Experiment 3                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-3/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 3 |
|:-------------------------|---------------:|
| N. Solutions             |     83         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      1         |
| Number of generations    |   4601         |
| OBJECTIVE Sum (QD score) |    -47.3078    |
| OBJECTIVE Mean           |     -0.569973  |
| OBJECTIVE Std            |      1.02172   |
| OBJECTIVE Min            |     -6.50681   |
| OBJECTIVE Max            |     -0.0292398 |

|           | Experiment 3                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-3/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |     83         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |   4601         |
| PLAYABILITY Sum (QD score) |    -33.9422    |
| PLAYABILITY Mean           |     -0.408942  |
| PLAYABILITY Std            |      0.536326  |
| PLAYABILITY Min            |     -3.01299   |
| PLAYABILITY Max            |     -0.0248031 |

|             | Experiment 3                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-3/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |      83        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       1        |
| Number of generations      |    4601        |
| RELIABILITY Sum (QD score) |     -12.8963   |
| RELIABILITY Mean           |      -0.155377 |
| RELIABILITY Std            |       0.928223 |
| RELIABILITY Min            |      -6.45648  |
| RELIABILITY Max            |      -0        |

|             | Experiment 3                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-3/evaluation_summary/reliability.png) |

<br/>

