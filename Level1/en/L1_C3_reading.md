# L1.C3 Root-Cause & Data Capture

## Navigation
**Course**: [[../../index|Course Home]] > [[../../Level1_index|Level 1]] > Chapter 3  
**Previous**: [[L1_C2_reading|Chapter 2: AS-IS Mapping & Bottleneck Hunting]]  
**Next**: [[L1_C4_reading|Chapter 4: TO-BE Process Design]]

---

## Learning Objectives
- Master systematic root cause analysis techniques beyond surface symptoms
- Design data collection strategies that capture reliable process performance evidence
- Apply statistical tools to identify patterns and validate improvement hypotheses
- Use fishbone diagrams, 5 Whys, and fault tree analysis for complex problem solving
- Build data-driven business cases that support process improvement investments

## Real-World Scenario

After mapping the hospital discharge process and identifying pharmacy reviews as the primary bottleneck, Lisa faced a crucial question: Why was the pharmacy taking so long? The surface answer seemed obvious—they were understaffed during peak hours. But Lisa had learned that obvious answers often miss the real problem.

Her initial investigation revealed that Mountain View's pharmacy had 2 pharmacists during day shift, same as comparable hospitals. But when she dug into the data, patterns emerged that challenged assumptions.

**Pattern 1: Time Variance by Medication Type**
Simple medications (5 or fewer drugs): 15-30 minutes average
Complex medications (6+ drugs, interactions): 45-180 minutes average
Discharge medications requiring new prescriptions: 2-4 hours average

**Pattern 2: Performance by Day of Week**
Monday-Wednesday: 75-minute average pharmacy review
Thursday-Friday: 120-minute average pharmacy review  
Weekend: 45-minute average pharmacy review

**Pattern 3: Performance by Pharmacist**
Dr. Martinez (15 years experience): 60-minute average, 95% accuracy
Dr. Patel (3 years experience): 105-minute average, 88% accuracy
Temporary staff: 150-minute average, 78% accuracy

The real breakthrough came when Lisa examined electronic health records and discovered that 40% of discharge medication orders contained errors or missing information requiring pharmacist clarification with physicians. On Thursdays and Fridays, physician response time to pharmacist questions averaged 3.2 hours because doctors were in surgery or had heavy clinic schedules.

The root cause wasn't pharmacy staffing—it was incomplete discharge orders creating rework loops, compounded by physician availability patterns and varying pharmacist experience levels. This discovery changed everything about the improvement strategy.

Lisa realized that surface-level solutions like "hire more pharmacists" would fail because they didn't address the real problem: information quality and communication timing. The hospital needed better discharge order protocols, physician communication systems, and pharmacist training—not just more staff.

## Core Theory

### Understanding Root Cause vs. Symptoms

Most process problems have multiple contributing factors, making systematic root cause analysis essential for effective solutions.

**Symptoms**: Observable effects of underlying problems
- Long cycle times
- High error rates  
- Customer complaints
- Resource bottlenecks
- Cost overruns

**Contributing Factors**: Elements that influence problem severity
- Staffing levels
- Training quality
- System performance
- Communication patterns
- Workload variation

**Root Causes**: Fundamental systemic issues that create problems
- Process design flaws
- Information architecture gaps
- Organizational structure conflicts
- Cultural and behavioral patterns
- Technology integration failures

### The 5 Whys Technique

Systematic questioning to drill down from symptoms to root causes:

**Problem**: Pharmacy reviews take too long

**Why #1**: Why do pharmacy reviews take too long?
*Because complex cases require extensive research and physician consultation*

**Why #2**: Why do complex cases require extensive research?
*Because discharge orders often lack complete medication history and interaction documentation*

**Why #3**: Why do discharge orders lack complete information?
*Because physicians don't have integrated access to outpatient pharmacy records during order writing*

**Why #4**: Why don't physicians have integrated access?
*Because hospital EHR system doesn't interface with community pharmacy databases*

**Why #5**: Why doesn't the EHR system interface with community pharmacies?
*Because IT budget prioritized regulatory compliance over care coordination features*

**Root Cause**: Technology investment priorities that don't support care coordination workflow

### Fishbone (Ishikawa) Diagram Analysis

Systematic examination of potential cause categories:

