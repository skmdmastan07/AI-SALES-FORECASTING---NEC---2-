import numpy as np


def safety_stock(std_dev, lead_time):

    z_score = 1.65

    return round(
        z_score * std_dev * np.sqrt(lead_time),
        2
    )


def reorder_point(
        avg_daily_demand,
        lead_time,
        safety_stock_value
):

    return round(
        (avg_daily_demand * lead_time)
        + safety_stock_value,
        2
    )


def eoq(
        annual_demand,
        ordering_cost,
        holding_cost
):

    value = np.sqrt(
        (2 * annual_demand * ordering_cost)
        / holding_cost
    )

    return round(value, 2)