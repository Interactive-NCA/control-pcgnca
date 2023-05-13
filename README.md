## :bug: About
Platform for experimentation with generating game levels via archive of Neural Cellular Automata trained using CMA-ME QD algorithm. The `README`
is structured into three main sections: environment setup, results reproduction, conduct new experiments. One of the main functionalities of this platform is 
to be able to train archive of NCA models while being able to differ many hyper-parameters. The main training loop is outlined in the figure below.

![Main trainining loop overview](assets/readme/training_overview_short.png)

## :snake: Conda Environment Setup
We use `conda` as our default virtual environment. First, create conda environment and install `pip`:

```bash
conda create --name pcgnca python=3.10
conda activate pcgnca
conda install pip
```

Then, install rest of the packages via `pip`:

```bash
python3.10 -m pip install -r requirements.txt
```
## :microscope: Reproduce the experiments
The reproduction of our experiments can be done in for subsequent steps: fixed tiles archive generation, archive training, archive evaluation, results summarisation. 
All these steps are documented in detail below.

### Fixed tiles archive generation
To generate archives with fixed tiles used in our work, run the following command:

```bash
# walls
python3 cli.py --gen-fixed-seeds --fixedgen-game "zelda" --fixedgen-nseeds 1000 --fixedgen-difficulty "easy"
# triples
python3 cli.py --gen-fixed-seeds --fixedgen-game "zelda" --fixedgen-nseeds 1000 --fixedgen-difficulty "all_special_random"
# pairs
python3 cli.py --gen-fixed-seeds --fixedgen-game "zelda" --fixedgen-nseeds 1000 --fixedgen-difficulty "two_special_random"
# singles
python3 cli.py --gen-fixed-seeds --fixedgen-game "zelda" --fixedgen-nseeds 1000 --fixedgen-difficulty "one_special_random"
# mixed
python3 cli.py --gen-fixed-seeds --fixedgen-game "zelda" --fixedgen-nseeds 1000 --fixedgen-difficulty "mixed"
```

You can then checkout the results in the [zelda fixed tiles folder](settings/fixed_tiles/zelda/) where each type of fixed tiles also has a corresponding `gif` showcasing ten percent of the fixed tiles archive sampled randomly. Below, you can see example of archive for fixed `Walls`, `Triples` and `Mixed`.

| Walls            |   Triples        |   Mixed          |
|:----------------:|:----------------:|:----------------:|
| ![](assets/readme/easy_1000.gif) | ![](assets/readme/all_special_random_1000.gif) | ![](assets/readme/mixed_1000.gif)

### Archive training

First, copy the settings of the experiments to be reproduced to the experiments folder:

```bash
cp -r reproduce/* experiments/
```

Then, to train the ith experiment `locally`, you can run the following command (example for the baseline archive):

```bash
python3 cli.py --train --expid 1 --n_cores 32 --n_generations 3000 --save_freq 100
```

where:
- `--expid`: the id of the experiment you want to train, our work included baseline (`1`), walls (`2`), triples (`3`), pairs (`4`), singles (`5`) and mixed (`6`).
- `--n_cores`: how many cpu cores you want to use
- `--n_generations`: how many training iterations you want to run
- `--save_freq`: how often do you want to save the state of the archive

If you want to run the experiment on slurm cluster, then you can use the `job` template specified below:

```bash
#!/bin/bash

#SBATCH --job-name=PCGNCA-EXPERIMENT-X
#SBATCH --output=experiments/ExperimentId-X/slurm.out
#SBATCH --cpus-per-task=32
#SBATCH --time=08:00:00
#SBATCH --partition=red,brown
#SBATCH --mail-user=user@uni.edu
#SBATCH --mail-type=BEGIN,FAIL,END
#SBATCH --exclude cn8

echo "Running on $(hostname)"

module load Anaconda3
source /home/user/.bashrc
conda activate pcgnca

python3 cli.py --train --expid 1 --n_cores 32 --n_generations 3000 --save_freq 100
```