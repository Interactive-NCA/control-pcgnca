:construction: **NOTE:** this repository is still under active development and therefore the documentation still has to be polished 

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
python3 cli.py --evaluate --expid 15 --n_cores 8 --fxd_til "easy" --fxd_til_size 1000 --n_evals 10 --eval_batch_size 10
```

### Summarising evaluation
Before summarising given experiments, make sure you evaluted each of them so you are looking at the most recent data!

```
python3 cli.py --summarise "1,2" --fxd_til "easy" --fxd_til_size 100 --n_evals 2 --eval_batch_size 10
```

### File transfer
Note that `--files_exclude` should be comma separated list of files or directories to exclude. Finally, before starting, checkout
the `settings/slurm/settings.json`, here you can specify parameters such as `domain` (of the server) and `username`.

#### From server to local
python3 cli.py --file-transfer --save_where "test/" --expid 2 --files_exclude "evolver.pkl" --server-to-local

#### From local to server
python3 cli.py --file-transfer --save_where "test/" --expid 2 --files_exclude "evolver.pkl"

### Archive subsampling
For production purposes, you may want to use smaller archive, this can be done via subsampling:

```bash
python3 cli.py --subsample --expid 15 --n_models 100
```