# UniZen – System Architecture

UniZen is a source-aware academic assistant designed to help college students access verified academic information in a calm and structured manner.

The system follows a step-by-step pipeline to ensure accuracy, simplicity, and clarity.

## Architecture Overview

1. Academic documents such as syllabus, lecture notes, and college guidelines are collected and stored.
2. Text content is extracted from the academic documents.
3. The extracted text is processed and cleaned for further use.
4. The processed text is divided into smaller, meaningful chunks.
5. Retrieved text is divided into smaller chunks to improve relevance during search.
6. Structured text chunks are prepared for storage and retrieval.
7. Text chunks are stored along with their source document for traceability.
8. User queries are matched with stored text chunks using basic similarity logic.
9. Retrieved academic content is used to generate clear, natural-language answers for students.



## Design Principles

- Accuracy over creativity
- Use of verified academic sources only
- Simple and modular system design
- Student-friendly and calm user experience

## Current Implementation Status

- Document loading functionality implemented
- Text chunking logic implemented
- Core system modules created
- Vector storage planned for subsequent stages
