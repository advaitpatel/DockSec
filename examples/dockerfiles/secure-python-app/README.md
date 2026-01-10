# Secure Python Flask Application Example

This is a secure Dockerfile example following industry best practices.

## Security Features

✅ **Specific base image tag** - No `latest` tag
✅ **SHA256 digest pinning** - Ensures reproducibility
✅ **Non-root user** - Runs as unprivileged user
✅ **Minimal attack surface** - Uses slim base image
✅ **Security updates** - Updates system packages
✅ **Proper permissions** - Read-only filesystem where possible
✅ **Health checks** - Container health monitoring
✅ **No secrets in image** - Uses environment variables
✅ **Layer optimization** - Efficient layer caching
✅ **Clean build** - Removes unnecessary files

## Security Score

When scanned with DockSec, this Dockerfile should achieve:
- **Score**: 85-100/100
- **Vulnerabilities**: Minimal (mostly informational)
- **Recommendations**: Minor optimizations only

## Build and Scan

```bash
# Build the image
docker build -t secure-python-app:latest .

# Scan with DockSec (Dockerfile only)
docksec Dockerfile

# Full scan (Dockerfile + Image)
docksec Dockerfile -i secure-python-app:latest
```

## Expected DockSec Output

- ✅ Non-root user detected
- ✅ Specific version tags used
- ✅ Health check configured
- ✅ No exposed secrets
- ✅ Minimal base image
- ⚠️ Consider using distroless for even smaller attack surface

## Run the Container

```bash
docker run -d -p 8080:8080 --name secure-app secure-python-app:latest
```

## Further Improvements

1. **Use distroless base image** for minimal attack surface
2. **Add read-only root filesystem** (`--read-only` flag)
3. **Implement multi-stage build** if build tools needed
4. **Add security scanning** in CI/CD pipeline
5. **Use secrets management** for sensitive configuration

## Resources

- [Docker Security Best Practices](https://docs.docker.com/develop/security-best-practices/)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)
