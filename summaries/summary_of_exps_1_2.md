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

