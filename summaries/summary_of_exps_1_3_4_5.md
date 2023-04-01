### 🔮 About experiment(s)

---

|                          | Experiment 1                              | Experiment 3                                        | Experiment 4                                                                 | Experiment 5                                                       |
|:-------------------------|:------------------------------------------|:----------------------------------------------------|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------|
| experiment_id            | 1                                         | 3                                                   | 4                                                                            | 5                                                                  |
| description              | Manual fixed tiles(100), 5000 generations | Automatic easy fixed tiles(10000), 5000 generations | Automatic easy fixed tiles(10000), 5000 generations, playability weight = 10 | Manual fixed tiles(100), 5000 generations, playability weight = 10 |
| game                     | zelda                                     | zelda                                               | zelda                                                                        | zelda                                                              |
| model_name               | NCA                                       | NCA                                                 | NCA                                                                          | NCA                                                                |
| step_size                | 0.05                                      | 0.05                                                | 0.05                                                                         | 0.05                                                               |
| fix_seeds                | False                                     | False                                               | False                                                                        | False                                                              |
| n_init_states            | 10                                        | 10                                                  | 10                                                                           | 10                                                                 |
| n_steps                  | 50                                        | 50                                                  | 50                                                                           | 50                                                                 |
| n_aux_chans              | 8                                         | 8                                                   | 8                                                                            | 8                                                                  |
| binary_channel           | True                                      | True                                                | True                                                                         | True                                                               |
| fixed_tiles              | True                                      | True                                                | True                                                                         | True                                                               |
| fixed_tiles_difficulty   | manual                                    | easy                                                | easy                                                                         | manual                                                             |
| fixed_tiles_archive_size | 100                                       | 10000                                               | 10000                                                                        | 100                                                                |
| overwrite                | True                                      | True                                                | True                                                                         | True                                                               |
| n_models_per_dim         | 100                                       | 100                                                 | 100                                                                          | 100                                                                |
| playability_weight       | 1                                         | 1                                                   | 10                                                                           | 10                                                                 |
| reliability_weight       | 1                                         | 1                                                   | 1                                                                            | 1                                                                  |
| bcs                      | ['symmetry', 'path-length']               | ['symmetry', 'path-length']                         | ['symmetry', 'path-length']                                                  | ['symmetry', 'path-length']                                        |
| bcs_bounds               | [[0, 1], [0, 271]]                        | [[0, 1], [0, 271]]                                  | [[0, 1], [0, 271]]                                                           | [[0, 1], [0, 271]]                                                 |
| n_tiles                  | 5                                         | 5                                                   | 5                                                                            | 5                                                                  |
| grid_dim                 | 16                                        | 16                                                  | 16                                                                           | 16                                                                 |

### 🔖 Training Process Summary

---

|                          |   Experiment 1 |   Experiment 3 |   Experiment 4 |   Experiment 5 |
|:-------------------------|---------------:|---------------:|---------------:|---------------:|
| N. Solutions             |   1184         |     806        |   769          |     265        |
| N. Solutions Possible    |  10000         |   10000        | 10000          |   10000        |
| Perc. of Archive Filled  |     12         |       8        |     8          |       3        |
| Number of generations    |   4701         |    4601        |  5001          |    4701        |
| OBJECTIVE Sum (QD score) |   -202.505     |    -107.958    |  -190.818      |    -238.96     |
| OBJECTIVE Mean           |     -0.171034  |      -0.133943 |    -0.248138   |      -0.901735 |
| OBJECTIVE Std            |      1.01443   |       0.976564 |     1.46036    |       2.10692  |
| OBJECTIVE Min            |    -11.0584    |     -11.2487   |   -11.7081     |     -13.3245   |
| OBJECTIVE Max            |     -0.0178626 |      -0        |    -0.00292317 |      -0.125429 |

|           | Experiment 1                                                      | Experiment 3                                                      | Experiment 4                                                      | Experiment 5                                                      |
|:----------|:------------------------------------------------------------------|:------------------------------------------------------------------|:------------------------------------------------------------------|:------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/training_summary/objective.png) | ![](../experiments/ExperimentId-3/training_summary/objective.png) | ![](../experiments/ExperimentId-4/training_summary/objective.png) | ![](../experiments/ExperimentId-5/training_summary/objective.png) |

<br/>

