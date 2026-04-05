# Testes para o TCC

<p align="center">
  <img src= "https://img.shields.io/badge/status-in%20progress-yellow" alt="Status do Projeto" />
  <img src="https://img.shields.io/github/last-commit/cintia-shinoda/tcc-lab" alt="GitHub Last Commit" />
  <img src="https://img.shields.io/github/forks/cintia-shinoda/tcc-lab" alt="GitHub Forks" />
  <img src="https://img.shields.io/github/stars/cintia-shinoda/tcc-lab" alt="GitHub Stars" />
</p>

<br>

Este repositório contém os testes realizados para o Trabalho de Conclusão de Curso (TCC) **"VULNERABILIDADE E RESILIÊNCIA DA REDE DE TRANSPORTE PÚBLICO DE SÃO PAULO: UMA ANÁLISE TOPOLÓGICA BASEADA EM TEORIA DOS GRAFOS"** requerimento do curso Bacharelado em Ciência de Dados na UNIVESP (Universidade Virtual do Estado de São Paulo).

 Os testes foram conduzidos para exploração e validar as hipóteses e os resultados apresentados no trabalho.



 <!-- "Este trabalho propõe uma abordagem interdisciplinar fundamentada na Inteligência Urbana para enfrentar os desafios críticos de mobilidade na Região Metropolitana de São Paulo, utilizando o "rastro digital" gerado pelos sistemas de transporte para transformar a gestão reativa em uma governança preditiva.
Descrição do Problema
O problema central reside na ineficiência sistêmica das megacidades, onde o transporte público opera sob constante pressão de fluxos massivos e vulnerabilidades a interrupções. Tradicionalmente, as análises de transporte em São Paulo são feitas de forma desacoplada — tratando ônibus, metrô e trens como redes independentes —, o que resulta na perda de propriedades fundamentais sobre a conectividade global e sobre como falhas em uma sub-rede impactam todo o ecossistema urbano. Além disso, a saturação do sistema viário impõe altos custos econômicos e ambientais, com prejuízos bilionários relacionados ao tempo perdido e às emissões de gases de efeito estufa.
Objetivos do Trabalho
O objetivo geral é investigar o sistema de transporte público de São Paulo de forma acoplada, realizando uma análise sistêmica de seus fluxos e de sua resiliência através de métricas de redes complexas." -->

---

## Estrutura

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
│   ├── bibliografia-inicial/
│   │   ├── artigos/
│   │   ├── fichas-de-leitura/
│   │   └── bibliografia-inicial.ipynb
│   │
│   ├── reunioes/
│   │
│   ├── 0-tema.md                  # Fernando Miguel Escribano Martinez
│   └── 1-fontes-de-dados.pdf      # Thiago Akira Ferreira
│
├── images/
│   ├── GTFS-SPTrans-Tabela.jpg  
│   └── MER-GTFS-SPTrans.png       # Willy Paulino de Oliveira Gomes
│
├── notebooks/
│   ├── 00_eda-dryad.ipynb
│   ├── 01_eda-gtfs.ipynb
│   ├── 02_teste-OSMnx.ipynb
│   ├── 03_hugging-face.ipynb
│   └── sp_transit_classifier.joblib
│
├── outputs/
│   ├── headway_por_hora.png
│   ├── headway-por-horario.png
│   ├── mapa_centralidades.png
│   ├── mapa_fluxo_rede.png
│   ├── mapa_interativo_centralidade.html
│   ├── mapa_paradas_modal_sp.png
│   └── mapa-headway-por-horario.png
│
├── .gitignore
├── config.json
├── README.md
└── requirements.txt
```

## Dados
- Dryad: https://datadryad.org/dataset/doi:10.15146/R3VM28
- GTFS SPTrans: https://www.sptrans.com.br/desenvolvedores/
- IBGE: https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2024/


## Stack
- Python 3.11.x
- Pandas
- Geopandas
- NetworkX


## Notebooks

|  | Notebook | Descrição |
|---|---|---|
| 0 | [Análise Exploratória Dryad](https://github.com/cintia-shinoda/tcc-lab/blob/main/notebooks/00_eda-dryad.ipynb) | Análise exploratória dos dados de bilhetagem da SPTrans |
| 1 | [Análise Exploratória do GTFS-SPTrans](https://github.com/cintia-shinoda/tcc-lab/blob/main/notebooks/01_eda-gtfs.ipynb) | Análise exploratória dos dados GTFS da SPTrans |
</a> |


----

<!-- Majdoub, Bassam (2018). Bilhetagem de Transporte Público - São Paulo [Dataset]. Dryad. Disponível em: https://doi.org/10.15146/R3VM28. Acesso em: 10 mar. 2026. -->

<!-- SPTrans. GTFS . Disponível em https://www.sptrans.com.br/desenvolvedores/perfil-desenvolvedor/. Acesso em 10 mar. 2026. -->

<!-- IBGE. Malhas Municipais. Disponível em: https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2024/. Acesso em: 10 mar. 2026. -->