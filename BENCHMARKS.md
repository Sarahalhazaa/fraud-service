# Benchmarks

python scripts/loadtest.py (2000 requests, 25 concurrent)

| Setup | p50 | p99 | Throughput |
|---|---|---|---|
| 1 worker, --reload | 546.0 ms | 809.3 ms | 48 req/s |
| 4 workers, no reload | 296.7 ms | 347.0 ms | 84 req/s |
