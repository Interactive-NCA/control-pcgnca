### 🔮 About experiment(s)

---

|                    | Experiment 3                |
|:-------------------|:----------------------------|
| experiment_id      | 3                           |
| game               | zelda                       |
| model_name         | NCA                         |
| step_size          | 0.05                        |
| fix_seeds          | False                       |
| n_init_states      | 10                          |
| n_steps            | 30                          |
| n_aux_chans        | 8                           |
| binary_channel     | True                        |
| fixed_tiles        | True                        |
| overwrite          | True                        |
| n_models_per_dim   | 100                         |
| playability_weight | 1                           |
| reliability_weight | 1                           |
| bcs                | ['symmetry', 'path-length'] |
| bcs_bounds         | [[0, 1], [0, 271]]          |
| n_tiles            | 5                           |
| grid_dim           | 16                          |

### 🔖 Training Process Summary

---

|                          |   Experiment 3 |
|:-------------------------|---------------:|
| N. Solutions             |     89         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      1         |
| Number of generations    |     51         |
| OBJECTIVE Sum (QD score) |    -41.1961    |
| OBJECTIVE Mean           |     -0.462877  |
| OBJECTIVE Std            |      1.05241   |
| OBJECTIVE Min            |     -7.35082   |
| OBJECTIVE Max            |     -0.0277396 |

|           | Experiment 3                                                                                                                                                                                                                                                             |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-3_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/training_summary/objective.png) |

<br/>

|          | Experiment 3                                                                                                                                                                                                                                                         |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-3_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 3 |
|:-------------------------|---------------:|
| N. Solutions             |      58        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       1        |
| Number of generations    |      51        |
| OBJECTIVE Sum (QD score) |     -20.4738   |
| OBJECTIVE Mean           |      -0.352996 |
| OBJECTIVE Std            |       0.46342  |
| OBJECTIVE Min            |      -1.4302   |
| OBJECTIVE Max            |      -0.029079 |

|           | Experiment 3                                                                                                                                                                                                                                                                           |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-3_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |     58         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      1         |
| Number of generations      |     51         |
| PLAYABILITY Sum (QD score) |    -17.7356    |
| PLAYABILITY Mean           |     -0.305786  |
| PLAYABILITY Std            |      0.448463  |
| PLAYABILITY Min            |     -1.36772   |
| PLAYABILITY Max            |     -0.0141732 |

|             | Experiment 3                                                                                                                                                                                                                                                                             |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-3_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |    58          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     1          |
| Number of generations      |    51          |
| RELIABILITY Sum (QD score) |    -2.64709    |
| RELIABILITY Mean           |    -0.0456394  |
| RELIABILITY Std            |     0.132657   |
| RELIABILITY Min            |    -0.928277   |
| RELIABILITY Max            |    -0.00117188 |

|             | Experiment 3                                                                                                                                                                                                                                                                             |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-3_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 3 |
|:-------------------------|---------------:|
| N. Solutions             |     44         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      0         |
| Number of generations    |     51         |
| OBJECTIVE Sum (QD score) |    -57.0938    |
| OBJECTIVE Mean           |     -1.29759   |
| OBJECTIVE Std            |      0.908746  |
| OBJECTIVE Min            |     -2.99922   |
| OBJECTIVE Max            |     -0.0662377 |

|           | Experiment 3                                                                                                                                                                                                                                                               |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-3_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |     44         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      0         |
| Number of generations      |     51         |
| PLAYABILITY Sum (QD score) |    -56.3365    |
| PLAYABILITY Mean           |     -1.28038   |
| PLAYABILITY Std            |      0.908743  |
| PLAYABILITY Min            |     -2.98583   |
| PLAYABILITY Max            |     -0.0619587 |

|             | Experiment 3                                                                                                                                                                                                                                                                 |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-3_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 3 |
|:---------------------------|---------------:|
| N. Solutions               |    44          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     0          |
| Number of generations      |    51          |
| RELIABILITY Sum (QD score) |    -0.529469   |
| RELIABILITY Mean           |    -0.0120334  |
| RELIABILITY Std            |     0.00788733 |
| RELIABILITY Min            |    -0.03918    |
| RELIABILITY Max            |    -0          |

|             | Experiment 3                                                                                                                                                                                                                                                                 |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-3_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/reliability.png) |

<br/>

