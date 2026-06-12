# 300 Google Colab Credits Execution Plan

## Decision

Use the 300 credits to create portfolio assets that can become products, not isolated experiments.

Priority:

1. StayProof Vision: computer vision for property inspection evidence.
2. NotaSafe/AutoFin NLP: fiscal and financial document extraction with structured validation.
3. Synthetic Retina Safety Lab: public and safe health AI benchmark without private research code.
4. Reporting and deployment assets: ONNX/TFLite exports, model cards, benchmark tables and GitHub documentation.

## Allocation

| Track | Credits | Goal |
|---|---:|---|
| StayProof Vision | 140 | Train object detection/classification models for inspection use cases. |
| NotaSafe/AutoFin NLP | 70 | Fine-tune or evaluate small LLM/RAG pipelines for structured fiscal/financial JSON. |
| Synthetic Retina Safety Lab | 40 | Build a safe public benchmark with synthetic/public images and XAI. |
| Reports and deployment | 30 | Export models, run benchmarks, create model cards and documentation. |
| Reserve | 20 | Failed runs, dataset fixes, retraining and final validation. |

## StayProof Vision

Target: property inspection, short-stay turnover and evidence automation.

Experiments:

- YOLO11n baseline.
- YOLO11s intermediate.
- YOLO11m main model.
- YOLO11m with augmentation.
- Export ONNX/TFLite.
- Benchmark inference latency.

Public portfolio outputs:

- notebooks/01_dataset_preparation.ipynb
- notebooks/02_train_yolo11.ipynb
- notebooks/03_evaluate_export.ipynb
- reports/metrics.csv
- reports/confusion_matrix.png
- reports/model_card.md

Do not use real client photos.

## NotaSafe and AutoFin NLP

Target: structured extraction and validation, not final tax advice.

Experiments:

- synthetic fiscal document dataset;
- baseline prompting;
- QLoRA small model experiment;
- RAG + deterministic rules comparison;
- Pydantic/FastAPI JSON validation.

Public portfolio outputs:

- datasets/synthetic_examples.jsonl
- notebooks/llm_structured_extraction.ipynb
- reports/base_vs_finetuned.csv
- docs/model_card.md

Do not automate government login, CAPTCHA, certificates or real tax submission.

## Synthetic Retina Safety Lab

Target: prove health AI experience safely.

Allowed:

- public datasets if licensing is clear;
- synthetic images;
- small baselines;
- metrics and explainability.

Forbidden:

- private dissertation code;
- private medical images;
- real model weights;
- complete sensitive architecture;
- unpublished article content.

## Rule

GPU is for training and inference benchmarks. Documentation, CSV preparation, README writing and simple API work should run without GPU.
