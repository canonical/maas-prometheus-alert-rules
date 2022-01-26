# maas-prometheus-alert-rules
A set of Prometheus rules for alerting on MAAS metrics

This repo provides alerting rules specifically for MAAS counters, for other alerts, see [the MAAS Loki rules repo](https://github.com/canonical/maas-loki-alert-rules)

## Setup

### For Direct Prometheus Use

```
make python-deps
make
# upload group.yml to prometheus
```
