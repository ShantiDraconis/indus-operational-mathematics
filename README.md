# Harappan Operational Mathematics System

## Sistema Operacional de Matemática Harappana - Bloco 373-417

Este repositório implementa o sistema operacional de matemática harappana conforme descrito na análise do bloco de símbolos 373-417. O sistema não é uma escrita fonética, mas um **protocolo operacional de validação de estados institucionais**.

## Visão Geral do Sistema

### 1. Três Famílias Funcionais (373-417)

Os símbolos 373-417 pertencem a três famílias funcionais com corpos-base distintos:

| Família | Intervalo | Corpo-base | Função no sistema |
|---------|-----------|------------|-------------------|
| **Ω (Tokens/Entidades)** | 373-399 | Oval/círculo simples | Representar entidades institucionais (objetos, atos, sujeitos) que podem ser qualificados |
| **Δ (Relações/Vínculos)** | 400-409 | Duplicação de ovais, nós, halteres | Estabelecer conexões formais (pares, contratos, trocas) |
| **Σ (Contagens/Pilhas)** | 410-417 | Empilhamento vertical de discos/ovais | Codificar quantidades, lotes, indexação |

### 2. Operadores Gráficos Universais (As "Runas")

Modificadores gráficos mínimos que aparecem transversalmente em múltiplas famílias:

| Operador | Forma gráfica | Efeito funcional | Exemplo no bloco 373-417 |
|----------|---------------|------------------|--------------------------|
| **Dot** | Ponto interno (•) | Marca instância/ativação | 374, 375, 376 (oval + ponto) |
| **Stroke** | Traço interno (\|) | Introduz partição/qualificação | 377, 378 (oval + traço) |
| **Fill/Hachura** | Preenchimento interno | Indica estado consumado/executado | 386, 387 (oval preenchido) |
| **Bracket** | Parênteses laterais | Delimita escopo/jurisdição | 379, 380 (oval + colchetes) |
| **SideBars** | Barras laterais (\|\|) | Define nível/grau/autoridade | 381, 382, 383 |
| **Crown/Prongs** | Dentes no topo | Multiplexação/canais múltiplos | 384, 385 (oval + coroa) |
| **Dup** | Duplicação do corpo-base | Cria par/relação binária | 400-406 (dois ovais) |
| **Knot** | Interlaçamento | Estabelece vínculo forte/travamento | 407 (nó) |
| **Stem** | Haste inferior/superior | Âncora/indexação externa | 408, 409 (halteres com haste) |
| **Stack** | Empilhamento vertical | Contagem/agregação | 410-417 (pilhas de discos) |

**Lei de conservação dos operadores**: Um operador mantém efeito funcional similar mesmo quando aplicado a corpos-base diferentes.

### 3. Sistema de Composição

#### 3.1 Conexões dentro da mesma família
- 373 (oval base) → Dot → 374 (entidade instanciada)
- 373 → Stroke → 377 (entidade qualificada)
- 373 → Bracket → 379 (entidade com escopo delimitado)

#### 3.2 Conexões entre famílias (composição hierárquica)
**Caso crítico**:
- **394 = 373 (oval base) + 343 (operador de fechamento da U-family)**
  - 373: entidade/token
  - 343: operador de fechamento qualificado (U + barra interna)
  - 394: registro institucional fechado sobre a entidade 373

Isto prova que:
- Operadores de fechamento (342-348) podem ser aplicados sobre corpos de outras famílias
- A escrita harappana admite composição gráfica hierárquica, não apenas linear

#### 3.3 Conexões via operadores universais
- Dup aplicado a 373 → 400-406 (pares de entidades)
- Knot aplicado a 400 → 407 (par vinculado)
- Stack aplicado a 373 → 410-417 (contagem de entidades)

## Estrutura do Código

### Módulos Principais

1. **`harappan_symbols.py`**: Define símbolos, famílias, operadores e sistema de composição
2. **`harappan_sequence.py`**: Representação de sequências e validação por autômato finito
3. **`harappan_frequency.py`**: Análise de frequência e distribuição (Tabelas I, II, IV)

### Classes Principais

- `Symbol`: Representa um símbolo harappano com ID, família e operadores
- `SymbolRegistry`: Registro completo de símbolos 373-417
- `CompositionSystem`: Regras de composição entre símbolos
- `HarappanSequence`: Sequência de símbolos harappanos
- `FiniteAutomaton`: Validador de sequências válidas
- `FrequencyAnalyzer`: Análise de frequência e distribuição

## Uso

### Exemplo 1: Criar e consultar símbolos

```python
from harappan_symbols import create_harappan_system, SymbolFamily

# Criar sistema completo
registry, composition = create_harappan_system()

# Consultar um símbolo
symbol_373 = registry.get_symbol(373)
print(f"Symbol {symbol_373.id}: {symbol_373.description}")
# Output: Symbol 373: Base entity token

# Consultar símbolos de uma família
omega_symbols = registry.get_family_symbols(SymbolFamily.OMEGA)
print(f"Omega family has {len(omega_symbols)} symbols")
# Output: Omega family has 27 symbols
```

### Exemplo 2: Aplicar composição

```python
from harappan_symbols import create_harappan_system, GraphicOperator

registry, composition = create_harappan_system()

# Aplicar operador Dot ao símbolo base 373
result = composition.get_composition(373, GraphicOperator.DOT)
print(f"373 + DOT = {result}")
# Output: 373 + DOT = 374

# Decompor um símbolo
decompositions = composition.get_decomposition(394)
for base, operator in decompositions:
    print(f"394 = {base} + {operator.value}")
# Output: 394 = 373 + █
```

