function chartOptions(yTitle = "") {
    return {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                labels: {
                    color: "#374151",
                    font: {
                        size: 13,
                        weight: "600"
                    }
                }
            },
            tooltip: {
                backgroundColor: "#111827",
                titleColor: "#ffffff",
                bodyColor: "#e5e7eb",
                padding: 10,
                cornerRadius: 6
            }
        },
        scales: {
            x: {
                ticks: { color: "#6b7280" },
                grid: { display: false }
            },
            y: {
                title: {
                    display: !!yTitle,
                    text: yTitle
                },
                ticks: { color: "#6b7280" },
                grid: { color: "rgba(0,0,0,0.05)" }
            }
        }
    };
}
new Chart(document.getElementById('segmentChart'), {
    type: 'bar',
    data: {
        labels: Object.keys(segmentData),
        datasets: [{
            label: 'Customer Segments',
            data: Object.values(segmentData),
            backgroundColor: '#4f46e5',
            borderRadius: 6
        }]
    },
    options: chartOptions("Customer Count")
});

new Chart(document.getElementById('revenueChart'), {
    type: 'line',
    data: {
        labels: Object.keys(revenueData),
        datasets: [{
            label: 'Monthly Revenue',
            data: Object.values(revenueData),
            borderColor: '#10b981',
            backgroundColor: 'rgba(16,185,129,0.1)',
            tension: 0.4,
            fill: true
        }]
    },
    options: chartOptions("Revenue")
});

new Chart(document.getElementById('topCustomersChart'), {
    type: 'bar',
    data: {
        labels: Object.keys(topCustomers),
        datasets: [{
            label: 'Revenue',
            data: Object.values(topCustomers),
            backgroundColor: '#9333ea',
            borderRadius: 6
        }]
    },
    options: {
        ...chartOptions("Revenue"),
        indexAxis: 'y'
    }
});

new Chart(document.getElementById('monetaryChart'), {
    type: 'bar',
    data: {
        labels: Object.keys(monetaryDistribution),
        datasets: [{
            label: 'Customers',
            data: Object.values(monetaryDistribution),
            backgroundColor: '#f59e0b',
            borderRadius: 6
        }]
    },
    options: chartOptions("Customers")
});

new Chart(document.getElementById('scatterChart'), {
    type: 'scatter',
    data: {
        datasets: [{
            label: 'Customer Behavior',
            data: scatterData.map(d => ({
                x: d.recency,
                y: d.frequency
            })),
            backgroundColor: '#ef4444'
        }]
    },
    options: {
        ...chartOptions(),
        scales: {
            x: {
                title: { display: true, text: 'Recency (days)' }
            },
            y: {
                title: { display: true, text: 'Frequency' }
            }
        }
    }
});
