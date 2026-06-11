"""
⚠️  DISCLAIMER: SPECULATIVE MODEL IDENTIFIERS FOR EDUCATIONAL PURPOSES
====================================================================

This file contains model configuration dictionaries with speculative and experimental
model identifiers that may not be available in current API versions. Many entries
include:

- FUTURE DATES (e.g., "gpt-5.5-2026-04-23") — These are placeholder identifiers
- EXPERIMENTAL MODELS (e.g., preview/beta variants) — Availability may vary by region
- OPEN-WEIGHT MODELS — Some may require local deployment via Ollama, HuggingFace, or similar

⚠️  BEFORE USING IN PRODUCTION:
1. Verify each model ID is available in your chosen provider's current API documentation
2. Replace speculative IDs with currently available, tested model identifiers
3. Test API calls before deploying to production
4. Check provider capability lists and rate limits

EDUCATIONAL USE: This file is designed for learning LangChain/LLM integration concepts.
Always validate model IDs against live provider APIs before deployment.
====================================================================
"""

GROQ_MODELS = {
    # Fast & lightweight
    "llama_3.1_8b":     "llama-3.1-8b-instant",       # 560 t/s — fastest, great for simple tasks
    "llama_3.3_70b":    "llama-3.3-70b-versatile",     # 280 t/s — best balance of speed & quality
    "gpt_oss_120b":     "openai/gpt-oss-120b",         # 500 t/s — most capable, reasoning + browser search
    "gpt_oss_20b":      "openai/gpt-oss-20b",          # 1000 t/s — fastest production model

    # Preview Models (experimental, not for production)
    "llama_4_scout":    "meta-llama/llama-4-scout-17b-16e-instruct",  # vision support
    "qwen3_32b":        "qwen/qwen3-32b",              # 400 t/s — strong reasoning

    # Agentic Systems (models + built-in tools)
    "compound":         "groq/compound",               # web search + code execution built in
    "compound_mini":    "groq/compound-mini",          # lighter version of compound
}

# ============================================================
# OPENAI MODELS DICTIONARY
# Based on current API-available models (June 2026)
# ============================================================

OPENAI_MODELS = {

    # --- FLAGSHIP / LATEST ---
    "gpt_5.5":          "gpt-5.5-2026-04-23",          # Most capable, frontier reasoning
    "gpt_5.5_pro":      "gpt-5.5-pro-2026-04-23",       # Pro variant, highest intelligence

    # --- GPT-5.4 FAMILY ---
    "gpt_5.4":          "gpt-5.4-2026-03-05",           # Complex professional work
    "gpt_5.4_mini":     "gpt-5.4-mini-2026-03-17",      # Fast, free-tier accessible ← your Udemy course uses this
    "gpt_5.4_nano":     "gpt-5.4-nano-2026-03-17",      # API only, ultra lightweight

    # --- GPT-5 FAMILY (stable) ---
    "gpt_5":            "gpt-5-2025-08-07",             # Original GPT-5, solid & stable
    "gpt_5_mini":       "gpt-5-mini-2025-08-07",        # Affordable GPT-5 variant

    # --- GPT-4.1 FAMILY (great for coding) ---
    "gpt_4.1":          "gpt-4.1-2025-04-14",           # Strong coding, 1M context
    "gpt_4.1_mini":     "gpt-4.1-mini-2025-04-14",      # Best budget option ← recommended for learning
    "gpt_4.1_nano":     "gpt-4.1-nano-2025-04-14",      # Fastest, cheapest

    # --- GPT-4o FAMILY (multimodal / audio) ---
    "gpt_4o":           "gpt-4o",                       # Still good for audio/vision tasks
    "gpt_4o_mini":      "gpt-4o-mini",                  # Budget multimodal

    # --- REASONING MODELS (o-series) ---
    "o3":               "o3-2025-04-16",                # Strong reasoning
    "o3_pro":           "o3-pro",                       # Highest reasoning effort

    # --- OPEN WEIGHT (same as Groq's) ---
    "gpt_oss_120b":     "gpt-oss-120b",                 # Open weight, 120B params
    "gpt_oss_20b":      "gpt-oss-20b",                  # Open weight, faster/cheaper
}

