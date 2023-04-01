### 🔮 About experiment(s)

---

|                          | Experiment 5                                                       |
|:-------------------------|:-------------------------------------------------------------------|
| experiment_id            | 5                                                                  |
| description              | Manual fixed tiles(100), 5000 generations, playability weight = 10 |
| game                     | zelda                                                              |
| model_name               | NCA                                                                |
| step_size                | 0.05                                                               |
| fix_seeds                | False                                                              |
| n_init_states            | 10                                                                 |
| n_steps                  | 50                                                                 |
| n_aux_chans              | 8                                                                  |
| binary_channel           | True                                                               |
| fixed_tiles              | True                                                               |
| fixed_tiles_difficulty   | manual                                                             |
| fixed_tiles_archive_size | 100                                                                |
| overwrite                | True                                                               |
| n_models_per_dim         | 100                                                                |
| playability_weight       | 10                                                                 |
| reliability_weight       | 1                                                                  |
| bcs                      | ['symmetry', 'path-length']                                        |
| bcs_bounds               | [[0, 1], [0, 271]]                                                 |
| n_tiles                  | 5                                                                  |
| grid_dim                 | 16                                                                 |

### 🔖 Training Process Summary

---

|                          |   Experiment 5 |
|:-------------------------|---------------:|
| N. Solutions             |     265        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       3        |
| Number of generations    |    4701        |
| OBJECTIVE Sum (QD score) |    -238.96     |
| OBJECTIVE Mean           |      -0.901735 |
| OBJECTIVE Std            |       2.10692  |
| OBJECTIVE Min            |     -13.3245   |
| OBJECTIVE Max            |      -0.125429 |

|           | Experiment 5                                                      |
|:----------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-5/training_summary/objective.png) |

<br/>

|          | Experiment 5                                                  |
|:---------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-5/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 5 |
|:-------------------------|---------------:|
| N. Solutions             |      43        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       0        |
| Number of generations    |    4701        |
| OBJECTIVE Sum (QD score) |    -162.328    |
| OBJECTIVE Mean           |      -3.77506  |
| OBJECTIVE Std            |       3.10716  |
| OBJECTIVE Min            |     -11.917    |
| OBJECTIVE Max            |      -0.168834 |

|           | Experiment 5                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-5/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 5 |
|:---------------------------|---------------:|
| N. Solutions               |      43        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       0        |
| Number of generations      |    4701        |
| PLAYABILITY Sum (QD score) |     -20.2756   |
| PLAYABILITY Mean           |      -0.471525 |
| PLAYABILITY Std            |       1.77632  |
| PLAYABILITY Min            |     -11.8145   |
| PLAYABILITY Max            |      -0.106299 |

|             | Experiment 5                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-5/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 5 |
|:---------------------------|---------------:|
| N. Solutions               |    43          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     0          |
| Number of generations      |  4701          |
| RELIABILITY Sum (QD score) |  -140.609      |
| RELIABILITY Mean           |    -3.26998    |
| RELIABILITY Std            |     2.96928    |
| RELIABILITY Min            |    -8.51444    |
| RELIABILITY Max            |    -0.00407824 |

|             | Experiment 5                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-5/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 5 |
|:-------------------------|---------------:|
| N. Solutions             |       58       |
| N. Solutions Possible    |    10000       |
| Perc. of Archive Filled  |        1       |
| Number of generations    |     4701       |
| OBJECTIVE Sum (QD score) |     -988.285   |
| OBJECTIVE Mean           |      -17.0394  |
| OBJECTIVE Std            |        9.79371 |
| OBJECTIVE Min            |      -30.1269  |
| OBJECTIVE Max            |       -0.309   |

|           | Experiment 5                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-5/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 5 |
|:---------------------------|---------------:|
| N. Solutions               |      58        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       1        |
| Number of generations      |    4701        |
| PLAYABILITY Sum (QD score) |    -987.511    |
| PLAYABILITY Mean           |     -17.0261   |
| PLAYABILITY Std            |       9.79203  |
| PLAYABILITY Min            |     -30.1181   |
| PLAYABILITY Max            |      -0.307087 |

|             | Experiment 5                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-5/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 5 |
|:---------------------------|---------------:|
| N. Solutions               |    58          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     1          |
| Number of generations      |  4701          |
| RELIABILITY Sum (QD score) |    -0.635025   |
| RELIABILITY Mean           |    -0.0109487  |
| RELIABILITY Std            |     0.00877153 |
| RELIABILITY Min            |    -0.0597363  |
| RELIABILITY Max            |    -0          |

|             | Experiment 5                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-5/evaluation_summary/reliability.png) |

<br/>

