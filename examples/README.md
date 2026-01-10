# DockSec Examples

This directory contains example Dockerfiles and usage scenarios to help you get started with DockSec.

## Directory Structure

```
examples/
├── dockerfiles/          # Sample Dockerfiles with various security levels
├── reports/             # Sample generated reports
├── configs/             # Example configuration files
└── scripts/             # Helper scripts for common scenarios
```

## Quick Start Examples

### Example 1: Secure Dockerfile (Best Practices)

See `dockerfiles/secure-python-app/Dockerfile` for a production-ready Python application following security best practices.

### Example 2: Vulnerable Dockerfile (Learning)

See `dockerfiles/vulnerable-node-app/Dockerfile` for common security mistakes to avoid.

### Example 3: Multi-stage Build

See `dockerfiles/multi-stage-golang/Dockerfile` for optimized multi-stage builds.

## Usage Examples

### 1. Scan a Secure Dockerfile

```bash
cd examples/dockerfiles/secure-python-app
docksec Dockerfile
```

**Expected Output:**
- High security score (85-100)
- Minimal vulnerabilities
- AI recommendations for further optimization

### 2. Scan a Vulnerable Dockerfile

```bash
cd examples/dockerfiles/vulnerable-node-app
docksec Dockerfile
```

**Expected Output:**
- Low security score (30-50)
- Multiple CRITICAL and HIGH severity issues
- Detailed remediation suggestions

### 3. Full Scan (Dockerfile + Image)

```bash
cd examples/dockerfiles/secure-python-app
docker build -t secure-python-app:latest .
docksec Dockerfile -i secure-python-app:latest
```

### 4. AI-Only Analysis

```bash
docksec examples/dockerfiles/multi-stage-golang/Dockerfile --ai-only
```

### 5. Scan-Only Mode (No AI)

```bash
docksec examples/dockerfiles/vulnerable-node-app/Dockerfile --scan-only
```

### 6. Image-Only Scan

```bash
docksec --image-only -i nginx:latest
```

## Example Scenarios

### Scenario 1: CI/CD Integration

See `scripts/ci-cd-scan.sh` for an example of how to integrate DockSec into your CI/CD pipeline.

### Scenario 2: Pre-commit Hook

See `scripts/pre-commit-hook.sh` for scanning Dockerfiles before committing.

### Scenario 3: Batch Scanning

See `scripts/batch-scan.sh` for scanning multiple Dockerfiles at once.

## Sample Reports

The `reports/` directory contains example reports in all supported formats:

- `sample-report.html` - Interactive HTML report
- `sample-report.pdf` - Professional PDF report
- `sample-report.json` - Machine-readable JSON
- `sample-report.csv` - Spreadsheet-compatible CSV

## Configuration Examples

See `configs/` directory for example configuration files:

- `.env.example` - Environment variables
- `docksec-config.yaml` - Advanced configuration (if supported)

## Building and Testing Examples

### Build All Example Images

```bash
cd examples
./scripts/build-all.sh
```

### Scan All Examples

```bash
cd examples
./scripts/scan-all.sh
```

## Learning Path

1. **Start here**: `dockerfiles/secure-python-app/` - See what good looks like
2. **Learn from mistakes**: `dockerfiles/vulnerable-node-app/` - Common security issues
3. **Advanced patterns**: `dockerfiles/multi-stage-golang/` - Optimization techniques
4. **Real-world**: `dockerfiles/production-examples/` - Production-grade configurations

## Common Issues and Solutions

### Issue: "Image not found"
```bash
# Build the image first
docker build -t myapp:latest .
# Then scan
docksec Dockerfile -i myapp:latest
```

### Issue: "OpenAI API key not set"
```bash
# Use scan-only mode
docksec Dockerfile --scan-only
# Or set API key
export OPENAI_API_KEY="your-key"
```

## Contributing Examples

Have a great example to share? Please contribute!

1. Add your Dockerfile to the appropriate directory
2. Include a README explaining the example
3. Test it with DockSec
4. Submit a PR

## Resources

- [Docker Security Best Practices](https://docs.docker.com/develop/security-best-practices/)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)
- [OWASP Docker Security](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)

---

For more information, visit the [main README](../README.md).
