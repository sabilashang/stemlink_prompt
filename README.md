# Prompt Engineering – Coding Workflows & Refactoring

## Introduction
This repository is a hands-on playground for learning and practicing prompt engineering with a focus on coding workflows and refactoring. You will:
- Refactor messy Python functions using proven prompt patterns.
- Practice 18 core prompting techniques with copy-paste templates.
- Explore guided examples (with hints) and self-guided exercises (no hints).
- Guardrails to ensure proper reliable code quality

## Prompt Patterns (18 Techniques)
The files under directory `refactoring/` provides description and relevant details with structured template for reuse on most commonly used Prompting Techniques

## Guided Refactoring
The files `refactoring/function_v1.py`, `refactoring/function_v2.py`, and `refactoring/function_v3.py` contain the same intentionally messy function (a factorial implementation) but each file starts with a different comment that demonstrates how to apply a specific prompt pattern during refactoring:
- `function_v1.py`: Role Prompting
- `function_v2.py`: Programmatic Prompting with Variables
- `function_v3.py`: Chain-of-Thought Prompting

Run them, read the comments, and then use the respective prompt pattern to refactor and improve the function. Consider readability, correctness, edge cases, and performance.

## Self Exercises
The files `refactoring/exercise_1.py` and `refactoring/exercise_2.py` each contain a different messy function (Fibonacci and prime checking). There are no hints. Choose any prompt pattern(s) from the `techniques` folder to refactor them. Aim for clear function signatures, docstrings, tests (if you add them), and robust handling of inputs.

## Guardrails
Guardrails are rules or constraints applied to AI outputs to ensure safety, reliability, and correct structure. In this repo, we explore prompt-based, post-processing, and multi-step guardrails with examples.

## CRUD
CRUD App building boiler template provided to be used as a prompt to build with AI code editors or prototyping application makers like Lovable and Bolt