# 🏢 Smart Office - Projeto Acadêmico

## 📄 Descrição
Projeto acadêmico para simulação de sensores IoT em um escritório inteligente (Smart Office).  
O projeto permite:

- 🟢 Simulação de dados de sensores (temperatura, luminosidade e ocupação).  
- 📊 Criação de resumos diários das salas.  
- 📝 Geração automática do dossiê em Word com análise de riscos, matriz RACI, plano de comunicação e relatórios de status.

Ideal para estudos de **gestão de projetos**, **IoT** e **análise de dados simulados**.

---

## 📁 Estrutura de Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `simulador_smart_office.py` | Gera os dados simulados (`smart_office_data.csv`) para 7 dias, com intervalos de 15 minutos. |
| `resumo_smart_office.py` | Processa o CSV e gera `smart_office_resumo.csv` com média diária de temperatura, luminosidade e pico de ocupação. |
| `gerar_dossie.py` | Cria automaticamente o documento Word `Dossie_SmartOffice_Beatriz.docx`. |
| `smart_office_data.csv` | CSV com dados simulados (opcional de subir no GitHub se for grande). |
| `smart_office_resumo.csv` | CSV com resumo diário (opcional). |
| `README.md` | Este arquivo, explicando o projeto e instruções de uso. |

---

## ⚙️ Como rodar o projeto localmente

1. **Clonar o repositório**
2. localhost:8000/index.html
```bash
git clone https://github.com/SEU_USUARIO/smart_office_project.git
python -m http.server
cd smart_office_project
pip install pandas numpy python-docx
python simulador_smart_office.py
python resumo_smart_office.py
python gerar_dossie.py