# ============================================================
# GOOGLE GEMINI MODELS DICTIONARY
# Based on official Gemini API docs (June 2026)
# ============================================================

GOOGLE_MODELS = {

    # --- GEMINI 3.5 (LATEST STABLE FLAGSHIP) ---
    "gemini_3.5_flash":         "gemini-3.5-flash",                  # Most intelligent, best for agentic/coding ← recommended

    # --- GEMINI 3.1 FAMILY ---
    "gemini_3.1_pro":           "gemini-3.1-pro-preview",            # Advanced intelligence, complex problem-solving
    "gemini_3.1_flash_lite":    "gemini-3.1-flash-lite",             # Stable, fast, cost-efficient
    "gemini_3.1_flash_live":    "gemini-3.1-flash-live-preview",     # Real-time dialogue / voice apps
    "gemini_3.1_flash_tts":     "gemini-3.1-flash-tts-preview",      # Text-to-speech

    # --- GEMINI 3 FAMILY ---
    "gemini_3_flash":           "gemini-3-flash-preview",            # Frontier-class, lower cost than Pro

    # --- GEMINI 2.5 FAMILY (stable, GA until Oct 2026) ---
    "gemini_2.5_pro":           "gemini-2.5-pro",                    # Most advanced 2.5, deep reasoning
    "gemini_2.5_flash":         "gemini-2.5-flash",                  # Best price/performance ← great for learning
    "gemini_2.5_flash_lite":    "gemini-2.5-flash-lite",             # Fastest & cheapest in 2.5 family

    # --- EMBEDDING MODELS ---
    "gemini_embedding_2":       "gemini-embedding-2",                # Multimodal embeddings (text, image, video, audio)
    "gemini_embedding":         "gemini-embedding-001",              # Text embeddings for RAG

    # --- AGENTIC / TOOL MODELS ---
    "computer_use":             "gemini-2.5-computer-use-preview-10-2025",  # UI automation agent
    "deep_research":            "deep-research-preview-04-2026",     # Multi-step research agent
    "antigravity_agent":        "antigravity-preview-05-2026",       # General-purpose autonomous agent
}

# ============================================================
# ANTHROPIC CLAUDE MODELS DICTIONARY
# Based on official Anthropic API docs (June 2026)
# ============================================================

ANTHROPIC_MODELS = {

    # --- OPUS 4 FAMILY (most capable) ---
    "opus_4.8":     "claude-opus-4-8",          # Most capable — complex reasoning, agentic coding, 1M context
    "opus_4.7":     "claude-opus-4-7",          # Previous Opus, still available
    "opus_4.6":     "claude-opus-4-6",          # Previous generation Opus

    # --- SONNET 4 FAMILY (best balance) ---
    "sonnet_4.6":   "claude-sonnet-4-6",        # Best speed + intelligence balance ← great for learning

    # --- HAIKU 4 FAMILY (fastest) ---
    "haiku_4.5":    "claude-haiku-4-5-20251001", # Fastest, near-frontier intelligence, cheapest
}

# ============================================================
# META LLAMA MODELS DICTIONARY
# Organized by generation and size (June 2026)
# ============================================================

LLAMA_MODELS = {

    # --- LLAMA 4 FAMILY (latest, multimodal) ---
    # Via Groq: use "meta-llama/" prefix
    # Via Ollama: use model name directly
    "llama4_maverick":  "meta-llama/llama-4-maverick-17b-128e-instruct",  # Multimodal, image + text, best quality
    "llama4_scout":     "meta-llama/llama-4-scout-17b-16e-instruct",      # Multimodal, faster/lighter than Maverick

    # --- LLAMA 3.3 FAMILY (text only, strong) ---
    "llama3.3_70b":     "llama-3.3-70b-versatile",    # Best text-only Llama on Groq ← recommended
    "llama3.3_70b_hf":  "meta-llama/Llama-3.3-70B-Instruct",  # HuggingFace / Ollama ID

    # --- LLAMA 3.2 FAMILY (vision + edge) ---
    "llama3.2_90b":     "llama3.2-90b-vision-preview",  # Largest 3.2, vision support
    "llama3.2_11b":     "llama3.2-11b-vision-preview",  # Lighter vision model
    "llama3.2_3b":      "llama3.2-3b-preview",          # Edge/mobile friendly
    "llama3.2_1b":      "llama3.2-1b-preview",          # Smallest, ultra-fast

    # --- LLAMA 3.1 FAMILY (open weights, widely supported) ---
    "llama3.1_405b":    "meta-llama/Llama-3.1-405B-Instruct",  # Largest open-weight model
    "llama3.1_70b":     "meta-llama/Llama-3.1-70B-Instruct",   # Great balance
    "llama3.1_8b":      "llama-3.1-8b-instant",                # Fast, Groq-hosted ← great for learning
}

