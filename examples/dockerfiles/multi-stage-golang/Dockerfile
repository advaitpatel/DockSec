# Multi-Stage Golang Application
# Optimized build with minimal final image

# Stage 1: Build stage
FROM golang:1.21-alpine AS builder

# Install build dependencies
RUN apk add --no-cache git ca-certificates tzdata

# Create appuser for runtime
RUN addgroup -g 1001 -S appuser && \
    adduser -S appuser -u 1001

# Set working directory
WORKDIR /build

# Copy go mod files
COPY go.mod go.sum ./

# Download dependencies (cached layer)
RUN go mod download && \
    go mod verify

# Copy source code
COPY . .

# Build the application
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build \
    -ldflags='-w -s -extldflags "-static"' \
    -a \
    -o /app/server .

# Stage 2: Runtime stage (distroless)
FROM gcr.io/distroless/static:nonroot

# Copy timezone data
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo

# Copy CA certificates
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

# Copy the binary
COPY --from=builder /app/server /app/server

# Use non-root user
USER nonroot:nonroot

# Expose port
EXPOSE 8080

# Health check using wget (available in distroless)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD ["/app/server", "healthcheck"]

# Set entrypoint
ENTRYPOINT ["/app/server"]
