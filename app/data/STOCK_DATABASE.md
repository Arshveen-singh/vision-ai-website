# 📊 Stock Database System

## Overview

The VISION AI stock database system provides comprehensive access to 7500+ US stock symbols with real-time price data, company information, and market analytics.

## Features

### 🔍 Stock Search
- Search by symbol (e.g., "AAPL", "MSFT")
- Search by company name (e.g., "Apple", "Microsoft")
- Fuzzy matching for partial queries
- Sector-based filtering

### 📈 Real-Time Data
- Current stock prices
- Daily change and percentage
- Intraday sparkline charts
- Market state (OPEN/CLOSED)
- Trading volume

### 📊 Market Analytics
- 5-day, 30-day, 90-day price history
- Trending stocks dashboard
- Sector performance analysis
- Market cap categorization

### 💼 Company Information
- Business sector and industry
- Market capitalization
- P/E ratio, EPS, dividend yield
- 52-week high/low
- Company description

## Usage Examples

### Voice Commands

```
"What's the price of Apple stock?"
"Show me Tesla stock"
"Search for tech stocks"
"Get trending stocks"
"Show me NVIDIA stock history"
"Compare Apple and Microsoft"
```

### API Endpoints

```python
from ai_core.weather_stocks_handler import weather_stocks

# Get stock price
result = weather_stocks.get_stock_price("AAPL")

# Search stocks
results = weather_stocks.search_stocks("technology")

# Get detailed info
info = weather_stocks.get_stock_detailed("TSLA")

# Get trending stocks
trending = weather_stocks.get_trending_stocks()

# Get price history
history = weather_stocks.get_stock_history("NVDA", days=30)
```

## Database Structure

### Stock Entry Format
```json
{
  "symbol": "AAPL",
  "name": "Apple Inc.",
  "sector": "Consumer Electronics",
  "market_cap": "3.77T"
}
```

### Market Cap Categories
- **Mega Cap**: > $200B (e.g., AAPL, MSFT, GOOGL)
- **Large Cap**: $10B - $200B
- **Mid Cap**: $2B - $10B
- **Small Cap**: $300M - $2B
- **Micro Cap**: < $300M

### Major Sectors
- Technology (Software, Hardware, Semiconductors)
- Financial Services (Banks, Insurance, Asset Management)
- Healthcare (Pharmaceuticals, Biotechnology, Medical Devices)
- Consumer (Retail, Food & Beverage, Apparel)
- Energy (Oil & Gas, Utilities, Renewable)
- Industrial (Manufacturing, Construction, Transportation)
- Real Estate (REITs, Development)
- Materials (Chemicals, Metals, Mining)

## Adding New Stocks

### Method 1: Using Python API
```python
from ai_core.stock_database import stock_db

stock_db.add_stock(
    symbol="NEWCO",
    name="New Company Inc.",
    sector="Technology",
    market_cap="5.2B"
)

stock_db.save_database()
```

### Method 2: Bulk Import
```python
# Create a file: data/new_stocks.txt
# Format: SYMBOL\tNAME\tSECTOR\tMARKET_CAP

python scripts/import_stock_data.py
```

### Method 3: Manual JSON Edit
Edit `data/stock_symbols.json` and add entries to the "stocks" array.

## Data Sources

- **Real-time Prices**: Yahoo Finance API
- **Company Data**: Yahoo Finance Summary API
- **Market Data**: Public financial data feeds

## Performance

- **Search Speed**: < 50ms for 7500+ symbols
- **Price Fetch**: < 2s per symbol
- **Cache Duration**: 10 minutes
- **Concurrent Requests**: Supported

## Integration with VISION AI

### Chat Interface
The stock system integrates seamlessly with the chat interface:

```
User: "What's Apple stock at?"
AI: 📈 AAPL: $185.50 (+2.30, +1.26%)
    [Shows interactive stock card with sparkline]
```

### Voice Mode
Natural language queries work in voice mode:

```
User: "Tell me about Tesla stock"
AI: [Speaks] "Tesla is currently trading at $242.50, 
    up 3.2% today. The stock is in the automotive 
    manufacturing sector with a market cap of 1.46 trillion."
```

### Context Panel
Stock data appears in the context panel for quick reference:
- Current portfolio value
- Watchlist stocks
- Market movers
- Sector performance

## API Reference

### WeatherStocksHandler Methods

#### `search_stocks(query: str) -> Dict`
Search for stocks by symbol or name.

**Parameters:**
- `query`: Search term (symbol or company name)

**Returns:**
```python
{
    "success": True,
    "message": "Search results...",
    "results": [...],
    "count": 5
}
```

#### `get_stock_price(symbol: str) -> Dict`
Get current stock price and basic info.

**Parameters:**
- `symbol`: Stock ticker symbol (e.g., "AAPL")

**Returns:**
```python
{
    "success": True,
    "type": "stock_card",
    "symbol": "AAPL",
    "name": "Apple Inc.",
    "price": 185.50,
    "change": 2.30,
    "change_percent": 1.26,
    "sparkline": [180, 182, 185, ...],
    "high": 186.20,
    "low": 183.40,
    "volume": 52000000
}
```

#### `get_stock_detailed(symbol: str) -> Dict`
Get comprehensive stock information.

**Returns:** Extended data including sector, P/E ratio, market cap, etc.

#### `get_trending_stocks() -> Dict`
Get list of trending/popular stocks with current prices.

#### `get_stock_history(symbol: str, days: int) -> Dict`
Get historical price data with chart.

**Parameters:**
- `symbol`: Stock ticker
- `days`: Number of days (default: 30)

## Troubleshooting

### "Stock not found"
- Verify the symbol is correct
- Check if it's a US-listed stock
- Try searching by company name

### "Price fetch failed"
- Check internet connection
- Verify Yahoo Finance is accessible
- Symbol may be delisted or invalid

### "Database not loaded"
- Ensure `data/stock_symbols.json` exists
- Run `python scripts/import_stock_data.py`
- Check file permissions

## Future Enhancements

- [ ] Real-time streaming prices (WebSocket)
- [ ] Portfolio tracking and management
- [ ] Price alerts and notifications
- [ ] Technical indicators (RSI, MACD, etc.)
- [ ] Options chain data
- [ ] Earnings calendar
- [ ] News sentiment analysis
- [ ] International markets support
- [ ] Cryptocurrency integration

## Contributing

To add more stocks to the database:

1. Prepare data in TSV format: `SYMBOL\tNAME\tSECTOR\tMARKET_CAP`
2. Run import script: `python scripts/import_stock_data.py`
3. Verify data: Check `data/stock_symbols.json`
4. Test search: Try searching for new symbols
5. Submit PR with updated database

## License

Stock data is sourced from public APIs and is subject to their respective terms of service. This system is for informational purposes only and should not be used as the sole basis for investment decisions.

---

**Last Updated**: January 16, 2025  
**Database Version**: 1.0  
**Total Symbols**: 7500+
