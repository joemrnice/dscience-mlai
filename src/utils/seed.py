import random
import numpy as np 
import torch
import os

SEED = 42

def set_global_seed(seed: int = SEED) -> None:
    """Ensure reproducible results across all libraries."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
    except ImportError:
        pass