### Exemplo 3: Validar sequência

```python
from harappan_sequence import validate_and_convert

# Validar sequência: entidade → relação → contagem
sequence = [373, 400, 410]
result = validate_and_convert(sequence)

print(f"Valid: {result['valid']}")
print(f"Functional notation: {result['functional_notation']}")
# Output: 
# Valid: True
# Functional notation: ∃x (Entity(373) ∧ Relation(400) ∧ Count(2))
```

### Exemplo 4: Representação JSON moderna

```python
from harappan_sequence import HarappanSequence
from harappan_symbols import create_harappan_system
import json

registry, _ = create_harappan_system()

# Criar sequência
sequence = HarappanSequence()
sequence.object_type = "seal"
sequence.provenance = "Harappa"
sequence.add_symbol(373)  # Entidade
sequence.add_symbol(410)  # Contagem = 2
sequence.add_symbol(394)  # Registro fechado

# Converter para JSON (equivalente moderno)
json_repr = sequence.to_json()
print(json.dumps(json_repr, indent=2))
```

Output:
```json
{
  "sequence": [
    {"symbol": 373, "position": "initial"},
    {"symbol": 410, "position": "medial"},
    {"symbol": 394, "position": "final"}
  ],
  "length": 3,
  "object_type": "seal",
  "provenance": "Harappa",
  "entities": [373, 394],
  "counts": [410]
}
```

### Exemplo 5: Análise de frequência

```python
from harappan_frequency import create_sample_data

# Criar analisador com dados de exemplo
analyzer = create_sample_data()

# Símbolos de alta frequência (operadores centrais)
high_freq = analyzer.get_high_frequency_symbols(threshold=10)
print(f"High frequency symbols: {high_freq}")
# Output: High frequency symbols: [373, 374, 400, 410]

# Símbolos de baixa frequência (instâncias específicas)
low_freq = analyzer.get_low_frequency_symbols(threshold=5)
print(f"Low frequency symbols: {low_freq}")
# Output: Low frequency symbols: [394, 407]

# Padrões de posição
patterns = analyzer.get_position_patterns(373)
print(f"Symbol 373 position distribution: {patterns}")
# Output: Symbol 373 position distribution: {'initial': 50.0, 'medial': 50.0, 'final': 0.0}
```

## Equivalência Moderna

O sistema harappano equivale formalmente a:

### JSON (Representação de dados)
```json
{
  "entity": "373",
  "quantity": 3,
  "relation": "bound",
  "status": "closed"
}
```

### Notação Lógica (Lógica de primeira ordem)
```
∃x (Entity(x, 373) ∧ Count(x, 3) ∧ Linked(x, y) ∧ Closed(x))
```

### Workflow / Autômato Finito
O sistema implementa um autômato finito que valida sequências:
- **Estados**: START → ENTITY → RELATION → COUNT → CLOSED
- **Transições**: Baseadas nas famílias de símbolos
- **Aceitação**: Estados ENTITY, COUNT ou CLOSED são terminais válidos

## Frequência e Distribuição

### Tabela I: Frequência por posição
- **Símbolos de alta frequência** (ex.: 373, 342, 343): operadores centrais, usados em múltiplos contextos
- **Símbolos de baixa frequência** (ex.: 394, 407): instâncias específicas, combinações validadas

### Tabela II: Pares recorrentes
Pares comuns que suportam as regras de composição:
- 373 → 410 (entidade + contagem)
- 373 → 400 (entidade + relação)
- 400 → 373 (relação + entidade)

### Tabela IV: Distribuição por objeto
- **Predominância**: selos e tabletes
- **Ausência**: objetos decorativos
- Indica uso institucional/administrativo

## Conexões com Outros Sistemas

### Disco de Festo
- ~45 signos distintos, carimbados em espiral
- **Operadores compartilhados**: Kano (canal/abertura), Dot (instância), Knot (vínculo)
- **Interpretação**: Mesmo tipo de sistema operacional – validação por estados, não narrativa

### Hieróglifos Egípcios
- 𓏺 (ponto) como marcador de unidade
- 𓈖 (canal) como contêiner
- Mesmos operadores gráficos para problemas cognitivos universais

### Chinês Antigo
- 丶 (ponto) como marcador
- 口 (abertura) como delimitador
- Convergência evolutiva em sistemas de escrita

## Conclusão

O sistema harappano é um **protocolo operacional**, não uma língua fonética:
- Usa ~45 símbolos principais (corpos-base + operadores)
- Gera ~417 estados válidos
- Operadores gráficos são universais
- Equivalente moderno: **JSON + workflow + autômato finito**

## Próximos Passos

1. ✅ Implementar modelo de símbolos e famílias
2. ✅ Implementar sistema de composição
3. ✅ Implementar autômato finito de validação
4. ✅ Implementar análise de frequência e distribuição
5. 🔄 Extrair automaticamente grafo de composição completo
6. 🔄 Implementar parser de textos harappanos reais
7. 🔄 Publicar modelo formal como artigo técnico

## Licença

MIT License - Veja arquivo LICENSE para detalhes.

## Referências

- Sign list (373-417): Progressão morfológica das famílias
- Table I: Frequência e posição sintática
- Table II: Pares recorrentes (regras de composição)
- Table IV: Distribuição por tipo de objeto
- Texts: Exemplos de uso real (sequências contendo 394)