**People Causes**:
- Skill gaps in complex medication management
- Experience level variations between pharmacists
- Physician training on complete discharge order writing
- Communication preferences and timing mismatches

**Process Causes**:
- Discharge order workflow design flaws
- Lack of standardized medication reconciliation procedures
- Missing quality checkpoints before pharmacy review
- No escalation procedures for urgent cases

**Technology Causes**:
- EHR system limitations in medication history access
- Lack of integration with outpatient pharmacy databases
- No automated drug interaction checking at order entry
- Communication tools inadequate for physician-pharmacist consultation

**Environment Causes**:
- Pharmacy location isolated from physician work areas
- Peak hour demand patterns overwhelming capacity
- Regulatory requirements creating documentation burden
- Organizational culture prioritizing speed over accuracy

**Materials Causes**:
- Incomplete patient medication histories at admission
- Missing documentation from referring physicians
- Outdated drug reference databases
- Lack of patient medication lists from home

### Statistical Tools for Process Analysis

**Control Charts**: Track performance over time to distinguish normal variation from special causes

```
Pharmacy Review Time Control Chart:
Upper Control Limit: 180 minutes
Average: 90 minutes  
Lower Control Limit: 0 minutes

Points above UCL indicate special causes requiring investigation
Points below LCL indicate exceptional performance worth studying
```

**Pareto Analysis**: Identify the vital few causes contributing to most problems

**80/20 Analysis of Pharmacy Delays:**
- Incomplete medication orders: 35% of delays
- Physician consultation wait: 28% of delays  
- Complex drug interactions: 18% of delays
- Missing patient history: 12% of delays
- System technical issues: 7% of delays

**Histogram Analysis**: Understand distribution patterns and identify outliers

**Correlation Analysis**: Examine relationships between variables
- Physician experience vs. discharge order completeness: r = 0.67
- Day of week vs. physician response time: r = 0.44
- Patient complexity vs. pharmacy review time: r = 0.58

### Data Collection Strategy Design

**Quantitative Data Sources**:

**System Data**: Electronic records providing objective measurements
- Transaction timestamps for each process step
- Error rates and rework frequencies
- Resource utilization and capacity data
- Quality metrics and compliance scores

**Observational Data**: Direct measurement of process performance
- Time and motion studies with representative sampling
- Error tracking and categorization
- Communication frequency and response times
- Workaround documentation and impact measurement

**Survey Data**: Stakeholder perspectives and satisfaction measurements
- Employee satisfaction with process tools and procedures
- Customer experience ratings and feedback
- Perception surveys about process effectiveness
- Training needs assessments and skill gap identification

**Qualitative Data Sources**:

**Interview Data**: Deep insights into process dynamics
- Structured interviews with process participants
- Focus groups exploring specific problem areas
- Expert consultations on technical issues
- Historical perspective interviews with long-term employees

**Observational Notes**: Context and behavior patterns
- Informal communication patterns and relationships
- Cultural factors affecting process adherence
- Environmental conditions impacting performance
- Emotional responses to process problems and changes

### Sampling Methodology for Process Data

**Representative Sampling**: Ensure data reflects true process performance

**Time-Based Sampling**:
- Capture different days of week, months, seasons
- Include both peak and off-peak periods
- Sample different shift patterns and staffing levels
- Account for cyclical business patterns

**Instance-Based Sampling**:
- Include range of complexity levels (simple, moderate, complex)
- Sample different customer types or product categories
- Ensure geographic or departmental representation
- Include both successful and failed process instances

**Statistical Power Considerations**:
- Calculate minimum sample size for reliable conclusions
- Account for expected variation in process performance
- Consider confidence levels required for decision making
- Plan for data collection logistics and resource constraints

### Hypothesis Testing for Process Improvement

**Forming Testable Hypotheses**:

**Null Hypothesis**: Process performance is not affected by proposed change
**Alternative Hypothesis**: Proposed change will improve process performance by specific amount

**Example Hypothesis Testing**:
H0: Standardized discharge order templates will not reduce pharmacy review time
H1: Standardized templates will reduce average pharmacy review time by >20%

**Data Collection for Testing**:
- Baseline performance measurement (before intervention)
- Controlled pilot implementation with treatment and control groups
- Post-implementation measurement with statistical comparison
- Long-term monitoring to ensure sustained improvement

