# DockSec System Architecture Diagram

This diagram illustrates the complete system architecture of DockSec, showing all components, external tools, and their interactions.

```mermaid
graph TB
    subgraph "User Interface"
        CLI[CLI - docksec.py]
        USER[User Input]
    end

    subgraph "Core Application Layer"
        MAIN[Main Orchestrator<br/>main.py]
        SCANNER[Docker Scanner<br/>docker_scanner.py]
        CONFIG[Configuration Manager<br/>config.py / config_manager.py]
        UTILS[Utilities<br/>utils.py]
    end

    subgraph "Analysis Layer"
        AI[AI Analysis Engine<br/>LangChain + GPT-4]
        SCORE[Security Score Calculator<br/>score_calculator.py]
    end

    subgraph "Report Generation Layer"
        REPORT[Report Generator<br/>report_generator.py]
        JSON[JSON Reporter]
        CSV[CSV Reporter]
        PDF[PDF Reporter]
        HTML[HTML Reporter]
    end

    subgraph "External Security Tools"
        HADOLINT[Hadolint<br/>Dockerfile Linter]
        TRIVY[Trivy<br/>Vulnerability Scanner]
        SCOUT[Docker Scout<br/>Advanced Scanner]
        DOCKER[Docker Engine<br/>Image Inspection]
    end

    subgraph "External Services"
        OPENAI[OpenAI API<br/>GPT-4o Model]
    end

    subgraph "Input Sources"
        DOCKERFILE[Dockerfile]
        IMAGE[Docker Image]
    end

    subgraph "Output Artifacts"
        RESULTS[Results Directory]
        JSON_FILE[scan_results.json]
        CSV_FILE[vulnerabilities.csv]
        PDF_FILE[security_report.pdf]
        HTML_FILE[security_report.html]
        TXT_FILE[security_report.txt]
    end

    subgraph "Configuration Sources"
        ENV[Environment Variables]
        DOTENV[.env File]
        DEFAULTS[Default Config]
    end

    %% User to CLI
    USER --> CLI

    %% CLI to Core
    CLI --> MAIN
    CLI --> SCANNER

    %% Configuration Flow
    ENV --> CONFIG
    DOTENV --> CONFIG
    DEFAULTS --> CONFIG
    CONFIG --> MAIN
    CONFIG --> SCANNER
    CONFIG --> AI
    CONFIG --> SCORE

    %% Input to Scanner
    DOCKERFILE --> SCANNER
    IMAGE --> SCANNER

    %% Core Layer Interactions
    MAIN --> UTILS
    MAIN --> AI
    SCANNER --> UTILS
    SCANNER --> SCORE
    SCANNER --> REPORT

    %% Scanner to External Tools
    SCANNER --> HADOLINT
    SCANNER --> TRIVY
    SCANNER --> SCOUT
    SCANNER --> DOCKER

    %% External Tools Response
    HADOLINT -.->|Linting Results| SCANNER
    TRIVY -.->|Vulnerability Data| SCANNER
    SCOUT -.->|Advanced Findings| SCANNER
    DOCKER -.->|Image Metadata| SCANNER

    %% AI Analysis Flow
    MAIN --> AI
    AI --> OPENAI
    OPENAI -.->|AI Insights| AI
    AI -.->|Recommendations| MAIN

    %% Score Calculation
    SCANNER --> SCORE
    SCORE --> OPENAI
    OPENAI -.->|Security Score| SCORE
    SCORE -.->|Score 0-100| SCANNER

    %% Report Generation
    SCANNER --> REPORT
    SCORE --> REPORT
    REPORT --> JSON
    REPORT --> CSV
    REPORT --> PDF
    REPORT --> HTML

    %% Output Generation
    MAIN -.->|Text Report| TXT_FILE
    JSON -.-> JSON_FILE
    CSV -.-> CSV_FILE
    PDF -.-> PDF_FILE
    HTML -.-> HTML_FILE

    %% Results Storage
    JSON_FILE --> RESULTS
    CSV_FILE --> RESULTS
    PDF_FILE --> RESULTS
    HTML_FILE --> RESULTS
    TXT_FILE --> RESULTS

    %% Utils Support
    UTILS -.->|Logging & Helpers| MAIN
    UTILS -.->|Logging & Helpers| SCANNER
    UTILS -.->|LLM Factory| AI
    UTILS -.->|LLM Factory| SCORE

    %% Styling
    classDef userLayer fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef coreLayer fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef analysisLayer fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef reportLayer fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    classDef externalTools fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    classDef externalServices fill:#f1f8e9,stroke:#33691e,stroke-width:2px
    classDef inputLayer fill:#e0f2f1,stroke:#004d40,stroke-width:2px
    classDef outputLayer fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    classDef configLayer fill:#e0e0e0,stroke:#424242,stroke-width:2px

    class CLI,USER userLayer
    class MAIN,SCANNER,CONFIG,UTILS coreLayer
    class AI,SCORE analysisLayer
    class REPORT,JSON,CSV,PDF,HTML reportLayer
    class HADOLINT,TRIVY,SCOUT,DOCKER externalTools
    class OPENAI externalServices
    class DOCKERFILE,IMAGE inputLayer
    class RESULTS,JSON_FILE,CSV_FILE,PDF_FILE,HTML_FILE,TXT_FILE outputLayer
    class ENV,DOTENV,DEFAULTS configLayer
```

