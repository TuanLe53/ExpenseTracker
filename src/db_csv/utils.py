from csv import writer

def write_csv_file(file_path, columns: list[str], data: list[list[str]]) -> None:
    with open(file_path, 'w') as f:
        w = writer(f, lineterminator='\n')
        w.writerow(columns)
        
        for record in data:
            w.writerow(record)