### Building Data-Driven Business Cases

**Quantifying Current State Costs**:

**Direct Costs**: Measurable resource consumption
- Labor hours for rework and delays
- Technology costs for inefficient systems
- Material costs for waste and errors
- Compliance costs for regulatory issues

**Indirect Costs**: Hidden impacts on organization
- Customer satisfaction and retention effects
- Employee turnover and recruitment costs
- Opportunity costs of capacity constraints
- Brand reputation and competitive impacts

**Solution Cost-Benefit Analysis**:

**Implementation Costs**:
- Technology investments and integration
- Training and change management
- Process redesign and documentation
- Temporary productivity losses during transition

**Expected Benefits**:
- Cycle time reduction value (customer satisfaction, capacity)
- Error reduction value (rework costs, quality improvements)
- Resource efficiency gains (labor, technology, space)
- Strategic benefits (competitive advantage, growth enablement)

## Tool Demonstration

### Root Cause Analysis: Hospital Pharmacy Example

**Step 1: Problem Definition**
"Pharmacy medication reviews for patient discharges average 90 minutes, causing 4.2-hour total discharge delays and customer dissatisfaction"

**Step 2: Data Collection and Pattern Analysis**

**Performance by Complexity**:
- Simple (≤5 medications): 30 min average, σ = 8 min
- Moderate (6-10 medications): 75 min average, σ = 22 min  
- Complex (>10 medications): 165 min average, σ = 45 min

**Performance by Information Quality**:
- Complete orders: 45 min average
- Missing information: 125 min average (+78% increase)
- Conflicting information: 180 min average (+300% increase)

**Communication Delays**:
- Physician immediately available: 15 min consultation
- Physician in clinic/surgery: 185 min average response
- Weekend/evening physician coverage: 45 min average response

**Step 3: Fishbone Analysis**

```
LONG PHARMACY REVIEW TIMES
        |
People  |-- Pharmacist experience variation
        |-- Physician availability patterns  
        |-- Communication preferences mismatch
        |
Process |-- Incomplete discharge order workflow
        |-- No quality checkpoints before pharmacy
        |-- Missing escalation procedures
        |-- Lack of standardized templates
        |
Technology |-- EHR system medication history gaps
           |-- No community pharmacy integration
           |-- Limited drug interaction checking
           |-- Poor physician-pharmacist communication tools
           |
Environment |-- Peak hour capacity constraints
            |-- Physical separation of departments
            |-- Regulatory documentation requirements
```

**Step 4: Root Cause Prioritization**

**Primary Root Cause (35% of problem)**:
Discharge order information quality—incomplete medication histories and missing interaction documentation require extensive research and physician consultation

**Secondary Root Cause (28% of problem)**:
Physician availability patterns—scheduled surgery and clinic times create communication delays when pharmacist questions arise

**Tertiary Root Cause (18% of problem)**:
Technology integration gaps—lack of community pharmacy database access requires manual verification of patient medication histories

**Step 5: Hypothesis Development**

**Hypothesis 1**: Implementing standardized discharge order templates with mandatory medication history fields will reduce pharmacy review time by 25%

**Test Design**: Pilot templates with 50% of discharges for 4 weeks, measure review times vs. control group

**Hypothesis 2**: Establishing dedicated physician coverage for pharmacy consultations during peak hours will reduce consultation delays by 60%

**Test Design**: Assign one physician for pharmacy questions 2-6 PM for 3 weeks, measure response times vs. baseline

### Data Collection Plan: Process Performance Analysis

**Objective**: Quantify baseline performance and identify improvement opportunities

**Data Sources and Collection Methods**:

**Electronic Health Record Data**:
- Discharge order timestamps (order written → pharmacy received)
- Pharmacy review completion times (pharmacy received → approved)
- Physician consultation request and response times
- Medication complexity scores (number of drugs, interactions)
- Sample size: All discharges over 8-week period (n≈800)

**Direct Observation Data**:
- Time studies of pharmacy workflow for different complexity levels
- Documentation of communication methods and timing
- Identification of interruptions and multitasking impacts
- Sample size: 40 pharmacy reviews across complexity range

