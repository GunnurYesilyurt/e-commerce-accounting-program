📊 E-Commerce Financial & Profit Analyzer Engine

An open-source, modular financial management and profit calculation engine built for e-commerce sellers on marketplaces such as Trendyol, Hepsiburada, and Etsy.

This project provides barcode-level cost mapping, marketplace commission and tax splitting, date-range batch transaction processing, and a lightweight web dashboard to deliver instant, itemized financial analytics and net profit insights.

🎯 Strategic Vision & Development Roadmap

This repository serves as the core architectural foundation (MVP) for an end-to-end e-commerce automation ecosystem. 

🚀 Planned Development Roadmap

[x] Core Accounting Engine (MVP): Barcode-level product/packaging cost mapping, commission/shipping fee breakdowns, date-range batch processing, and mock data simulation.

[x] Web Dashboard Interface: Lightweight UI for configuring cost structures and visualizing consolidated date-filtered financial reports.

[ ] Live Marketplace API Integrations: Asynchronous API clients (httpx / REST) to fetch real-time orders, commissions, shipping deductions, and withholding taxes directly from Trendyol & Hepsiburada seller APIs.

[ ] Database & Multi-Tenancy Architecture: Integration of PostgreSQL/SQLAlchemy ORM with JWT user authentication to support multi-seller data isolation.

[ ] Real-Time Inventory Synchronization: Inventory tracking and automated stock updates triggered by processed order statuses.

[ ] Automated Invoicing Engine: Automated PDF invoice generation and e-archive compliance mapping based on tax and shipping outputs.

🏗️ Repository Architecture

The project follows a clean, decoupled Object-Oriented Programming (OOP) structure, separating core financial domain logic from presentation and test suites:

e-commerce-accounting/
├── core/                       # Core Financial Domain & Business Logic
│   ├── __init__.py
│   ├── models.py               # Data models for ProductCost, Transaction, and Barcode mappings
│   ├── calculator.py           # Single-item & Batch financial breakdown calculators
│   └── mock_data.py            # Simulated order dataset across date ranges and barcodes
├── web/                        # Web Dashboard & Application Layer
│   ├── __init__.py
│   ├── app.py                  # Web server endpoints & controller logic
│   ├── static/
│   │   ├── css/style.css       # Dashboard styling
│   │   └── js/main.js          # Dynamic date picker & AJAX calculation updates
│   └── templates/
│       └── index.html          # Dashboard user interface
├── tests/                      # Automated Test Suite
│   ├── __init__.py
│   └── test_calculator.py      # Unit tests for financial logic, barcode mapping, & date filtering
├── run.py                      # Application entry point
├── requirements.txt            # Dependency configuration
└── README.md                   # Project documentation
