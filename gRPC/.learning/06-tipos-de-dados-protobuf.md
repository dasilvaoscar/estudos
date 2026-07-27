# Tipos de dados do Protobuf e seus tamanhos

Separar sempre: o **tipo declarado no `.proto`** ≠ o **tamanho na serialização
(wire)**. O tamanho não é fixo pela declaração; depende da codificação. A POC usa
só `string`.

## Tipos escalares e tamanhos no fio

| Tipo `.proto` | Wire type | Tamanho (bytes) | Observação |
|---|---|---|---|
| `bool` | varint | 1 | |
| `int32` | varint | 1–5 (10 se negativo) | negativo sempre ocupa 10 bytes |
| `int64` | varint | 1–10 | |
| `uint32` | varint | 1–5 | |
| `uint64` | varint | 1–10 | |
| `sint32` | varint (ZigZag) | 1–5 | eficiente p/ negativos |
| `sint64` | varint (ZigZag) | 1–10 | eficiente p/ negativos |
| `fixed32` | 32-bit | 4 (sempre) | bom quando valores são grandes |
| `sfixed32` | 32-bit | 4 (sempre) | |
| `float` | 32-bit | 4 (sempre) | IEEE 754 |
| `fixed64` | 64-bit | 8 (sempre) | |
| `sfixed64` | 64-bit | 8 (sempre) | |
| `double` | 64-bit | 8 (sempre) | IEEE 754 |
| `string` | length-delimited | variável | UTF-8; prefixo de tamanho (varint) + bytes |
| `bytes` | length-delimited | variável | prefixo de tamanho (varint) + bytes |
| `enum` | varint | 1–5 | codificado como `int32` |

## Varint

Codificação de tamanho variável: números pequenos ocupam menos bytes. Cada byte
usa 7 bits para o valor e 1 bit de continuação. Ex.: `1` → 1 byte; `300` → 2 bytes.

**Pegadinha:** `int32` negativo é estendido para 64 bits → sempre 10 bytes. Se o
campo pode ser negativo, use `sint32`/`sint64` (ZigZag), que mapeia negativos para
positivos pequenos.

## Overhead por campo (tag)

Cada campo carrega uma **tag** = número do campo + wire type, codificada como
varint: **1 byte** para field numbers 1–15, **2 bytes** para 16–2047. Reservar os
tags 1–15 para os campos mais frequentes.

## Tipos compostos

| Construção | O que é |
|---|---|
| `message` | tipo estruturado aninhado (length-delimited) |
| `enum` | conjunto fechado de valores nomeados |
| `repeated` | lista (0..N); numéricos são *packed* por padrão no proto3 |
| `map<K,V>` | mapa (açúcar sintático p/ `repeated` de pares chave-valor) |
| `oneof` | união: só um campo setado por vez |
| `Any` | mensagem arbitrária embrulhada com seu type URL |
| Well-known types | `Timestamp`, `Duration`, `StringValue`, etc. |

## Proto3: valores default não trafegam

Campo com valor zero (`0`, `""`, `false`, enum 0) ocupa **0 bytes no fio** — não é
serializado. Consequências:

- Impossível distinguir "não setado" de "setado com default" em escalares, a menos
  que se use `optional` ou wrappers (`StringValue`, etc.).
- Mensagens esparsas ficam bem compactas.
