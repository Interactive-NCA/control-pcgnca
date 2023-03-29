# control-pcgnca
Procedural Content Generation via Neural Cellular Automata.


## Guide
### Training
Example command:

```
python3 cli.py --train --expid 3 --n_cores 8 --n_generations 50 --save_freq 5
```

### Summarising evaluation
Before summarising given experiments, make sure you evaluted each of them so you are looking at the most recent data!

```
python3 cli.py --summarise "1,2,3"
```