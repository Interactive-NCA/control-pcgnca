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

You can then checkout the results in the zelda fixed tiles folder where each type of fixed tiles also has a corresponding `gif` showcasing ten percent of the fixed tiles archive sampled randomly. 
Below, you can see example of archive for fixed `Walls`, `Triples` and `Mixed`.

| Walls            |   Triples        |   Mixed          |
|:----------------:|:----------------:|:----------------:|
| ![](assets/readme/easy_1000.gif) | ![](assets/readme/all_special_random_1000.gif) | ![](assets/readme/mixed_1000.gif)
