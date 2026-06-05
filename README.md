# Financial Performance Metrics

A lightweight Python toolkit for calculating common investment and portfolio performance metrics.

## Features

* CAGR (Compound Annual Growth Rate)
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta
* Maximum Drawdown
* Tracking Error

## Installation

```bash
pip install -r requirements.txt
```

## Example

```python
from metrics import calculate_sharpe_ratio

sharpe = calculate_sharpe_ratio(
    returns
)
```

## Metrics Included

### CAGR

Measures annualized growth over a period.

### Sharpe Ratio

Risk-adjusted return using total volatility.

### Sortino Ratio

Risk-adjusted return using downside volatility only.

### Alpha & Beta

Measures fund performance relative to a benchmark.

### Maximum Drawdown

Largest peak-to-trough decline.

### Tracking Error

Deviation from benchmark performance.

## Author

Rajnandini Singh Solanki
