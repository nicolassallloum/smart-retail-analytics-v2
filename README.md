<!DOCTYPE html>
<html lang="en" data-theme="light" style=""><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Retail Analytics - Project Documentation</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    <style>
      /* Document Setup & Reset */
      :root {
        --font-family-sans-serif: 'Arial', 'Helvetica', sans-serif;
        --font-family-monospace: 'Courier New', Courier, monospace;
        --primary-color: #000000;
        --secondary-color: #444444;
        --border-color: #d1d1d1;
      }

      body {
        font-family: var(--font-family-sans-serif);
        line-height: 1.5;
        color: #000000;
        background-color: #ffffff;
        max-width: 880px;
        margin: 0 auto;
        padding: 40px 60px; /* Word-like margins */
        position: relative;
        box-sizing: border-box;
        text-align: justify;
      }

      /* Typography */
      h1 {
        font-size: 24pt;
        font-weight: bold;
        color: #2e5894; /* Professional Blue */
        margin-bottom: 12px;
        border-bottom: 2px solid #2e5894;
        padding-bottom: 8px;
        text-align: left;
      }

      h2 {
        font-size: 18pt;
        font-weight: bold;
        color: #333333;
        margin-top: 24px;
        margin-bottom: 12px;
        border-bottom: 1px solid #eeeeee;
        padding-bottom: 4px;
      }

      h3 {
        font-size: 14pt;
        font-weight: bold;
        color: #444444;
        margin-top: 18px;
        margin-bottom: 8px;
      }

      p,
      li {
        font-size: 11pt;
        margin-bottom: 10px;
      }

      /* Links */
      a {
        color: #0563c1;
        text-decoration: underline;
      }

      /* Lists */
      ul {
        margin-bottom: 16px;
        padding-left: 24px;
      }
      li {
        margin-bottom: 4px;
      }

      /* Code Blocks */
      pre {
        background-color: #f5f5f5;
        border: 1px solid #dcdcdc;
        padding: 12px;
        font-family: var(--font-family-monospace);
        font-size: 10pt;
        white-space: pre-wrap;
        margin-bottom: 16px;
        border-radius: 0; /* No rounded corners */
      }
      code {
        font-family: var(--font-family-monospace);
        background-color: #f5f5f5;
        padding: 2px 4px;
        font-size: 10pt;
      }

      /* Tables */
      table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
        font-size: 11pt;
      }
      th,
      td {
        border: 1px solid #000000;
        padding: 8px 12px;
        text-align: left;
      }
      th {
        background-color: #f0f0f0;
        font-weight: bold;
      }

      /* Badges Simulation (Text-based for print friendliness) */
      .badges {
        font-size: 9pt;
        color: #555;
        margin-bottom: 24px;
        font-family: var(--font-family-monospace);
      }

      /* Architecture Diagram Simulation */
      .architecture-diagram {
        border: 1px dashed #999;
        padding: 20px;
        text-align: center;
        margin: 20px 0;
        background-color: #fafafa;
        font-family: var(--font-family-sans-serif);
      }
      .arch-step {
        font-weight: bold;
        margin: 10px 0;
      }
      .arrow {
        color: #666;
        margin: 5px 0;
        font-size: 14pt;
      }

      /* Footer */
      .footer {
        margin-top: 60px;
        padding-top: 20px;
        border-top: 1px solid #000;
        font-size: 9pt;
        text-align: center;
        color: #666;
      }

      .header-section {
        text-align: center;
        margin-bottom: 40px;
      }
      .header-title {
        font-size: 28pt;
        font-weight: bold;
        color: #000;
        margin-bottom: 5px;
      }
      .header-subtitle {
        font-size: 14pt;
        color: #555;
        font-style: italic;
      }
    </style>
  </head>
  <body style="">
    <!-- Header Section -->
    <div class="header-section">
      <div class="header-title">Smart Retail Analytics</div>
      <div class="header-subtitle">End-to-End Data Engineering &amp; Retail Analytics Project</div>
    </div>

    <div class="badges">
      [Docker: Containerized] &nbsp; [PostgreSQL: 15] &nbsp; [Python: ETL] &nbsp; [Power BI: Visualization]
    </div>

    <h1>1. Project Overview</h1>
    <p>
      Smart Retail Analytics is a complete end-to-end data engineering project designed to simulate a real-world retail
      data warehouse architecture. This project reflects enterprise-grade retail analytics architecture suitable for
      production-scale systems.
    </p>

    <p>The project demonstrates the following key capabilities:</p>
    <ul>
      <li>Data ingestion and transformation (ETL)</li>
      <li>Star schema data warehouse modeling</li>
      <li>PostgreSQL-based analytical storage</li>
      <li>Dockerized infrastructure</li>
      <li>Business Intelligence integration (Power BI)</li>
    </ul>

    <h1>2. Architecture Overview</h1>
    <div class="architecture-diagram">
      <div class="arch-step">Raw Data (CSV / Generated Data)</div>
      <div class="arrow">↓</div>
      <div class="arch-step">Python ETL Pipeline</div>
      <div class="arrow">↓</div>
      <div class="arch-step">PostgreSQL Data Warehouse (Star Schema)</div>
      <div class="arrow">↓</div>
      <div class="arch-step">Power BI Desktop (Analytics Layer)</div>
    </div>

    <h1>3. Tech Stack</h1>
    <table>
      <thead>
        <tr>
          <th>Layer</th>
          <th>Technology</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Containerization</td>
          <td>Docker &amp; Docker Compose</td>
        </tr>
        <tr>
          <td>Data Warehouse</td>
          <td>PostgreSQL 15</td>
        </tr>
        <tr>
          <td>ETL</td>
          <td>Python (Pandas, Psycopg2 / SQLAlchemy)</td>
        </tr>
        <tr>
          <td>Data Modeling</td>
          <td>Star Schema</td>
        </tr>
        <tr>
          <td>BI Layer</td>
          <td>Power BI Desktop</td>
        </tr>
        <tr>
          <td>Optional NoSQL</td>
          <td>MongoDB</td>
        </tr>
      </tbody>
    </table>

    <h1>4. Project Structure</h1>
    <pre>smart-retail-analytics/
