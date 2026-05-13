def parse_response(data):
    """Extract relevant data from API response."""
    if not data:
        return None
    rate = data["rates"].get("EUR")
    date = data.get("date")
    base = data.get("base", "USD")
    print(f"{date} ³ {base}³EUR: {rate}")
    return {"date": date, "rate": rate, "base": base}