# ============================================================
# QWEN MODELS DICTIONARY (Alibaba Cloud)
# Based on official Alibaba Cloud Model Studio docs (June 2026)
# ============================================================

QWEN_MODELS = {

    # --- FLAGSHIP TEXT MODELS ---
    "qwen3_max":        "qwen3-max",            # Most capable, complex tasks, 262k context
    "qwen3.5_plus":     "qwen3.5-plus",         # Best balance — text + image + video, 1M context ← recommended
    "qwen3.5_flash":    "qwen3.5-flash",        # Fastest & cheapest, 1M context ← great for learning
    "qwen_plus":        "qwen-plus",            # Balanced speed/quality, Qwen3 series
    "qwen_flash":       "qwen-flash",           # Fast & low-cost, Qwen3 series
    "qwen_turbo":       "qwen-turbo",           # Legacy, use qwen-flash instead

    # --- REASONING MODELS ---
    "qwq_plus":         "qwq-plus",             # Strong math & code reasoning (like o1-style thinking)

    # --- VISION / MULTIMODAL ---
    "qwen3_vl_plus":    "qwen3-vl-plus",        # Vision + reasoning, 262k context
    "qwen3_vl_flash":   "qwen3-vl-flash",       # Faster vision model
    "qwen_vl_max":      "qwen-vl-max",          # Previous gen vision, still solid
    "qvq_max":          "qvq-max",              # Visual reasoning (math + code from images)

    # --- OMNI (text + audio + video) ---
    "qwen3.5_omni_plus":  "qwen3.5-omni-plus",  # Multimodal: text, image, audio, video
    "qwen3.5_omni_flash": "qwen3.5-omni-flash", # Fast omni variant

    # --- OPEN SOURCE (via HuggingFace / Ollama) ---
    "qwen3_235b":       "Qwen/Qwen3-235B-A22B", # Flagship open-weight, 235B MoE
    "qwen3_32b":        "Qwen/Qwen3-32B",       # Strong open-weight, runs on good GPU ← also on Groq
    "qwen3_8b":         "Qwen/Qwen3-8B",        # Lightweight, runs locally
    "qwen2.5_72b":      "Qwen/Qwen2.5-72B-Instruct",  # Previous gen, widely supported
    "qwen2.5_coder":    "Qwen/Qwen2.5-Coder-32B-Instruct",  # Coding specialist
}

# ============================================================
# DEEPSEEK MODELS DICTIONARY
# Based on official DeepSeek API docs (June 2026)
# ============================================================

DEEPSEEK_MODELS = {

    # --- LATEST V4 FAMILY (current, 1M context) ---
    "v4_flash":     "deepseek-v4-flash",    # Fast & cheap, thinking + non-thinking ← recommended
    "v4_pro":       "deepseek-v4-pro",      # Most capable, 1.6T params, complex reasoning

    # --- LEGACY ALIASES (deprecated July 24, 2026) ---
    # deepseek-chat     → maps to deepseek-v4-flash (non-thinking mode)
    # deepseek-reasoner → maps to deepseek-v4-flash (thinking mode)
    # Migrate to v4_flash or v4_pro before July 24, 2026

    # --- OPEN WEIGHT (via HuggingFace / Ollama / Groq) ---
    "r1":           "deepseek-ai/DeepSeek-R1",          # Strong open-weight reasoning model
    "r1_distill_qwen_32b": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",  # Smaller R1, runs on GPU
    "r1_distill_qwen_14b": "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B",  # Even lighter
    "r1_distill_qwen_7b":  "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",   # Local-friendly
    "v3":           "deepseek-ai/DeepSeek-V3",           # Previous gen, still widely used
}

