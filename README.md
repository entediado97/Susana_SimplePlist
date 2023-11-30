# Susana 

Bem-vindo ao Susana - Simple Plist, uma ferramenta ágil  projetada para transformar o modo como você lida com arquivos `.plist` em projetos de pentest mobile iOS. Este script simplifica a busca e análise de arquivos `.plist`, convertendo-os em `.xml` para facilitar a pesquisa na fase de reconhecimento.

## 🌟 Características

- **Busca Automatizada**: Localiza e processa todos os arquivos `.plist` em um diretório especificado.
- **Conversão Intuitiva para XML**: Transforma `.plist` em `.xml` para análises mais aprofundadas.
- **Barra de Progresso Interativa**: Acompanhe o progresso da conversão em tempo real.
- **Pesquisa Otimizada**: Melhora significativamente a eficiência na busca por informações específicas.

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado em seu ambiente (Python 3.x recomendado).

## 🚀 Instalação e Configuração

Clone o repositório do projeto:

```bash
git clone https://github.com/bhonori/Susana_SimplePlist.git
cd caminho-para-SimplePlist-Susana
```

Não há dependências externas necessárias para rodar o script.

## 🛠️ Como Usar

Para iniciar o script:

```bash
python Susana_SimplePlist.py
```

Insira os caminhos solicitados para os diretórios de origem e destino. O script iniciará o processamento, mostrado por uma barra de progresso.

### 🔍 Sugestões Avançadas de Uso com Grep

Após a conversão, você pode utilizar o `grep` para realizar buscas poderosas. Aqui estão algumas sugestões:

1. **Buscar por uma String Específica**:
   ```bash
   grep -rin 'string_especifica' CAMINHO/Info-plist
   ```
   Use isso para encontrar ocorrências exatas de uma string.

2. **Ignorar Diferenças entre Maiúsculas e Minúsculas**:
   ```bash
   grep -ri 'stringComMaiúsculas' CAMINHO/Info-plist
   ```
   Isso é útil quando a capitalização da string alvo é desconhecida.

3. **Procurar por Múltiplas Strings**:
   ```bash
   grep -E 'string1|string2' CAMINHO/Info-plist
   ```
   Use para pesquisar várias strings diferentes ao mesmo tempo.

4. **Listar Apenas os Nomes dos Arquivos com Correspondências**:
   ```bash
   grep -rl 'stringParaBuscar' CAMINHO/Info-plist
   ```
   Isso retorna apenas os nomes dos arquivos que contêm a string.

5. **Contar o Número de Correspondências**:
   ```bash
   grep -rc 'stringParaContar' CAMINHO/Info-plist
   ```
   Útil para saber quantas vezes uma string específica aparece.

## 🤝 Contribuições

Todas as contribuições são bem-vindas! Se você tem ideias para melhorar a ferramenta, sinta-se à vontade para criar um fork e enviar suas sugestões através de pull requests.

## 📄 Licença

Este projeto é distribuído sob a Licença MIT. Veja `LICENSE.md` para mais informações.

## ✉️ Contato

Para perguntas e sugestões, entre em contato por [aqui.](https://www.instagram.com/bhonori/)

---