**Survey Data**:
- Pharmacist perception of information quality and communication effectiveness
- Physician awareness of discharge timing impacts and communication preferences
- Patient satisfaction with discharge timing and medication education
- Response target: 80% of relevant staff (n≈25)

**Interview Data**:
- Structured interviews with experienced pharmacists about process variations
- Focus group with physicians about discharge order workflow challenges
- Patient interviews about medication understanding and satisfaction
- Target: 6 pharmacists, 8 physicians, 10 patients

**Statistical Analysis Plan**:

**Descriptive Statistics**:
- Central tendency and variation for all time measurements
- Distribution analysis to identify outliers and patterns
- Correlation analysis between variables (complexity, experience, timing)

**Inferential Statistics**:
- Control charts to distinguish special vs. common cause variation
- Regression analysis to quantify relationships between factors
- Hypothesis testing for proposed improvement solutions

**Reporting Framework**:
- Daily dashboard showing current performance vs. targets
- Weekly trend analysis identifying patterns and special causes
- Monthly business case updates with cost-benefit analysis
- Quarterly strategic review of improvement initiative progress

## Mini Project

**Root Cause Analysis and Data Collection Design**

Conduct systematic root cause analysis for a real process problem, design data collection strategy, and build quantitative business case for improvement.

**Project Scope:**
Choose a process problem where you can access performance data:
- **Workplace process**: High error rates, long cycle times, resource constraints
- **Service process**: Customer complaints, quality issues, efficiency problems
- **Educational process**: Student performance gaps, administrative inefficiencies
- **Personal process**: Recurring problems with measurable impacts

**Requirements:**
- Problem must have **measurable impacts** (time, cost, quality, satisfaction)
- Access to **historical data** or ability to collect new data
- **Multiple potential causes** requiring systematic analysis
- **Stakeholder availability** for interviews and validation

**Deliverables:**

### 1. Problem Definition and Impact Analysis (400 words)

**Problem Statement** (150 words):
- Specific, measurable description of current performance gap
- Quantified impact on stakeholders (time, cost, quality, satisfaction)
- Business context explaining why this problem matters
- Scope and boundaries of analysis

**Current State Evidence** (150 words):
- Historical performance data showing problem magnitude
- Trend analysis indicating whether problem is worsening
- Variation analysis showing consistency vs. outlier patterns
- Stakeholder impact documentation with specific examples

**Improvement Opportunity** (100 words):
- Potential benefits of solving the problem
- Estimated value of improvement (time savings, cost reduction, quality improvement)
- Strategic importance beyond immediate metrics
- Urgency and consequences of not addressing the problem

### 2. Systematic Root Cause Analysis (600 words)

**5 Whys Analysis** (200 words):
- Document complete 5 Whys chain from problem statement to root cause
- Explain reasoning for each "why" with supporting evidence
- Identify the fundamental systemic issue that creates the problem
- Validate root cause conclusion with stakeholder feedback

**Fishbone Diagram Analysis** (200 words):
- Create comprehensive fishbone diagram examining all potential cause categories
- People: Skills, training, motivation, communication patterns
- Process: Workflow design, procedures, quality controls, handoffs
- Technology: System capabilities, integration, user interface, reliability
- Environment: Physical space, timing, regulations, organizational culture
- Materials: Information quality, tool availability, resource constraints

**Data-Driven Cause Validation** (200 words):
- Present quantitative evidence supporting primary root causes
- Use statistical analysis (correlations, control charts, Pareto analysis)
- Distinguish between contributing factors and fundamental causes
- Prioritize causes by impact magnitude and improvement feasibility

### 3. Data Collection Strategy Design (500 words)

**Data Requirements Definition** (150 words):
- Specify exactly what data is needed to validate root causes
- Define data quality requirements (accuracy, completeness, timeliness)
- Identify both quantitative metrics and qualitative insights needed
- Establish baseline measurement requirements for improvement tracking

**Collection Methods and Sources** (200 words):
- **System Data**: What electronic records or databases can provide objective measurements?
- **Observational Data**: What direct observation or time studies are needed?
- **Survey Data**: What stakeholder perceptions and experiences must be captured?
- **Interview Data**: What deep insights require structured conversations?