# ============================================================
# HUGGINGFACE POPULAR MODELS DICTIONARY (June 2026)
# Organized by use case — most used by developers
# ============================================================

HUGGINGFACE_MODELS = {

    # --- TEXT GENERATION / CHAT (LLMs) ---
    "llama3.3_70b":         "meta-llama/Llama-3.3-70B-Instruct",       # Most popular open LLM ← #1
    "llama3.1_8b":          "meta-llama/Llama-3.1-8B-Instruct",        # Lightweight, runs locally
    "llama4_maverick":      "meta-llama/Llama-4-Maverick-17B-128E-Instruct",  # Multimodal, latest
    "deepseek_r1":          "deepseek-ai/DeepSeek-R1",                 # Best open reasoning model
    "deepseek_v3":          "deepseek-ai/DeepSeek-V3",                 # Strong general purpose
    "qwen3_32b":            "Qwen/Qwen3-32B",                          # Best Qwen open weight
    "qwen3_8b":             "Qwen/Qwen3-8B",                           # Lightweight Qwen
    "qwen2.5_72b":          "Qwen/Qwen2.5-72B-Instruct",               # Previous gen, widely used
    "mistral_7b":           "mistralai/Mistral-7B-Instruct-v0.3",      # Classic, very popular
    "mixtral_8x7b":         "mistralai/Mixtral-8x7B-Instruct-v0.1",    # MoE, fast & capable
    "gemma2_9b":            "google/gemma-2-9b-it",                    # Google open model
    "phi4":                 "microsoft/phi-4",                         # Small but strong (14B)
    "kimi_k2":              "moonshotai/Kimi-K2-Instruct",             # Strong agentic model (1.1T MoE)

    # --- CODING MODELS ---
    "qwen2.5_coder":        "Qwen/Qwen2.5-Coder-32B-Instruct",        # Best open coding model ← #1
    "deepseek_coder_v2":    "deepseek-ai/DeepSeek-Coder-V2-Instruct",  # Strong code specialist
    "codellama_70b":        "codellama/CodeLlama-70b-Instruct-hf",     # Meta's code model

    # --- EMBEDDINGS (for RAG pipelines) ---
    "bge_large":            "BAAI/bge-large-en-v1.5",                  # Most popular embedding ← #1 for RAG
    "bge_m3":               "BAAI/bge-m3",                             # Multilingual embeddings
    "gte_qwen2":            "Alibaba-NLP/gte-Qwen2-7B-instruct",       # Strong long-context embeddings
    "e5_large":             "intfloat/e5-large-v2",                    # Classic, widely used
    "nomic_embed":          "nomic-ai/nomic-embed-text-v1",            # Great for local RAG

    # --- VISION / MULTIMODAL ---
    "llava_next":           "llava-hf/llava-v1.6-mistral-7b-hf",      # Popular vision-language
    "qwen_vl":              "Qwen/Qwen2.5-VL-7B-Instruct",            # Vision + language, strong
    "idefics3":             "HuggingFaceM4/Idefics3-8B-Llama3",       # HuggingFace's own vision model

    # --- SPEECH (STT / TTS) ---
    "whisper_large":        "openai/whisper-large-v3",                 # Best open STT ← most used
    "whisper_medium":       "openai/whisper-medium",                   # Lighter whisper
    "speecht5_tts":         "microsoft/speecht5_tts",                  # Popular open TTS

    # --- CLASSIFICATION / NLP TASKS ---
    "bert_base":            "google-bert/bert-base-uncased",           # Classic NLP backbone
    "roberta_large":        "FacebookAI/roberta-large",                # Stronger BERT variant
    "distilbert":           "distilbert/distilbert-base-uncased",      # Lightweight BERT
    "deberta_v3":           "microsoft/deberta-v3-large",              # Best for classification tasks

    # --- IMAGE GENERATION ---
    "flux_dev":             "black-forest-labs/FLUX.1-dev",            # Best open image gen ← #1
    "flux_schnell":         "black-forest-labs/FLUX.1-schnell",        # Fast image gen (Apache 2.0)
    "sdxl":                 "stabilityai/stable-diffusion-xl-base-1.0", # Classic, widely used
}