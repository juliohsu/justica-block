# justica-block
### Verificar se está com todos os documentos
- Analisar por assunto de Processo
- Órgão julgador: Fazenda Pública da Capital
  - Modelo de correto de processo Apto: 7
  - Não aptos: 6,11,18,19
# justica-block

### Objetivo
Este projeto tem como objetivo auxiliar na análise de processos judiciais, verificando se todos os documentos necessários estão presentes e categorizando os dados extraídos.

### Funcionalidade da Branch `extrat`
A branch `extrat` é responsável por:
- **Extração de dados**: Processar arquivos PDF para extrair texto e imagens relevantes.
- **Categorização**: Classificar os dados extraídos em categorias específicas para facilitar a análise.
- **Preparação para interpretação**: Enviar os dados extraídos e categorizados para um sistema de multiagentes que verifica a ausência de documentos ou informações.

### Fluxo de Trabalho
1. **Entrada**: PDFs contendo informações de processos judiciais.
2. **Processamento**:
   - Extração de texto e imagens.
   - Categorização dos dados.
3. **Saída**: Dados organizados e categorizados prontos para análise por agentes inteligentes.

### Exemplos de Categorias
- **Assunto do Processo**: Identificação do tema principal do processo.
- **Órgão Julgador**: Exemplo: Fazenda Pública da Capital.
- **Status do Processo**:
  - Modelos corretos: 7, 11, 19, 22.
  - Não aptos: 6, 8, 18.

### Tecnologias Utilizadas
- Python para processamento de PDFs.
- Frameworks de IA para categorização e análise.

### Como Executar
1. Certifique-se de que os PDFs estão na pasta de entrada.
2. Execute o script principal da branch `extrat`.
3. Verifique os resultados na pasta de saída.

### Próximos Passos
- Integração com o sistema de multiagentes.
- Melhorias na precisão da categorização.