**Sampling and Statistical Plan** (150 words):
- Sample size calculations for reliable conclusions
- Sampling methodology ensuring representative data
- Statistical analysis approaches for hypothesis testing
- Control for confounding variables and bias sources

### 4. Business Case for Improvement (400 words)

**Current State Cost Analysis** (150 words):
- Quantify direct costs of current problem (labor, materials, rework)
- Estimate indirect costs (customer satisfaction, employee turnover, opportunity cost)
- Calculate total annual impact in financial terms
- Include qualitative costs difficult to quantify but important to consider

**Proposed Solution and Investment** (150 words):
- Describe specific improvement approach based on root cause analysis
- Estimate implementation costs (technology, training, process redesign)
- Timeline for implementation and expected results
- Resource requirements and stakeholder commitments needed

**Return on Investment Analysis** (100 words):
- Projected benefits from solving the root cause problem
- Implementation costs vs. expected annual savings
- Payback period and 3-year ROI calculation
- Risk assessment and sensitivity analysis for key assumptions

## Submission Format

**File Name**: `root_cause_analysis_[problem_name].pdf`

**Document Structure**:
1. Executive Summary (1 page)
2. Problem Definition and Impact Analysis (400 words)
3. Root Cause Analysis with Visual Tools (600 words, 1-2 pages)
4. Data Collection Strategy (500 words, 1 page)
5. Business Case for Improvement (400 words, 1 page)
6. Appendix: Data analysis, interview notes, calculations

**Total Length**: 6-8 pages including visuals and supporting data

## Evaluation Criteria

### Excellent (90-100%)
- **Problem Definition**: Clear, measurable problem with compelling business impact
- **Root Cause Analysis**: Systematic analysis using multiple tools with data validation
- **Data Strategy**: Comprehensive collection plan with appropriate statistical rigor
- **Business Case**: Compelling ROI analysis with realistic assumptions and risk assessment

### Proficient (80-89%)
- **Problem Understanding**: Good problem definition with adequate impact documentation
- **Analysis Quality**: Sound root cause analysis with reasonable tool application
- **Data Planning**: Adequate collection strategy with basic statistical considerations
- **Financial Analysis**: Reasonable business case with basic cost-benefit analysis

### Developing (70-79%)
- **Basic Problem Definition**: Adequate problem statement but limited impact analysis
- **Simple Analysis**: Basic root cause analysis with limited depth or validation
- **Limited Data Planning**: Simple collection approach without statistical rigor
- **Weak Business Case**: Basic financial analysis without comprehensive consideration

### Inadequate (Below 70%)
- **Poor Problem Definition**: Unclear problem statement or missing impact analysis
- **Inadequate Analysis**: Superficial analysis missing root causes or using tools incorrectly
- **Missing Data Strategy**: No systematic data collection plan or statistical consideration
- **No Business Case**: Missing or unrealistic financial analysis

## Quiz Placeholder
<QUIZ_LINK will be replaced by generated HTML file>

---

### Portuguese Version

# L1.C3 Análise de Causa Raiz & Captura de Dados

## Objetivos de Aprendizagem
- Dominar técnicas sistemáticas de análise de causa raiz além de sintomas superficiais
- Projetar estratégias de coleta de dados que capturem evidências confiáveis de performance de processos
- Aplicar ferramentas estatísticas para identificar padrões e validar hipóteses de melhoria
- Usar diagramas de fishbone, 5 Whys e análise de árvore de falhas para resolução de problemas complexos
- Construir business cases baseados em dados que apoiem investimentos em melhoria de processos

## Cenário do Mundo Real

Depois de mapear o processo de alta hospitalar e identificar revisões de farmácia como o gargalo primário, Lisa enfrentou uma questão crucial: Por que a farmácia estava demorando tanto? A resposta superficial parecia óbvia—estavam com falta de pessoal durante horários de pico. Mas Lisa havia aprendido que respostas óbvias frequentemente perdem o problema real.

Sua investigação inicial revelou que a farmácia do Mountain View tinha 2 farmacêuticos durante o turno diurno, igual a hospitais comparáveis. Mas quando ela examinou os dados, padrões emergiram que desafiaram suposições.

**Padrão 1: Variação de Tempo por Tipo de Medicamento**
Medicamentos simples (5 ou menos drogas): 15-30 minutos média
Medicamentos complexos (6+ drogas, interações): 45-180 minutos média
Medicamentos de alta exigindo novas prescrições: 2-4 horas média

