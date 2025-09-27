# Smart Office - Projeto Acadêmico

## Descrição
Projeto para simulação de sensores IoT em um escritório inteligente (Smart Office).  
Inclui geração de dados, resumo diário e criação automatizada de dossiê em Word.

## Arquivos
- `simulador_smart_office.py` → Gera dados simulados dos sensores.
- `resumo_smart_office.py` → Cria resumo diário a partir do CSV gerado.
- `gerar_dossie.py` → Gera o dossiê Word com riscos, RACI, plano de comunicação e relatórios.

## Como usar
1. Instale as dependências:
```bash
pip install pandas numpy python-docx
