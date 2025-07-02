from schema import InvoiceModel


def filter_invoices(inv: list[InvoiceModel]):
    filtered = [invoice for invoice in inv if invoice.is_invoice]
    # for invoice in inv:
    #     if invoice.invoice_number != "":
    #         filtered.append(invoice)
    #     if invoice.is_invoice:
    #         filtered.append(invoice)
    return filtered


def filter_non_invoices(inv: list[InvoiceModel]):
    return [invoice for invoice in inv if not invoice.is_invoice]
