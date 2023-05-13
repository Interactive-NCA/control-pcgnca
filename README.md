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

### Archive evaluation
To evaluate the archives `locally`, you can run (example for the baseline):

```bash
python3 cli.py --evaluate --expid 1 --n_cores 32 --fxd_til "easy" --fxd_til_size 1000 --n_evals 10 --eval_batch_size 10
```

where:
- `--fxd_til`: type of fixed tiles you want to evaluate the archive on
- `--fxd_til_size`: size of the fixed tiles archive
- `--n_evals`: number of evaluations to run
- `--eval_batch_size`: size of the batch in each evaluation based on which BCs and objective of each model should be computed

For cluster, you can again use the template:

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

python3 cli.py --evaluate --expid 1 --n_cores 32 --fxd_til "easy" --fxd_til_size 1000 --n_evals 10 --eval_batch_size 10
```

### Summarising results
Once the results are computed, you can use the summarisation script that puts them in a nice markdown overiew. Assuming we have trained all our experiments and 
evaluated them against fixed walls (`easy`) with the archive size of fixed tiles being 1000, number of evalutions was 10 and evaluation batch size was 10 as well:

```bash
python3 cli.py --summarise "1,2,3,4,5,6" --fxd_til "easy" --fxd_til_size 1000 --n_evals 10 --eval_batch_size 10
```

You can then view the result in [summaries folder](summaries/). If you are using VS code, you can simply click on the markdown file and then in upper right corner click on
`Open preview to the side`.