### 🔮 About experiment(s)

---

|                          | Experiment 10                                                                        |
|:-------------------------|:-------------------------------------------------------------------------------------|
| experiment_id            | 10                                                                                   |
| description              | Same as baseline except: use of MANUAL fixed tiles, padding type 1 and no diversity. |
| game                     | zelda                                                                                |
| model_name               | NCA                                                                                  |
| step_size                | 0.05                                                                                 |
| n_init_states            | 10                                                                                   |
| n_steps                  | 50                                                                                   |
| n_aux_chans              | 3                                                                                    |
| binary_channel           | True                                                                                 |
| fixed_tiles              | True                                                                                 |
| fixed_tiles_difficulty   | manual                                                                               |
| fixed_tiles_archive_size | 100                                                                                  |
| evolve_strategy          | default                                                                              |
| padding_type             | 1                                                                                    |
| overwrite                | True                                                                                 |
| playability_weight       | 1                                                                                    |
| reliability_weight       | 1                                                                                    |
| include_diversity        | False                                                                                |
| bcs                      | ['symmetry', 'path_length']                                                          |
| bcs_bounds               | [[0, 1], [0, 271]]                                                                   |
| n_models_per_bc          | [100, 100]                                                                           |
| n_tiles                  | 8                                                                                    |
| grid_dim                 | 16                                                                                   |

### 🔖 Training Process Summary

---

|                          |   Experiment 10 |
|:-------------------------|----------------:|
| N. Solutions             |    1010         |
| N. Solutions Possible    |   10000         |
| Perc. of Archive Filled  |      10         |
| Number of generations    |     196         |
| OBJECTIVE Sum (QD score) |   -5922.52      |
| OBJECTIVE Mean           |      -5.86388   |
| OBJECTIVE Std            |       2.15804   |
| OBJECTIVE Min            |     -11.1384    |
| OBJECTIVE Max            |      -0.0298507 |

|           | Experiment 10                                                      |
|:----------|:-------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-10/training_summary/objective.png) |

<br/>

|          | Experiment 10                                                  |
|:---------|:---------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-10/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 10 |
|:-------------------------|----------------:|
| N. Solutions             |      435        |
| N. Solutions Possible    |    10000        |
| Perc. of Archive Filled  |        4        |
| Number of generations    |      196        |
| OBJECTIVE Sum (QD score) |    -3338.91     |
| OBJECTIVE Mean           |       -7.67565  |
| OBJECTIVE Std            |        3.08762  |
| OBJECTIVE Min            |      -11.546    |
| OBJECTIVE Max            |       -0.037329 |

|           | Experiment 10                                                                    |
|:----------|:---------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |     435         |
| N. Solutions Possible      |   10000         |
| Perc. of Archive Filled    |       4         |
| Number of generations      |     196         |
| PLAYABILITY Sum (QD score) |    -127.392     |
| PLAYABILITY Mean           |      -0.292855  |
| PLAYABILITY Std            |       0.189543  |
| PLAYABILITY Min            |      -0.763298  |
| PLAYABILITY Max            |      -0.0102362 |

|             | Experiment 10                                                                      |
|:------------|:-----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |    435          |
| N. Solutions Possible      |  10000          |
| Perc. of Archive Filled    |      4          |
| Number of generations      |    196          |
| RELIABILITY Sum (QD score) |  -3204.66       |
| RELIABILITY Mean           |     -7.36703    |
| RELIABILITY Std            |      3.03339    |
| RELIABILITY Min            |    -11.1014     |
| RELIABILITY Max            |     -0.00429688 |

|             | Experiment 10                                                                      |
|:------------|:-----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 10 |
|:-------------------------|----------------:|
| N. Solutions             |      100        |
| N. Solutions Possible    |    10000        |
| Perc. of Archive Filled  |        1        |
| Number of generations    |      196        |
| OBJECTIVE Sum (QD score) |      -24.844    |
| OBJECTIVE Mean           |       -0.24844  |
| OBJECTIVE Std            |        0.202222 |
| OBJECTIVE Min            |       -0.87649  |
| OBJECTIVE Max            |       -0.026667 |

|           | Experiment 10                                                        |
|:----------|:---------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-10/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |     100         |
| N. Solutions Possible      |   10000         |
| Perc. of Archive Filled    |       1         |
| Number of generations      |     196         |
| PLAYABILITY Sum (QD score) |     -22.826     |
| PLAYABILITY Mean           |      -0.22826   |
| PLAYABILITY Std            |       0.193185  |
| PLAYABILITY Min            |      -0.86811   |
| PLAYABILITY Max            |      -0.0228346 |

|             | Experiment 10                                                          |
|:------------|:-----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-10/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |     100         |
| N. Solutions Possible      |   10000         |
| Perc. of Archive Filled    |       1         |
| Number of generations      |     196         |
| RELIABILITY Sum (QD score) |      -1.14474   |
| RELIABILITY Mean           |      -0.0114474 |
| RELIABILITY Std            |       0.0142396 |
| RELIABILITY Min            |      -0.0816584 |
| RELIABILITY Max            |      -0         |

|             | Experiment 10                                                          |
|:------------|:-----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-10/evaluation_summary/reliability.png) |

<br/>

