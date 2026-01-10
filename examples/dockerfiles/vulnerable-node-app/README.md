# Vulnerable Node.js Application Example

⚠️ **WARNING**: This Dockerfile is intentionally insecure for educational purposes only!

## Purpose

This example demonstrates **common security mistakes** in Dockerfiles. Use it to:
- Learn what NOT to do
- Test DockSec's detection capabilities
- Understand security vulnerabilities

## Security Issues in This Dockerfile

### Critical Issues 🔴

1. **Hardcoded Secrets** (Lines 31-33)
   - Database passwords in plain text
   - API keys exposed
   - JWT secrets hardcoded

2. **Running as Root** (No USER directive)
   - Application runs with root privileges
   - No privilege separation

3. **Outdated/Vulnerable Dependencies**
   - Using old package versions with known CVEs
   - No version pinning

### High Issues 🟠

4. **Using 'latest' Tag** (Line 5)
   - Unpredictable builds
   - Potential breaking changes

5. **Unnecessary Packages** (Lines 11-17)
   - vim, wget, ssh, sudo installed
   - Increases attack surface

6. **Debug Mode Enabled** (Lines 43-44)
   - Verbose logging
   - Performance impact

### Medium Issues 🟡

7. **No Health Checks**
   - Cannot detect unhealthy containers

8. **Excessive Port Exposure** (Line 36)
   - SSH port exposed
   - Debug port exposed

9. **Large Image Size**
   - Uncleaned package cache
   - Unnecessary files included

### Low Issues 🔵

10. **No Layer Optimization**
    - Poor caching strategy
    - Slow builds

## Expected DockSec Results

When scanned with DockSec:

```bash
docksec Dockerfile
```

**Expected Output:**
- **Security Score**: 20-35/100 ❌
- **Critical Issues**: 5-10
- **High Issues**: 10-15
- **Medium Issues**: 5-10
- **Total Vulnerabilities**: 30+

## AI Recommendations You'll Receive

DockSec's AI will recommend:

1. ✅ Use specific version tags (e.g., `node:18-alpine`)
2. ✅ Create and use non-root user
3. ✅ Remove hardcoded secrets (use environment variables)
4. ✅ Add `.dockerignore` file
5. ✅ Update vulnerable dependencies
6. ✅ Remove unnecessary packages
7. ✅ Add health checks
8. ✅ Use multi-stage builds
9. ✅ Enable production mode
10. ✅ Minimize exposed ports

## How to Fix

See the `secure-python-app` example for best practices, or compare with this fixed version:

```dockerfile
# Fixed version
FROM node:18-alpine

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies (as root, then switch)
RUN npm ci --only=production

# Copy application code
COPY --chown=nodejs:nodejs . .

# Switch to non-root user
USER nodejs

# Health check
HEALTHCHECK CMD node healthcheck.js

# Expose only necessary port
EXPOSE 3000

# Production mode
ENV NODE_ENV=production

# Run application
CMD ["node", "app.js"]
```

## Learning Exercise

1. Scan this Dockerfile with DockSec
2. Review all findings
3. Try to fix each issue
4. Rescan and compare scores
5. Aim for 85+ score

## Resources

- [Node.js Docker Best Practices](https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md)
- [OWASP Docker Security](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [Snyk's 10 Docker Security Best Practices](https://snyk.io/blog/10-docker-image-security-best-practices/)

---

**Remember**: These vulnerabilities are for educational purposes only. Never deploy insecure containers to production!
