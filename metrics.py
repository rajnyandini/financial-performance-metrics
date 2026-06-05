import numpy as np
from scipy.stats import linregress


def calculate_cagr(start_value, end_value, years):
    return (end_value / start_value) ** (1 / years) - 1


def calculate_sharpe_ratio(returns, risk_free_rate=0.065):
    excess_return = np.mean(returns) - (risk_free_rate / 252)
    return (excess_return / np.std(returns)) * np.sqrt(252)


def calculate_sortino_ratio(returns, risk_free_rate=0.065):
    excess_return = np.mean(returns) - (risk_free_rate / 252)

    downside_returns = returns[returns < 0]

    downside_std = np.std(downside_returns)

    return (excess_return / downside_std) * np.sqrt(252)


def calculate_alpha_beta(fund_returns, benchmark_returns):

    beta, alpha, _, _, _ = linregress(
        benchmark_returns,
        fund_returns
    )

    annualized_alpha = alpha * 252

    return annualized_alpha, beta


def calculate_max_drawdown(nav_series):

    running_max = np.maximum.accumulate(nav_series)

    drawdowns = nav_series / running_max - 1

    return np.min(drawdowns)


def calculate_tracking_error(
    fund_returns,
    benchmark_returns
):

    diff = fund_returns - benchmark_returns

    return np.std(diff) * np.sqrt(252)