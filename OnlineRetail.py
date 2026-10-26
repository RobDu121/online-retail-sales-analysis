import pandas as pd

df = pd.read_excel('Online Retail.xlsx')

df['Revenue'] = df['Quantity'] * df['UnitPrice']

completed_orders = df[~df['InvoiceNo'].astype(str).str.startswith('C')
                      & (df['Quantity'] > 0)
                        & (df['UnitPrice'] > 0)].copy()

completed_orders["Month"] = completed_orders["InvoiceDate"].dt.to_period("M").astype(str)

canceled_orders = df[df['InvoiceNo'].astype(str).str.startswith('C')].copy()

canceled_orders["Month"] = canceled_orders["InvoiceDate"].dt.to_period("M").astype(str)

with pd.ExcelWriter("online_retail_cleaned.xlsx") as writer:
    completed_orders.to_excel(writer, sheet_name="Completed Orders", index=False)
    canceled_orders.to_excel(writer, sheet_name="Canceled Orders", index=False)
