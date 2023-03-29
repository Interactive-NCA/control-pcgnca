### 🔮 About experiment(s)

---

|                    | Experiment 1                |
|:-------------------|:----------------------------|
| experiment_id      | 1                           |
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

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |     84         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      1         |
| Number of generations    |     26         |
| OBJECTIVE Sum (QD score) |     -6.3089    |
| OBJECTIVE Mean           |     -0.0751059 |
| OBJECTIVE Std            |      0.182278  |
| OBJECTIVE Min            |     -1.59431   |
| OBJECTIVE Max            |     -0.0258987 |

|           | Experiment 1                                                                                                                                                                                                                                                             |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/training_summary/objective.png) |

<br/>

|          | Experiment 1                                                                                                                                                                                                                                                         |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| timeline | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/archive_snaps/timeline.gif) |

<br/>

### 🎯 Evaluation on seeds WITH Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |     21         |
| N. Solutions Possible    |  10000         |
| Perc. of Archive Filled  |      0         |
| Number of generations    |     26         |
| OBJECTIVE Sum (QD score) |     -3.76838   |
| OBJECTIVE Mean           |     -0.179447  |
| OBJECTIVE Std            |      0.348166  |
| OBJECTIVE Min            |     -1.58237   |
| OBJECTIVE Max            |     -0.0286909 |

|           | Experiment 1                                                                                                                                                                                                                                                                           |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |     21         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      0         |
| Number of generations      |     26         |
| PLAYABILITY Sum (QD score) |     -3.33511   |
| PLAYABILITY Mean           |     -0.158815  |
| PLAYABILITY Std            |      0.348136  |
| PLAYABILITY Min            |     -1.57112   |
| PLAYABILITY Max            |     -0.0165354 |

|             | Experiment 1                                                                                                                                                                                                                                                                             |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |    21          |
| N. Solutions Possible      | 10000          |
| Perc. of Archive Filled    |     0          |
| Number of generations      |    26          |
| RELIABILITY Sum (QD score) |    -0.422238   |
| RELIABILITY Mean           |    -0.0201066  |
| RELIABILITY Std            |     0.00811709 |
| RELIABILITY Min            |    -0.0330095  |
| RELIABILITY Max            |    -0.00234375 |

|             | Experiment 1                                                                                                                                                                                                                                                                             |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 1 |
|:-------------------------|---------------:|
| N. Solutions             |      40        |
| N. Solutions Possible    |   10000        |
| Perc. of Archive Filled  |       0        |
| Number of generations    |      26        |
| OBJECTIVE Sum (QD score) |     -62.4839   |
| OBJECTIVE Mean           |      -1.5621   |
| OBJECTIVE Std            |       1.15876  |
| OBJECTIVE Min            |      -4.23487  |
| OBJECTIVE Max            |      -0.023622 |

|           | Experiment 1                                                                                                                                                                                                                                                               |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |      40        |
| N. Solutions Possible      |   10000        |
| Perc. of Archive Filled    |       0        |
| Number of generations      |      26        |
| PLAYABILITY Sum (QD score) |     -61.6209   |
| PLAYABILITY Mean           |      -1.54052  |
| PLAYABILITY Std            |       1.15617  |
| PLAYABILITY Min            |      -4.22696  |
| PLAYABILITY Max            |      -0.023622 |

|             | Experiment 1                                                                                                                                                                                                                                                                 |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 1 |
|:---------------------------|---------------:|
| N. Solutions               |     40         |
| N. Solutions Possible      |  10000         |
| Perc. of Archive Filled    |      0         |
| Number of generations      |     26         |
| RELIABILITY Sum (QD score) |     -0.799493  |
| RELIABILITY Mean           |     -0.0199873 |
| RELIABILITY Std            |      0.02248   |
| RELIABILITY Min            |     -0.0875819 |
| RELIABILITY Max            |     -0         |

|             | Experiment 1                                                                                                                                                                                                                                                                 |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-1_Game-zelda_ModelName-NCA_StepSize-0.05_FixSeeds-False_NInitStates-10_NSteps-30_NAuxChans-8_BinaryChannel-True_FixedTiles-True_Overwrite-True_NModelsPerDim-100_PlayabilityWeight-1_ReliabilityWeight-1/evaluation_summary/reliability.png) |

<br/>

