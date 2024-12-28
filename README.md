# LinkedIn Bot

Este projeto é um bot automatizado para enviar solicitações de conexão no LinkedIn com base em buscas específicas. Ele utiliza o Selenium para automação do navegador e organização do código em módulos.

## Requisitos

Antes de começar, certifique-se de que você atenda aos seguintes requisitos:

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)
- Google Chrome instalado
- ChromeDriver compatível com a sua versão do Google Chrome (pode ser baixado [aqui](https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br))

## Instalação e Configuração

### Passo 1: Clonar o Repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/linkedin-bot.git
cd linkedin-bot
```

### Passo 2: Criar Ambiente Virtual

Crie e ative um ambiente virtual para isolar as dependências:

```bash
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no macOS/Linux
source venv/bin/activate
```

### Passo 3: Instalar Dependências

Instale as dependências do projeto listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Passo 4: Baixar o ChromeDriver

1. Acesse [ChromeDriver Downloads](https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br).
2. Baixe a versão do ChromeDriver compatível com a sua versão do Google Chrome.
3. Extraia o arquivo baixado e copie o caminho completo do executável `chromedriver`.

### Passo 5: Configurar o Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto e configure as seguintes variáveis:

```env
USER=seu-email@exemplo.com
PASSWORD=sua-senha
```

Substitua `/caminho/completo/para/o/chromedriver`, em config.py pelo caminho completo do seu ChromeDriver, e insira seu e-mail e senha do LinkedIn nas variáveis `USER` e `PASSWORD`.

### Personalização da Busca no LinkedIn
O bot está configurado por padrão para realizar buscas por pessoas interessadas em "Inteligência Artificial". Isso é definido pela variável search_url no arquivo linkedin_bot.py.

Caso deseje alterar o tipo de busca, siga estas instruções:

Acesse manualmente o LinkedIn e realize a busca desejada (ex.: por pessoas em uma área específica ou com interesses diferentes).
Copie a URL da página de resultados da busca.
Substitua a URL padrão no código (search_url) pela nova URL copiada.
Exemplo de URL padrão no código:

```bash
search_url = "https://www.linkedin.com/search/results/people/?keywords=intelig%C3%AAncia%20artificial&origin=SWITCH_SEARCH_VERTICAL&sid=Qvr"
```
Substitua pela URL copiada para personalizar a busca.

## Uso

### Passo 1: Executar o Bot

No terminal, execute o arquivo `main.py`:

```bash
python main.py
```

O bot irá:

1. Fazer login no LinkedIn usando as credenciais fornecidas.
2. Navegar pelos resultados da pesquisa e enviar solicitações de conexão automaticamente.

### Passo 2: Monitorar Logs

Durante a execução, o bot exibirá logs no terminal, indicando o progresso das ações realizadas.

## Estrutura do Projeto

- `linkedin_bot.py`: Contém a lógica principal do bot.
- `config.py`: Gerencia a configuração do WebDriver e credenciais.
- `main.py`: Orquestra a execução do bot.
- `.env`: Arquivo de configuração com credenciais sensíveis (não compartilhado).

## Notas de Uso

1. **Evite Bloqueios:** O LinkedIn possui restrições contra automação. Configure intervalos adequados para evitar ser bloqueado.
2. **Segurança:** Nunca compartilhe suas credenciais em público. O arquivo `.env` deve ser mantido privado.
3. **Atualizações do Chrome:** Certifique-se de manter o ChromeDriver atualizado e compatível com sua versão do Google Chrome.

## Contribuição

Contribuições são bem-vindas! Abra um pull request ou relate problemas na página de issues.


