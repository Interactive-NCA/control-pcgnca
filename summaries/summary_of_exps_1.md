### 🔮 About experiment(s)

---

|                          | Experiment 1                              |
|:-------------------------|:------------------------------------------|
| experiment_id            | 1                                         |
| description              | Manual fixed tiles(100), 5000 generations |
| game                     | zelda                                     |
| model_name               | NCA                                       |
| step_size                | 0.05                                      |
| fix_seeds                | False                                     |
| n_init_states            | 10                                        |
| n_steps                  | 50                                        |
| n_aux_chans              | 8                                         |
| binary_channel           | True                                      |
| fixed_tiles              | True                                      |
| fixed_tiles_difficulty   | manual                                    |
| fixed_tiles_archive_size | 100                                       |
| overwrite                | True                                      |
| n_models_per_dim         | 100                                       |
| playability_weight       | 1                                         |
| reliability_weight       | 1                                         |
| bcs                      | ['symmetry', 'path-length']               |
| bcs_bounds               | [[0, 1], [0, 271]]                        |
| n_tiles                  | 5                                         |
| grid_dim                 | 16                                        |

### 🔖 Training Process Summary

---

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |   1184         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |     12         |
| Number of generations    |   4701         |
| OBJECTIVE Sum (QD score) |   -202.505     |
| OBJECTIVE Mean           |     -0.171034  |
| OBJECTIVE Std            |      1.01443   |
| OBJECTIVE Min            |    -11.0584    |
| OBJECTIVE Max            |     -0.0178626 |

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
| N. Solutions             |    102         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      1         |
| Number of generations    |   4701         |
| OBJECTIVE Sum (QD score) |   -418.124     |
| OBJECTIVE Mean           |     -4.09926   |
| OBJECTIVE Std            |      3.65177   |
| OBJECTIVE Min            |    -11.3806    |
| OBJECTIVE Max            |     -0.0269687 |

|           | Experiment 1                                                                    |
|:----------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |    102         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |   4701         |
| PLAYABILITY Sum (QD score) |     -2.38414   |
| PLAYABILITY Mean           |     -0.0233739 |
| PLAYABILITY Std            |      0.0146679 |
| PLAYABILITY Min            |     -0.110741  |
| PLAYABILITY Max            |     -0.011811  |

|             | Experiment 1                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |    102         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |   4701         |
| RELIABILITY Sum (QD score) |   -415.515     |
| RELIABILITY Mean           |     -4.07368   |
| RELIABILITY Std            |      3.65381   |
| RELIABILITY Min            |    -11.2698    |
| RELIABILITY Max            |     -0.0046054 |

|             | Experiment 1                                                                      |
|:------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |     82         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      1         |
| Number of generations    |   4701         |
| OBJECTIVE Sum (QD score) |    -59.099     |
| OBJECTIVE Mean           |     -0.72072   |
| OBJECTIVE Std            |      0.725609  |
| OBJECTIVE Min            |     -5.57835   |
| OBJECTIVE Max            |     -0.0198545 |

|           | Experiment 1                                                        |
|:----------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |     82         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |   4701         |
| PLAYABILITY Sum (QD score) |    -51.8122    |
| PLAYABILITY Mean           |     -0.631856  |
| PLAYABILITY Std            |      0.482669  |
| PLAYABILITY Min            |     -1.91965   |
| PLAYABILITY Max            |     -0.0188976 |

|             | Experiment 1                                                          |
|:------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |     82         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |   4701         |
| RELIABILITY Sum (QD score) |     -6.34957   |
| RELIABILITY Mean           |     -0.0774338 |
| RELIABILITY Std            |      0.6124    |
| RELIABILITY Min            |     -5.55472   |
| RELIABILITY Max            |     -0         |

|             | Experiment 1                                                          |
|:------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/evaluation_summary/reliability.png) |

<br/>