│
├── docker-compose.yml
├── README.md
│
├── etl/
│   ├── generate_raw_data.py
│   ├── transform_data.py
│   └── load_to_postgres.py
│
├── sql/
│   ├── create_tables.sql
│   └── indexes.sql
│
├── data/
│   └── raw_sales.csv
│
└── powerbi/
   └── dashboard.pbix</pre>

    <h1>5. Data Warehouse Design</h1>
    <p>The data warehouse follows a strict <strong>Star Schema Model</strong> to optimize for analytical queries.</p>

    <h3>Fact Table</h3>
    <p><strong>fact_sales</strong></p>
    <ul>
      <li>order_id</li>
      <li>date_id</li>
      <li>customer_id</li>
      <li>product_id</li>
      <li>quantity</li>
      <li>gross_amount</li>
      <li>net_amount</li>
      <li>discount</li>
      <li>payment_method</li>
      <li>is_returned</li>
    </ul>

    <h3>Dimension Tables</h3>
    <ul>
      <li><strong>dim_customer</strong>: Customer demographics and details.</li>
      <li><strong>dim_product</strong>: Product categorization and pricing.</li>
      <li><strong>dim_date</strong>: Date hierarchy for temporal analysis.</li>
    </ul>

    <h1>6. How to Run the Project</h1>

    <h3>1. Clone the Repository</h3>
    <pre>git clone https://github.com/yourusername/smart-retail-analytics.git
cd smart-retail-analytics</pre>

    <h3>2. Start Infrastructure</h3>
    <pre>docker compose up -d</pre>
    <p>PostgreSQL will run on: <code>localhost:55432</code></p>

    <h3>3. Run ETL Pipeline</h3>
    <p>Set environment variable:</p>
    <pre>export DB_PASSWORD=sra_password</pre>
    <p>Run the loader script:</p>
    <pre>python etl/load_to_postgres.py</pre>
    <p>Expected output:</p>
    <pre>🚀 Starting Load to Postgres...
