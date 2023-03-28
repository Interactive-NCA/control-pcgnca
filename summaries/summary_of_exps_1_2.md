### 🔮 About experiment(s)

---

|                    | Experiment 1                | Experiment 2                |
|:-------------------|:----------------------------|:----------------------------|
| game               | zelda                       | zelda                       |
| model_name         | NCA                         | NCA                         |
| step_size          | 0.05                        | 0.05                        |
| fix_seeds          | False                       | False                       |
| n_init_states      | 10                          | 10                          |
| n_steps            | 30                          | 30                          |
| n_aux_chans        | 8                           | 8                           |
| binary_channel     | True                        | True                        |
| fixed_tiles        | True                        | True                        |
| overwrite          | True                        | True                        |
| n_models_per_dim   | 100                         | 100                         |
| playability_weight | 10                          | 1                           |
| reliability_weight | 1                           | 1                           |
| bcs                | ['symmetry', 'path-length'] | ['symmetry', 'path-length'] |
| bcs_bounds         | [[0, 1], [0, 271]]          | [[0, 1], [0, 271]]          |
| n_tiles            | 8                           | 8                           |
| grid_dim           | 16                          | 16                          |

### 🔖 Training Process Summary

---

|                          |   Experiment 1 |   Experiment 2 |
|:-------------------------|---------------:|---------------:|
| N. Solutions             |      96        |     223        |
| N. Solutions Possible    |   10000        |   10000        |
| Perc. of Archive Filled  |       1        |       2        |
| Number of generations    |      29        |     202        |
| OBJECTIVE Sum (QD score) |    -401.909    |    -178        |
| OBJECTIVE Mean           |      -4.18655  |      -0.798206 |
| OBJECTIVE Std            |       3.63195  |       0.24586  |
| OBJECTIVE Min            |     -15.2673   |      -1        |
| OBJECTIVE Max            |      -0.315532 |      -0.5      |

|           | Experiment 1                                                                                                                                                                                                                                                              | Experiment 2                                                                                                                                                                                                                                                             |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/training_summary/objective.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/training_summary/objective.png) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |   Experiment 2 |
|:-------------------------|---------------:|---------------:|
| N. Solutions             |      57        |     123        |
| N. Solutions Possible    |   10000        |   10000        |
| Perc. of Archive Filled  |       1        |       1        |
| Number of generations    |      29        |     202        |
| OBJECTIVE Sum (QD score) |    -206.889    |    -499.352    |
| OBJECTIVE Mean           |      -3.62963  |      -4.05977  |
| OBJECTIVE Std            |       2.51952  |       3.20921  |
| OBJECTIVE Min            |     -11.3967   |     -10.4975   |
| OBJECTIVE Max            |      -0.344984 |      -0.709211 |

|           | Experiment 1                                                                                                                                                                                                                                                                            | Experiment 2                                                                                                                                                                                                                                                                           |
|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/fixed_tiles_evaluation_summary/objective.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |      57        |     123        |
| N. Solutions Possible      |   10000        |   10000        |
| Perc. of Archive Filled    |       1        |       1        |
| Number of generations      |      29        |     202        |
| PLAYABILITY Sum (QD score) |    -189.115    |    -140.64     |
| PLAYABILITY Mean           |      -3.3178   |      -1.14341  |
| PLAYABILITY Std            |       2.10954  |       0.373276 |
| PLAYABILITY Min            |     -10.3404   |      -2.28834  |
| PLAYABILITY Max            |      -0.327647 |      -0.68376  |

|             | Experiment 1                                                                                                                                                                                                                                                                              | Experiment 2                                                                                                                                                                                                                                                                             |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/fixed_tiles_evaluation_summary/playability.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |    57          |   123          |
| N. Solutions Possible      | 10000          | 10000          |
| Perc. of Archive Filled    |     1          |     1          |
| Number of generations      |    29          |   202          |
| RELIABILITY Sum (QD score) |   -16.1483     |  -358.373      |
| RELIABILITY Mean           |    -0.283303   |    -2.9136     |
| RELIABILITY Std            |     1.11719    |     3.35015    |
| RELIABILITY Min            |    -5.34298    |    -9.58091    |
| RELIABILITY Max            |    -0.00845953 |    -0.00720277 |

|             | Experiment 1                                                                                                                                                                                                                                                                              | Experiment 2                                                                                                                                                                                                                                                                             |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/fixed_tiles_evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |   Experiment 2 |
|:-------------------------|---------------:|---------------:|
| N. Solutions             |      48        |      52        |
| N. Solutions Possible    |   10000        |   10000        |
| Perc. of Archive Filled  |       0        |       1        |
| Number of generations    |      29        |     202        |
| OBJECTIVE Sum (QD score) |    -531.628    |     -90.9075   |
| OBJECTIVE Mean           |     -11.0756   |      -1.74822  |
| OBJECTIVE Std            |       7.17214  |       0.617727 |
| OBJECTIVE Min            |     -30.611    |      -3.01444  |
| OBJECTIVE Max            |      -0.832039 |      -0.664222 |

|           | Experiment 1                                                                                                                                                                                                                                                                | Experiment 2                                                                                                                                                                                                                                                               |
|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/evaluation_summary/objective.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |       48       |      52        |
| N. Solutions Possible      |    10000       |   10000        |
| Perc. of Archive Filled    |        0       |       1        |
| Number of generations      |       29       |     202        |
| PLAYABILITY Sum (QD score) |     -530.718   |     -89.9754   |
| PLAYABILITY Mean           |      -11.0566  |      -1.7303   |
| PLAYABILITY Std            |        7.17717 |       0.610027 |
| PLAYABILITY Min            |      -30.6078  |      -2.98913  |
| PLAYABILITY Max            |       -0.76706 |      -0.659903 |

|             | Experiment 1                                                                                                                                                                                                                                                                  | Experiment 2                                                                                                                                                                                                                                                                 |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/evaluation_summary/playability.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |    48          |     52         |
| N. Solutions Possible      | 10000          |  10000         |
| Perc. of Archive Filled    |     0          |      1         |
| Number of generations      |    29          |    202         |
| RELIABILITY Sum (QD score) |    -0.62262    |     -0.775835  |
| RELIABILITY Mean           |    -0.0129712  |     -0.0149199 |
| RELIABILITY Std            |     0.00802682 |      0.01581   |
| RELIABILITY Min            |    -0.0496324  |     -0.0795246 |
| RELIABILITY Max            |    -0          |     -0         |

|             | Experiment 1                                                                                                                                                                                                                                                                  | Experiment 2                                                                                                                                                                                                                                                                 |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/reliability.png) |

<br/>

