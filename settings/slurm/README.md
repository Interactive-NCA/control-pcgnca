Explain what kinda settings you can put here.

Example command for:

**Training**

```
python3 cli.py --gen-slurm-script --train --n_generations 3000 --save_freq 100 --n_cores 32 --timeout_after "08:00:00"
```


## Create new conda env

The cli assummes that you have actually created the env and installed all the packages. Here is a little helper script with that: 

```
conda create --name pcgnca-v2

module load Anaconda3
source /home/luci/.bashrc
source activate pcgnca-v2

conda install pip
pip install -r requirements.txt
```