## Architecture Components Overview

### 1. User Interface Layer
- **CLI (docksec.py)**: Entry point for command-line interface
- Handles argument parsing and mode selection
- Supports multiple scan modes: full, AI-only, scan-only, image-only

### 2. Core Application Layer
- **Main Orchestrator (main.py)**: Coordinates AI-based Dockerfile analysis
- **Docker Scanner (docker_scanner.py)**: Main scanning engine (1289 lines)
  - Orchestrates all security scans
  - Manages external tool execution
  - Handles validation and error recovery
- **Configuration Manager**: Centralized configuration with validation
- **Utilities**: Common helpers, logging, and LLM factory

### 3. Analysis Layer
- **AI Analysis Engine**: LangChain + OpenAI GPT-4o integration
  - Analyzes Dockerfile for security issues
  - Provides best practice recommendations
  - Identifies exposed credentials
  - Suggests remediation steps
- **Security Score Calculator**: LLM-based scoring (0-100)
  - Evaluates vulnerability severity
  - Assesses configuration risks
  - Provides contextual feedback

### 4. Report Generation Layer
- **Report Generator**: Multi-format report creation
  - JSON: Machine-readable structured data
  - CSV: Spreadsheet-friendly vulnerability list
  - PDF: Professional formatted reports
  - HTML: Interactive web-based reports with styling

### 5. External Security Tools
- **Hadolint**: Dockerfile linting and best practices
- **Trivy**: Comprehensive vulnerability scanning
- **Docker Scout**: Advanced security analysis (optional)
- **Docker Engine**: Image inspection and metadata

### 6. External Services
- **OpenAI API**: GPT-4o model for AI analysis and scoring
  - Retry logic with exponential backoff
  - Rate limiting support
  - Timeout handling

### 7. Configuration Sources
- Environment variables
- .env file support
- Default configuration values
- Runtime validation

### 8. Input Sources
- **Dockerfile**: For static analysis and AI recommendations
- **Docker Image**: For vulnerability scanning and runtime analysis

### 9. Output Artifacts
All reports stored in `results/` directory:
- JSON: Complete vulnerability data with metadata
- CSV: Tabular format for spreadsheet analysis
- PDF: Professional document with formatted sections
- HTML: Interactive report with modern UI
- TXT: Human-readable summary with AI insights

## Key Features

### Security & Validation
- Input validation and sanitization
- Path traversal protection
- Command injection prevention
- Secure subprocess execution

### Error Handling & Reliability
- Automatic retry with exponential backoff
- Rate limiting support for API calls
- Graceful degradation (scan-only mode)
- Comprehensive error messages with troubleshooting

### Performance
- Parallel report generation
- Progress indicators for long operations
- Configurable timeouts
- Optimized scanning

### Flexibility
- Multiple scan modes
- Works with or without OpenAI API key
- Configurable via environment variables
- Support for different severity levels

## Data Flow

1. **Input Phase**: User provides Dockerfile and/or image name via CLI
2. **Configuration Phase**: Load and validate configuration from environment
3. **Scanning Phase**: Execute external tools (Hadolint, Trivy, Scout)
4. **Analysis Phase**: AI analyzes results and provides recommendations
5. **Scoring Phase**: Calculate security score based on findings
6. **Report Phase**: Generate all report formats in parallel
7. **Output Phase**: Save reports to results directory

## Integration Points

- **OpenAI API**: For AI analysis and security scoring
- **Hadolint**: For Dockerfile linting
- **Trivy**: For vulnerability scanning
- **Docker Scout**: For advanced scanning (optional)
- **Docker Engine**: For image inspection

## Security Considerations

- No API keys stored in code
- Input validation on all user inputs
- Secure subprocess execution (shell=False)
- Path traversal protection
- Timeout protection for all operations

