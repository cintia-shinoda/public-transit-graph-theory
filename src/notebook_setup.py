
import pickle
from pathlib import Path
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

REPO_ROOT = Path.cwd().parent
DATA_RAW = REPO_ROOT / 'data' / 'raw' / 'gtfs'
DATA_PROCESSED = REPO_ROOT / 'data' / 'processed'

def carregar_gtfs():
    """Carrega DataFrames do GTFS bruto."""
    return {
        'stop_times': pd.read_csv(DATA_RAW / 'stop_times.txt'),
        'trips': pd.read_csv(DATA_RAW / 'trips.txt'),
        'routes': pd.read_csv(DATA_RAW / 'routes.txt'),
        'stops': pd.read_csv(DATA_RAW / 'stops.txt'),
    }

def carregar_artefatos():
    """Carrega artefatos processados."""
    with open(DATA_PROCESSED / 'grafo_principal.gpickle', 'rb') as f:
        G_principal = pickle.load(f)
    stops_com_modal = pd.read_parquet(DATA_PROCESSED / 'stops_com_modal.parquet')
    return G_principal, stops_com_modal