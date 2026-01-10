# Vulnerable Node.js Application
# ⚠️ This Dockerfile intentionally contains security vulnerabilities for educational purposes
# DO NOT USE IN PRODUCTION

# Issue 1: Using 'latest' tag (unpredictable)
FROM node:latest

# Issue 2: Running as root user (default)
# No USER directive specified

# Issue 3: Installing unnecessary packages
RUN apt-get update && apt-get install -y \
    vim \
    curl \
    wget \
    git \
    sudo \
    ssh

# Issue 4: Not cleaning apt cache
# Increases image size and attack surface

# Issue 5: Setting working directory as root
WORKDIR /app

# Issue 6: Copying files as root
COPY . .

# Issue 7: Hardcoded secrets in Dockerfile
ENV DATABASE_PASSWORD=mysecretpassword123
ENV API_KEY=sk-1234567890abcdef
ENV JWT_SECRET=supersecret

# Issue 8: Exposing too many ports
EXPOSE 3000 8080 9229 22

# Issue 9: Installing dependencies as root
RUN npm install

# Issue 10: No health check defined

# Issue 11: Installing global packages
RUN npm install -g nodemon pm2

# Issue 12: Copying sensitive files
# .git directory, .env files, etc.

# Issue 13: Running with elevated privileges
# No security options or capabilities dropped

# Issue 14: Debug mode enabled
ENV NODE_ENV=development
ENV DEBUG=*

# Issue 15: No version pinning in package.json
# Can lead to unexpected behavior

# Issue 16: Running with shell form (security risk)
CMD npm start

# Security Issues Summary:
# - CVE vulnerabilities in outdated packages
# - Running as root user
# - Hardcoded secrets
# - Unnecessary packages installed
# - Large attack surface
# - No health checks
# - Debug mode in production
# - Unpinned dependencies
