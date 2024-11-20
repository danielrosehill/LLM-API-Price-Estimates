# General reference notes on LLM API pricing

Updated: Nov 24

# Units used in LLM API pricing

Typically, both inputs and outputs are priced as `$/1M`.

This means:

US dollars per one *million* tokens.

## Nomenclature

LLMs being so use, standardisation around how to denominate this unit is still in its early stages. 

Anthropic uses `MTok` to denote millions of tokens so ... USD/MTok (or EUR/MTok or $/MTok or €/MTok) could all work. 

---

# Tokenisation: inputs versus outputs

To the best of my knowledge (but I may be wrong!) tokenisation does not "work" any differently whether we're talking about tokenising prompts (inputs) or outputs. 

While different LLMs have different tokenisation algorithms, at least for the most part, 

---

## Other Details

The purpose of this repo was to create "back of the envelope" calcs.

In reality, LLM API pricing is a bit more complicated than what is shown here: there are discounts available for batching APIs, caching inputs, etc. 