# Multi-Stage Golang Build Example

This Dockerfile demonstrates advanced multi-stage build patterns for optimal security and size.

## Features

✅ **Multi-stage build** - Separates build and runtime
✅ **Distroless base image** - Minimal attack surface (< 5MB)
✅ **Non-root user** - Runs as unprivileged user
✅ **Static binary** - No external dependencies
✅ **Build optimization** - Cached dependency layers
✅ **Small image size** - 10-20MB final image
✅ **Security hardening** - Stripped binaries
✅ **CA certificates included** - For HTTPS calls

## Benefits of Multi-Stage Builds

### Build Stage
- Full toolchain available (Go compiler, git, etc.)
- Dependencies downloaded and cached
- Source code compiled
- ~1GB in size

### Runtime Stage
- Only compiled binary included
- No build tools or source code
- Distroless base (no shell, package manager)
- ~10-20MB in size

## Security Score

Expected DockSec results:
- **Score**: 90-100/100 ⭐
- **Vulnerabilities**: None or very few
- **Image Size**: 10-20MB
- **Attack Surface**: Minimal

## Build and Scan

```bash
# Build the image
docker build -t golang-app:latest .

# Check image size
docker images golang-app:latest

# Scan with DockSec
docksec Dockerfile -i golang-app:latest
```

## Image Size Comparison

| Build Type | Size | Notes |
|------------|------|-------|
| Single-stage (golang:1.21) | ~1GB | Includes build tools |
| Multi-stage (alpine) | ~50MB | Smaller but has shell |
| Multi-stage (distroless) | ~15MB | Minimal, no shell |
| Multi-stage (scratch) | ~10MB | Absolute minimum |

## Why Distroless?

Distroless images:
- ✅ No shell (prevents shell-based attacks)
- ✅ No package manager (can't install malware)
- ✅ Minimal CVEs (fewer packages = fewer vulnerabilities)
- ✅ Smaller attack surface
- ⚠️ Harder to debug (no shell to exec into)

## Running the Container

```bash
# Run the container
docker run -d -p 8080:8080 --name golang-app golang-app:latest

# Check health
curl http://localhost:8080/health

# View logs (no shell access)
docker logs golang-app
```

## Advanced Optimizations

### 1. Layer Caching
```dockerfile
# Copy dependency files first
COPY go.mod go.sum ./
RUN go mod download

# Then copy source code
COPY . .
```

### 2. Build Flags
```bash
-ldflags='-w -s'          # Strip debug info
-extldflags "-static"      # Static linking
CGO_ENABLED=0             # Disable CGO
```

### 3. Security Scanning
```bash
# Scan build stage separately
docker build --target=builder -t myapp:builder .
docksec Dockerfile --image-only -i myapp:builder

# Scan final stage
docksec Dockerfile -i myapp:latest
```

## Troubleshooting

### Can't debug without shell?
```bash
# Use debug variant temporarily
FROM gcr.io/distroless/static:debug

# Or use docker cp to extract files
docker cp golang-app:/app/server ./server
```

### Need CA certificates?
Already included in this example! See builder stage.

### Binary too large?
```bash
# Use these flags
-ldflags='-w -s'           # Strips symbols (~30% smaller)
upx --best /app/server     # Compress binary (50% smaller)
```

## Comparison with Other Patterns

### Pattern 1: Scratch (Smallest)
```dockerfile
FROM scratch
COPY --from=builder /app/server /server
ENTRYPOINT ["/server"]
```
- Size: ~10MB
- No CA certs, no timezone data

### Pattern 2: Alpine (Balance)
```dockerfile
FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /app/server /server
USER 1001
ENTRYPOINT ["/server"]
```
- Size: ~50MB
- Has shell (debugging easier)

### Pattern 3: Distroless (Recommended)
This example - best balance of size and security!

## Resources

- [Distroless Images](https://github.com/GoogleContainerTools/distroless)
- [Go Docker Best Practices](https://docs.docker.com/language/golang/build-images/)
- [Multi-stage Builds](https://docs.docker.com/build/building/multi-stage/)

---

This pattern is recommended for production Go applications!