**Padrão 2: Performance por Dia da Semana**
Segunda-Quarta: 75 minutos média revisão farmácia
Quinta-Sexta: 120 minutos média revisão farmácia
Fim de semana: 45 minutos média revisão farmácia

**Padrão 3: Performance por Farmacêutico**
Dr. Martinez (15 anos experiência): 60 minutos média, 95% precisão
Dr. Patel (3 anos experiência): 105 minutos média, 88% precisão
Funcionários temporários: 150 minutos média, 78% precisão

O breakthrough real veio quando Lisa examinou registros eletrônicos de saúde e descobriu que 40% das ordens de medicamentos de alta continham erros ou informações faltantes exigindo esclarecimento do farmacêutico com médicos. Nas quintas e sextas, tempo de resposta médica para perguntas de farmacêuticos tinha média de 3,2 horas porque médicos estavam em cirurgia ou tinham agendas de clínica pesadas.

A causa raiz não era pessoal da farmácia—eram ordens de alta incompletas criando loops de retrabalho, agravados por padrões de disponibilidade médica e níveis de experiência variados de farmacêuticos. Esta descoberta mudou tudo sobre a estratégia de melhoria.

Lisa percebeu que soluções superficiais como "contratar mais farmacêuticos" falhariam porque não abordavam o problema real: qualidade de informação e timing de comunicação. O hospital precisava de melhores protocolos de ordem de alta, sistemas de comunicação médica e treinamento de farmacêuticos—não apenas mais funcionários.

## Teoria Central

### Entendendo Causa Raiz vs. Sintomas

A maioria dos problemas de processo tem múltiplos fatores contribuintes, tornando análise sistemática de causa raiz essencial para soluções eficazes.

**Sintomas**: Efeitos observáveis de problemas subjacentes
- Cycle times longos
- Altas taxas de erro
- Reclamações de clientes
- Gargalos de recursos
- Sobrecusto

**Fatores Contribuintes**: Elementos que influenciam severidade do problema
- Níveis de pessoal
- Qualidade de treinamento
- Performance do sistema
- Padrões de comunicação
- Variação de carga de trabalho

**Causas Raiz**: Questões sistêmicas fundamentais que criam problemas
- Falhas de design de processo
- Lacunas de arquitetura de informação
- Conflitos de estrutura organizacional
- Padrões culturais e comportamentais
- Falhas de integração tecnológica

### A Técnica dos 5 Whys

Questionamento sistemático para aprofundar de sintomas para causas raiz:

**Problema**: Revisões de farmácia demoram muito tempo

**Why #1**: Por que revisões de farmácia demoram muito tempo?
*Porque casos complexos exigem pesquisa extensiva e consulta médica*

**Why #2**: Por que casos complexos exigem pesquisa extensiva?
*Porque ordens de alta frequentemente carecem de histórico medicamentoso completo e documentação de interação*

**Why #3**: Por que ordens de alta carecem de informação completa?
*Porque médicos não têm acesso integrado a registros de farmácia ambulatorial durante escrita de ordens*

**Why #4**: Por que médicos não têm acesso integrado?
*Porque sistema EHR hospitalar não se interfacia com bancos de dados de farmácias comunitárias*

**Why #5**: Por que o sistema EHR não se interfacia com farmácias comunitárias?
*Porque orçamento de TI priorizou compliance regulatória sobre recursos de coordenação de cuidado*

**Causa Raiz**: Prioridades de investimento tecnológico que não apoiam workflow de coordenação de cuidado

### Análise de Diagrama Fishbone (Ishikawa)

Exame sistemático de categorias de causas potenciais:

**Causas de Pessoas**:
- Lacunas de habilidade em gerenciamento de medicamento complexo
- Variações de nível de experiência entre farmacêuticos
- Treinamento médico em escrita completa de ordem de alta
- Preferências de comunicação e incompatibilidades de timing

**Causas de Processo**:
- Falhas de design de workflow de ordem de alta
- Falta de procedimentos padronizados de reconciliação de medicamentos
- Pontos de controle de qualidade faltantes antes da revisão de farmácia
- Sem procedimentos de escalação para casos urgentes

