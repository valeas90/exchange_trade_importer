from xlrd import open_workbook

class FileProcesser:
    def __init__(self):
        self.header = None

    def parse_file(self, file_path):
        """Returns a generator with one parsed row at a time"""
        book = open_workbook(file_path, on_demand=True)
        for name in book.sheet_names():
            sheet = book.sheet_by_name(name)
            stats = {'num_colums': sheet.ncols, 'num_rows': sheet.nrows}
            for row in sheet.get_rows():
                if not self.header:
                    self.header = self.read_header(row)
                    continue
                
                parsed_row = self.parse_row(row)
                yield parsed_row

    def read_header(self, header_line):
        header = {
            'list': [],
            'order': {}
        }
        for i, element in enumerate(header_line):
            header['list'].append(element.value)
            header['order'][i] = element.value

        return header

    def parse_row(self, row):
        parsed_row = {}
        for i, element in enumerate(row):
            parsed_row[self.header['order'][i]] = element.value

        return parsed_row
