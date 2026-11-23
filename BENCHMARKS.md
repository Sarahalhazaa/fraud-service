# Benchmarks

python scripts/loadtest.py (2000 requests, 25 concurrent)

| Setup | p50 | p99 | Throughput |
|---|---|---|---|
| 1 worker, --reload | 546.0 ms | 809.3 ms | 48 req/s |
| 4 workers, no reload | 296.7 ms | 347.0 ms | 84 req/s |

## Docker images

| Image | Context sent | Size | First build | Rebuild after code edit | User |
|---|---|---|---|---|---|
| fraud-service:naive | 481.65 MB | 3.33 GB (845 MB content) | 1m14s | - | root |
| fraud-service:dev | 2.94 kB | 846 MB (180 MB content) | 1m02s | 0.8s | appuser |

Container (compose, 2 workers, no access log): p50 162.8 ms, p99 199.9 ms, 156 req/s, memory 402.7MiB / 512MiB, graceful stop 0.6s
