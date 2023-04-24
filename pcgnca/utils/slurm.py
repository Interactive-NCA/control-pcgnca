"""
Utility scripts that should help with the preparation of the
slurm file which can then be submitted to the cluster and
run the given experiment on more powerful computer/node
on the cluster.
"""

# --------------------- External libraries imports
import os

# --------------------- Public functions
def get_slurm_file(settings, args):

    # - Save the data into a string
    result = "#!/bin/bash\n\n"

    # - Parse aguments specific for the slurm
    # -- Job name
    result += f"#SBATCH --job-name=PCGNCA-EXPERIMENT-{settings['experiment_id']}\n"
    # -- Output folder (where the print statements go a.k.a. std out)
    result += f"#SBATCH --output={os.path.join(settings['save_path'], 'slurm.out')}\n"
    # -- Number of cores per task
    result += f"#SBATCH --cpus-per-task={settings['n_cores']}\n"
    # -- Max time to run the experiment
    result += f"#SBATCH --time={settings['timeout_after']}\n"
    # -- Which cluster partition to run the code on, e.g. brown
    if settings.get("partition"):
        result += f"#SBATCH --partition={settings['partition']}\n"
    # -- Should someone be informed by email about certain events
    if settings.get("emails"): 
        result += f"#SBATCH --mail-user={settings['emails']}\n"
        result += f"#SBATCH --mail-type=BEGIN,FAIL,END\n"
    # -- Students account
    result += "#SBATCH --account=students\n"
    # -- Any nodes to be excluded?
    if settings.get("exclude_nodes"):
        result += f"#SBATCH --exclude {settings['exclude_nodes']}\n"
 
    # - Show on which node is the code running
    result += '\necho "Running on $(hostname)"\n\n'

    # - Setup the environment
    # -- Activate it
    result += "module load Anaconda3\n"
    result += f"source {settings['bashrc_path']}\n"
    result += f"conda activate {settings['envname']}\n\n"

    # - Install packages if needed
    if settings["install_req"]:
        result += f"conda install pip\n"
        result += f"pip install -r requirements.txt\n\n"

    # - Run the evolution via cli
    result += f"python{settings['python_version']} cli.py " + f"--expid {settings['experiment_id']} "
    for k, v in args.items():
        # -- Evaluate if add based on key
        if k == "gen_slurm_script":
            continue

        # -- Evaluate if add based on value
        if v is not None:
            if type(v) is int:
                result += f"--{k} {v} "
            elif type(v) is str:
                result += f'--{k} "{v}" '
            elif type(v) is bool and v:
                result += f"--{k} "

    # - Save the file to the root
    with open("slurm.job", "w") as f:
        f.write(result)