📥 Inserting data...
✅ Completed successfully</pre>

    <h3>4. Verify Data</h3>
    <pre>psql -h localhost -p 55432 -U postgres -d smart_retail_dw</pre>
    <p>Example validation query:</p>
    <pre>SELECT COUNT(*) FROM fact_sales;</pre>

    <h1>7. Power BI Integration</h1>
    <p>To connect Power BI Desktop to the data warehouse:</p>
    <ol>
      <li>Open Power BI Desktop.</li>
      <li>Click <strong>Get Data</strong> → <strong>PostgreSQL</strong>.</li>
      <li>
        Use the following credentials:
        <ul>
          <li><strong>Server:</strong> localhost</li>
          <li><strong>Port:</strong> 55432</li>
          <li><strong>Database:</strong> smart_retail_dw</li>
          <li><strong>Username:</strong> postgres</li>
          <li><strong>Password:</strong> sra_password</li>
        </ul>
      </li>
    </ol>

    <h1>8. Sample Dashboard Metrics</h1>
    <p>The project enables the creation of the following analytical views:</p>
    <ul>
      <li>💰 <strong>Total Revenue KPI</strong></li>
      <li>📦 <strong>Total Orders</strong></li>
      <li>📈 <strong>Revenue by Month</strong></li>
      <li>🏷 <strong>Sales by Category</strong></li>
      <li>💳 <strong>Payment Method Distribution</strong></li>
      <li>🔥 <strong>Top 10 Products</strong></li>
      <li>📍 <strong>Sales by City</strong></li>
    </ul>

    <h1>9. ETL Process Overview</h1>
    <p>The ETL pipeline performs the following logical steps:</p>
    <ol>
      <li>Data ingestion from CSV / generated dataset.</li>
      <li>Data cleansing and validation.</li>
      <li>Data transformation.</li>
      <li>Star schema mapping.</li>
      <li>Bulk insert into PostgreSQL.</li>
    </ol>

    <h1>10. Configuration</h1>

    <h3>Environment Variables</h3>
    <table>
      <thead>
        <tr>
          <th>Variable</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>DB_PASSWORD</code></td>
          <td>PostgreSQL password</td>
        </tr>
      </tbody>
    </table>

    <h3>Docker Services</h3>
    <table>
      <thead>
        <tr>
          <th>Service</th>
          <th>Port</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>PostgreSQL</td>
          <td>55432</td>
        </tr>
        <tr>
          <td>MongoDB</td>
          <td>27017</td>
        </tr>
      </tbody>
    </table>

    <h1>11. Project Objectives &amp; Future Enhancements</h1>

    <h3>Objectives</h3>
    <ul>
      <li>Demonstrate practical data engineering workflow.</li>
      <li>Design analytical-ready schema.</li>
      <li>Build BI-ready warehouse.</li>
      <li>Simulate enterprise retail analytics architecture.</li>
    </ul>

    <h3>Future Enhancements</h3>
    <ul>
      <li>Add Apache Airflow for orchestration.</li>
      <li>Implement Kafka streaming ingestion.</li>
      <li>Add CDC with Debezium.</li>
      <li>Deploy Superset for server-side BI.</li>
      <li>Add ClickHouse for high-performance analytics.</li>
      <li>Cloud deployment on AWS / GCP.</li>
    </ul>

    <h1>12. Why This Project Matters</h1>
    <p>
      This project showcases real-world warehouse modeling, Dockerized infrastructure management, ETL pipeline
      engineering, and BI integration. It demonstrates end-to-end data lifecycle management.
    </p>

    <p>It reflects skills relevant for the following roles:</p>
    <ul>
      <li>Data Engineering</li>
      <li>Analytics Engineering</li>
      <li>Business Intelligence</li>
      <li>Data Architecture</li>
    </ul>

    <br>
    <hr>

    <div class="footer">
      <p><strong>Author:</strong> Nicolas Salloum (Nix) | Data Engineer</p>
      <p>© 2026 Smart Retail Analytics. All rights reserved.</p>
    </div>
  

</body></html>
