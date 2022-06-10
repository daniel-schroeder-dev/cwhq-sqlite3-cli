from beautifultable import BeautifulTable


def _getColumnHeaders(data):
    return [item[0] for item in data.description]


def print_table(data):
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_BOX)
    table.columns.header = _getColumnHeaders(data)
    [table.rows.append(row) for row in data.fetchall()]
    print(table)