**Causas de Tecnologia**:
- Limitações do sistema EHR no acesso a histórico de medicamentos
- Falta de integração com bancos de dados de farmácia ambulatorial
- Sem verificação automatizada de interação de drogas na entrada de ordem
- Ferramentas de comunicação inadequadas para consulta médico-farmacêutico

**Causas de Ambiente**:
- Localização da farmácia isolada das áreas de trabalho médico
- Padrões de demanda de horário de pico sobrecarregando capacidade
- Requisitos regulatórios criando carga de documentação
- Cultura organizacional priorizando velocidade sobre precisão

**Causas de Materiais**:
- Históricos de medicamento de paciente incompletos na admissão
- Documentação faltante de médicos referenciadores
- Bancos de dados de referência de drogas desatualizados
- Falta de listas de medicamento de paciente de casa

## Demonstração de Ferramenta

### Análise de Causa Raiz: Exemplo de Farmácia Hospitalar

**Passo 1: Definição do Problema**
"Revisões de medicamentos de farmácia para altas de pacientes têm média de 90 minutos, causando 4,2 horas de atrasos totais de alta e insatisfação do cliente"

**Passo 2: Coleta de Dados e Análise de Padrões**

**Performance por Complexidade**:
- Simples (≤5 medicamentos): 30 min média, σ = 8 min
- Moderado (6-10 medicamentos): 75 min média, σ = 22 min
- Complexo (>10 medicamentos): 165 min média, σ = 45 min

**Performance por Qualidade de Informação**:
- Ordens completas: 45 min média
- Informação faltante: 125 min média (+78% aumento)
- Informação conflitante: 180 min média (+300% aumento)

**Atrasos de Comunicação**:
- Médico imediatamente disponível: 15 min consulta
- Médico em clínica/cirurgia: 185 min resposta média
- Cobertura médica fim de semana/noite: 45 min resposta média

## Mini Projeto

**Análise de Causa Raiz e Design de Coleta de Dados**

Conduza análise sistemática de causa raiz para um problema real de processo, projete estratégia de coleta de dados e construa business case quantitativo para melhoria.

**Escopo do Projeto:**
Escolha um problema de processo onde você pode acessar dados de performance:
- **Processo de trabalho**: Altas taxas de erro, cycle times longos, restrições de recursos
- **Processo de serviço**: Reclamações de clientes, problemas de qualidade, problemas de eficiência
- **Processo educacional**: Lacunas de performance de estudantes, ineficiências administrativas
- **Processo pessoal**: Problemas recorrentes com impactos mensuráveis

**Requisitos:**
- Problema deve ter **impactos mensuráveis** (tempo, custo, qualidade, satisfação)
- Acesso a **dados históricos** ou habilidade de coletar novos dados
- **Múltiplas causas potenciais** exigindo análise sistemática
- **Disponibilidade de stakeholder** para entrevistas e validação

**Entregáveis:**

### 1. Definição do Problema e Análise de Impacto (400 palavras)

**Declaração do Problema** (150 palavras):
- Descrição específica e mensurável da lacuna de performance atual
- Impacto quantificado em stakeholders (tempo, custo, qualidade, satisfação)
- Contexto empresarial explicando por que este problema importa
- Escopo e limites da análise

**Evidência do Estado Atual** (150 palavras):
- Dados de performance histórica mostrando magnitude do problema
- Análise de tendência indicando se problema está piorando
- Análise de variação mostrando padrões consistentes vs. outlier
- Documentação de impacto de stakeholder com exemplos específicos

**Oportunidade de Melhoria** (100 palavras):
- Benefícios potenciais de resolver o problema
- Valor estimado de melhoria (economia de tempo, redução de custo, melhoria de qualidade)
- Importância estratégica além de métricas imediatas
- Urgência e consequências de não abordar o problema

### 2. Análise Sistemática de Causa Raiz (600 palavras)

**Análise 5 Whys** (200 palavras):
- Documente cadeia completa 5 Whys da declaração do problema à causa raiz
- Explique raciocínio para cada "why" com evidência de apoio
- Identifique a questão sistêmica fundamental que cria o problema
- Valide conclusão de causa raiz com feedback de stakeholder

