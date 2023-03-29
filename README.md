## About
Platform for experimentation with generating game levels via archive of Neural Cellular Automata.

## Environment setup
### Install dependencies
How to install dependencies.

### Fixed tiles generation based on game
Here, I should describe how to generate fixed tiles.

## Guide
This should describe the whole experimentation procedure.

### Training
There are two ways to start training procedure, both described below. There 

#### From SCRATCH
If there was no training ran for the given experiment, i.e., there is no folder with the given experiment ID in [experiments](experiments), then you should follow these steps:
1. Setup experiment parameters [experiment settings](settings/experiment/settings.json)
2. Start the training procedure by running in the command line:

```
python3 cli.py --train --n_cores 8 --n_generations 50 --save_freq 5
```

#### From EXISTING EVOLVER
Example:
```
python3 cli.py --train --expid 3 --n_cores 8 --n_generations 50 --save_freq 5
```

### Evaluate
Example command:

```
python3 cli.py --evaluate --expid 1 --n_cores 8
```

### Summarising evaluation
Before summarising given experiments, make sure you evaluted each of them so you are looking at the most recent data!

```
python3 cli.py --summarise "1,2,3"
```