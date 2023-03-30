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
| N. Solutions             |      12        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       0        |
| Number of generations    |      26        |
| OBJECTIVE Sum (QD score) |      -2.84288  |
| OBJECTIVE Mean           |      -0.236907 |
| OBJECTIVE Std            |       0.569341 |
| OBJECTIVE Min            |      -2.03554  |
| OBJECTIVE Max            |      -0.023622 |

|           | Experiment 1                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |      12        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       0        |
| Number of generations      |      26        |
| PLAYABILITY Sum (QD score) |      -2.68617  |
| PLAYABILITY Mean           |      -0.223847 |
| PLAYABILITY Std            |       0.569947 |
| PLAYABILITY Min            |      -2.02512  |
| PLAYABILITY Max            |      -0.011811 |

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
| RELIABILITY Sum (QD score) |    -0.151616   |
| RELIABILITY Mean           |    -0.0126346  |
| RELIABILITY Std            |     0.00504229 |
| RELIABILITY Min            |    -0.0174736  |
| RELIABILITY Max            |    -0          |

|             | Experiment 1                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |      32        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       0        |
| Number of generations    |      26        |
| OBJECTIVE Sum (QD score) |     -86.1493   |
| OBJECTIVE Mean           |      -2.69217  |
| OBJECTIVE Std            |       0.537578 |
| OBJECTIVE Min            |      -3.03928  |
| OBJECTIVE Max            |      -0.550604 |

|           | Experiment 1                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |      32        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       0        |
| Number of generations      |      26        |
| PLAYABILITY Sum (QD score) |     -85.5824   |
| PLAYABILITY Mean           |      -2.67445  |
| PLAYABILITY Std            |       0.537193 |
| PLAYABILITY Min            |      -3.0189   |
| PLAYABILITY Max            |      -0.542126 |

|             | Experiment 1                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |     32         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      0         |
| Number of generations      |     26         |
| RELIABILITY Sum (QD score) |     -0.557469  |
| RELIABILITY Mean           |     -0.0174209 |
| RELIABILITY Std            |      0.0153416 |
| RELIABILITY Min            |     -0.0692324 |
| RELIABILITY Max            |     -0         |

|             | Experiment 1                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/evaluation_summary/reliability.png) |

<br/>

