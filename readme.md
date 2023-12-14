# Dashboard de finanças TecnoJR

## Índice

* [Instruções de uso](#instruções-de-uso)
* [Contribuições](#contribuições)
* [Licença](#licença)
* [Autores](#autores)

## Instruções de uso

Para usar o repositório, basta cloná-lo para o seu computador. Você pode usar o seguinte comando para clonar o repositório:

```bash
git clone https://github.com/matheusssilva991/compiladores.git
```

Em seguida, você deve criar um ambiente virtual ou ambiente Anaconda para instalar as bibliotecas necessárias para executar as atividades.

### Criar um ambiente virtual com Python

Para criar um ambiente virtual com Python, você pode usar o seguinte comando:

```bash
python -m venv [nome-do-ambiente]
```

Para ativar o ambiente virtual, você pode usar o seguinte comando:

* Windows

```bash
.\[nome-do-ambiente]\Script\activate
```

* Linux

```bash
source [nome-do-ambiente]/bin/activate
```

Para instalar as bibliotecas usando os arquivos de requisitos, você pode usar o seguinte comando:

```bash
pip install -r requirements.txt
```

* Windows e Linux

Para desativar o ambiente, você pode usar o seguinte comando

```bash
deactivate
```

### Criar um ambiente Anaconda

Para criar um ambiente Anaconda, você pode usar o seguinte comando:

```bash
conda env create -f environment.yml
```

Para ativar o ambiente anaconda, você pode usar o seguinte comando:

```bash
conda activate [nome-do-ambiente]
```

Para desativar o ambiente, você pode usar o seguinte comando

```bash
conda deactivate
```

### Rodar o dashboard

Para rodar o dashboard, você pode usar o seguinte comando

```bash
streamlit run ./src/dashboard.py
```

## Contribuições

Se você tiver alguma contribuição para o repositório, fique à vontade para enviar um pull request.

## Licença

Este repositório está licenciado sob a licença MIT.

## Autores

* [Matheus Santos Silva](https://github.com/matheusssilva991)
