# Testes para o TCC


Este repositório contém os testes realizados para o Trabalho de Conclusão de Curso (TCC) **"INTELIGÊNCIA URBANA E MOBILIDADE: ANÁLISE SISTÊMICA DE FLUXOS E RESILIÊNCIA EM REDES DE TRANSPORTE PÚBLICO ATRAVÉS DA CIÊNCIA DE DADOS E TEORIA DOS GRAFOS"** requerimento do curso Bacharelado em Ciência de Dados na UNIVESP (Universidade Virtual do Estado de São Paulo).

 Os testes foram conduzidos para validar as hipóteses e os resultados apresentados no trabalho.



 <!-- "Este trabalho propõe uma abordagem interdisciplinar fundamentada na Inteligência Urbana para enfrentar os desafios críticos de mobilidade na Região Metropolitana de São Paulo, utilizando o "rastro digital" gerado pelos sistemas de transporte para transformar a gestão reativa em uma governança preditiva.
Descrição do Problema
O problema central reside na ineficiência sistêmica das megacidades, onde o transporte público opera sob constante pressão de fluxos massivos e vulnerabilidades a interrupções. Tradicionalmente, as análises de transporte em São Paulo são feitas de forma desacoplada — tratando ônibus, metrô e trens como redes independentes —, o que resulta na perda de propriedades fundamentais sobre a conectividade global e sobre como falhas em uma sub-rede impactam todo o ecossistema urbano. Além disso, a saturação do sistema viário impõe altos custos econômicos e ambientais, com prejuízos bilionários relacionados ao tempo perdido e às emissões de gases de efeito estufa.
Objetivos do Trabalho
O objetivo geral é investigar o sistema de transporte público de São Paulo de forma acoplada, realizando uma análise sistêmica de seus fluxos e de sua resiliência através de métricas de redes complexas." -->

## Estrutura

```bash
├── data/
│   ├── raw/
│   │   ├── dryad/
│   │   ├── gtfs/
│   │   └── ibge/
│   │
│   └── processed/
│
├── docs/
│   ├── fontes-de-dados.pdf      # Thiago Akira Ferreira
│   └── tema.md                  # Fernando Miguel Escribano Martinez
│
├── images/
│   └── MER-GTFS-SPTrans.png     # Willy Paulino de Oliveira Gomes
│
├── notebooks/
│   ├── 00-exploracao-dryad.ipynb
│   └── 01_exploracao-gtfs.ipynb
│
├── outputs/
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Dados
- Dryad: https://datadryad.org/dataset/doi:10.15146/R3VM28
- GTFS SPTrans: https://www.sptrans.com.br/desenvolvedores/
- IBGE: https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2024/


<!-- ## Stack -->



## Notebooks

|  | Notebook | Descrição |
|---|---|---|
| 0 | [Análise Exploratória Dryad](https://github.com/cintia-shinoda/tcc-lab/blob/main/notebooks/00-exploracao-dryad.ipynb) | Análise exploratória dos dados de bilhetagem da SPTrans |
| 1 | [Análise Exploratória do GTFS-SPTrans](https://github.com/cintia-shinoda/tcc-lab/blob/main/notebooks/01_exploracao-gtfs.ipynb) | Análise exploratória dos dados GTFS da SPTrans |
</a> |


----

<!-- Majdoub, Bassam (2018). Bilhetagem de Transporte Público - São Paulo [Dataset]. Dryad. Disponível em: https://doi.org/10.15146/R3VM28. Acesso em: 10 mar. 2026. -->

<!-- SPTrans. GTFS . Disponível em https://www.sptrans.com.br/desenvolvedores/perfil-desenvolvedor/. Acesso em 10 mar. 2026. -->

<!-- IBGE. Malhas Municipais. Disponível em: https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2024/. Acesso em: 10 mar. 2026. -->