### 🔮 About experiment(s)

---

|                          | Experiment 4                                                                 |
|:-------------------------|:-----------------------------------------------------------------------------|
| experiment_id            | 4                                                                            |
| description              | Automatic easy fixed tiles(10000), 5000 generations, playability weight = 10 |
| game                     | zelda                                                                        |
| model_name               | NCA                                                                          |
| step_size                | 0.05                                                                         |
| fix_seeds                | False                                                                        |
| n_init_states            | 10                                                                           |
| n_steps                  | 50                                                                           |
| n_aux_chans              | 8                                                                            |
| binary_channel           | True                                                                         |
| fixed_tiles              | True                                                                         |
| fixed_tiles_difficulty   | easy                                                                         |
| fixed_tiles_archive_size | 10000                                                                        |
| overwrite                | True                                                                         |
| n_models_per_dim         | 100                                                                          |
| playability_weight       | 10                                                                           |
| reliability_weight       | 1                                                                            |
| bcs                      | ['symmetry', 'path-length']                                                  |
| bcs_bounds               | [[0, 1], [0, 271]]                                                           |
| n_tiles                  | 5                                                                            |
| grid_dim                 | 16                                                                           |

### 🔖 Training Process Summary

---

|                          |   Experiment 4 |
|:-------------------------|---------------:|
| N. Solutions             |   769          |
| N. Solutions Possible    | 10000          |
| Perc. of Archive Filled  |     8          |
| Number of generations    |  5001          |
| OBJECTIVE Sum (QD score) |  -190.818      |
| OBJECTIVE Mean           |    -0.248138   |
| OBJECTIVE Std            |     1.46036    |
| OBJECTIVE Min            |   -11.7081     |
| OBJECTIVE Max            |    -0.00292317 |

|           | Experiment 4                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-4/training_summary/objective.png) |

<br/>

|          | Experiment 4                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-4/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 4 |
|:-------------------------|---------------:|
| N. Solutions             |    50          |
| N. Solutions Possible    | 10000          |
| Perc. of Archive Filled  |     1          |
| Number of generations    |  5001          |
| OBJECTIVE Sum (QD score) |  -293.062      |
| OBJECTIVE Mean           |    -5.86123    |
| OBJECTIVE Std            |     4.15505    |
| OBJECTIVE Min            |   -11.5886     |
| OBJECTIVE Max            |    -0.00721335 |

|           | Experiment 4                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-4/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 4 |
|:---------------------------|---------------:|
| N. Solutions               |     50         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |   5001         |
| PLAYABILITY Sum (QD score) |     -4.17163   |
| PLAYABILITY Mean           |     -0.0834326 |
| PLAYABILITY Std            |      0.137396  |
| PLAYABILITY Min            |     -0.546875  |
| PLAYABILITY Max            |     -0         |

|             | Experiment 4                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-4/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 4 |
|:---------------------------|---------------:|
| N. Solutions               |    50          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     1          |
| Number of generations      |  5001          |
| RELIABILITY Sum (QD score) |  -288.88       |
| RELIABILITY Mean           |    -5.77759    |
| RELIABILITY Std            |     4.10212    |
| RELIABILITY Min            |   -11.5314     |
| RELIABILITY Max            |    -0.00721335 |

|             | Experiment 4                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-4/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 4 |
|:-------------------------|---------------:|
| N. Solutions             |      87        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       1        |
| Number of generations    |    5001        |
| OBJECTIVE Sum (QD score) |   -1868.72     |
| OBJECTIVE Mean           |     -21.4796   |
| OBJECTIVE Std            |      12.0646   |
| OBJECTIVE Min            |     -58.7885   |
| OBJECTIVE Max            |      -0.594956 |

|           | Experiment 4                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-4/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 4 |
|:---------------------------|---------------:|
| N. Solutions               |      87        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       1        |
| Number of generations      |    5001        |
| PLAYABILITY Sum (QD score) |   -1867.02     |
| PLAYABILITY Mean           |     -21.46     |
| PLAYABILITY Std            |      12.054    |
| PLAYABILITY Min            |     -58.7573   |
| PLAYABILITY Max            |      -0.592335 |

|             | Experiment 4                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-4/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 4 |
|:---------------------------|---------------:|
| N. Solutions               |     87         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |   5001         |
| RELIABILITY Sum (QD score) |     -1.22717   |
| RELIABILITY Mean           |     -0.0141054 |
| RELIABILITY Std            |      0.0129133 |
| RELIABILITY Min            |     -0.0711005 |
| RELIABILITY Max            |     -0         |

|             | Experiment 4                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-4/evaluation_summary/reliability.png) |

<br/>

