// Fetch and render cost cards on load
window.onload = async () => {
    const res = await fetch('/api/costs');
    const costs = await res.json();
    const container = document.getElementById('cost-cards');
    
    for (const [barcode, data] of Object.entries(costs)) {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <h3>${data.product_name} (${barcode})</h3>
            <label>Product Cost (₺)</label>
            <input type="number" id="pc-${barcode}" value="${data.product_cost}">
            <label>Packaging (₺)</label>
            <input type="number" id="pkg-${barcode}" value="${data.packaging_cost}">
            <label>Other (₺)</label>
            <input type="number" id="oth-${barcode}" value="${data.other_expenses}">
            <button onclick="updateCost('${barcode}')">Save</button>
        `;
        container.appendChild(card);
    }
};

// Update costs via API
async function updateCost(barcode) {
    const data = {
        barcode: barcode,
        product_cost: document.getElementById(`pc-${barcode}`).value,
        packaging_cost: document.getElementById(`pkg-${barcode}`).value,
        other_expenses: document.getElementById(`oth-${barcode}`).value
    };
    await fetch('/api/costs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    alert('Cost updated successfully!');
}

// Calculate and render report
async function calculateReport() {
    const data = {
        start_date: document.getElementById('start-date').value,
        end_date: document.getElementById('end-date').value
    };
    
    const res = await fetch('/api/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    
    const summary = await res.json();
    
    document.getElementById('report-dashboard').style.display = 'grid';
    document.getElementById('res-revenue').innerText = `₺${summary.total_revenue.toFixed(2)}`;
    document.getElementById('res-profit').innerText = `₺${summary.net_profit.toFixed(2)}`;
    document.getElementById('res-margin').innerText = `%${summary.profit_margin.toFixed(2)}`;
    document.getElementById('res-prod-cost').innerText = `₺${summary.total_product_cost.toFixed(2)}`;
    document.getElementById('res-pack').innerText = `₺${summary.total_packaging_cost.toFixed(2)}`;
    document.getElementById('res-comm').innerText = `₺${summary.total_commission.toFixed(2)}`;
}