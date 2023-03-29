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
| N. Solutions             |     109        |    235         |
| N. Solutions Possible    |   10000        |  10000         |
| Perc. of Archive Filled  |       1        |      2         |
| Number of generations    |      50        |    221         |
| OBJECTIVE Sum (QD score) |    -457.333    |   -258.475     |
| OBJECTIVE Mean           |      -4.19571  |     -1.0999    |
| OBJECTIVE Std            |       3.93363  |      1.64988   |
| OBJECTIVE Min            |     -15.5676   |    -12.1665    |
| OBJECTIVE Max            |      -0.265611 |     -0.0285004 |

|           | Experiment 1                                                                                                                                                                                                                                                              | Experiment 2                                                                                                                                                                                                                                                             |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/training_summary/objective.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/training_summary/objective.png) |

<br/>

|          | Experiment 1                                                                                                                                                                                                                                                          | Experiment 2                                                                                                                                                                                                                                                         |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/archive_snaps/timeline.gif) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |   Experiment 2 |
|:-------------------------|---------------:|---------------:|
| N. Solutions             |      57        |    117         |
| N. Solutions Possible    |   10000        |  10000         |
| Perc. of Archive Filled  |       1        |      1         |
| Number of generations    |      50        |    221         |
| OBJECTIVE Sum (QD score) |    -120.627    |   -428.462     |
| OBJECTIVE Mean           |      -2.11626  |     -3.66207   |
| OBJECTIVE Std            |       2.23197  |      3.29062   |
| OBJECTIVE Min            |      -9.50277  |     -9.50061   |
| OBJECTIVE Max            |      -0.265498 |     -0.0382783 |

|           | Experiment 1                                                                                                                                                                                                                                                                            | Experiment 2                                                                                                                                                                                                                                                                           |
|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/fixed_tiles_evaluation_summary/objective.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |      57        |    117         |
| N. Solutions Possible      |   10000        |  10000         |
| Perc. of Archive Filled    |       1        |      1         |
| Number of generations      |      50        |    221         |
| PLAYABILITY Sum (QD score) |    -113.679    |    -89.0019    |
| PLAYABILITY Mean           |      -1.99438  |     -0.7607    |
| PLAYABILITY Std            |       2.01549  |      0.531966  |
| PLAYABILITY Min            |      -9.48469  |     -1.99646   |
| PLAYABILITY Max            |      -0.244094 |     -0.0192913 |

|             | Experiment 1                                                                                                                                                                                                                                                                              | Experiment 2                                                                                                                                                                                                                                                                             |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/fixed_tiles_evaluation_summary/playability.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |    57          |    117         |
| N. Solutions Possible      | 10000          |  10000         |
| Perc. of Archive Filled    |     1          |      1         |
| Number of generations      |    50          |    221         |
| RELIABILITY Sum (QD score) |    -6.75321    |   -339.156     |
| RELIABILITY Mean           |    -0.118477   |     -2.89877   |
| RELIABILITY Std            |     0.697647   |      3.16676   |
| RELIABILITY Min            |    -5.2918     |     -8.54217   |
| RELIABILITY Max            |    -0.00772411 |     -0.0098221 |

|             | Experiment 1                                                                                                                                                                                                                                                                              | Experiment 2                                                                                                                                                                                                                                                                             |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/fixed_tiles_evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |   Experiment 2 |
|:-------------------------|---------------:|---------------:|
| N. Solutions             |      38        |      54        |
| N. Solutions Possible    |   10000        |   10000        |
| Perc. of Archive Filled  |       0        |       1        |
| Number of generations    |      50        |     221        |
| OBJECTIVE Sum (QD score) |    -267.994    |     -90.2449   |
| OBJECTIVE Mean           |      -7.05247  |      -1.6712   |
| OBJECTIVE Std            |       6.56062  |       0.625502 |
| OBJECTIVE Min            |     -28.4394   |      -2.83837  |
| OBJECTIVE Max            |      -0.340145 |      -0.61947  |

|           | Experiment 1                                                                                                                                                                                                                                                                | Experiment 2                                                                                                                                                                                                                                                               |
|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/evaluation_summary/objective.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |      38        |      54        |
| N. Solutions Possible      |   10000        |   10000        |
| Perc. of Archive Filled    |       0        |       1        |
| Number of generations      |      50        |     221        |
| PLAYABILITY Sum (QD score) |    -267.444    |     -89.4451   |
| PLAYABILITY Mean           |      -7.038    |      -1.65639  |
| PLAYABILITY Std            |       6.56058  |       0.621474 |
| PLAYABILITY Min            |     -28.437    |      -2.82441  |
| PLAYABILITY Max            |      -0.338583 |      -0.613533 |

|             | Experiment 1                                                                                                                                                                                                                                                                  | Experiment 2                                                                                                                                                                                                                                                                 |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/evaluation_summary/playability.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |   Experiment 2 |
|:---------------------------|---------------:|---------------:|
| N. Solutions               |    38          |     54         |
| N. Solutions Possible      | 10000          |  10000         |
| Perc. of Archive Filled    |     0          |      1         |
| Number of generations      |    50          |    221         |
| RELIABILITY Sum (QD score) |    -0.501802   |     -0.668161  |
| RELIABILITY Mean           |    -0.0132053  |     -0.0123734 |
| RELIABILITY Std            |     0.00847089 |      0.011192  |
| RELIABILITY Min            |    -0.0466237  |     -0.0671458 |
| RELIABILITY Max            |    -0          |     -0         |

|             | Experiment 1                                                                                                                                                                                                                                                                  | Experiment 2                                                                                                                                                                                                                                                                 |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-10_ReliabilityWeight-1/evaluation_summary/reliability.png) | ![](../experiments/ExperimentId-2_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/reliability.png) |

<br/>

