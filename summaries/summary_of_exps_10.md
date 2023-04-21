### 🔮 About experiment(s)

---

|                          | Experiment 10                                       |
|:-------------------------|:----------------------------------------------------|
| experiment_id            | 10                                                  |
| description              | Same as baseline except we are not using diversity. |
| game                     | zelda                                               |
| model_name               | NCA                                                 |
| step_size                | 0.05                                                |
| n_init_states            | 10                                                  |
| n_steps                  | 50                                                  |
| n_aux_chans              | 3                                                   |
| binary_channel           | True                                                |
| fixed_tiles              | True                                                |
| fixed_tiles_difficulty   | manual                                              |
| fixed_tiles_archive_size | 100                                                 |
| evolve_strategy          | default                                             |
| padding_type             | 1                                                   |
| overwrite                | True                                                |
| playability_weight       | 1                                                   |
| reliability_weight       | 1                                                   |
| include_diversity        | False                                               |
| bcs                      | ['symmetry', 'path_length']                         |
| bcs_bounds               | [[0, 1], [0, 271]]                                  |
| n_models_per_bc          | [100, 100]                                          |
| n_tiles                  | 8                                                   |
| grid_dim                 | 16                                                  |

### 🔖 Training Process Summary

---

|                          |   Experiment 10 |
|:-------------------------|----------------:|
| N. Solutions             |     682         |
| N. Solutions Possible    |   10000         |
| Perc. of Archive Filled  |       7         |
| Number of generations    |      46         |
| OBJECTIVE Sum (QD score) |   -4085.22      |
| OBJECTIVE Mean           |      -5.99006   |
| OBJECTIVE Std            |       2.31798   |
| OBJECTIVE Min            |     -11.1384    |
| OBJECTIVE Max            |      -0.0395273 |

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
| N. Solutions             |     226         |
| N. Solutions Possible    |   10000         |
| Perc. of Archive Filled  |       2         |
| Number of generations    |      46         |
| OBJECTIVE Sum (QD score) |   -1111.53      |
| OBJECTIVE Mean           |      -4.91828   |
| OBJECTIVE Std            |       2.73158   |
| OBJECTIVE Min            |     -11.552     |
| OBJECTIVE Max            |      -0.0488227 |

|           | Experiment 10                                                                    |
|:----------|:---------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |     226         |
| N. Solutions Possible      |   10000         |
| Perc. of Archive Filled    |       2         |
| Number of generations      |      46         |
| PLAYABILITY Sum (QD score) |     -54.7146    |
| PLAYABILITY Mean           |      -0.2421    |
| PLAYABILITY Std            |       0.202633  |
| PLAYABILITY Min            |      -1.16135   |
| PLAYABILITY Max            |      -0.0141732 |

|             | Experiment 10                                                                      |
|:------------|:-----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |    226          |
| N. Solutions Possible      |  10000          |
| Perc. of Archive Filled    |      2          |
| Number of generations      |     46          |
| RELIABILITY Sum (QD score) |  -1053.01       |
| RELIABILITY Mean           |     -4.65934    |
| RELIABILITY Std            |      2.71062    |
| RELIABILITY Min            |    -11.2635     |
| RELIABILITY Max            |     -0.00349386 |

|             | Experiment 10                                                                      |
|:------------|:-----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 10 |
|:-------------------------|----------------:|
| N. Solutions             |      86         |
| N. Solutions Possible    |   10000         |
| Perc. of Archive Filled  |       1         |
| Number of generations    |      46         |
| OBJECTIVE Sum (QD score) |     -21.4243    |
| OBJECTIVE Mean           |      -0.24912   |
| OBJECTIVE Std            |       0.194025  |
| OBJECTIVE Min            |      -0.66055   |
| OBJECTIVE Max            |      -0.0267655 |

|           | Experiment 10                                                        |
|:----------|:---------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-10/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |      86         |
| N. Solutions Possible      |   10000         |
| Perc. of Archive Filled    |       1         |
| Number of generations      |      46         |
| PLAYABILITY Sum (QD score) |     -19.9459    |
| PLAYABILITY Mean           |      -0.231929  |
| PLAYABILITY Std            |       0.18719   |
| PLAYABILITY Min            |      -0.651181  |
| PLAYABILITY Max            |      -0.0259843 |

|             | Experiment 10                                                          |
|:------------|:-----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-10/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |      86         |
| N. Solutions Possible      |   10000         |
| Perc. of Archive Filled    |       1         |
| Number of generations      |      46         |
| RELIABILITY Sum (QD score) |      -0.802104  |
| RELIABILITY Mean           |      -0.0093268 |
| RELIABILITY Std            |       0.0092743 |
| RELIABILITY Min            |      -0.0508147 |
| RELIABILITY Max            |      -0         |

|             | Experiment 10                                                          |
|:------------|:-----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-10/evaluation_summary/reliability.png) |

<br/>

