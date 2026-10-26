# Online Retail Sales Analysis

A retail sales project using Python to prepare transaction data in Excel and a Power BI report for dashboard analysis.

## Project files

| File | Purpose |
| --- | --- |
| `Online Retail.xlsx` | Input transaction workbook |
| `OnlineRetail.py` | Python data preparation script |
| `online_retail_cleaned.xlsx` | Prepared workbook supplied with the project |
| `E-Commerce Customer Segmentation Dashboard.pbix` | Power BI report supplied with the project |

## Data preparation

The Python script reads the input workbook and:

1. Calculates `Revenue` as `Quantity × UnitPrice`.
2. Selects completed orders whose invoice number does not start with `C`, with positive quantity and unit price.
3. Selects canceled orders whose invoice number starts with `C`.
4. Adds a `Month` field derived from `InvoiceDate` to both groups.
5. Writes `Completed Orders` and `Canceled Orders` sheets to `online_retail_cleaned.xlsx`.

Non-canceled rows with nonpositive quantities or prices are excluded from the completed-order output. The script does not explicitly remove duplicates or missing customer identifiers.

## Run the Python preparation

Install Python, then open a terminal in this repository folder:

```sh
python -m pip install -r requirements.txt
python OnlineRetail.py
```

Keep the input workbook in the same folder and run the script from that folder. Running the script overwrites `online_retail_cleaned.xlsx`.

The input must contain `InvoiceNo`, `Quantity`, `UnitPrice`, and `InvoiceDate`; the invoice date column must load as dates.

## Open the Power BI report

Open `E-Commerce Customer Segmentation Dashboard.pbix` in Power BI Desktop. If refreshing prompts for a missing source, update the report's data-source path to the corresponding workbook in your local repository folder, then refresh.

The report file is included for exploration in Power BI Desktop. Its visuals, measures, and segmentation logic have not been independently verified as part of this repository setup.

## Tools

- Python and pandas for data preparation
- openpyxl for Excel file support
- Excel workbooks for source and prepared data
- Power BI Desktop for the report

## Data provenance and licensing

The workbooks and report were supplied by the project owner. An original dataset source and redistribution license have not yet been recorded in this repository. No license is granted by this README.
