# Rule: Captura de aprendizados a cada prompt

**Objetivo**: manter a pasta `.learning/` como um registro incremental e fiel de
tudo que for aprendido nesta POC, atualizado a cada interação.

## Quando aplicar

A cada prompt do usuário, ao final da resposta, avaliar se surgiu algum
aprendizado novo (conceito, decisão de arquitetura, armadilha, número medido,
comando útil, correção). Se sim, registrar em `.learning/` **antes de encerrar a
resposta**.

## Como registrar

1. **Localizar o tema**: existe um arquivo em `.learning/` que já cobre o assunto?
   - Sim → editar/complementar esse arquivo (não duplicar).
   - Não → criar `.learning/NN-tema.md` com prefixo numérico sequencial.
2. **Atualizar o índice** em `.learning/README.md` sempre que criar um arquivo novo.
3. **Conteúdo**: escrever em português, direto ao ponto, com exemplos de código e
   números medidos quando houver. Preferir seções curtas e tabelas a texto corrido.
4. **Fidelidade**: registrar apenas o que foi de fato verificado/discutido na
   conversa. Marcar suposições como suposições.

## O que NÃO registrar

- O que já está óbvio no código-fonte da POC (a menos que tenha sido um ponto
  não-óbvio, e aí registrar o *porquê*).
- Detalhes efêmeros só relevantes a um prompt específico.

## Fechamento

Ao registrar, mencionar na resposta ao usuário, em uma linha, qual arquivo de
`.learning/` foi criado ou atualizado.
