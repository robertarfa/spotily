# Projeto - Spotify

    Nesse projeto iremos descobrir insights sobre características sonoras que tornam músicas populares (dançabilidade, energia, etc.) e descobrir artistas emergentes com base em métricas de popularidade.

## Passo a Passo para Configurar a Autenticação

    1. Criar uma Aplicação no Spotify Developer
      Acesse Spotify for Developers.
      Clique em Dashboard (no canto superior direito) e faça login com sua conta Spotify.
      No painel, clique em Create an App:
      Nome: Escolha um nome para sua aplicação (ex.: "Análise Musical").
      Descrição: Insira algo como "Projeto para explorar dados via API do Spotify".
      Após criar a aplicação, você verá o Client ID e o Client Secret:
      Copie esses valores para usarmos no código.

      2. Configurar o Ambiente de Desenvolvimento

      Instale os pacotes:

        poetry add pandas numpy matplotlib seaborn plotly streamlit spotipy
        poetry add pytest black flake8 --group dev

      3. Criar as pastas e subpastas

      mkdir -p projeto-spotify/{data/{raw,processed},notebooks,src/{data,features,models,visualization,dashboard},tests}

      4. Boas Práticas
      Linting e formatação: Use o black e flake8 para garantir um código limpo.

      poetry run black src/
      poetry run flake8 src/