|          | Experiment 1                                                  | Experiment 3                                                  | Experiment 4                                                  | Experiment 5                                                  |
|:---------|:--------------------------------------------------------------|:--------------------------------------------------------------|:--------------------------------------------------------------|:--------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-1/archive_snaps/timeline.gif) | ![](../experiments/ExperimentId-3/archive_snaps/timeline.gif) | ![](../experiments/ExperimentId-4/archive_snaps/timeline.gif) | ![](../experiments/ExperimentId-5/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |   Experiment 3 |   Experiment 4 |   Experiment 5 |
|:-------------------------|---------------:|---------------:|---------------:|---------------:|
| N. Solutions             |    102         |      103       |    50          |      43        |
| N. Solutions Possible    |  10000         |    10000       | 10000          |   10000        |
| Perc. of Archive Filled  |      1         |        1       |     1          |       0        |
| Number of generations    |   4701         |     4601       |  5001          |    4701        |
| OBJECTIVE Sum (QD score) |   -418.124     |     -322.457   |  -293.062      |    -162.328    |
| OBJECTIVE Mean           |     -4.09926   |       -3.13065 |    -5.86123    |      -3.77506  |
| OBJECTIVE Std            |      3.65177   |        3.88317 |     4.15505    |       3.10716  |
| OBJECTIVE Min            |    -11.3806    |      -11.4723  |   -11.5886     |     -11.917    |
| OBJECTIVE Max            |     -0.0269687 |       -0       |    -0.00721335 |      -0.168834 |

|           | Experiment 1                                                                    | Experiment 3                                                                    | Experiment 4                                                                    | Experiment 5                                                                    |
|:----------|:--------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/objective.png) | ![](../experiments/ExperimentId-3/fixed_tiles_evaluation_summary/objective.png) | ![](../experiments/ExperimentId-4/fixed_tiles_evaluation_summary/objective.png) | ![](../experiments/ExperimentId-5/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |   Experiment 3 |   Experiment 4 |   Experiment 5 |
|:---------------------------|---------------:|---------------:|---------------:|---------------:|
| N. Solutions               |    102         |    103         |     50         |      43        |
| N. Solutions Possible      |  10000         |  10000         |  10000         |   10000        |
| Perc. of Archive Filled    |      1         |      1         |      1         |       0        |
| Number of generations      |   4701         |   4601         |   5001         |    4701        |
| PLAYABILITY Sum (QD score) |     -2.38414   |     -3.1411    |     -4.17163   |     -20.2756   |
| PLAYABILITY Mean           |     -0.0233739 |     -0.0304961 |     -0.0834326 |      -0.471525 |
| PLAYABILITY Std            |      0.0146679 |      0.0609924 |      0.137396  |       1.77632  |
| PLAYABILITY Min            |     -0.110741  |     -0.397804  |     -0.546875  |     -11.8145   |
| PLAYABILITY Max            |     -0.011811  |     -0         |     -0         |      -0.106299 |

|             | Experiment 1                                                                      | Experiment 3                                                                      | Experiment 4                                                                      | Experiment 5                                                                      |
|:------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/playability.png) | ![](../experiments/ExperimentId-3/fixed_tiles_evaluation_summary/playability.png) | ![](../experiments/ExperimentId-4/fixed_tiles_evaluation_summary/playability.png) | ![](../experiments/ExperimentId-5/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |   Experiment 3 |   Experiment 4 |   Experiment 5 |
|:---------------------------|---------------:|---------------:|---------------:|---------------:|
| N. Solutions               |    102         |      103       |    50          |    43          |
| N. Solutions Possible      |  10000         |    10000       | 10000          | 10000          |
| Perc. of Archive Filled    |      1         |        1       |     1          |     0          |
| Number of generations      |   4701         |     4601       |  5001          |  4701          |
| RELIABILITY Sum (QD score) |   -415.515     |     -319.266   |  -288.88       |  -140.609      |
| RELIABILITY Mean           |     -4.07368   |       -3.09967 |    -5.77759    |    -3.26998    |
| RELIABILITY Std            |      3.65381   |        3.89938 |     4.10212    |     2.96928    |
| RELIABILITY Min            |    -11.2698    |      -11.4257  |   -11.5314     |    -8.51444    |
| RELIABILITY Max            |     -0.0046054 |       -0       |    -0.00721335 |    -0.00407824 |

|             | Experiment 1                                                                      | Experiment 3                                                                      | Experiment 4                                                                      | Experiment 5                                                                      |
|:------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/fixed_tiles_evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-3/fixed_tiles_evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-4/fixed_tiles_evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-5/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |   Experiment 3 |   Experiment 4 |   Experiment 5 |
|:-------------------------|---------------:|---------------:|---------------:|---------------:|
| N. Solutions             |     82         |     83         |      87        |       58       |
| N. Solutions Possible    |  10000         |  10000         |   10000        |    10000       |
| Perc. of Archive Filled  |      1         |      1         |       1        |        1       |
| Number of generations    |   4701         |   4601         |    5001        |     4701       |
| OBJECTIVE Sum (QD score) |    -59.099     |    -47.3078    |   -1868.72     |     -988.285   |
| OBJECTIVE Mean           |     -0.72072   |     -0.569973  |     -21.4796   |      -17.0394  |
| OBJECTIVE Std            |      0.725609  |      1.02172   |      12.0646   |        9.79371 |
| OBJECTIVE Min            |     -5.57835   |     -6.50681   |     -58.7885   |      -30.1269  |
| OBJECTIVE Max            |     -0.0198545 |     -0.0292398 |      -0.594956 |       -0.309   |

|           | Experiment 1                                                        | Experiment 3                                                        | Experiment 4                                                        | Experiment 5                                                        |
|:----------|:--------------------------------------------------------------------|:--------------------------------------------------------------------|:--------------------------------------------------------------------|:--------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1/evaluation_summary/objective.png) | ![](../experiments/ExperimentId-3/evaluation_summary/objective.png) | ![](../experiments/ExperimentId-4/evaluation_summary/objective.png) | ![](../experiments/ExperimentId-5/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |   Experiment 3 |   Experiment 4 |   Experiment 5 |
|:---------------------------|---------------:|---------------:|---------------:|---------------:|
| N. Solutions               |     82         |     83         |      87        |      58        |
| N. Solutions Possible      |  10000         |  10000         |   10000        |   10000        |
| Perc. of Archive Filled    |      1         |      1         |       1        |       1        |
| Number of generations      |   4701         |   4601         |    5001        |    4701        |
| PLAYABILITY Sum (QD score) |    -51.8122    |    -33.9422    |   -1867.02     |    -987.511    |
| PLAYABILITY Mean           |     -0.631856  |     -0.408942  |     -21.46     |     -17.0261   |
| PLAYABILITY Std            |      0.482669  |      0.536326  |      12.054    |       9.79203  |
| PLAYABILITY Min            |     -1.91965   |     -3.01299   |     -58.7573   |     -30.1181   |
| PLAYABILITY Max            |     -0.0188976 |     -0.0248031 |      -0.592335 |      -0.307087 |

|             | Experiment 1                                                          | Experiment 3                                                          | Experiment 4                                                          | Experiment 5                                                          |
|:------------|:----------------------------------------------------------------------|:----------------------------------------------------------------------|:----------------------------------------------------------------------|:----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1/evaluation_summary/playability.png) | ![](../experiments/ExperimentId-3/evaluation_summary/playability.png) | ![](../experiments/ExperimentId-4/evaluation_summary/playability.png) | ![](../experiments/ExperimentId-5/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |   Experiment 3 |   Experiment 4 |   Experiment 5 |
|:---------------------------|---------------:|---------------:|---------------:|---------------:|
| N. Solutions               |     82         |      83        |     87         |    58          |
| N. Solutions Possible      |  10000         |   10000        |  10000         | 10000          |
| Perc. of Archive Filled    |      1         |       1        |      1         |     1          |
| Number of generations      |   4701         |    4601        |   5001         |  4701          |
| RELIABILITY Sum (QD score) |     -6.34957   |     -12.8963   |     -1.22717   |    -0.635025   |
| RELIABILITY Mean           |     -0.0774338 |      -0.155377 |     -0.0141054 |    -0.0109487  |
| RELIABILITY Std            |      0.6124    |       0.928223 |      0.0129133 |     0.00877153 |
| RELIABILITY Min            |     -5.55472   |      -6.45648  |     -0.0711005 |    -0.0597363  |
| RELIABILITY Max            |     -0         |      -0        |     -0         |    -0          |

|             | Experiment 1                                                          | Experiment 3                                                          | Experiment 4                                                          | Experiment 5                                                          |
|:------------|:----------------------------------------------------------------------|:----------------------------------------------------------------------|:----------------------------------------------------------------------|:----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1/evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-3/evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-4/evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-5/evaluation_summary/reliability.png) |

<br/>

