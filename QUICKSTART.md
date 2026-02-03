# Quick Start Guide

## Sistema Operacional de Matemática Harappana - Guia Rápido

### Instalação

Nenhuma instalação necessária! O sistema usa apenas a biblioteca padrão do Python.

**Requisitos:**
- Python 3.7 ou superior (para suporte a dataclasses)

### Uso Básico

#### 1. Importar o Sistema

```python
from harappan_symbols import create_harappan_system, SymbolFamily, GraphicOperator
from harappan_sequence import validate_and_convert, HarappanSequence
from harappan_frequency import create_sample_data
```

#### 2. Criar o Sistema

```python
# Criar sistema completo com todos os 45 símbolos
registry, composition = create_harappan_system()
```

#### 3. Consultar Símbolos

```python
# Obter um símbolo específico
symbol = registry.get_symbol(373)
print(f"Símbolo {symbol.id}: {symbol.description}")

# Obter todos os símbolos de uma família
omega_symbols = registry.get_family_symbols(SymbolFamily.OMEGA)
print(f"Família Ω tem {len(omega_symbols)} símbolos")
```

#### 4. Aplicar Composições

```python
# Aplicar operador a um símbolo
result = composition.get_composition(373, GraphicOperator.DOT)
print(f"373 + DOT = {result}")

# Decompor um símbolo
decompositions = composition.get_decomposition(394)
for base, operator in decompositions:
    print(f"394 = {base} + {operator.value}")
```

#### 5. Validar Sequências

```python
# Validar uma sequência de símbolos
sequence = [373, 400, 410]  # entidade → relação → contagem
result = validate_and_convert(sequence)

print(f"Válida: {result['valid']}")
print(f"Notação: {result['functional_notation']}")
```

#### 6. Criar Sequência JSON

```python
import json

# Criar sequência institucional
sequence = HarappanSequence()
sequence.object_type = "seal"
sequence.provenance = "Harappa"
sequence.add_symbol(373)
sequence.add_symbol(410)
sequence.add_symbol(394)

# Converter para JSON
print(json.dumps(sequence.to_json(), indent=2))
```

### Executar Exemplos Completos

Para ver todos os exemplos em ação:

```bash
python3 examples.py
```

Este script demonstra:
1. Consulta de símbolos básicos
2. Sistema de composição
3. Validação de sequências
4. Representação JSON moderna
5. Análise de frequência
6. Autômato finito de validação

### Conceitos-Chave

#### Três Famílias de Símbolos

- **Ω (Omega, 373-399)**: Entidades/Tokens
  - Corpo-base: oval/círculo
  - Função: representar entidades institucionais

- **Δ (Delta, 400-409)**: Relações/Vínculos
  - Corpo-base: pares de ovais, nós, halteres
  - Função: estabelecer conexões formais

- **Σ (Sigma, 410-417)**: Contagens/Pilhas
  - Corpo-base: empilhamento de discos
  - Função: codificar quantidades

#### Operadores Gráficos Universais

10 operadores que modificam símbolos base:

1. **Dot** (•): Instância/ativação
2. **Stroke** (│): Partição/qualificação
3. **Fill** (█): Estado consumado
4. **Bracket** (⟦⟧): Escopo/jurisdição
5. **SideBars** (║): Nível/autoridade
6. **Crown** (⸙): Multiplexação
7. **Dup** (⊕): Duplicação/par
8. **Knot** (⚭): Vínculo forte
9. **Stem** (⊥): Âncora/indexação
10. **Stack** (≡): Contagem/agregação

#### Composição Hierárquica

**Caso crítico**: 394 = 373 + 343

- Operadores podem ser aplicados entre famílias
- Sistema admite composição hierárquica, não apenas linear

### Teste Rápido

Execute este código para verificar se tudo está funcionando:

```python
from harappan_symbols import create_harappan_system
from harappan_sequence import validate_and_convert

# Criar sistema
registry, composition = create_harappan_system()

# Validar sequência
result = validate_and_convert([373, 400, 410])

# Verificar resultado
assert result['valid'] == True
assert 'Entity(373)' in result['functional_notation']
assert 'Relation(400)' in result['functional_notation']
assert 'Count(2)' in result['functional_notation']

print("✓ Sistema funcionando corretamente!")
```

### Estrutura de Arquivos

```
.
├── README.md                  # Documentação completa
├── TECHNICAL_SUMMARY.md       # Resumo técnico
├── QUICKSTART.md             # Este arquivo
├── harappan_symbols.py       # Símbolos, famílias e composição
├── harappan_sequence.py      # Sequências e validação
├── harappan_frequency.py     # Análise de frequência
├── examples.py               # Exemplos completos
└── requirements.txt          # Sem dependências externas
```

### Próximos Passos

1. Execute `python3 examples.py` para ver demonstrações
2. Leia `README.md` para documentação completa
3. Consulte `TECHNICAL_SUMMARY.md` para detalhes técnicos
4. Explore o código fonte para entender a implementação

### Recursos Adicionais

- **Documentação Completa**: README.md
- **Resumo Técnico**: TECHNICAL_SUMMARY.md
- **Exemplos Executáveis**: examples.py
- **Código Fonte**: harappan_*.py

### Suporte

Para questões sobre implementação:
1. Consulte a documentação nos arquivos .md
2. Execute os exemplos para ver padrões de uso
3. Leia os comentários no código fonte

### Licença

MIT License - Veja arquivo LICENSE para detalhes.

---

**Versão**: 1.0.0  
**Python**: 3.7+  
**Dependências**: Nenhuma (apenas biblioteca padrão)
