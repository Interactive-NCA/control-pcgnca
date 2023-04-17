"""
This module includes helper functions that
generate commands for transfering experiment folders
from server to local and vice versa.
"""

"""
from server to local
scp -r lukr@hpc.itu.dk:../data_shares/interactive_nca/control-pcgnca/pcgnca/experiments/localcopy .

from local to server
scp -r /path/to/file username@a:/path/to/destination
"""

import os
import shutil

def transfer_exp_folder(from_server, save_path, transfer_path, username_and_domain, target_path, expid, exclude=None):

    # - Store the resulting command as string
    result = "scp -r "

    # - Prepare the folder for transfer 
    # -- Get the path to experiment and where to copy it
    exp_name = f"ExperimentId-{expid}"
    exp_path = os.path.join(save_path, exp_name)
    copy_to = os.path.join(transfer_path, exp_name)

    # -- Copy the experiment there
    if os.path.exists(copy_to):
        shutil.rmtree(copy_to)
    shutil.copytree(exp_path, copy_to)

    # -- Remove files/folders as specified in the copied version
    if exclude is not None:
        to_remove = exclude.split(",")
        for item in to_remove:
            item_path = os.path.join(copy_to, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            else:
                shutil.rmtree(item_path)

    # - Come up with the command
    if from_server:
        result +=  f"{username_and_domain}:/{copy_to} {target_path}"
    else:
        result += f"{copy_to} {username_and_domain}:/{target_path}"

    # - Show the result 
    print(result)
