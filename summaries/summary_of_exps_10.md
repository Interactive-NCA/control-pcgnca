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
| N. Solutions             |     771         |
| N. Solutions Possible    |   10000         |
| Perc. of Archive Filled  |       8         |
| Number of generations    |      96         |
| OBJECTIVE Sum (QD score) |   -4523.26      |
| OBJECTIVE Mean           |      -5.86674   |
| OBJECTIVE Std            |       2.35811   |
| OBJECTIVE Min            |     -11.1384    |
| OBJECTIVE Max            |      -0.0375349 |

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
| N. Solutions             |     287         |
| N. Solutions Possible    |   10000         |
| Perc. of Archive Filled  |       3         |
| Number of generations    |      96         |
| OBJECTIVE Sum (QD score) |   -1558.74      |
| OBJECTIVE Mean           |      -5.43116   |
| OBJECTIVE Std            |       2.92994   |
| OBJECTIVE Min            |      -9.09765   |
| OBJECTIVE Max            |      -0.0360167 |

|           | Experiment 10                                                                    |
|:----------|:---------------------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |     287         |
| N. Solutions Possible      |   10000         |
| Perc. of Archive Filled    |       3         |
| Number of generations      |      96         |
| PLAYABILITY Sum (QD score) |     -79.1943    |
| PLAYABILITY Mean           |      -0.275938  |
| PLAYABILITY Std            |       0.202012  |
| PLAYABILITY Min            |      -0.808574  |
| PLAYABILITY Max            |      -0.0141732 |

|             | Experiment 10                                                                      |
|:------------|:-----------------------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |    287          |
| N. Solutions Possible      |  10000          |
| Perc. of Archive Filled    |      3          |
| Number of generations      |     96          |
| RELIABILITY Sum (QD score) |  -1472.07       |
| RELIABILITY Mean           |     -5.12917    |
| RELIABILITY Std            |      2.90179    |
| RELIABILITY Min            |     -8.65551    |
| RELIABILITY Max            |     -0.00324477 |

|             | Experiment 10                                                                      |
|:------------|:-----------------------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-10/fixed_tiles_evaluation_summary/reliability.png) |

<br/>

### 🎯 Evaluation on seeds WITHOUT Fixed tiles

---

👉 **OBJECTIVE**

|                          |   Experiment 10 |
|:-------------------------|----------------:|
| N. Solutions             |      97         |
| N. Solutions Possible    |   10000         |
| Perc. of Archive Filled  |       1         |
| Number of generations    |      96         |
| OBJECTIVE Sum (QD score) |     -24.9881    |
| OBJECTIVE Mean           |      -0.257609  |
| OBJECTIVE Std            |       0.20776   |
| OBJECTIVE Min            |      -0.688752  |
| OBJECTIVE Max            |      -0.0261537 |

|           | Experiment 10                                                        |
|:----------|:---------------------------------------------------------------------|
| objective | ![](../experiments/ExperimentId-10/evaluation_summary/objective.png) |

<br/>

👉 **PLAYABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |      97         |
| N. Solutions Possible      |   10000         |
| Perc. of Archive Filled    |       1         |
| Number of generations      |      96         |
| PLAYABILITY Sum (QD score) |     -23.0565    |
| PLAYABILITY Mean           |      -0.237695  |
| PLAYABILITY Std            |       0.197208  |
| PLAYABILITY Min            |      -0.605906  |
| PLAYABILITY Max            |      -0.0248031 |

|             | Experiment 10                                                          |
|:------------|:-----------------------------------------------------------------------|
| playability | ![](../experiments/ExperimentId-10/evaluation_summary/playability.png) |

<br/>

👉 **RELIABILITY**

|                            |   Experiment 10 |
|:---------------------------|----------------:|
| N. Solutions               |      97         |
| N. Solutions Possible      |   10000         |
| Perc. of Archive Filled    |       1         |
| Number of generations      |      96         |
| RELIABILITY Sum (QD score) |      -1.02195   |
| RELIABILITY Mean           |      -0.0105355 |
| RELIABILITY Std            |       0.0137796 |
| RELIABILITY Min            |      -0.0855317 |
| RELIABILITY Max            |      -0         |

|             | Experiment 10                                                          |
|:------------|:-----------------------------------------------------------------------|
| reliability | ![](../experiments/ExperimentId-10/evaluation_summary/reliability.png) |

<br/>

