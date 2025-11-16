---
name: dashboard-patterns
description: Reusable React/JavaScript patterns for Somali dialect classifier dashboard. Covers Chart.js integration, data card components, filter patterns, responsive layouts, and dashboard-specific UI patterns. Auto-invokes when building dashboard components, charts, data visualizations, or dashboard UI.
allowed-tools: Read, Grep
---

# Dashboard Patterns for Somali Dialect Classifier

## Chart.js Integration

### Pattern 1: Bar Chart Component

```javascript
function DialectDistributionChart({ data }) {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    if (!chartRef.current) return;

    // Destroy previous chart
    if (chartInstance.current) {
      chartInstance.current.destroy();
    }

    const ctx = chartRef.current.getContext('2d');

    chartInstance.current = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Northern', 'Southern', 'Central'],
        datasets: [{
          label: 'Records',
          data: [data.northern, data.southern, data.central],
          backgroundColor: ['#33BBEE', '#0077BB', '#66CCEE']  // Data colors
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false
          }
        }
      }
    });

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [data]);

  return (
    <div className="chart-container" style={{ height: '300px' }}>
      <canvas ref={chartRef}></canvas>
    </div>
  );
}
```

### Pattern 2: Line Chart with Time Series

```javascript
function MetricsOverTimeChart({ timeSeriesData }) {
  const chartRef = useRef(null);

  useEffect(() => {
    if (!chartRef.current) return;

    const ctx = chartRef.current.getContext('2d');

    new Chart(ctx, {
      type: 'line',
      data: {
        labels: timeSeriesData.map(d => d.date),
        datasets: [{
          label: 'Accuracy',
          data: timeSeriesData.map(d => d.accuracy),
          borderColor: '#33BBEE',  // Data cyan
          backgroundColor: 'rgba(51, 187, 238, 0.1)',
          tension: 0.4
        }]
      },
      options: {
        responsive: true,
        plugins: {
          tooltip: {
            callbacks: {
              label: (context) => `Accuracy: ${(context.parsed.y * 100).toFixed(1)}%`
            }
          }
        }
      }
    });
  }, [timeSeriesData]);

  return <canvas ref={chartRef}></canvas>;
}
```

---

## Data Card Components

### Pattern 1: Metric Card

```javascript
function MetricCard({ label, value, trend, trendDirection }) {
  return (
    <div className="data-card">
      <div className="data-card__label">{label}</div>
      <div className="data-card__value">{value.toLocaleString()}</div>
      {trend && (
        <div className="data-card__trend">
          {trendDirection === 'up' && <span className="trend-icon">↑</span>}
          {trendDirection === 'down' && <span className="trend-icon">↓</span>}
          <span className="data-card__trend-text">{trend}</span>
        </div>
      )}
    </div>
  );
}

// Usage
<MetricCard
  label="Total Records"
  value={12345}
  trend="+12.5% from last month"
  trendDirection="up"
/>
```

### Pattern 2: Grid of Metric Cards

```javascript
function MetricsGrid({ metrics }) {
  return (
    <div className="metrics-grid">
      {metrics.map((metric, idx) => (
        <MetricCard
          key={idx}
          label={metric.label}
          value={metric.value}
          trend={metric.trend}
          trendDirection={metric.trendDirection}
        />
      ))}
    </div>
  );
}

// CSS
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}
```

---

## Filter Patterns

### Pattern 1: Toggle Capsule Filter

```javascript
function DialectFilter({ selected, onChange }) {
  const dialects = ['All', 'Northern', 'Southern', 'Central'];

  return (
    <div className="data-toggle">
      {dialects.map(dialect => (
        <button
          key={dialect}
          className={`data-toggle__option ${
            selected === dialect ? 'data-toggle__option--active' : ''
          }`}
          onClick={() => onChange(dialect)}
        >
          {dialect}
        </button>
      ))}
    </div>
  );
}
```

### Pattern 2: Date Range Filter

