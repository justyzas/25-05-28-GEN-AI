
from schema import InvoiceModel


def write_structured_invoice_output_to_csv(invoices: list[InvoiceModel]):
    # column_names = """"Sąskaitos numeris","Data","Apmokėjimo terminas","Pardavėjas","Pirkėjas","Valiuta","Suma(Be PVM)", "PVM suma", "Suma (Su PVM)" """

    # Stulpeliu apibrezimas (protingas, su tolimesnėmis automatizacijos )
    columns_config = [
        {"local_name": "Sąskaitos numeris", "model_field_name": "invoice_number"},
        {"local_name": "Data", "model_field_name": "invoice_date"},
        {"local_name": "Apmokėjimo terminas",
            "model_field_name": "payment_due_date"},
        {"local_name": "Pardavėjas", "model_field_name": "vendor_name"},
        {"local_name": "Pirkėjas", "model_field_name": "customer_name"},
        {"local_name": "Valiuta", "model_field_name": "currency_code"},
        {"local_name": "Suma(Be PVM)", "model_field_name": "subtotal"},
        {"local_name": "PVM suma", "model_field_name": "sales_tax"},
        {"local_name": "Suma (Su PVM)", "model_field_name": "total"}]

    first_line = ",".join([column_config["local_name"]
                          for column_config in columns_config])

    csv_output = first_line

    for invoice in invoices:
        # Sugeneruojama saskaitos eilute csv faile
        # invoice_number = getattr(invoice, 'invoice_number')
        invoice_number = invoice.invoice_number
        invoice_date = getattr(invoice, 'invoice_date')
        payment_due_date = getattr(invoice, 'payment_due_date')

        invoice_line = f"\n{invoice_number},{invoice_date},{payment_due_date},{getattr(invoice, 'vendor_name')},{getattr(invoice, 'customer_name')},{getattr(invoice, 'currency_code')},{getattr(invoice, 'subtotal')},{getattr(invoice, 'sales_tax')},{getattr(invoice, 'total')}"
        # prijungiama saskaitos eilute i csv faila
        csv_output += invoice_line

    with open("output.csv", "w", encoding="utf-8-sig") as f:
        f.write(csv_output)
