import csv


class Database:
    def __init__(self):
        self.fieldnames = ["Brand", "Model", "Year", "Color"]
        self.filename = "db_car.csv"

        with open(self.filename, "w", newline="") as csvfile:
            self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            self.writer.writeheader()

    def add(self, brand, model, year, color):
        record = {
            "Brand": brand,
            "Model": model,
            "Year": year,
            "Color": color,
        }

        with open(self.filename, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow(record)

    def reed(self):
        with open(self.filename, "r") as cvs_file:
            csv_reader = csv.DictReader(cvs_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                print(
                    f'{row["Brand"]} have model {row["Model"]} is year {row["Year"]} and have color{row["Color"]}'
                )
                line_count += 1

    def find(self, crit):
        with open(self.filename, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                for fieldname in self.fieldnames:
                    if crit in row[fieldname]:
                        print(
                            f'You find:{row["Brand"]}  {row["Model"]}  {row["Year"]} {row["Color"]}'
                        )

    def delete(self, crit):
        records_to_keep = []

        with open(self.filename, "r+") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                match = False
                for fieldname in self.fieldnames:
                    if crit in row[fieldname]:
                        match = True
                        break
                if not match:
                    records_to_keep.append(row)

        with open(self.filename, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(records_to_keep)

    def update(self, field_to_update, criteria, updated_value):
        records_to_update = []

        with open(self.filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                if row[field_to_update] == criteria:
                    row[field_to_update] = updated_value
                records_to_update.append(row)

        with open(self.filename, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(records_to_update)

    def middle_year(self):
        with open(self.filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            middle = 0
            count = 0
            for row in reader:
                middle += int(row["Year"])
                count += 1

            print(f"Middle:{middle/count}")


database = Database()
database.add("Ford", "Focus", "2005", "Pink")
database.add("Lada", "BA3 2115", "1985", "Black")
database.add("Lada", "BA3 2116", "2000", "Green")
database.reed()
database.find("Pink")
database.update("Year", "2005", "2023")
database.middle_year()