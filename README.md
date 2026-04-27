# Vulnerability and Resilience of São Paulo's Public Transit Network: A Topological Analysis Based on Graph Theory

<p align="center">
  <img src= "https://img.shields.io/badge/status-in%20progress-yellow" alt="Status do Projeto" />
  <img src="https://img.shields.io/github/last-commit/cintia-shinoda/tcc-lab" alt="GitHub Last Commit" />
  <img src="https://img.shields.io/github/forks/cintia-shinoda/tcc-lab" alt="GitHub Forks" />
  <img src="https://img.shields.io/github/stars/cintia-shinoda/tcc-lab" alt="GitHub Stars" />
</p>

<br>

This repository contains analysis and tests conducted to explore and validate the hypotheses and results presented to the Undergraduate's Final Course Project (TCC): **“VULNERABILITY AND RESILIENCE OF THE SÃO PAULO PUBLIC TRANSIT NETWORK: A TOPOLOGICAL ANALYSIS BASED ON GRAPH THEORY”** ("Vulnerabilidade E Resiliência da Rede de Transporte Público de São Paulo: Uma Análise Topológica Baseada em Teoria dos Grafos"), a requirement for the Bachelor's Degree in Data Science at UNIVESP (Virtual University of the State of São Paulo).

---



## Repository Structure

```bash
tcc-lab/
├── data/
│   ├── raw/
│   │   ├── dryad/
│   │   ├── gtfs/
│   │   └── ibge/
│   │
│   └── processed/
│       └── metricas_centralidade.csv
│
├── docs/
│   ├── initial-bibliography/
│   │   ├── papers/
│   │   ├── reading-outlines/
│   │   └── initial-bibliography.ipynb
│
├── images/
│   └── GTFS-SPTrans-Tables.png
│
├── notebooks/
│   ├── exploratory/
│   │   ├── 00_eda-dryad.ipynb
│   │   ├── 01_research-gtfs.ipynb
│   │   ├── 02_test-OSMnx.ipynb
│   │   ├── 03_model-classification-hugging-face.ipynb
│   │   └── sp_transit_classifier.joblib
│   ├── 01_eda_gtfs.ipynb
│   ├── 02_grafo.ipynb
│   ├── 03_vulnerabilidade.ipynb
│   ├── 04_resiliencia.ipynb
│   └── 05_modelo-classificacao.ipynb
│
├── outputs/
│   ├── headway_por_hora.png
│   ├── headway-por-horario.png
│   ├── hist_graus_antes.png
│   ├── mapa_antes_depois_integracao.png
│   ├── mapa_centralidades.png
│   ├── mapa_fluxo_rede.png
│   ├── mapa_interativo_centralidade.html
│   ├── mapa_paradas_modal_sp.png
│   ├── mapa-headway-por-horario.png
│   └── mapas_regionais_integracao.png
│
├── .gitignore
├── config.json
├── README.md
└── requirements.txt
```

---

## Datasets

- Dryad: https://datadryad.org/dataset/doi:10.15146/R3VM28
- GTFS SPTrans: https://www.sptrans.com.br/desenvolvedores/
- IBGE: https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2024/

<!-- ERM-GTFS: <iframe width="560" height="315" src='https://dbdiagram.io/e/69ec0665c6a36f9c1b76016a/69ec0684c6a36f9c1b760206'> </iframe> -->

---

## Stack
- Python 3.11.x
- Pandas
- Numpy
- Matplotlib
- NetworkX
- Geopandas
- Folium
- OSMnx

---

<!-- ## Notebooks de Exploração

|  | Notebook | Description |
|---|---|---|
| 0 | [Dryad's EDA](https://github.com/cintia-shinoda/tcc-lab/blob/main/notebooks/00_eda-dryad.ipynb) | Exploratory data analysis of a sample of ticketing data from SPTrans |
| 1 | [GTFS-SPTrans' EDA](https://github.com/cintia-shinoda/tcc-lab/blob/main/notebooks/01_eda-gtfs.ipynb) | Exploratory analysis of GTFS from SPTrans |
| 2 | [OSMnx Test](https://github.com/cintia-shinoda/tcc-lab/blob/main/notebooks/02_test-OSMnx.ipynb) | Testing OSMnx for mapping and analyzing the transportation network of São Paulo |
| 3 | [Hugging Face's SPTrans Classifier Model](https://github.com/cintia-shinoda/tcc-lab/blob/main/notebooks/03_hugging-face.ipynb) | Implementation of a classification model for SPTrans data | -->

## Notebooks

| # | Notebook |
|---|---|
| 1 | [Análise Exploratória do GTFS-SPTrans](https://github.com/cintia-shinoda/public-transit-graph-theory/blob/main/notebooks/1_eda_gtfs.ipynb) |
| 2 | [Modelagem do Grafo, Componentes e Medidas de Centralidade](https://github.com/cintia-shinoda/public-transit-graph-theory/blob/main/notebooks/2_grafo.ipynb) |
| 3 | [Análise de Vulnerabilidade](https://github.com/cintia-shinoda/public-transit-graph-theory/blob/main/notebooks/3_vulnerabilidade.ipynb) |
| 4 | [Simulação - Resiliência](https://github.com/cintia-shinoda/public-transit-graph-theory/blob/main/notebooks/4_resiliencia.ipynb) |
| 5 | [Modelagem Preditiva de Criticidade](https://github.com/cintia-shinoda/public-transit-graph-theory/blob/main/notebooks/5_modelo-classificacao.ipynb) |


---

## 

1. Clone repository:
```bash
git clone https://github.com/cintia-shinoda/tcc-lab.git

cd tcc-lab
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run Jupyter Notebook:
```bash
jupyter notebook
```

Open the notebooks in the `notebooks/` directory to explore the analyses.
