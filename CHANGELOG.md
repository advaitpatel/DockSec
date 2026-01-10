# Changelog

All notable changes to DockSec will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.19] - 2025-06-26

### Added
- Latest stable release with full feature set
- Enhanced error handling and retry mechanisms
- Improved documentation and examples

## [0.0.18] - 2025-06-26

### Added
- Production-ready reliability features
- Automatic retry logic with exponential backoff
- Rate limiting support for OpenAI API
- Configurable timeouts for all scanning tools
- Comprehensive error recovery mechanisms

### Improved
- Enhanced logging with structured output
- Better progress indicators for long-running operations
- More actionable error messages with troubleshooting steps

## [0.0.17] - 2025-06-26

### Added
- Multi-format report generation (JSON, CSV, PDF, HTML)
- Professional HTML reports with interactive styling
- Security score calculation (0-100 rating)

### Fixed
- Report generation issues with special characters
- PDF formatting improvements
- CSV export compatibility

## [0.0.16] - 2025-06-26

### Added
- Image-only scanning mode
- Support for scanning Docker images without Dockerfile
- Enhanced Docker Scout integration

### Improved
- CLI argument validation
- Better error messages for missing dependencies

## [0.0.15] - 2025-06-25

### Added
- AI-only analysis mode
- Scan-only mode (no AI required)
- Configuration via environment variables
- Support for .env files

### Changed
- Refactored CLI interface for better usability
- Improved help documentation

## [0.0.14] - 2025-06-25

### Added
- Rich terminal formatting with progress bars
- Real-time scan progress indicators
- Color-coded severity levels

### Improved
- Terminal output formatting
- Progress tracking for long operations

## [0.0.13] - 2025-06-24

### Added
- Docker Scout integration for vulnerability scanning
- Support for multiple scanning tools (Trivy, Hadolint, Docker Scout)
- Severity-based filtering (CRITICAL, HIGH, MEDIUM, LOW)

## [0.0.12] - 2025-06-24

### Fixed
- Dependency resolution issues
- Package installation errors
- Import path corrections

## [0.0.11] - 2025-06-24

### Added
- LangChain integration for AI-powered analysis
- OpenAI GPT-4 support for intelligent recommendations
- Context-aware security suggestions

## [0.0.10] - 2025-06-24

### Added
- Automated security scoring system
- CVE detection and analysis
- CVSS score reporting

## [0.0.9] - 2025-06-24

### Added
- Trivy integration for comprehensive vulnerability scanning
- Hadolint integration for Dockerfile best practices

## [0.0.8] - 2025-06-24

### Changed
- Major refactoring of core scanning engine
- Improved code organization and modularity

## [0.0.7] - 2025-06-24

### Added
- Basic report generation capabilities
- JSON output format

## [0.0.6] - 2025-06-24

### Fixed
- Critical bug fixes in scanning logic
- Improved error handling

## [0.0.5] - 2025-06-12

### Added
- Initial CLI interface
- Basic Dockerfile analysis

## [0.0.4] - 2025-06-12

### Changed
- Package structure improvements
- Better dependency management

## [0.0.3] - 2025-06-11

### Added
- Initial public release
- Basic Docker security scanning functionality
- AI-powered recommendations using OpenAI
- Support for Dockerfile analysis

### Features
- Command-line interface for easy usage
- Integration with external security tools
- Automated report generation

---

## Version History Notes

### Breaking Changes
- v0.0.15: CLI argument structure changed - see documentation for migration guide
- v0.0.10: Report format updated - old reports may not be compatible

### Deprecations
- v0.0.15: Legacy Python script execution (`python main.py`) still supported but deprecated in favor of CLI (`docksec`)

### Security Updates
- All versions include security-focused scanning and analysis
- Regular updates to vulnerability databases
- No known security issues in any released versions

---

## Upcoming Features (Roadmap)

### Planned for v0.1.0
- [ ] Docker Compose support
- [ ] Multi-container analysis
- [ ] Kubernetes manifest scanning
- [ ] Custom rule engine
- [ ] Plugin system for extensibility

### Planned for v0.2.0
- [ ] Web dashboard interface
- [ ] Team collaboration features
- [ ] Historical trend analysis
- [ ] Integration with CI/CD platforms (GitHub Actions, GitLab CI, Jenkins)

### Under Consideration
- [ ] Support for additional LLM providers (Claude, Gemini, local models)
- [ ] Offline mode with cached vulnerability databases
- [ ] Container runtime security monitoring
- [ ] Image signing and verification
- [ ] SBOM (Software Bill of Materials) generation

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## Support

For issues, questions, or feature requests, please visit:
- GitHub Issues: https://github.com/advaitpatel/DockSec/issues
- Documentation: https://github.com/advaitpatel/DockSec/blob/main/README.md