```javascript
function DateRangeFilter({ startDate, endDate, onChange }) {
  return (
    <div className="filter-group">
      <label>Date Range</label>
      <div className="date-inputs">
        <input
          type="date"
          value={startDate}
          onChange={(e) => onChange({ start: e.target.value, end: endDate })}
          className="form__input"
        />
        <span>to</span>
        <input
          type="date"
          value={endDate}
          onChange={(e) => onChange({ start: startDate, end: e.target.value })}
          className="form__input"
        />
      </div>
    </div>
  );
}
```

---

## Data Fetching Patterns

### Pattern 1: Custom Hook for Data Fetching

```javascript
function useDataFetch(endpoint) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        setLoading(true);
        const response = await fetch(endpoint);
        if (!response.ok) throw new Error('Failed to fetch');
        const json = await response.json();
        setData(json);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, [endpoint]);

  return { data, loading, error };
}

// Usage
function DashboardView() {
  const { data, loading, error } = useDataFetch('/api/metrics');

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage message={error} />;

  return <MetricsGrid metrics={data} />;
}
```

---

## Loading & Empty States

### Pattern 1: Loading Skeleton

```javascript
function ChartSkeleton() {
  return (
    <div className="chart-skeleton">
      <div className="skeleton-bar" />
      <div className="skeleton-bar" />
      <div className="skeleton-bar" />
    </div>
  );
}

// CSS
.skeleton-bar {
  height: 200px;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
  border-radius: 8px;
  margin-bottom: 1rem;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

### Pattern 2: Empty State

```javascript
function EmptyState({ message, action }) {
  return (
    <div className="empty-state">
      <svg className="empty-state__icon" width="64" height="64">
        {/* Icon SVG */}
      </svg>
      <p className="empty-state__message">{message}</p>
      {action && (
        <button className="btn btn--primary" onClick={action.onClick}>
          {action.label}
        </button>
      )}
    </div>
  );
}

// Usage
<EmptyState
  message="No data available. Upload your first dataset to get started."
  action={{
    label: "Upload Dataset",
    onClick: handleUpload
  }}
/>
```

---

## Responsive Layout Patterns

### Pattern 1: Responsive Grid

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1.5rem;
  padding: 2rem;
}

.dashboard-grid__full {
  grid-column: 1 / -1;
}

.dashboard-grid__half {
  grid-column: span 6;
}

.dashboard-grid__third {
  grid-column: span 4;
}

@media (max-width: 768px) {
  .dashboard-grid__half,
  .dashboard-grid__third {
    grid-column: 1 / -1;
  }
}
```

---

## Error Handling

### Pattern 1: Error Boundary

```javascript
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Dashboard error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-message">
          <h2>Something went wrong</h2>
          <p>{this.state.error.message}</p>
          <button onClick={() => window.location.reload()}>
            Reload Dashboard
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

// Usage
<ErrorBoundary>
  <DashboardView />
</ErrorBoundary>
```

---

## Performance Optimization

### Pattern 1: Memoized Chart Component

```javascript
const MemoizedChart = React.memo(({ data }) => {
  return <DialectDistributionChart data={data} />;
}, (prevProps, nextProps) => {
  // Only re-render if data actually changed
  return JSON.stringify(prevProps.data) === JSON.stringify(nextProps.data);
});
```

### Pattern 2: Debounced Filter

```javascript
function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => clearTimeout(handler);
  }, [value, delay]);

  return debouncedValue;
}

// Usage in search filter
function SearchFilter() {
  const [searchTerm, setSearchTerm] = useState('');
  const debouncedSearch = useDebounce(searchTerm, 300);

  useEffect(() => {
    if (debouncedSearch) {
      fetchFilteredData(debouncedSearch);
    }
  }, [debouncedSearch]);

  return (
    <input
      type="text"
      value={searchTerm}
      onChange={(e) => setSearchTerm(e.target.value)}
      placeholder="Search..."
    />
  );
}
```

---

## When This Skill Activates

This skill auto-invokes when you mention:
- Dashboard, dashboard components, dashboard UI
- Chart.js, charts, data visualization
- React patterns, React components, React hooks
- Data cards, metric cards, KPI cards
- Filters, filtering, toggle filters
- Loading states, empty states, skeletons
- Responsive layout, grid layout
- Data fetching, API integration

---

**Version:** 1.0.0
**Last Updated:** 2025-11-06
**Project:** Somali Dialect Classifier Dashboard