**Análise de Diagrama Fishbone** (200 palavras):
- Crie diagrama fishbone abrangente examinando todas as categorias de causa potencial
- Pessoas: Habilidades, treinamento, motivação, padrões de comunicação
- Processo: Design de workflow, procedimentos, controles de qualidade, handoffs
- Tecnologia: Capacidades do sistema, integração, interface do usuário, confiabilidade
- Ambiente: Espaço físico, timing, regulamentações, cultura organizacional
- Materiais: Qualidade de informação, disponibilidade de ferramenta, restrições de recursos

**Validação de Causa Baseada em Dados** (200 palavras):
- Apresente evidência quantitativa apoiando causas raiz primárias
- Use análise estatística (correlações, control charts, análise Pareto)
- Distinga entre fatores contribuintes e causas fundamentais
- Priorize causas por magnitude de impacto e viabilidade de melhoria

### 3. Design de Estratégia de Coleta de Dados (500 palavras)

**Definição de Requisitos de Dados** (150 palavras):
- Especifique exatamente que dados são necessários para validar causas raiz
- Defina requisitos de qualidade de dados (precisão, completude, pontualidade)
- Identifique tanto métricas quantitativas quanto insights qualitativos necessários
- Estabeleça requisitos de medição baseline para rastreamento de melhoria

**Métodos de Coleta e Fontes** (200 palavras):
- **Dados do Sistema**: Que registros eletrônicos ou bancos de dados podem fornecer medições objetivas?
- **Dados Observacionais**: Que observação direta ou estudos de tempo são necessários?
- **Dados de Survey**: Que percepções e experiências de stakeholder devem ser capturadas?
- **Dados de Entrevista**: Que insights profundos exigem conversas estruturadas?

**Plano de Amostragem e Estatístico** (150 palavras):
- Cálculos de tamanho de amostra para conclusões confiáveis
- Metodologia de amostragem garantindo dados representativos
- Abordagens de análise estatística para teste de hipótese
- Controle para variáveis confusas e fontes de viés

### 4. Business Case para Melhoria (400 palavras)

**Análise de Custo de Estado Atual** (150 palavras):
- Quantifique custos diretos do problema atual (trabalho, materiais, retrabalho)
- Estime custos indiretos (satisfação do cliente, rotatividade de funcionários, custo de oportunidade)
- Calcule impacto anual total em termos financeiros
- Inclua custos qualitativos difíceis de quantificar mas importantes a considerar

**Solução Proposta e Investimento** (150 palavras):
- Descreva abordagem específica de melhoria baseada em análise de causa raiz
- Estime custos de implementação (tecnologia, treinamento, redesign de processo)
- Timeline para implementação e resultados esperados
- Requisitos de recursos e compromissos de stakeholder necessários

**Análise de Retorno sobre Investimento** (100 palavras):
- Benefícios projetados de resolver o problema de causa raiz
- Custos de implementação vs. economia anual esperada
- Período de payback e cálculo de ROI de 3 anos
- Avaliação de risco e análise de sensibilidade para suposições chave

**Arquivo para submeter**: `analise_causa_raiz_[nome_problema].pdf`

**Critérios de Avaliação:**
- **Definição do Problema**: Problema claro e mensurável com impacto empresarial convincente (25%)
- **Análise de Causa Raiz**: Análise sistemática usando múltiplas ferramentas com validação de dados (35%)
- **Estratégia de Dados**: Plano abrangente de coleta com rigor estatístico apropriado (25%)
- **Business Case**: Análise convincente de ROI com suposições realistas e avaliação de risco (15%)

## Quiz Placeholder
<QUIZ_LINK will be replaced by generated HTML file>

---

## Chapter Links
- 🧠 **Quiz**: [[L1_C3_quiz.html|Take the Root-Cause Analysis Quiz]]
- 🎯 **Project**: [[L1_C3_project|Project Assignment]]  
- ✅ **Solutions**: [[L1_C3_solutions|Solutions Guide]]

## Navigation
**Previous**: [[L1_C2_reading|Chapter 2: AS-IS Mapping & Bottleneck Hunting]]  
**Next**: [[L1_C4_reading|Chapter 4: TO-BE Process Design]]  
**Up**: [[../../Level1_index|Level 1 Index]]