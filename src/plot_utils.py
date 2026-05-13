import matplotlib.pyplot as plt


def plot_prices(prices):
    """Visualize exchange rate trends."""
    if not prices:
        print("No data to plot")
        return

    dates = [p["date"] for p in prices]
    rates = [p["rate"] for p in prices]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, rates, marker="o", linewidth=2, markersize=8)
    plt.title("USD³EUR Exchange Rate Trend")
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate")
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
